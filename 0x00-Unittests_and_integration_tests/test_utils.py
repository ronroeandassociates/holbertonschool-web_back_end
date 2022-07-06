#!/usr/bin/env python3
"""Module for test_utils"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json
from unittest.mock import TestCase, mock


class TestAccessNestedMap(unittest.TestCase):
    """ Defines the TestAccessNestedMap"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test that utils.access_nested_map returns the expected result"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test that an exception is raised"""
        with self.assertRaises(KeyError) as exception_context_manager:
            access_nested_map(nested_map, path)

class TestGetJson(TestCase):
    """Test get_json"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, payload):
        """Test get_json"""
        with mock.patch("requests.get") as mock_get:
            mock_get.return_value.json.return_value = payload
            self.assertEqual(get_json(url), payload)
