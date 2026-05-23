import argparse

from .parser import create_request
from .request import make_request


def setup_arguments():
    parser = argparse.ArgumentParser(
        prog="curlpy",
        description="A implementation of curl with Python3",
    )
    parser.add_argument("url", type=str, help="URL curl will connect to.")
    parser.add_argument(
        "-p", "--port", type=int, help="Port that curl will connect to."
    )
    parser.add_argument(
        "-i",
        "--include-headers",
        action="store_true",
        help="Keeps HTTP header in output.",
    )
    parser.add_argument(
        "-X", "--request", type=str, help="HTTP methods to use ie. GET, POST..."
    )

    return parser.parse_args()


def main() -> None:
    args = setup_arguments()
    request = create_request(args)
    response = make_request(request).decode(errors="replace")

    if args.include_headers is False:
        print(response.split("\r\n\r\n")[1])
    else:
        print(response)
