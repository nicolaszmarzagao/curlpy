import argparse
import socket
import ssl
from urllib.parse import urlparse
from dataclasses import dataclass

@dataclass
class HttpRequest:
    scheme: str
    host: str
    port: int
    path: str
    method: str

def get_default_port(scheme):
    if scheme == "https": 
        return 443
    else: 
        return 80

def remove_header(output):

    return output

def setup_arguments():
    parser = argparse.ArgumentParser(
        prog="curlpy",
        description="A implementation of curl with Python3",
    )
    parser.add_argument(
        "url", type=str, 
        help="URL curl will connect to."
    )
    parser.add_argument(
        "-p", "--port", 
        type=int, help="Port that curl will connect to."
    )
    parser.add_argument(
        "-i", "--include-headers",
        action="store_true", help="Keeps HTTP header in output."
    )

    return parser

def parse_arguments(parser):
    args = parser.parse_args()
    parsed_url = urlparse(args.url)

    if args.port is not None:
        port = args.port
    elif parsed_url.port is not None:
        port = parsed_url
    else:
        port = get_default_port(parsed_url.scheme)

    request = HttpRequest(
        scheme=parsed_url.scheme,
        host=parsed_url.hostname,
        port=port,
        path=parsed_url.path,
        method="GET"
    )

    return request

def make_request(request):
    s = socket.create_connection((request.host, request.port))

    if request.scheme == "https":
        context = ssl.create_default_context()
        s = context.wrap_socket(s, server_hostname=request.host)

    r = (
        f"{request.method} {request.path} HTTP/1.1\r\n"
        f"Host: {request.host}\r\n"
        f"User-Agent: curlpy/0.1\r\n"
        f"Connection: close\r\n"
        f"\r\n"
    )

    s.sendall(r.encode())

    response = b""
    while True:
        chunk = s.recv(4096)
        if not chunk:
            break
        response += chunk

    s.close()

    return response


def main() -> None:
    parser     = setup_arguments()
    request    = parse_arguments(parser)
    response   = make_request(request).decode(errors="replace")

    if parser.parse_args().include_headers is False: 
        print(response.split("\r\n\r\n")[1])
    else:
        print(response)


