from ThreadedServer import *

class ExtendedServer(ThreadedServer):
    
    client_map = {}

    CMD_REGISTER = "reg_client"

    def register_client(self, data):
        #if (data.con)
        pass
        pass

    def on_receive(self, client, address):
        if CMD_REGISTER in self.data:
            self.register_client(self.data)
            pass

        splitted_data = self.data.split(';')
        if len(splitted_data) >= 3:
            _from = splitted_data[0]
            #_to = 
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