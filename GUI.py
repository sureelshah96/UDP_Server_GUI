import sys
import socket
import time
import datetime
import tkinter as tk
from tkinter import *
from tkinter import ttk
import threading



on = 1
message = 'Hello'

def on_1():
    curr_time = datetime.datetime.now()
    sys_timestamp = float(curr_time.strftime('%S')) + (float(curr_time.strftime('%f')) / 1000000)  #Get UDP_Server Time in seconds
    message = '0'
    client.sendto(message.encode(), ('192.168.1.4',1000))
    

def off_1():
    on = 0
    curr_time = datetime.datetime.now()
    sys_timestamp = float(curr_time.strftime('%S')) + (float(curr_time.strftime('%f')) / 1000000)  #Get UDP_Server Time in seconds
    message = '1'
    client.sendto(message.encode(), ('192.168.1.4',1000))


def on_2():
    curr_time = datetime.datetime.now()
    sys_timestamp = float(curr_time.strftime('%S')) + (float(curr_time.strftime('%f')) / 1000000)  #Get UDP_Server Time in seconds
    message = '0'
    client.sendto(message.encode(), ('192.168.137.195',1000))
    

def off_2():
    on = 0
    curr_time = datetime.datetime.now()
    sys_timestamp = float(curr_time.strftime('%S')) + (float(curr_time.strftime('%f')) / 1000000)  #Get UDP_Server Time in seconds
    message = '1'
    client.sendto(message.encode(), ('192.168.137.195',1000))    

def on_3():
    curr_time = datetime.datetime.now()
    sys_timestamp = float(curr_time.strftime('%S')) + (float(curr_time.strftime('%f')) / 1000000)  #Get UDP_Server Time in seconds
    message = '0'
    client.sendto(message.encode(), ('192.168.137.173',1000))
    

def off_3():
    on = 0
    curr_time = datetime.datetime.now()
    sys_timestamp = float(curr_time.strftime('%S')) + (float(curr_time.strftime('%f')) / 1000000)  #Get UDP_Server Time in seconds
    message = '1'
    client.sendto(message.encode(), ('192.168.137.173',1000))   

def on_4():
    curr_time = datetime.datetime.now()
    sys_timestamp = float(curr_time.strftime('%S')) + (float(curr_time.strftime('%f')) / 1000000)  #Get UDP_Server Time in seconds
    message = '0'
    client.sendto(message.encode(), ('192.168.1.4',1000))
    

def off_4():
    on = 0
    curr_time = datetime.datetime.now()
    sys_timestamp = float(curr_time.strftime('%S')) + (float(curr_time.strftime('%f')) / 1000000)  #Get UDP_Server Time in seconds
    message = '1'
    client.sendto(message.encode(), ('192.168.1.4',1000)) 

def on_5():
    curr_time = datetime.datetime.now()
    sys_timestamp = float(curr_time.strftime('%S')) + (float(curr_time.strftime('%f')) / 1000000)  #Get UDP_Server Time in seconds
    message = '0'
    client.sendto(message.encode(), ('192.168.137.4',1000))
    

def off_5():
    on = 0
    curr_time = datetime.datetime.now()
    sys_timestamp = float(curr_time.strftime('%S')) + (float(curr_time.strftime('%f')) / 1000000)  #Get UDP_Server Time in seconds
    message = '1'
    client.sendto(message.encode(), ('192.168.137.4',1000)) 

def on_6():
    curr_time = datetime.datetime.now()
    sys_timestamp = float(curr_time.strftime('%S')) + (float(curr_time.strftime('%f')) / 1000000)  #Get UDP_Server Time in seconds
    message = '0'
    client.sendto(message.encode(), ('192.168.137.4',1000))
    

def off_6():
    on = 0
    curr_time = datetime.datetime.now()
    sys_timestamp = float(curr_time.strftime('%S')) + (float(curr_time.strftime('%f')) / 1000000)  #Get UDP_Server Time in seconds
    message = '1'
    client.sendto(message.encode(), ('192.168.137.4',1000)) 

def on_7():
    curr_time = datetime.datetime.now()
    sys_timestamp = float(curr_time.strftime('%S')) + (float(curr_time.strftime('%f')) / 1000000)  #Get UDP_Server Time in seconds
    message = '0'
    client.sendto(message.encode(), ('192.168.137.4',1000))
    

def off_7():
    on = 0
    curr_time = datetime.datetime.now()
    sys_timestamp = float(curr_time.strftime('%S')) + (float(curr_time.strftime('%f')) / 1000000)  #Get UDP_Server Time in seconds
    message = '1'
    client.sendto(message.encode(), ('192.168.137.4',1000))  

def milli():
    return round(time.time() * 1000)

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)  # UDP

# Uncomment this if you plan to broadcast from this script
#client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# Set the socket to non blocking, allows the program to continue and not wait for data the whole time
client.setblocking(1)

# Bind to all interfaces and to port 2255
client.bind(('', 2255))

def check_data():
    try:
        # Data received
        data, addr = client.recvfrom(1024)
        # print("received message: %s from %s" % (data,(addr)))

        # return the decoded bytes as a string
        return data.decode(), addr
    # If no data is received just return None
    except socket.error:
        return None

def main():
    # Main loop
    
    while True:
        # Check for UDP data
        # root.update()
        line, addr = check_data()
        # If there is data split it and print it to console
        if line:
            curr_time = datetime.datetime.now()
            sys_timestamp = float(curr_time.strftime('%S')) + (float(curr_time.strftime('%f')) / 1000000)  #Get UDP_Server Time in seconds

            split_line = line.split('|')
            print(split_line, "System Seconds: ", sys_timestamp)
            message = 'Hello' + " System Seconds: "+ str(sys_timestamp)
            # client.sendto(message.encode(), addr)
            # print(sys_timestamp)

        # Continue with main loop
        # print("...")

class MyTkApp():
    def __init__(self):
        # threading.Thread.__init__(self)
        self.root = tk.Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.callback)

        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)
        self.root.columnconfigure(3, weight=1)
        self.root.columnconfigure(4, weight=1)
        self.root.columnconfigure(5, weight=1)
        self.root.columnconfigure(6, weight=1)

        self.root.title("Control Panel")
        self.root.geometry("400x100")

        startButton = tk.Button(self.root,text="ON-1",command=on_1)
        startButton.grid(column=0, row=0, padx=10, pady=10)
        stopButton = tk.Button(self.root,text="OFF-1",command=off_1)
        stopButton.grid(column=0, row=1, padx=10, pady=10)
        startButton2 = tk.Button(self.root,text="ON-2",command=on_2)
        startButton2.grid(column=1, row=0, padx=10, pady=10)
        stopButton2 = tk.Button(self.root,text="OFF-2",command=off_2)
        stopButton2.grid(column=1, row=1, padx=10, pady=10)
        startButton3 = tk.Button(self.root,text="ON-3",command=on_3)
        startButton3.grid(column=2, row=0, padx=10, pady=10)
        stopButton3 = tk.Button(self.root,text="OFF-3",command=off_3)
        stopButton3.grid(column=2, row=1, padx=10, pady=10)

        startButton = tk.Button(self.root,text="ON-4",command=on_4)
        startButton.grid(column=3, row=0, padx=10, pady=10)
        stopButton = tk.Button(self.root,text="OFF-4",command=off_4)
        stopButton.grid(column=3, row=1, padx=10, pady=10)
        startButton2 = tk.Button(self.root,text="ON-5",command=on_5)
        startButton2.grid(column=4, row=0, padx=10, pady=10)
        stopButton2 = tk.Button(self.root,text="OFF-5",command=off_5)
        stopButton2.grid(column=4, row=1, padx=10, pady=10)
        startButton3 = tk.Button(self.root,text="ON-6",command=on_6)
        startButton3.grid(column=5, row=0, padx=10, pady=10)
        stopButton3 = tk.Button(self.root,text="OFF-6",command=off_6)
        stopButton3.grid(column=5, row=1, padx=10, pady=10)

        startButton3 = tk.Button(self.root,text="ON-7",command=on_7)
        startButton3.grid(column=6, row=0, padx=10, pady=10)
        stopButton3 = tk.Button(self.root,text="OFF-7",command=off_7)
        stopButton3.grid(column=6, row=1, padx=10, pady=10)


        # self.start()
        self.root.mainloop()


    def callback(self):
        self.root.quit()

    # def run(self):
        


        # label = tk.Label(self.root, text="Hello World")
        # label.pack()



if __name__ == '__main__':
    try:

        # main()
    # CTRL + C pressed so exit gracefully
        app = MyTkApp()
        # main()

    except KeyboardInterrupt:
        print('Interrupted.')
        # app.callback()
        sys.exit()