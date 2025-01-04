import socket
import pygame
from pygame.locals import QUIT
from time import sleep
import random
HOST = "192.168.18.135"
PORT = 8000


pygame.init()
size = (800,600)
X = size[0]
Y = size[1]
surface=pygame.display.set_mode(size)
clock=pygame.time.Clock()

def data_set(data):
    return data.split("-")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.connect((HOST, PORT))
    except:
        s.connect((HOST, PORT+1))
    surface.fill((0,0,0))
    pygame.display.flip()
    list_bullit = []
    num_cicle = 0
    while True:
        num_cicle += 1

        s.sendall("1".encode("ASCII"))
        if num_cicle == 5:
            while True:
                data = s.recv(4060)
                if len(data)<45:
                    break
            num_cicle = 0


        random_bot = random.randint(1, 10)
        if random_bot == 2 or random_bot ==5 or random_bot == 3 or random_bot == 7:
            s.sendall("d".encode("ASCII"))
            s.sendall("U".encode("ASCII"))

            sleep(1)
        if random_bot == 4 or random_bot ==8 or random_bot ==1 or random_bot ==10 :
            s.sendall("u".encode("ASCII"))
            s.sendall("D".encode("ASCII"))

            sleep(1)

        data = s.recv(9).decode("ASCII")


        if not data:
            continue

        try:
            x, y, z = data_set(data)
        except:
            pass
        list_bullit.append(z)

        if list_bullit[len(list_bullit)-1]!= list_bullit[len(list_bullit)-2] and int(x)-int(y)<0:
            s.sendall("d".encode("ASCII"))
            s.sendall("U".encode("ASCII"))
            sleep(0.2)


        if list_bullit[len(list_bullit)-1]!=list_bullit[len(list_bullit)-2] and int(x)-int(y)>0:
            s.sendall("u".encode("ASCII"))
            s.sendall("D".encode("ASCII"))
            sleep(0.2
                  )

        if int(x)>int(y):
            s.sendall("D".encode("ASCII"))
            if int(x)<int(y):
                s.sendall("d".encode("ASCII"))

        if int(x)<int(y):
            s.sendall("U".encode("ASCII"))
            if int(x) > int(y):
                s.sendall("u".encode("ASCII"))

        if abs(int(x)-int(y)) < 250 and abs(int(x)-int(y)) > 50:
            print("------------")
            s.sendall("1".encode("ASCII"))
            sleep(0.15)
            s.sendall("1".encode("ASCII"))




        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()

                                                    #Uu Dd 1 p
                                                     #s.sendall("U".encode("ASCII"))
