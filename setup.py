from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="tree-values-viewer",
    version="0.1.5",
    author="Burak Keskin",
    author_email="me@burak.dev",
    description="A tool to view project tree and file contents",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/keskinbu/tree-values-viewer",
    packages=find_packages(),
    install_requires=[
        'prettytable',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            'view-project=tree_values:main',
        ],
    },
)