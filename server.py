import socket
import threading

def handle_client(client_socket):
    try:
        while True:
            message = client_socket.recv(1024).decode('utf-8')
            if message == 'quit':
                break
            print(f'Received: {message}')
            client_socket.send(message.encode('utf-8'))
    finally:
        client_socket.close()

def start_server(host='localhost', port=65432):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f'Server listening on {host}:{port}')

    try:
        while True:
            client_socket, addr = server.accept()
            print(f'Connection from {addr}')
            client_handler = threading.Thread(target=handle_client, args=(client_socket,))
            client_handler.start()
    finally:
        server.close()

if __name__ == '__main__':
    start_server()
