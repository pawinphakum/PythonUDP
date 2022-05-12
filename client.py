import socket
client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# (Optional) if you want specific client port, use this line.
client_sock.bind(('127.0.0.1', 1200))

msg = 'Hello UDP Server'
server_addr = ('127.0.0.1', 1201)
client_sock.sendto(msg.encode('utf-8'), server_addr)
data, addr = client_sock.recvfrom(1024)
print('Server says')
print(str(data))
client_sock.close()