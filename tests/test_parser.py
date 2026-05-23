import argparse
import unittest

from curlpy.models import HttpRequest
from curlpy.parser import create_request, decide_port


class TestParser(unittest.TestCase):
    def test_decide_port(self):
        self.assertEqual(decide_port(8080, None, "http"), 8080, "Testing url_port.")
        self.assertEqual(decide_port(None, 8000, "http"), 8000, "Testing arg_port.")
        self.assertEqual(decide_port(None, None, "http"), 80, "Testing http scheme.")
        self.assertEqual(decide_port(None, None, "https"), 443, "Testing https scheme.")

    def test_decide_port_value_error(self):
        with self.assertRaises(ValueError):
            decide_port(None, None, None)
        with self.assertRaises(ValueError):
            decide_port(None, None, "htp")

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


if __name__ == "__main__":
    unittest.main()
