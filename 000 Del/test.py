user_paths = user_path.split(os.pathsep)

# Display all user-specific paths
print("User PATH directories:")
for path in user_paths:
    print(path)

# Optionally, you can also extract system paths, or gather them via registry (advanced use)
print("\nSystem PATH directories (from SystemRoot):")
print(system_path)
