import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(('0.0.0.0', 12345))
print('Bind UDP on 12345...')
while True:
    data, addr = s.recvfrom(1024)
    s.sendto(data, addr)
