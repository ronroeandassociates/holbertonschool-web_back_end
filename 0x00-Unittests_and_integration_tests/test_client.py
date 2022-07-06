#!/usr/bin/env python3
"""_
Parameterize a unit test
"""

import unittest
from unittest import patch, TestCase, MagicMock, mock, PropertyMock
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(TestCase):
    """Test for GithubOrgClient"""

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch("client.get_json",
           MagicMock(return_value={'key': 'value'}))
    def test_org(self, org_name):
        "test org method"
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, {'key': 'value'})

    def test_public_repos_url(self):
        """Test public_repos_url method"""
        with patch("client.get_json",
                   new_callable=PropertyMock,
                   return_value={"repos_url": "url"}):
            client = GithubOrgClient("google")
            self.assertEqual(client._public_repos_url, "url")
