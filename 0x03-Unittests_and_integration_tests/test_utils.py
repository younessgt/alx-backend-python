#!/usr/bin/env python3
""" script using unitest to test the function "access_nested_map"""
import unittest
from utils import access_nested_map
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    '''Class usin functions to test access_nested_map function.'''
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
