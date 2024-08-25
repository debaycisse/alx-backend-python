#!/usr/bin/env python3
"""This modules houses the definition of a class that tests the
GithubOrgClient class, defined in the client.py module"""
import unittest
from client import (
    GithubOrgClient,
    get_json
)
from unittest.mock import (
    patch,
    PropertyMock,
    Mock
)
from parameterized import parameterized  # type: ignore
from typing import (
    Dict,
    Any
)


class TestGithubOrgClient(unittest.TestCase):
    """This class defines various integration tests for the GithubOrgClient
    class with other components from other module(s)"""

    @parameterized.expand([
        ('google', ),
        ('abc', ),
    ])
    @patch('client.get_json')
    def test_org(self, org: str, mock_get_json: Mock):
        """Tests that GithubOrgClient.org returns the correct value"""
        cls = GithubOrgClient(org)
        cls.org()
        prmtr = cls.ORG_URL.format(org=org)
        mock_get_json.called_with_once(prmtr)

    def test_public_repos_url(self):
        """Tests that GithubOrgCLient._public_repos_url works correctly"""
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            org = 'google'
            cls = GithubOrgClient(org)
            expected = cls.ORG_URL.format(org=org)
            mock_org.return_value = {'repos_url': expected}
            self.assertEqual(cls._public_repos_url, expected)
