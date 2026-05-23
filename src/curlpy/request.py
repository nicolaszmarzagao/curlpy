import socket
import ssl


def wrap_socket(socket, scheme, host):
    if scheme == "https":
        context = ssl.create_default_context()
        return context.wrap_socket(socket, server_hostname=host)
    return socket


# add agent later
def create_request(method, path, host):
    path = path or "/"
    return (
        f"{method} {path} HTTP/1.1\r\n"
        f"Host: {host}\r\n"
        f"User-Agent: curlpy/0.1\r\n"
        f"Connection: close\r\n"
        f"\r\n"
    )


def receive_response(socket):
    response = b""
    while True:
        chunk = socket.recv(4096)
        if not chunk:
            break
        response += chunk

    return response


def make_request(request):
    socket_con = wrap_socket(
        socket.create_connection((request.host, request.port)),
        request.scheme,
        request.host,
    )
    request = create_request(request.method, request.path, request.host)
    socket_con.sendall(request.encode())
    response = receive_response(socket_con)

    socket_con.close()

    return response
