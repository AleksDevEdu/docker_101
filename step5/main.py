import json
import socket

CONFIG_PATH = 'cfg/config.json'


def read_config(fpath):
    with open(fpath) as f:
        # read as dict
        config = json.load(f)

    return config


def main(config):
    # .get(key, default)
    name = config.get('name', '%DefaultName')
    port = 8080  # Must be in range [1025; 65535]

    s = socket.socket()
    s.bind(('', port))
    while True:
        print(f'Start listening on {port}')
        s.listen(1)
        client_socket, adress = s.accept()
        print(f'Connection from: {str(adress)}')
        while True:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break
            print(f'From user: {data}')
            data = f'Hello from {name}'
            client_socket.send(data.encode('utf-8'))
        client_socket.close()


if __name__ == '__main__':
    config = read_config(CONFIG_PATH)
    main(config)
