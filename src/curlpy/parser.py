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
    if method not in ["GET", "POST"]:
        raise ValueError(f"Unsupported method: {method}")


def parse_args(args, parsed_url):
    return HttpRequest(
        scheme=get_scheme(parsed_url.scheme),
        host=parsed_url.hostname,
        port=get_port(args.port, parsed_url.port, parsed_url.scheme),
        path=parsed_url.path or "/",
        method=get_method(args.method, args.data),
        data=args.data or "",
    )


def get_scheme(scheme):
    if scheme:
        valid_scheme(scheme)
        return scheme
    return "http"


def get_port(args_port, url_port, scheme):
    if args_port:
        return args_port
    elif url_port:
        return url_port
    return get_default_port(scheme)


def get_method(args_method, args_data):
    if args_method:
        valid_method(args_method)
        return args_method
    elif args_data:
        return "POST"
    return "GET"


def create_request(args):
    return parse_args(args, urlparse(normalize_url(args.url)))
