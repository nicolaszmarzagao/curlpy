import unittest

from curlpy.request import create_request, make_request, receive_response, wrap_socket


# Helper class
class FakeSocket:
    def __init__(self, chunks):
        self.chunks = chunks

    def recv(self, size):
        return self.chunks.pop(0)


class TestRequest(unittest.TestCase):
    def test_create_request_root_path(self):
        result = create_request("GET", "/", "google.com")

        self.assertEqual(
            result,
            "GET / HTTP/1.1\r\n"
            "Host: google.com\r\n"
            "User-Agent: curlpy/0.1\r\n"
            "Connection: close\r\n"
            "\r\n",
        )

    def test_create_request_empty_path_defaults_to_root(self):
        result = create_request("GET", "", "google.com")

        self.assertTrue(result.startswith("GET / HTTP/1.1\r\n"))

    def test_receive_response_reads_until_empty_chunk(self):
        fake_socket = FakeSocket(
            [
                b"HTTP/1.1 200 OK\r\n",
                b"\r\n",
                b"Hello",
                b"",
            ]
        )

        result = receive_response(fake_socket)

        self.assertEqual(result, b"HTTP/1.1 200 OK\r\n\r\nHello")

    def test_wrap_socket_http_returns_original_socket(self):
        fake_socket = object()

        result = wrap_socket(fake_socket, "http", "example.com")

        self.assertIs(result, fake_socket)
