import os
import argparse

# Common files and folders to ignore
COMMON_IGNORES = [
    "dist", "node_modules", "venv", ".terraform", ".next",
    ".terraform.lock.hcl", "package-lock.json"
]

def should_ignore(path, additional_ignores):
    """Check if the file or folder should be ignored"""
    path_lower = path.lower()
    filename = os.path.basename(path_lower)
    path_parts = path_lower.split(os.sep)

    for ignore in COMMON_IGNORES + additional_ignores:
        ignore_lower = ignore.lower()
        if ignore_lower == filename or ignore_lower in path_parts:
            return True
    return False

def print_tree(additional_ignores):
    """Display the project tree"""
    for root, dirs, files in os.walk('.'):
        # Filter directories and files
        dirs[:] = [d for d in dirs if not should_ignore(os.path.join(root, d), additional_ignores)]
        files = [f for f in files if not should_ignore(os.path.join(root, f), additional_ignores)]

        level = root.replace(os.getcwd(), '').count(os.sep)
        indent = '    ' * level
        print(f'{indent}|____{os.path.basename(root)}/')
        subindent = '    ' * (level + 1)
        for f in files:
            print(f'{subindent}|____{f}')

def print_values(additional_ignores):
    """Print file contents and names"""
    for root, dirs, files in os.walk('.'):
        # Filter directories and files
        dirs[:] = [d for d in dirs if not should_ignore(os.path.join(root, d), additional_ignores)]
        files = [f for f in files if not should_ignore(os.path.join(root, f), additional_ignores)]

        for f in files:
            file_path = os.path.join(root, f)
            print(f"File: {file_path}")
            try:
                with open(file_path, 'r', encoding="utf-8") as file:
                    print(file.read())
            except UnicodeDecodeError:
                print("Unable to read file contents (possibly a binary file)")
            print('-' * 40)

def main():
    parser = argparse.ArgumentParser(description="Project tree and values viewer.")
    parser.add_argument('command', choices=['tree', 'values'],
                        help="tree: View project tree, values: View file names and contents.")
    parser.add_argument('--ignore', help="Comma separated list of additional files or directories to ignore.",
                        default="")

    args = parser.parse_args()

    additional_ignores = [ignore.strip() for ignore in args.ignore.split(',') if ignore.strip()]

    if args.command == "tree":
        print_tree(additional_ignores)
    elif args.command == "values":
        print_values(additional_ignores)

if __name__ == '__main__':
    main()