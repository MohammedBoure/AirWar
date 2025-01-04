import socket
import pygame


HOST = "192.168.43.144"
PORT = 8000

def hit(hitbox,point): #(a,b) ,(x,y,dx,dy)
     a,b=point
     a*=X
     b*=Y
     x,y,dx,dy=hitbox
     if x<=a<=x+dx and y<=b<=y+dy:
         return True
     return False


pygame.init()
size = pygame.display.get_desktop_sizes()[0]
X = size[0]
Y = size[1]
surface=pygame.display.set_mode(size)
clock=pygame.time.Clock()

class hitbox:
    top_left = (0,0,X//2,Y//2)
    bot_left = (0,Y//2,X//2,Y//2)
    top_right = (X//2,0,X//2,Y//2)
    bot_right = (X//2,Y//2,X//2,Y//2)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    surface.fill((0,0,0))
    pygame.display.flip()
    while True:
        for e in pygame.event.get():
            if e.type==1792:
                if hit(hitbox.top_left,(e.x,e.y)):
                    s.sendall("U".encode("ASCII"))
                if hit(hitbox.bot_left,(e.x,e.y)):
                    s.sendall("D".encode("ASCII"))
                if hit(hitbox.bot_right, (e.x, e.y)):
                    s.sendall("1".encode("ASCII"))
                if hit(hitbox.top_right,(e.x,e.y)):
                    s.sendall("p".encode("ASCII"))
            if e.type==1793:
                if hit(hitbox.top_left,(e.x,e.y)):
                    s.sendall("u".encode("ASCII"))
                if hit(hitbox.bot_left,(e.x,e.y)):
                    s.sendall("d".encode("ASCII"))
