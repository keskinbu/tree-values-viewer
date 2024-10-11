# Tree Values Viewer

A simple tool to view project tree structure and file contents.

## Installation

```
pip install tree-values-viewer
```

## Usage

```
view-project tree
view-project values
view-project values --ignore .env,.git
```

## Package Creation and Upload Commands
# Install required tools
pip install setuptools wheel twine

# Create distribution packages
python setup.py sdist bdist_wheel

# Upload to Test PyPI (optional)
twine upload --repository-url https://test.pypi.org/legacy/ dist/*

# Upload to PyPI
twine upload dist/*