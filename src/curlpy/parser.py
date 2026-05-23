from urllib.parse import urlparse

from .models import HttpRequest


def get_default_port(scheme):
    if scheme == "https":
        return 443
    else:
        return 80


def valid_scheme(scheme):
    if scheme == "http" or scheme == "https":
        return True
    else:
        raise ValueError("Unsupported scheme")


def valid_method(method):
    return method in ["GET"]


def decide_port(url_port, arg_port, scheme):
    valid_scheme(scheme)
    if arg_port is not None:
        port = arg_port
    elif url_port is not None:
        port = url_port
    else:
        port = get_default_port(scheme)

    return port


def create_request(args):
    parsed_url = urlparse(args.url)

    valid_scheme(parsed_url.scheme)

    port = decide_port(parsed_url.port, args.port, parsed_url.scheme)
    method = args.method

    if method is None:
        method = "GET"
    elif not valid_method(method):
        raise ValueError("Unsupported method")

    return HttpRequest(
        scheme=parsed_url.scheme,
        host=parsed_url.hostname,
        port=port,
        path=parsed_url.path,
        method=method,
    )
