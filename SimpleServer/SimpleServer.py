import socket
from threading import Thread

import ctypes
class Server(Thread):
    """A simple TCP/IP Server which receives data from client and redirect it to all other connected clients"""
    
    clients = []
    threads = []

    def __init__(self, host='localhost', port=48569, timeout=60, sname='TCP/IP Server'):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.sname = sname
        Thread.__init__(self)
        self.print(self.sname + ' was initialized')

    def run(self):
        self.print(self.sname + ' was started')
        self.listen()

    def stop(self):
        pass

    def bind(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))
        self.print([self.sname, 'was bound to IP:', self.host, 'Port:', str(self.port)])
        
    def listen(self):
        self.bind()
        self.sock.listen(5)
        self.print(self.sname + ' is listening')

        while True:
            client, address = self.sock.accept()
            client.settimeout(self.timeout)
            self.clients.append(client)
            thread = Thread(target=self.client_handle, args=(client, address,)).start()
            self.threads.append(thread)

    def on_receive(self, client_ip=''):
        self.print(['Received data from', client_ip + ':', self.data.rstrip('\n')])

    def print(self, msg):
        if type(msg) == type([]):
            print(' '.join(msg))
        if type(msg) == type(''):
            print(msg)

    def client_handle(self, client, address):
        buf_size = 4096

        self.print(['Client connected with IP:', address[0], 'Port:', str(address[1])])

        while True:
            try:
                self.data = client.recv(buf_size).decode('utf-8')
                if self.data:
                    self.on_receive(address[0])
                    for item in self.clients:
                        if item != client:
                            item.send(self.data.encode('utf-8'))
                else:
                    raise error('Client disconnected')

            except Exception as e:
                self.print(['Client with IP:', address[0], 'was disconnected!'])
                self.clients.remove(client)
                client.close()
                return False

if __name__ == '__main__':
    host = socket.gethostbyname(socket.gethostname())
    server = Server(host=host, 
                           port=48569, 
                           timeout=None, 
                           sname='CoffeeRobot TCP/IP Server')
    server.start()
    pass