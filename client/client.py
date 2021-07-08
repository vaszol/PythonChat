import socket
import json

chat = []
my_msg = []

with open('config.json') as json_file:
    config = json.load(json_file)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.connect((config['ip'], config['port']))
connection_msg = '< ' + config['name'] + ' connected >'
client_socket.sendall(str.encode(connection_msg))
my_msg.append(connection_msg)

with open('template.txt') as file:
    template_reset = file.read()

with open('chat.txt', 'w') as file:
    file.write('<! You logged in as: ' + config['name'] + ' !>\n')
    file.write(template_reset)

try:
    while True:
        data = client_socket.recv(1024)

        print(data.decode('utf-8'))

        if not data:
            break
except KeyboardInterrupt:
    disconnection_msg = '< ' + config['name'] + ' disconnected >'
    client_socket.sendall(str.encode(disconnection_msg))
    my_msg.append(disconnection_msg)
    client_socket.close()
    with open('chat.txt', 'w') as file:
        file.write('')
