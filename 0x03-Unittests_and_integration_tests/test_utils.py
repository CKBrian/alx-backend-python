#!/usr/bin/env/ python3
'''
       Defines a test_utils module with a TestAccessNestedMap class
'''

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    '''Defines a TestAccessNestedMap unit testing class'''
    @parameterized.expand([
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {'b': 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2)
    ])

    def test_access_nested_map(self, nested_map, path, expected):
        '''tests the utils access_nested_map method'''
        res = access_nested_map(nested_map, path)
        self.assertEqual(res, expected)

if __name__ == '__main__':
    unittest.main()
