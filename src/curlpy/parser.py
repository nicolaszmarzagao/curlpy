from .models import HttpRequest
from urllib.parse import urlparse

def get_default_port(scheme):
    if scheme == "https": 
        return 443
    else: 
        return 80

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
