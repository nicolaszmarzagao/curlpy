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
    return method in ["GET", "POST"]


def create_request(args):
    parsed_url = urlparse(normalize_url(args.url))

    scheme = parsed_url.scheme
    if hasattr(parsed_url, "scheme"):
        valid_scheme(parsed_url.scheme)
    else:
        scheme = "http"

    port = get_default_port(parsed_url.scheme)
    if hasattr(args, "port") and args.port:
        port = args.port
    elif parsed_url.port:
        port = parsed_url.port
    
    method = "GET"
    if hasattr(args, "method"):
        method = args.method
        if not valid_method(method):
            raise ValueError("Unsupported method")

    data = ""
    if hasattr(args, "data"):
        data = args.data
        method = "POST"

    return HttpRequest(
        scheme=scheme,
        host=parsed_url.hostname,
        port=port,
        path=parsed_url.path or "/",
        method=method,
        data=data,
    )
