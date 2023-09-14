import socket


def init_server_socket():
    server_socket = socket.socket()
    port = 3030
    server_socket.bind(('', port))
    server_socket.listen(1)
    return server_socket


def main():
    server = init_server_socket()
    while True:
        conn, address = server.accept()  # This acts as a block
        print(f"connection from {address}")

        client_msg = conn.recv(1080).decode()
        print(f"Received msg: {client_msg}")

        conn.send(client_msg.upper().encode())
        conn.close()


if __name__ == '__main__':
    main()
