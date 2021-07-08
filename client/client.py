import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.connect(('192.168.1.46', 5555))
print('Client => 192.168.1.46:5555')

config = {
    'name':'Super'
}

connection_msg = '< ' + config['name'] + ' connected >'
client_socket.sendall(str.encode(connection_msg))

while True:
    data = client_socket.recv(1024)

    print(data.decode('utf-8'))

    if not data:
        break

client_socket.close()