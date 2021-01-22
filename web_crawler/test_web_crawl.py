#!/usr/bin/env python3
"""Test for web_crawl.py"""

import unittest
from web_crawl import *
import requests_mock
import os

class Testing(unittest.TestCase):

# -------------------------------------------------

    def test_file_present(self):

        """Checks if all test files are present in the current directory"""

        self.assertTrue(os.path.exists('./web_crawl.py'))
        self.assertTrue(os.path.exists('./fake_response.txt'))
        self.assertTrue(os.path.exists('./expected.txt'))
        self.assertTrue(os.path.exists('./output_from_fn.txt'))

# -------------------------------------------------

    @requests_mock.mock()
    def test_get_local_links(self, m):

        """
        get requests are mocked by giving the input text response from fake_response.txt file. 
        This file contains both 1st and 3rd party links. The test asserts that the function returns only 1st party links

        """

        a = Crawl()
        result = {"https://kishore.com/about/", "https://kishore.com/usa/"}
        with open('fake_response.txt', 'r') as f:
            data = f.read().replace('\n', '')
        m.get('https://kishore.com', text=data)
        self.assertSetEqual(a.get_local_links('https://kishore.com'), result)

# -------------------------------------------------

    @requests_mock.mock()
    def test_get_all_links(self, m):

        """
        get requests are mocked by giving the input text response from fake_response.txt file. 
        This file contains both 1st and 3rd party links. The test asserts that the function returns all the links(1st + 3rd party)
        Checks if all links are returned by placing them inside a sorted list and asserting the lists to be equal
        
        """

        a = Crawl()    
        with open('fake_response.txt', 'r') as f:
            data = f.read()
        m.get('https://monzo.com', text=data)

        with open("output_from_fn.txt", "w+") as f:
            f.write(a.get_all_links('https://monzo.com'))

        with open("output_from_fn.txt", "r") as f:
            returned_list = f.read().splitlines()
        returned_list.sort()

        with open('expected.txt', 'r') as f:
            expected_list = f.read().splitlines()
        expected_list.sort()
        
        self.assertListEqual(returned_list, expected_list)

# -------------------------------------------------

if __name__ == "__main__":
    unittest.main()

