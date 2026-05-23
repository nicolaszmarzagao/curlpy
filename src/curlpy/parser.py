from urllib.parse import urlparse

from .models import HttpRequest

def normalize_url(url):
    if "://" not in url:
        return "http://" + url
    return url

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
    parsed_url = urlparse(normalize_url(args.url))

    scheme = parsed_url.scheme
    if hasattr(args, "scheme"):
        valid_scheme(parsed_url.scheme)
    else:
        scheme = "http"

    port = decide_port(parsed_url.port, args.port, scheme)

    if hasattr(args, "method"):
        method = args.method
        if not valid_method(method):
            raise ValueError("Unsupported method")
    else:
        method = "GET"

    return HttpRequest(
        scheme=scheme,
        host=parsed_url.hostname,
        port=port,
        path=parsed_url.path,
        method=method,
    )
