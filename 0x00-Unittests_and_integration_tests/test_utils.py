#!/usr/bin/env python3
"""_
Parameterize a unit test
"""
import unittest
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """ Define the TestAccessNestedMap Class """
    @parameterized.expand([
      ({"a": 1}, ("a",), 1),
      ({"a": {"b": 2}}, ("a",), {'b': 2})
      ({"a": {"b": 2}}, (("a", "b"), 2))
    ])
    def TestAccessNestedMap(self, nested_map, path, expected):
        """
        Test the access of a nested map
        """
        self.assertEqual(access_nested_map(nested_map), expected)
