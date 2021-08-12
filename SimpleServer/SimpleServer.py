from ThreadedServer import *

if __name__ == '__main__':
    host = socket.gethostbyname(socket.gethostname())
    server = ThreadedServer(host=host, 
                           port=48569, 
                           timeout=None, 
                           sname='CoffeeRobot TCP/IP Server')
    server.start()
    pass