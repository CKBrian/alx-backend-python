#!/usr/bin/env python3
'''
       Defines a test_utils module with a TestAccessNestedMap class
'''

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)


class TestAccessNestedMap(unittest.TestCase):
    '''Defines a TestAccessNestedMap unit testing class'''

    @parameterized.expand([
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {'b': 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self,
                               nested_map: Mapping,
                               path: Sequence,
                               expected: Any) -> None:
        '''tests the utils access_nested_map method'''
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
            ({}, ("a",), KeyError),
            ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self,
                                         nested_map: Mapping,
                                         path: Sequence,
                                         expected: Any) -> None:
        '''tests the utils access_nested_map method'''
        self.assertRaises(KeyError, access_nested_map, nested_map, path)


class TestGetJson(unittest.TestCase):
    '''get_json unittest class'''
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self,
                      test_url: str,
                      test_payload: Dict,
                      ) -> None:
        '''test that utils.get_json method returns the expected result'''
        # Mock the return value of get_json
        with patch('utils.requests.get') as MockGet:
            MockGet.return_value.json.return_value = test_payload

            # Call the function under test
            res = get_json(test_url)

            # Assertions
            self.assertEqual(res, test_payload)

            # Test that the mocked get method was called exactly
            # once (per input) with test_url as argument.
            MockGet.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    '''Memoize unittest class'''
    class TestClass:

        def a_method(self):
            return 42

        @memoize
        def a_property(self):
            return self.a_method()

    def test_memoize(self) -> None:
        '''Tests memoization of a function output in cache'''
        with patch.object(self.TestClass, 'a_method') as MockMemoize:
            # Mock the return value of get_json
            MockMemoize.return_value = 42

            # Call the function under test
            obj = self.TestClass()
            obj.a_property
            res = obj.a_property

            # Assertions
            self.assertEqual(res, 42)
            MockMemoize.assert_called_once()


if __name__ == '__main__':
    unittest.main()
