import argparse
import unittest

from curlpy.models import HttpRequest
from curlpy.parser import create_request, normalize_url


def make_args(**kwargs):
    defaults = dict(url="example.com", method=None, data=None, port=None)
    return argparse.Namespace(**{**defaults, **kwargs})


class TestParser(unittest.TestCase):
    def test_create_request_default(self):
        result = create_request(make_args(url="example.com"))
        self.assertEqual(result.scheme, "http")
        self.assertEqual(result.host, "example.com")
        self.assertEqual(result.port, 80)
        self.assertEqual(result.method, "GET")
        self.assertEqual(result.data, "")

    def test_create_request_with_data_defaults_to_post(self):
        result = create_request(make_args(url="example.com", data="test=data"))
        self.assertEqual(result.method, "POST")

    def test_https_url(self):
        result = create_request(make_args(url="https://example.com"))
        self.assertEqual(result.scheme, "https")

    def test_url_with_explicit_port(self):
        result = create_request(make_args(url="example.com:8080"))
        self.assertEqual(result.port, 8080)

    def test_url_with_path(self):
        result = create_request(make_args(url="example.com/hello"))
        self.assertEqual(result.path, "/hello")


