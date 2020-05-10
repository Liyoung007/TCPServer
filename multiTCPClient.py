import socket

host_port = 'localhost', 8888
sk = socket.socket()
sk.connect(host_port)
while True:
    msg = input('>>:').strip()
    sk.sendall(msg)
    server_reply = sk.recv(1024)
    print('server reply:' + server_reply)
sk.close()
