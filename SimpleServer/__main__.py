import Server

if __name__ == '__main__':
    server = Server.Server(host='192.168.0.248', 
                           port=48569, 
                           timeout=None, 
                           sname='CoffeeRobot TCP/IP Server')
    server.start()