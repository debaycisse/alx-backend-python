#!/usr/bin/env python3
"""This module houses definition of the tests for the util.py module"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """This class via its inheritance of the TestCase
    tests a function in the utils's module"""

    @parameterized.expand([
        ({"a": 1}, ["a"], 1),
        ({"a": {"b": 2}}, ["a"], {"b": 2}),
        ({"a": {"b": 2}}, ["a", "b"], 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Tests access_nested_map function, with each of the parameters"""
        self.assertEqual(access_nested_map(nested_map, path), expected)
