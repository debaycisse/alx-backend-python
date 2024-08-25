#!/usr/bin/env python3
"""This module houses definition of the tests for the util.py module"""
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import memoize

import unittest
import utils


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
        self.assertEqual(utils.access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ["a"]),
        ({"a": 1}, ["a", "b"]),
        ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Tests that excecption is raised for non-existing key(s)"""
        with self.assertRaises(KeyError):
            utils.access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Tests get_json function with various inputs"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """Tests the get_json function, using mock object"""
        with patch('utils.requests.get') as mocked_get:
            mocked_get.return_value.json.return_value = test_payload

            utils.get_json(test_url)
            mocked_get.assert_called_once_with(test_url)

            self.assertEqual(utils.get_json(test_url), test_payload)


class TestMemoize(unittest.TestCase):
    """Tests the memoize function, which demonstrate the memoize concept"""

    def test_memoize(self):
        """A test unit for the memoize function"""

        class TestClass:
            """This class is used for testing the memoize function"""

            def a_method(self):
                """This method is used along with the class for the testing"""
                return 42

            @memoize
            def a_property(self):
                """A property, used for testing the memoize wrapping"""
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mk_a_mtd:
            t_cls = TestClass()
            t_cls.a_property()
            t_cls.a_property()

            mk_a_mtd.assert_called_once()
