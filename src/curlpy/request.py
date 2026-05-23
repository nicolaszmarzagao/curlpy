import socket
import ssl


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
