import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('127.0.0.1', 1201))

while True:
    data, addr = sock.recvfrom(1024)
    print('from '+str(addr))
    print(str(data))
    
    # msg = bytes('Server here!', encoding='utf8')
    #sock.sendto(msg, addr)
    
    msg = 'Server here!'
    
    # option1 sendto origin address
    sock.sendto(msg.encode('utf-8'), addr)

    # option2 forward to another adress
    #sock.sendto(msg.encode('utf-8'), ('127.0.0.1', 1234))