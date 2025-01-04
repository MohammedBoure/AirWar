import pygame
from pygame.locals import QUIT

BLACK=(0,0,0)
WHITE=(255,255,255)
ORANGE=(178,255,102)
RED=(255,0,0)
size=(800, 600)

clock=pygame.time.Clock()
pygame.init()


surface=pygame.display.set_mode(size)
coor=[300,300] #coor[0] is the y coor for player 1

bg=pygame.transform.scale(pygame.image.load("bg.png"),(800,600))
air1=pygame.transform.scale(pygame.image.load("air1.png"),(100,50))
air2=pygame.transform.scale(pygame.image.load("air2.png"),(100,50))

up=0
down=0
up2=0
down2=0
shots=[]
time=0
time2=0

p1,p2=True,True
cd,cd2=0,0

def hit1():
    if   50<shot[0]<150 and  coor[0]<shot[1]< coor[0]+50 :
        return True
    return False

def hit2():
    if   650<shot[0]<750 and  coor[1]<shot[1]< coor[1]+50 :
        return True
    return False


while True:
    clock.tick(60)
    surface.blit(bg,(0,0))
    if p2:
        surface.blit(air1,(50,coor[0]))
        #pygame.draw.rect(surface,ORANGE,(50,coor[0],100,50))
    if p1:
        surface.blit(air2, (650, coor[1]))
        #pygame.draw.rect(surface, ORANGE, (650, coor[1], 100, 50))
    for shot in shots:
        pygame.draw.circle(surface,RED,(shot[0],shot[1]),5)
        if shot[2]== 1:
            if hit2():
                p1=False

            shot[0]+=30
        if shot[2]==2:
            if hit1():
                p2=False
            shot[0]-=30
    pygame.display.flip()
    time-=1
    time2-=1
    #
    if up2==1:
        coor[1]-=15
    elif down2==1:
        coor[1]+=15
    #
    elif up==1:
        coor[0]-=15
    elif down==1:
        coor[0]+=15
    elif coor[0]>650:
        coor[0]=0
    cd-=1
    cd2-=1
    
    for event in pygame.event.get():
        if (event.type == 768) and (event.key == 122):
            up=1
        if (event.type == 769) and (event.key == 122):
            up=0
        if (event.type == 768) and (event.key == 115):
            down = 1
        if (event.type == 769) and (event.key == 115):
            down = 0
        if (event.type == 768) and (event.key == 98):
            if up==1:
                if 0>cd2:
                    cd2=40
                    coor[0]-=120
            if down==1:
                if 0>cd2:
                    cd2=40
                    coor[0]+=120
                    
        ############
        if (event.type == 768) and (event.key == 1073741906):
            up2=1
        if (event.type == 769) and (event.key == 1073741906):
            up2=0
        if (event.type == 768) and (event.key == 1073741905):
            down2 = 1
        if (event.type == 769) and (event.key == 1073741905):
            down2 = 0
        if (event.type == 768) and (event.key == 1073741920):
            if up2==1:
                if 0>cd:
                    cd=40
                    coor[1]-=120
            if down2==1:
                if 0>cd:
                    cd=40
                    coor[1]+=120
        ###################################"

        if time<0:
            if (event.type == 769) and (event.key == 32):
                shots.append([150,coor[0]+25,1])
                time=20
        if time2<0:
            if (event.type == 769) and (event.key == 1073741917):
                shots.append([650,coor[1]+25,2])
                time2=20
        if (event.type == 769) and (event.key == 114):
            p1,p2=True,True
        if event.type == QUIT:
            quit()

