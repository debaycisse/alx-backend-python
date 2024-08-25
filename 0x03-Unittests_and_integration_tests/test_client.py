#!/usr/bin/env python3
"""This modules houses the definition of a class that tests the
GithubOrgClient class, defined in the client.py module"""
import unittest
from client import GithubOrgClient
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
        ('google', {'payload': True}),
        ('abc', {'payload': False}),
    ])
    @patch('utils.requests.get')
    def test_org(self, org: str, payload: Dict, mock_get: Mock):
        """Tests that GithubOrgClient.org returns the correct value"""
        mock_get.return_value.json.return_value = payload
        cls = GithubOrgClient(org)
        self.assertEqual(cls.org, payload)

    @parameterized.expand([
        ('google', {'repos_url': 'https://api.github.com/orgs/google'}),
        ('abc', {'repos_url': 'https://api.github.com/orgs/abc'}),
    ])
    def test_public_repos_url(self, org: str, expected: Dict):
        """Tests that GithubOrgCLient._public_repos_url works correctly"""
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = expected
            cls = GithubOrgClient(org)
            self.assertEqual(cls._public_repos_url, expected['repos_url'])
