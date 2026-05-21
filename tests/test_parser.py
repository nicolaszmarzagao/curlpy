import unittest
import argparse
from curlpy.parser import decide_port, create_request

class TestParser(unittest.TestCase):
    def test_decide_port(self):
        self.assertEqual(
            decide_port(8080, None, "http"),
            8080,
            "Testing url_port."
        )
        self.assertEqual(
            decide_port(None, 8000, "http"),
            8000,
            "Testing arg_port."
        )
        self.assertEqual(
            decide_port(None, None, "http"),
            80,
            "Testing http scheme."
        )
        self.assertEqual(
            decide_port(None, None, "https"),
            443,
            "Testing https scheme."
        )

    def test_decide_port_value_error(self):
        with self.assertRaises(ValueError):
            decide_port(None, None, None)
        with self.assertRaises(ValueError):
            decide_port(None, None, "htp")

    def test_create_request_simple_case(self):
        n = argparse.Namespace(
            url="https://example.com",
            port=80,
            method="GET",
        )

        # cant do one equals the other because they have diffrent attributes
        self.assertEqual(
            create_request(n).port,
            80,
        )
    
    def test_create_request_value_error(self):
        n = argparse.Namespace (
            url="https://example.com",
            port=80,
            method="NOTAMETHOD",
        )

        with self.assertRaises(ValueError):
            create_request(n)
            
        n.url ="xxx://example.com"
        n.method = "GET"

        with self.assertRaises(ValueError):
            create_request(n)

if __name__ == '__main__':
    unittest.main()        
