import socket
from threading import Thread

class Server(Thread):
    """A simple TCP/IP Server which receives data from client and redirect it to all other connected clients"""
    
    clients = []

    def __init__(self, host='localhost', port=48569, timeout=60, sname='TCP/IP Server'):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.sname = sname
        Thread.__init__(self)
        print(self.sname + ' was initialized')

    def run(self):
        print(self.sname + ' was started')
        self.listen()

    def bind(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))
        
    def listen(self):
        self.bind()
        self.sock.listen(5)
        print(self.sname + ' is listening')

        while True:
            client, address = self.sock.accept()
            client.settimeout(self.timeout)
            self.clients.append(client)
            Thread(target=self.client_handle, args=(client, address,)).start()

    def client_handle(self, client, address):
        buf_size = 4096

        print(' '.join(['Client connected with IP:', address[0], 'Port:', str(address[1])]))

        while True:
            try:
                data = client.recv(buf_size).decode('utf-8')
                if data:
                    print(' '.join(['Received data from', address[0] + ':', data]))
                    for item in self.clients:
                        if item != client:
                            item.send(data.encode('utf-8'))
                else:
                    raise error('Client disconnected')

            except:
                print(' '.join(['Client with IP:', address[0], 'was disconnected!']))
                self.clients.remove(client)
                client.close()
                return False

if __name__ == '__main__':
    server = Server(host='192.168.0.248', 
                           port=48569, 
                           timeout=None, 
                           sname='CoffeeRobot TCP/IP Server')
    server.start()