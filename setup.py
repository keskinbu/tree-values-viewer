from setuptools import setup

setup(
    name='tree_values',
    version='1.0.0',
    py_modules=['tree_values'],
    entry_points={
        'console_scripts': [
            'view_project=tree_values:main',
        ],
    },
    install_requires=[],
    tests_require=['unittest'],
    test_suite='test_tree_values',
)