import argparse
import unittest

from curlpy.models import HttpRequest
from curlpy.parser import create_request


class TestParser(unittest.TestCase):
    def test_create_request_simple_case(self):
        n = argparse.Namespace(
            url="https://example.com/",
            port=80,
            method="GET",
        )

        result = create_request(n)
        answer = HttpRequest(
            scheme="https", host="example.com", port=80, path="/", method="GET"
        )
        self.assertEqual(result, answer)

    def test_create_request_value_error(self):
        n = argparse.Namespace(
            url="https://example.com",
            port=80,
            method="NOTAMETHOD",
        )

        with self.assertRaises(ValueError):
            create_request(n)

        n.url = "xxx://example.com"
        n.method = "GET"

        with self.assertRaises(ValueError):
            create_request(n)

    def test_create_request_post_case(self):
        n = argparse.Namespace(url="example.com", data="test=data")
        result = create_request(n)
        answer = HttpRequest(
            scheme="http",
            host="example.com",
            port=80,
            path="/",
            method="POST",
            data="test=data",
        )

        self.assertEqual(result, answer)
