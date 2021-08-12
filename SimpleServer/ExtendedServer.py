from ThreadedServer import *

class ExtendedServer(ThreadedServer):
    
    def on_receive(self, client, address):
        #splitted_data = self.data.split()
        for item in self.clients:
            if item != client:
                item.send(self.data.encode('utf-8'))
        self.print_received(address[0])


if __name__ == '__main__':
    host = socket.gethostbyname(socket.gethostname())
    server = ExtendedServer(host=host, 
                           port=48569, 
                           timeout=None, 
                           sname='CoffeeRobot TCP/IP Server')
    server.start()
    pass