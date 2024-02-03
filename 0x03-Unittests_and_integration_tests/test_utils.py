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
