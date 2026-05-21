from .models import HttpRequest
from urllib.parse import urlparse

def get_default_port(scheme):
    if scheme == "https": 
        return 443
    elif scheme == "http": 
        return 80
    else:
        raise ValueError("Unsupported scheme")

def valid_method(method):
    return method in ['GET']

def decide_port(url_port, arg_port, scheme):
    if arg_port is not None:
        port = arg_port
    elif url_port is not None:
        port = url_port
    else:
        port = get_default_port(scheme)

    return port

def create_request(args):
    parsed_url = urlparse(args.url)
    port       = decide_port(parsed_url.port, args.port, args.scheme)

    if not valid_method(args.method):
        raise ValueError("Unsupported method")

    return HttpRequest(
        scheme=parsed_url.scheme,
        host=parsed_url.hostname,
        port=port,
        path=parsed_url.path,
        method=args.method
    )
