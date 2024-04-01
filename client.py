import socket

def start_client(server_host='localhost', server_port=65432):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_host, server_port))

    try:
        while True:
            message = input('Enter message: ')
            client.send(message.encode('utf-8'))
            if message == 'quit':
                break
            response = client.recv(1024).decode('utf-8')
            print(f'Server response: {response}')
    finally:
        client.close()

if __name__ == '__main__':
    start_client()
