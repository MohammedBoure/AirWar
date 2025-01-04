import pygame
from pygame.locals import QUIT
#~~~~~~~~~~~~~~~~colors
BLACK=(0,0,0)
WHITE=(255,255,255)
ORANGE=(178,255,102)
RED=(255,0,0)
#~~~~~~~~~~~~~~~~
clock=pygame.time.Clock()
pygame.init()
size=(800, 600)
pygame.display.set_caption("Air_War")
surface=pygame.display.set_mode(size)
#~~~~~~~~~~~~~~~~images
background=pygame.transform.scale(pygame.image.load("dist/bg.png"), (800, 600))
air1L=pygame.transform.scale(pygame.image.load("dist/air01.png"), (60, 60))
air1R=pygame.transform.scale(pygame.image.load("dist/air02.png"), (60, 60))
#~~~~~~~~~~~~~~~~
def hit1():
    if   50<shot[0]<150 and  coor[0]<shot[1]< coor[0]+50 :
        return True
    return False

def hit2():
    if   650<shot[0]<750 and  coor[1]<shot[1]< coor[1]+50 :
        return True
    return False
#~~~~~~~~~~~~~~~~
def move():
    c=coor
    if up[0]==1:
        c[0]-=move_speed[0]
    if down[0]==1:
        c[0]+=move_speed[0]
    if coor[0]>600:
        c[0]=-50
    if coor[0]<-50:
        c[0]=600
    if up[1]==1:
        c[1]-=move_speed[1]
    if down[1]==1:
        c[1]+=move_speed[1]
    if coor[1]>600:
        c[1]=-50
    if coor[1]<-50:
        c[1]=600
    return c
#--------------
def printt(strr,c):
    font = pygame.font.Font(None,30)
    text = font.render(str(strr),True,WHITE)
    surface.blit(text,c)
#~~~~~~~~~~~~~~~~
coor=[300,300]
up=[0,0]
down=[0,0]
skillcd=[0,0]
shotcd=[0,0]
shots=[]
p1,p2=True,True
score=[0,0]
#~~~~~~~~~~~~~~~~
move_speed=[15,15]
shot_speed=30
#~~~~~~~~~~~~~~~~


while True:
    clock.tick(60)
    surface.blit(background, (0, 0))
    printt(score,(380,30))
    if not skillcd[0]<0:
        printt(skillcd[0],(20,570))
    else:
        printt(0, (20, 570))
    if not skillcd[1]<0:
        printt(skillcd[1],(755,570))
    else:
        printt(0, (755, 570))
    #surface.fill(BLACK)
    if p2:
        surface.blit(air1L, (50, coor[0]))
        #pygame.draw.rect(surface,ORANGE,(50,coor[0],100,50))
    if p1:
        surface.blit(air1R, (650, coor[1]))
        #pygame.draw.rect(surface, ORANGE, (650, coor[1], 100, 50))
    for shot in shots:
        pygame.draw.circle(surface,RED,(shot[0],shot[1]),5)
        if shot[2]==1:
            if hit2() and p1:
                p1=False
                score[0]+=1
            shot[0]+=shot_speed
        if shot[2]==2:
            if hit1() and p2:
                p2=False
                score[1]+=1
            shot[0]-=shot_speed
    pygame.display.flip()
    coor=move()
    skillcd[0]-=1
    skillcd[1]-=1
    shotcd[0]-=1
    shotcd[1]-=1
    for event in pygame.event.get():
        if (event.type == 768) and (event.key == 122):
            up[0]=1
        if (event.type == 769) and (event.key == 122):
            up[0]=0
        if (event.type == 768) and (event.key == 115):
            down[0] = 1
        if (event.type == 769) and (event.key == 115):
            down[0] = 0
        if (event.type == 768) and (event.key == 98):
            if up[0]==1:
                if 0>skillcd[0]:
                    skillcd[0]=60
                    coor[0]-=80
            if down[0]==1:
                if 0>skillcd[0]:
                    skillcd[0]=60
                    coor[0]+=80
        ############
        if (event.type == 768) and (event.key == 1073741906):
            up[1]=1
        if (event.type == 769) and (event.key == 1073741906):
            up[1]=0
        if (event.type == 768) and (event.key == 1073741905):
            down[1] = 1
        if (event.type == 769) and (event.key == 1073741905):
            down[1] = 0
        if (event.type == 768) and (event.key == 1073741920):
            if up[1]==1:
                if 0>skillcd[1]:
                    skillcd[1]=60
                    coor[1]-=80
            if down[1]==1:
                if 0>skillcd[1]:
                    skillcd[1]=60
                    coor[1]+=80
        ###################################

        if shotcd[0]<0 and p2:
            if (event.type == 769) and (event.key == 32):
                shots.append([150,coor[0]+25,1])
                shotcd[0]=15
        if shotcd[1]<0 and p1:
            if (event.type == 769) and (event.key == 1073741917):
                shots.append([650,coor[1]+25,2])
                shotcd[1]=15
        if (event.type == 769) and (event.key == 114):
            p1,p2=True,True
        if event.type == QUIT:
            quit()
