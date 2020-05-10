import socketserver


class Handler(socketserver.BaseRequestHandler):
    def handle(self):
        print('new conn: %s' % str(self.client_address))
        while True:
            data = self.request.recv(1024)
            if not data:
                break
            else:
                print('client said:' + data)
                self.request.sendall(data)


if __name__ == '__main__':
    host, port = 'localhost', 8888
    server = socketserver.ThreadingTCPServer((host, port), Handler)
    server.serve_forever()
