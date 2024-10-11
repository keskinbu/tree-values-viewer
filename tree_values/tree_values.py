import os
import argparse
from prettytable import PrettyTable

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

def print_values_info(additional_ignores):
    """Print file information sorted by line count"""
    file_info = []
    total_lines = 0

    for root, dirs, files in os.walk('.'):
        # Filter directories and files
        dirs[:] = [d for d in dirs if not should_ignore(os.path.join(root, d), additional_ignores)]
        files = [f for f in files if not should_ignore(os.path.join(root, f), additional_ignores)]

        for f in files:
            file_path = os.path.join(root, f)
            try:
                with open(file_path, 'r', encoding="utf-8") as file:
                    lines = len(file.readlines())
                    file_info.append((file_path, lines))
                    total_lines += lines
            except UnicodeDecodeError:
                file_info.append((file_path, "N/A (Binary file)"))

    # Sort file_info by line count (descending order)
    file_info.sort(key=lambda x: x[1] if isinstance(x[1], int) else -1, reverse=True)

    # Create and print the table
    table = PrettyTable()
    table.field_names = ["File Path", "Line Count"]
    for path, lines in file_info:
        table.add_row([path, lines])

    print(table)
    print(f"\nTotal lines of code: {total_lines}")

def main():
    parser = argparse.ArgumentParser(description="Project tree and values viewer.")
    parser.add_argument('command', choices=['tree', 'values', 'values-info'],
                        help="tree: View project tree, values: View file names and contents, values-info: View file information")
    parser.add_argument('--ignore', help="Comma separated list of additional files or directories to ignore.",
                        default="")

    args = parser.parse_args()

    additional_ignores = [ignore.strip() for ignore in args.ignore.split(',') if ignore.strip()]

    if args.command == "tree":
        print_tree(additional_ignores)
    elif args.command == "values":
        print_values(additional_ignores)
    elif args.command == "values-info":
        print_values_info(additional_ignores)

if __name__ == '__main__':
    main()