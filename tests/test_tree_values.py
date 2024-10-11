import unittest
from unittest.mock import patch, mock_open
import io
import sys
from contextlib import redirect_stdout
import tempfile
import os
import shutil

# Assuming your main script is named 'tree_values.py'
# Update this import statement with the correct filename if it's different
from tree_values import should_ignore, print_tree, print_values, main

class TestProjectTreeViewer(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory for testing
        self.test_dir = tempfile.mkdtemp()
        os.chdir(self.test_dir)

        # Create a simple directory structure for testing
        os.makedirs('test_folder/subfolder')
        open('test_folder/file1.txt', 'w').close()
        open('test_folder/subfolder/file2.txt', 'w').close()
        os.makedirs('node_modules')
        open('node_modules/should_ignore.txt', 'w').close()

    def tearDown(self):
        # Remove the temporary directory after the test
        os.chdir(os.path.dirname(self.test_dir))
        shutil.rmtree(self.test_dir)

    def test_should_ignore(self):
        self.assertTrue(should_ignore('node_modules', []))
        self.assertTrue(should_ignore('test_folder/node_modules/file.txt', []))
        self.assertFalse(should_ignore('test_folder/file1.txt', []))
        self.assertTrue(should_ignore('custom_ignore.txt', ['custom_ignore.txt']))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_tree(self, mock_stdout):
        print_tree([])
        output = mock_stdout.getvalue()
        self.assertIn('|____test_folder/', output)
        self.assertIn('|____subfolder/', output)
        self.assertIn('|____file1.txt', output)
        self.assertNotIn('node_modules', output)

    @patch('builtins.open', new_callable=mock_open, read_data="test content")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_values(self, mock_stdout, mock_file):
        print_values([])
        output = mock_stdout.getvalue()
        self.assertIn('File: ./test_folder/file1.txt', output)
        self.assertIn('test content', output)
        self.assertNotIn('node_modules', output)

    @patch('sys.argv', ['script_name', 'tree'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_main_tree(self, mock_stdout):
        main()
        output = mock_stdout.getvalue()
        self.assertIn('|____test_folder/', output)

    @patch('sys.argv', ['script_name', 'values'])
    @patch('builtins.open', new_callable=mock_open, read_data="test content")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_main_values(self, mock_stdout, mock_file):
        main()
        output = mock_stdout.getvalue()
        self.assertIn('File: ./test_folder/file1.txt', output)
        self.assertIn('test content', output)

    @patch('sys.argv', ['script_name', 'tree', '--ignore', 'test_folder'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_main_tree_with_ignore(self, mock_stdout):
        main()
        output = mock_stdout.getvalue()
        self.assertNotIn('test_folder', output)

if __name__ == '__main__':
    unittest.main()