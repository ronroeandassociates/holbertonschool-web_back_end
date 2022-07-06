#!/usr/bin/env python3
"""_
Parameterize a unit test
"""

import unittest
from unittest import patch, TestCase, MagicMock
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """Test GithubOrgClient"""

    @parameterized.expand([
      ("google"),
      ("abc")
    ])
    @patch("client.get_json",
           MagicMock(return_value={"key": "value"}))
    def test_org(self, org_name):
        """Test org"""
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, {"key": "value"})
