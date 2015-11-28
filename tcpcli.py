from sys import argv
import socket

script, data = argv

target_host = "127.0.0.1"
target_port = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_host, target_port))

client.send(data)

response = client.recv(4096)

print response

