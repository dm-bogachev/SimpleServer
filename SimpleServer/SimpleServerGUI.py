from ThreadedServer import *
import tkinter as tk
import tkinter.ttk as ttk
from datetime import datetime
import socket

class ServerGUIExtension(ThreadedServer):
    """A simple TCP/IP Server extension implementing GUI functions"""

    def __init__(self, host='localhost', port=48569, timeout=60, sname='TCP/IP Server', tkroot=None):
        self.tkroot = tkroot
        if tkroot is not None:
            self.tkroot.title("Server log")
            self.tk_init_treeview()
            self.tk_init_listbox()
        return super().__init__(host=host, port=port, timeout=timeout, sname=sname)

    def print_received(self, client_ip):
        if (self.tkroot != None):
            self.receive_log.insert("", tk.END, values=(datetime.now().strftime('%H:%M:%S'), 
                                                        client_ip, 
                                                        self.data))
            self.receive_log.yview_moveto(1)

    def print(self, msg):
        if self.tkroot is not None:
            if type(msg) == type([]):
                self.connect_log.insert(tk.END, datetime.now().strftime('%H:%M:%S') + ' ' + ' '.join(msg))
            if type(msg) == type(''):
                self.connect_log.insert(tk.END, datetime.now().strftime('%H:%M:%S') + ' ' + msg)
            self.connect_log.see(tk.END)
        else:
            return super().print(msg=msg)

    def tk_init_listbox(self):
        self.connect_log = tk.Listbox(self.tkroot, height=15)
        ysb = ttk.Scrollbar(self.tkroot, orient="vertical",command=self.connect_log.yview)
        self.connect_log.configure(yscrollcommand=ysb.set)
        self.connect_log.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        ysb.grid(row=0, column=1, sticky=tk.N + tk.S)

    def tk_init_treeview(self):
        self.receive_log = ttk.Treeview(self.tkroot, height=21)
        ysb = ttk.Scrollbar(self.tkroot, orient="vertical",command=self.receive_log.yview)
        self.receive_log.configure(yscrollcommand=ysb.set)
        self.receive_log['columns']=('Time', 'From', 'Data')
        self.receive_log.column('#0', width=0, stretch=tk.NO)
        self.receive_log.column('Time', anchor=tk.CENTER, width=60)
        self.receive_log.column('From', anchor=tk.CENTER, width=80)
        self.receive_log.column('Data', width=1000)
        self.receive_log.heading('#0', text='', anchor=tk.CENTER)
        self.receive_log.heading('Time', text='Time', anchor=tk.CENTER)
        self.receive_log.heading('From', text='From', anchor=tk.CENTER)
        self.receive_log.heading('Data', text='Data')
        self.receive_log.grid(row=1, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        ysb.grid(row=1, column=1, sticky=tk.N + tk.S)


if __name__ == '__main__':
    log_root = tk.Tk()
    log_root.geometry('1160x700')
    log_root.resizable(0, 0)
    log_root.protocol('WM_DELETE_WINDOW', log_root.destroy)
    host = socket.gethostbyname(socket.gethostname())
    server = ServerGUIExtension(host=host,
                port=48569, 
                timeout=None, 
                sname='CoffeeRobot TCP/IP Server',
                tkroot=log_root)
    server.start()
    log_root.mainloop()
    print('Now you can close this window')


    





