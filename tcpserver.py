import socket
import signal
import sys
import os

# initilize parameter
BACK_LOG = 5
BUFFER_SIZE = 1024

# get hostname and port
host = socket.gethostname()
port = 4002

# print host IP address
hostIP = socket.gethostbyname(host)
print("hostIP: ", hostIP)

# init tcp server
tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create socket object
tcpServer.bind((host, port))  # bind port number
tcpServer.listen(BACK_LOG)  # set max connect number, if timeout aline

while True:
    clientConn, clientAddr = tcpServer.accept()
    print("clientAddr = ", clientAddr)
    while True:
        data = clientConn.recv(BUFFER_SIZE)
        if not data:
            break
        print('receive data:', data.decode('utf-8'))
        response = os.popen(data.decode('utf-8')).read()
        if len(response) == 0:
            clientConn.sendall('command no result!')
        else:
            ack_msg = 'cmd result size is | %s' % len(response)
            clientConn.sendall(ack_msg.encode('utf-8'))
            client_ack = clientConn.recv(BUFFER_SIZE)
            print(client_ack)
            if client_ack.decode('utf-8') == 'client_ready_to_recv':
                clientConn.sendall(response.encode('utf-8'))
    clientConn.close()
