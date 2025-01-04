import threading
import socket
from config import server_controler,HOST,PORT
#------server--------------

if server_controler:
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        try:
            s.bind((HOST,PORT))
            print("host:8000")
        except:
            print("host:8001")
            PORT = 8001
            s.bind((HOST, PORT))
        s.listen()
        data_line_1 = s.accept()[0]
        print("cnnecte player 1")
        s.listen()
        data_line_2 = s.accept()[0]
        print("connecet player 2")
else:
    data_line_1 = 0
    data_line_2 = 0

#---------threading---------
list1 = []
list2 = []
def recv1(data_line_1):
    while True:
        data = data_line_1.recv(16).decode("ASCII")
        data = [data[i] for i in range(len(data))]
        for i in range(len(data)):
            list1.append(data[i])
def recv2(data_line_2):
    while True:
        data = data_line_2.recv(16).decode("ASCII")
        data = [data[i] for i in range(len(data))]
        for i in range(len(data)):
            list2.append(data[i])

x = threading.Thread(target=recv1, args=(data_line_1,))
y = threading.Thread(target=recv2, args=(data_line_2,))