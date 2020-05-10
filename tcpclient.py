import socket

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
clientHost = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientHost.connect((host, port))

while True:
    cmd = input('cmd:')
    if len(cmd) == 0:
        continue
    if cmd == 'q':
        break
    clientHost.sendall(cmd.encode('utf-8'))
    server_ack_msg = clientHost.recv(BUFFER_SIZE)
    cmd_res_size = int(server_ack_msg.decode('utf-8').split('|')[1])
    print(server_ack_msg.decode('utf-8'))
    if server_ack_msg.decode('utf-8').split('|')[0] == 'cmd result size is ':
        print('hello')
        clientHost.sendall("client_ready_to_recv".encode('utf-8'))
    res = ''
    recv_size = 0
    while recv_size < cmd_res_size:
        data = clientHost.recv(BUFFER_SIZE)
        recv_size += len(data)
        res += data.decode('utf-8')
    else:
        print(res)
clientHost.close()
