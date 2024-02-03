#!/usr/bin/env python3
""" script using unitest to test the function "access_nested_map"""
import unittest
from unittest import mock
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    '''Class using functions to test access_nested_map function.'''
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        '''Method to test access_nested_map function.'''
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b")
    ])
    def test_access_nested_map_exception(self, nested_map, path, keyerror):
        '''Method to test access_nested_map function with exception.'''
        with self.assertRaises(KeyError) as catch:
            access_nested_map(nested_map, path)
        self.assertIn(keyerror, str(catch.exception))


class TestGetJson(unittest.TestCase):
    """ class using functions to test get_json function."""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """Method to test get_json function."""
        with mock.patch('requests.get') as mock_get:
            mock_get.return_value.json.return_value = test_payload
            self.assertEqual(get_json(test_url), test_payload)


class TestMemoize(unittest.TestCase):
    """" class using functions to test memoize function."""

    def test_memoize(self):
        """Method to test memoize function."""

        class TestClass:
            """class to define."""

            def a_method(self):
                """method to define"""
                return 42

            @memoize
            def a_property(self):
                """method to define"""
                return self.a_method()

        with mock.patch.object(TestClass,
                               'a_method',
                               return_value=42) as mock_patch:
            test_obj = TestClass()
            ret = test_obj.a_property
            ret = test_obj.a_property

            self.assertEqual(ret, 42)
            mock_patch.assert_called_once()
