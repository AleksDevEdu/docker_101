import socket


def main():
    host = 'localhost'
    port = 8080

    s = socket.socket()
    s.connect((host, port))

    while True:
        message = input('==> ')
        s.send(message.encode('utf-8'))
        data = s.recv(1024).decode('utf-8')
        print(f'Received from server: {data}')
    s.close()


if __name__ == '__main__':
    main()
