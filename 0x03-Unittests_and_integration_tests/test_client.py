#!/usr/bin/env python3
"""This modules houses the definition of a class that tests the
GithubOrgClient class, defined in the client.py module"""
import unittest
from client import GithubOrgClient
from unittest.mock import patch
from utils import get_json
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """This class defines various integration tests for the GithubOrgClient
    class with other components from other module(s)"""

    @parameterized.expand([
        ('google', {'payload': True}),
        ('abc', {'payload': False}),
    ])
    @patch('utils.requests.get')
    def test_org(self, org, payload, mock_get):
        """Tests that GithubOrgClient.org returns the correct value"""
        mock_get.return_value.json.return_value = payload
        cls = GithubOrgClient(org)
        self.assertEqual(cls.org, payload)
