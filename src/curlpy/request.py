import socket
import ssl


def wrap_socket(sock, scheme, host):
    if scheme == "https":
        context = ssl.create_default_context()
        return context.wrap_socket(sock, server_hostname=host)
    return sock


# add agent later
def create_request(method, path, host, data=""):
    path = path or "/"
    request = (
        f"{method} {path} HTTP/1.1\r\n"
        f"Host: {host}\r\n"
        "User-Agent: curlpy/0.1\r\n"
        "Connection: close\r\n"
    )
    if data:
        request += f"Content-Length: {len(data)}\r\n"

    request += "\r\n"
    if data:
        request += data
    return request


def receive_response(sock):
    response = b""
    while True:
        chunk = sock.recv(4096)
        if not chunk:
            break
        response += chunk

    return response


def make_request(request):
    # needs try blocks here
    socket_con = wrap_socket(
        socket.create_connection((request.host, request.port)),
        request.scheme,
        request.host,
    )
    raw_request = create_request(request.method, request.path, request.host, request.data)
    socket_con.sendall(raw_request.encode())
    response = receive_response(socket_con)

    socket_con.close()

    return response
