from dataclasses import dataclass

@dataclass
class HttpRequest:
    scheme: str
    host: str
    port: int
    path: str
    method: str
