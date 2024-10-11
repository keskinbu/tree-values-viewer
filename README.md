# Tree Values Viewer

A simple and powerful tool to view project tree structure, file contents, and file information.

## Features

- Display project directory structure
- View file contents
- Show file information including line count
- Ignore specific files or directories

## Installation

You can install Tree Values Viewer using pip:

```
pip install tree-values-viewer
```

## Usage

Tree Values Viewer provides three main commands:

1. `tree`: Display the project directory structure
2. `values`: View file contents
3. `values-info`: Show file information including line count

### Viewing Project Structure

To view the project directory structure:

```
view-project tree
```

Example output:
```
|____project_root/
    |____src/
        |____main.py
        |____utils.py
    |____tests/
        |____test_main.py
    |____README.md
```

### Viewing File Contents

To view the contents of all files in the project:

```
view-project values
```

This will display the content of each file, separated by a line of dashes.

### Viewing File Information

To view information about files, including their line count:

```
view-project values-info
```

Example output:
```
+------------------------+------------+
|       File Path        | Line Count |
+------------------------+------------+
| ./src/main.py          |    100     |
| ./src/utils.py         |     50     |
| ./tests/test_main.py   |     75     |
| ./README.md            |     30     |
+------------------------+------------+
Total lines of code: 255
```

### Ignoring Files or Directories

You can ignore specific files or directories using the `--ignore` option:

```
view-project tree --ignore .env,.git,node_modules
view-project values --ignore .env,.git,node_modules
view-project values-info --ignore .env,.git,node_modules
```

This will exclude the specified files or directories from the output.

## Development

### Setting Up the Development Environment

1. Clone the repository:
   ```
   git clone https://github.com/keskinbu/tree-values-viewer.git
   cd tree-values-viewer
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the development dependencies:
   ```
   pip install -r requirements-dev.txt
   ```

### Running Tests

To run the tests:

```
python -m unittest discover tests
```

### Building and Publishing

1. Install the required tools:
   ```
   pip install setuptools wheel twine
   ```

2. Create distribution packages:
   ```
   python setup.py sdist bdist_wheel
   ```

3. Upload to PyPI:
   ```
   twine upload dist/* --repository-url https://upload.pypi.org/legacy/ -u __token__ -p $PYPI_API_TOKEN
   ```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.