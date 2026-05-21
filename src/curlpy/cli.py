import argparse
import socket
import ssl
from urllib.parse import urlparse

def get_default_port(scheme):
    if scheme == "https": 
        return 443
    else: 
        return 80

def main() -> None:
    parser = argparse.ArgumentParser(
        prog="curlpy",
        description="A implementation of curl with Python3",
    )

    parser.add_argument("url", type=str, help="URL curl will connect to.")
    parser.add_argument(
        "-p", "--port", 
        type=int, help="Port that curl will connect to."
    )

    args = parser.parse_args()
    parsed_url = urlparse(args.url)

    if args.port is not None:
        port = args.port
    elif parsed_url.port is not None:
        port = parsed_url.port
    else:
        port = get_default_port(parsed_url.scheme)

    s = socket.create_connection((parsed_url.hostname, port))
    if parsed_url.scheme == "https":
        context = ssl.create_default_context()
        s = context.wrap_socket(s, server_hostname=parsed_url.hostname)

    get_request = (
        f"GET {parsed_url.path} HTTP/1.1\r\n"
        f"Host: {parsed_url.hostname}\r\n"
        f"User-Agent: curlpy/0.1\r\n"
        f"Connection: close\r\n"
        f"\r\n"
    )
    s.sendall(get_request.encode())

    response = b""
    while True:
        chunk = s.recv(4096)
        if not chunk:
            break
        response += chunk

    s.close()

    print(response.decode(errors="replace").split("\r\n\r\n")[1])


