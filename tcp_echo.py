import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('0.0.0.0', 12345))
s.listen(5)
print('Bind TCP on 12345...')
while True:
    client, addr = s.accept()
    data = client.recv(1024)
    client.send(data)
    client.close()
