import os

def get_user_and_system_paths():
    # Get the current process's PATH environment variable (combination of system and user)
    combined_path_env = os.environ.get('PATH', '')

    # Split into a list of paths
    combined_path_list = combined_path_env.split(os.pathsep)

    # On Windows, you can separate system and user paths using registry or manual inspection
    if os.name == 'nt':  # For Windows
        import winreg
        
        def get_registry_path_value(key_path, value_name):
            try:
                with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path) as key:
                    return winreg.QueryValueEx(key, value_name)[0]
            except FileNotFoundError:
                return None
        
        system_path = get_registry_path_value(r"SYSTEM\CurrentControlSet\Control\Session Manager\Environment", "Path")
        user_path = os.environ.get("Path")  # User-level PATH variable is already accessible in `os.environ`

        system_path_list = system_path.split(os.pathsep) if system_path else []
        user_path_list = user_path.split(os.pathsep) if user_path else []

    else:  # For Unix-like systems, there's typically no distinction between user/system paths
        system_path_list = combined_path_list
        user_path_list = []  # Not directly available

    return system_path_list, user_path_list


# Get the paths
system_paths, user_paths = get_user_and_system_paths()

# Display the results
print("System PATHs:")
for path in system_paths:
    print(path)

print("\nUser PATHs:")
for path in user_paths:
    print(path)
