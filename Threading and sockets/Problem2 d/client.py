import socket


def main():
    while True:
        client = socket.socket()
        client.connect(('localhost', 3030))

        client_msg = input("Enter a message: ")
        client.send(client_msg.encode())

        server_msg = client.recv(1024).decode()
        print(f"servers msg: {server_msg}")

        client.close()


if __name__ == '__main__':
    main()
