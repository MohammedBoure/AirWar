import pygame
import socket
from pygame.locals import QUIT
import threading

class ev:
    type = 5
#------server--------------
HOST = "192.168.43.75"
PORT = 8000

server_controler = False
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

# -----colors--------------
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (180,20,20)

# -----------------------
size = (800, 600)
surface = pygame.display.set_mode(size)
clock = pygame.time.Clock()

# ---------images-----------
laser_p2,laser_p1=0,0
if True:
    plane0_p1 = pygame.transform.scale(pygame.image.load("images/plane0_p1.png"), (64, 64))
    plane0_p2 = pygame.transform.scale(pygame.image.load("images/plane0_p2.png"), (64, 64))
    plane1_p1 = pygame.transform.scale(pygame.image.load("images/plane1_p1.png"), (64, 64))
    plane1_p2 = pygame.transform.scale(pygame.image.load("images/plane1_p2.png"), (64, 64))
    plane2_p1 = pygame.transform.scale(pygame.image.load("images/plane2_p1.png"), (80, 50))  # 143*90      1.58888/1
    plane2_p2 = pygame.transform.scale(pygame.image.load("images/plane2_p2.png"), (80, 50))
    plane3_p1 = pygame.transform.scale(pygame.image.load("images/plane3_p1.png"), (64, 64))
    plane3_p2 = pygame.transform.scale(pygame.image.load("images/plane3_p2.png"), (64, 64))
    plane4_p1 = pygame.transform.scale(pygame.image.load("images/plane4_p1.png"), (64, 64))
    plane4_p2 = pygame.transform.scale(pygame.image.load("images/plane4_p2.png"), (64, 64))
    bullet_plane0_p2 = pygame.transform.scale(pygame.image.load("images/bullet_plane0_p2.png"), (10, 4))
    bullet_plane0_p1 = pygame.transform.scale(pygame.image.load("images/bullet_plane0_p1.png"), (10, 4))
    bullet_plane1_p2 = pygame.transform.scale(pygame.image.load("images/bullet_plane1_p2.png"), (24, 16))
    bullet_plane1_p1 = pygame.transform.scale(pygame.image.load("images/bullet_plane1_p1.png"), (24, 16))
    bullet_plane2_p2 = pygame.transform.scale(pygame.image.load("images/bullet_plane1_p2.png"), (10, 5))
    bullet_plane2_p1 = pygame.transform.scale(pygame.image.load("images/bullet_plane1_p1.png"), (10, 5))
    
    bullet_plane4_p2 = pygame.transform.scale(pygame.image.load("images/bullet_plane4_p2.png"), (20,20))
    bullet_plane4_p1 = pygame.transform.scale(pygame.image.load("images/bullet_plane4_p1.png"), (25, 25))
    heart = pygame.transform.scale(pygame.image.load("images/heart.png"), (30, 30))
    amo_p1 = pygame.transform.scale(pygame.image.load("images/amo_p1.png"), (25, 10))
    amo_p2 = pygame.transform.scale(pygame.image.load("images/amo_p2.png"), (25, 10))

    mainpage_background = pygame.transform.scale(pygame.image.load("images/mainpage.png"), (800, 600))
    selectpage_background = pygame.transform.scale(pygame.image.load("images/selectpage.jpeg"), (800, 600))
    map1 = pygame.transform.scale(pygame.image.load("images/map1.jpg"), (800, 600))
    map2 = pygame.transform.scale(pygame.image.load("images/map2.jpeg"), (800, 600))
    map3 = pygame.transform.scale(pygame.image.load("images/map3.jpeg"), (800, 600))
    map4 = pygame.transform.scale(pygame.image.load("images/map4.jpeg"), (800, 600))
    map5 = pygame.transform.scale(pygame.image.load("images/map5.jpeg"), (800, 600))
    map6 = pygame.transform.scale(pygame.image.load("images/map6.jpg"), (800, 600))
    map7 = pygame.transform.scale(pygame.image.load("images/map7.jpeg"), (800, 600))
    map8 = pygame.transform.scale(pygame.image.load("images/map8.jpeg"), (800, 600))

    fire1_p1 = pygame.transform.scale(pygame.image.load("images/fire1_p1.png"), (30, 15))
    fire2_p1 = pygame.transform.scale(pygame.image.load("images/fire2_p1.png"), (30, 15))
    fire1_p2 = pygame.transform.scale(pygame.image.load("images/fire1_p2.png"), (30, 15))
    fire2_p2 = pygame.transform.scale(pygame.image.load("images/fire2_p2.png"), (30, 15))

    bullet_plane3_p2 = pygame.transform.scale(pygame.image.load("images/bullet_plane0_p2.png"), (800, 20))
    bullet_plane3_p1 = pygame.transform.scale(pygame.image.load("images/bullet_plane0_p1.png"), (800, 20))

    l = pygame.transform.scale(pygame.image.load("images/l.png"), (800, 20))
    ll = pygame.transform.scale(pygame.image.load("images/l.png"), (800, 20))
    lll = pygame.transform.scale(pygame.image.load("images/ll.png"), (800, 20))
    llll = pygame.transform.scale(pygame.image.load("images/lll.png"), (800, 20))

    k = pygame.transform.scale(pygame.image.load("images/k.png"), (800, 20))
    kk = pygame.transform.scale(pygame.image.load("images/k.png"), (800, 20))
    kkk = pygame.transform.scale(pygame.image.load("images/kk.png"), (800, 20))
    kkkk = pygame.transform.scale(pygame.image.load("images/kkk.png"), (800, 20))

    quit_button = pygame.transform.scale(pygame.image.load("images/quit.png"), (200, 65))
    start_button = pygame.transform.scale(pygame.image.load("images/start.png"), (200, 65))
    setting_button = pygame.transform.scale(pygame.image.load("images/settings.png"), (200, 65))
    pointer_p1_button = pygame.transform.scale(pygame.image.load("images/pointer_p1.png"), (30, 30))
    pointer_p2_button = pygame.transform.scale(pygame.image.load("images/pointer_p2.png"), (30, 30))
    pointer_mainpage_button = pygame.transform.scale(pygame.image.load("images/pointer_mainpage.png"), (30, 30))
    cadre = pygame.transform.scale(pygame.image.load("images/cadre.png"), (100,100))

# ---------planes info-------
fire_p1=[fire1_p1,fire2_p1]
fire_p2=[fire1_p2,fire2_p2]
maps_images = [map1,map2,map3,map4,map5,map6,map7,map8]
planes_images = [[plane0_p1, plane0_p2], [plane1_p1, plane1_p2], [plane2_p1, plane2_p2], [plane3_p1, plane3_p2], [plane4_p1, plane4_p2]]
air_shot_p1 = [[112, 20, bullet_plane0_p1], [112, 40, bullet_plane1_p1], [112, 25, bullet_plane2_p2], [112,0,laser_p1],[112,25,bullet_plane4_p1]]  # [x,speed,image]
air_shot_p2 = [[688, -20, bullet_plane0_p2], [688, -40, bullet_plane1_p2], [688, -25, bullet_plane2_p2], [668,0,laser_p2], [668,-25,bullet_plane4_p2]]
speed = [10, 8, 15, 7, 14]  #
basic_cd = [40, 70, 25, 350, 60]
hp = [5, 5, 3, 7, 3]
bullet_num = [4, 3, 6, 1, 12]
lasers_p2=[l,ll,lll,llll]
lasers_p1=[k,kk,kkk,kkkk]
lcd1,lcd2=(15,15)
time_for_death_out_of_map=100
music_volume = 0.04
sound_volume = 0.07
# ----------keys---
if True:
    def key_down(e):
        if e.type == 768 and e.key == 1073741905:
            return True
        return False


    def key_down_up(e):
        if e.type == 769 and e.key == 1073741905:
            return True
        return False


    def key_right(e):
        if e.type == 768 and e.key == 1073741903:
            return True
        return False


    def key_up(e):
        if e.type == 768 and e.key == 1073741906:
            return True
        return False


    def key_up_up(e):
        if e.type == 769 and e.key == 1073741906:
            return True
        return False


    def key_left(e):
        if e.type == 768 and e.key == 1073741904:
            return True
        return False


    def key_5(e):
        if e.type == 768 and e.key == 1073741917:
            return True
        return False

    def key_9(e):
        if e.type == 768 and e.key == 1073741921:
            return True
        return False


    def key_q(e):
        if e.type == 768 and e.key == 113:
            return True
        return False


    def key_d(e):
        if e.type == 768 and e.key == 100:
            return True
        return False


    def key_z(e):
        if e.type == 768 and e.key == 122:
            return True
        return False


    def key_z_up(e):
        if e.type == 769 and e.key == 122:
            return True
        return False


    def key_s(e):
        if e.type == 768 and e.key == 115:
            return True
        return False


    def key_s_up(e):
        if e.type == 769 and e.key == 115:
            return True
        return False


    def key_g(e):
        if e.type == 768 and e.key == 103:
            return True
        return False

    def key_h(e):
        if e.type == 768 and e.key == 104:
            return True
        return False


    def key_space(e):
        if e.type == 768 and e.key == 32:
            return True
        return False


    def key_entrer(e):
        if e.type == 768 and e.key == 13:
            return True
        return False


    def key_echap(e):
        if e.type == 768 and e.key == 27:
            return True
        return False  ##  ##5555555555555555


# --------------def----------
def mainpage():
    pointer_coor = (200, 280, 360)
    pointer_index = 0  # 0;1;2
    while True:
        clock.tick(25)
        pygame.display.set_caption("mainpage")
        surface.blit(mainpage_background, (0, 0))
        surface.blit(start_button,(300,180))
        surface.blit(setting_button, (300, 260))
        surface.blit(quit_button, (300, 340))
        surface.blit(pointer_mainpage_button, (505, pointer_coor[pointer_index]))

        pygame.display.flip()
        for e in pygame.event.get():
            if key_down(e) or key_s(e):
                pointer_index += 1
                if pointer_index == 3:
                    pointer_index = 0
            if key_up(e) or key_z(e):
                pointer_index -= 1
                if pointer_index == -1:
                    pointer_index = 2

            if e.type == QUIT:
                if server_controler:
                    data_line_1.close()
                    data_line_2.close()
                quit()
            if key_space(e) or key_entrer(e):
                if pointer_index == 0:
                    return "selectpage"
                if pointer_index == 1:
                    return "settingpage"
                if pointer_index == 2:
                    quit()

def settingpage():
    while True:
        clock.tick(25)
        pygame.display.set_caption("settingpage")
        surface.fill(BLACK)
        pygame.display.flip()
        pygame.draw.rect(surface,WHITE,(270,270,60,60))
        for e in pygame.event.get():
            if key_echap(e):
                return "mainpage"
            if e.type == QUIT:
                if server_controler:
                    data_line_1.close()
                    data_line_2.close()

                quit()



def selectpage():
    selected, selected_p1, selected_p2 = 0, True, True
    pointer_coor_p1 = (75, 225, 375, 525, 675)
    pointer_coor_p2 = (125, 275, 425, 575, 725)
    pointer_index_p1 = 0
    pointer_index_p2 = 4
    while True:
        clock.tick(25)
        pygame.display.set_caption("selectpage")
        surface.blit(selectpage_background,(0,0))
        pygame.draw.rect(surface, RED ,(30, 232,100,90))
        pygame.draw.rect(surface, RED ,(30+150, 232,100,90))
        pygame.draw.rect(surface, RED ,(30+300, 232,100,90))
        pygame.draw.rect(surface, RED ,(30+450, 232,100,90))
        pygame.draw.rect(surface, RED ,(30+600, 232,100,90))
        surface.blit(cadre, ((30, 230)))
        surface.blit(cadre, ((30 + 150, 230)))
        surface.blit(cadre, ((30 + 300, 230)))
        surface.blit(cadre, ((30 + 450, 230)))
        surface.blit(cadre, ((30 + 600, 230)))
        surface.blit(plane0_p1, (50, 250-4))
        surface.blit(plane1_p1, (200, 250-4))
        surface.blit(plane2_p1, (340, 250))
        surface.blit(plane3_p1, (500, 250-4))
        surface.blit(plane4_p1, (650, 250-4))

        if selected_p1:
            surface.blit(pointer_p1_button,(pointer_coor_p1[pointer_index_p1]-35, 350))
        if selected_p2:
            surface.blit(pointer_p2_button, (pointer_coor_p2[pointer_index_p2]-35, 350))
        pygame.display.flip()
        for e in pygame.event.get():
            if key_d(e):
                pointer_index_p1 += 1
                if pointer_index_p1 == 5:
                    pointer_index_p1 = 0
            if key_q(e):
                pointer_index_p1 -= 1
                if pointer_index_p1 == -1:
                    pointer_index_p1 = 4
            if key_right(e):
                pointer_index_p2 += 1
                if pointer_index_p2 == 5:
                    pointer_index_p2 = 0
            if key_left(e):
                pointer_index_p2 -= 1
                if pointer_index_p2 == -1:
                    pointer_index_p2 = 4
            if key_g(e) and selected_p1:
                selected += 1
                selected_p1 = False
            if key_5(e) and selected_p2:
                selected += 1
                selected_p2 = False
            if key_echap(e):
                return ("mainpage",0,0)
            if e.type == QUIT:
                quit()
            if selected == 2:
                return ("mappage", pointer_index_p1, pointer_index_p2)


def mappage():
    map_selected = 0
    while True:
        clock.tick(25)
        pygame.display.set_caption("mappage")
        surface.blit(maps_images[map_selected], (0, 0))
        pygame.display.flip()
        for e in pygame.event.get():
            if e.type == QUIT:
                if server_controler:
                    data_line_1.close()
                    data_line_2.close()

                quit()
            if key_left(e):

                map_selected += 1
                if map_selected == len(maps_images):
                    map_selected = 0
            if key_right(e):
                map_selected-=1
                if map_selected==-1:
                    map_selected=len(maps_images)-1
            if key_space(e) or key_entrer(e):
                return "gamepage",map_selected
            if key_echap(e):
                return ("selectpage",0)


def gamepage():
    # ---------def------------
    def hitt(point, rect):  # (x,y)    (a,b,c,d)
        x, y = point
        a, b, c, d = rect[0], rect[1], rect[2], rect[3]
        if a < x < a + c and b < y < b + d:
            return True
        return False

    def hit(rect1, rect2):
        x, y, dx, dy = rect1
        if hitt((x, y), rect2) or hitt((x + dx, y), rect2) or hitt((x, y + dy), rect2) or hitt((x + dx, y + dy),
                                                                              rect2):  # >   <
            return True
        return False

    def shot_update(bullet, p):  # bullet=[x,speed,image,coor] if selected=0
        if p == 1:
            if selected_p1 == 0:
                surface.blit(bullet[2], (bullet[0], bullet[3] + 8))
                surface.blit(bullet[2], (bullet[0], bullet[3] + 52))
                bullet[0] += bullet[1]
                return bullet
            if selected_p1 == 1:
                surface.blit(bullet[2], (bullet[0], bullet[3] + 25))  # [112,10,bullet_plane0_p1]
                bullet[0] += bullet[1]
                return bullet
            if selected_p1 == 2:
                surface.blit(bullet[2], (bullet[0], bullet[3] + 25))
                bullet[0] += bullet[1]
                return bullet
            if selected_p1 == 3:
                if life_p1:
                    surface.blit(bullet[2], (bullet[0] - 45, coor_p1 + 21))
                    surface.blit(planes_images[selected_p1][0], (50, coor_p1))
                return bullet
            if selected_p1 == 4:
                surface.blit(bullet[2], (bullet[0], bullet[3] + 25))
                bullet[0] += bullet[1]
                return bullet
        if p == 2:
            if selected_p2 == 0:
                surface.blit(bullet[2], (bullet[0], bullet[3] + 8))
                surface.blit(bullet[2], (bullet[0], bullet[3] + 52))
                bullet[0] += bullet[1]
                return bullet
            if selected_p2 == 1:
                surface.blit(bullet[2], (bullet[0], bullet[3] + 25))
                bullet[0] += bullet[1]
                return bullet
            if selected_p2 == 2:
                surface.blit(bullet[2], (bullet[0], bullet[3] + 25))
                bullet[0] += bullet[1]
                return bullet
            if selected_p2 == 3:
                if life_p2:
                    surface.blit(bullet[2], (-65, coor_p2 + 22))
                    surface.blit(planes_images[selected_p2][1], (686, coor_p2))
                return bullet

            if selected_p2 == 4:
                surface.blit(bullet[2], (bullet[0], bullet[3] + 32-7))
                bullet[0] += bullet[1]
                return bullet

    def update(i,j):
        j += 1
        if j == 4:
            j = 0
            i += 1
            if i == len(fire_p1):
                i = 0
        return i,j
    # ---fin------------------
    frame=0
    timer,timer2 = 200,200
    plane2_passive,plane2_passive2=False,False
    plane4_passive,plane4_passive2=False,False
    speed3=speed[3]
    laser_cd_p1,laser_cd_p2=0,0
    laser_type_p1,laser_type_p2=0,0
    fire_p1_i,fire_p1_j,fire_p2_i,fire_p2_j = 0,0,0,0
    bullet_num_p1 = bullet_num[selected_p1]
    bullet_num_p2 = bullet_num[selected_p2]
    life_p1, life_p2 = True, True
    shot_cd_time = [0, 0]
    bullet_p1 = []
    bullet_p2 = []
    coor_p1, coor_p2 = 280, 280
    hp_p1 = hp[selected_p1]
    hp_p2 = hp[selected_p2]
    plane_p1 = planes_images[selected_p1][0]
    plane_p2 = planes_images[selected_p2][1]
    speed_p1 = speed[selected_p1]
    speed_p2 = speed[selected_p2]
    up_p1, up_p2, down_p1, down_p2 = False, False, False, False
    m=(0,0,0,0)
    
    while True:
        controle_net_1 = list1.pop(0) if list1 else False
        controle_net_2 = list2.pop(0) if list2 else False
        if controle_net_2:
            print(controle_net_2)
        if not server_controler:
            controle_net_1 = False
            controle_net_2 = False
        clock.tick(60)
        air_shot_p1[3][2] = lasers_p1[laser_type_p1]
        air_shot_p2[3][2] = lasers_p2[laser_type_p2]
        frame += 1
        if frame == 40:
            frame = 0
        pygame.display.set_caption("gamepage")
        surface.blit(maps_images[map_selected],(0,0))

        if life_p1:
            surface.blit(planes_images[selected_p1][0], (50, coor_p1))
            #fire_p1_i,fire_p1_j=update(fire_p1_i,fire_p1_j)
            #surface.blit(fire_p1[fire_p1_i], (10,coor_p1+30))
            pygame.draw.rect(surface, BLACK, m)
        if life_p2:
            surface.blit(planes_images[selected_p2][1], (686, coor_p2))
            #fire_p2_i, fire_p2_j=update(fire_p2_i,fire_p2_j)
            #j = update(fire_p2_i, fire_p2_j)
            #surface.blit(fire_p2[fire_p2_i], (750, coor_p2 + 25))
        shot_cd_time[0] -= 1
        shot_cd_time[1] -= 1
        if shot_cd_time[0] < 0:
            shot_cd_time[0] = basic_cd[selected_p1]
            if bullet_num_p1<bullet_num[selected_p1]:
                bullet_num_p1 += 1
        if shot_cd_time[1] < 0:
            shot_cd_time[1]=basic_cd[selected_p2]
            if bullet_num_p2 < bullet_num[selected_p2]:
                bullet_num_p2+=1
        for fire_p1_i in range(len(bullet_p1)):
            if not bullet_p1[fire_p1_i]:
                continue
            if bullet_p1[fire_p1_i][4]<0:
                bullet_p1[fire_p1_i]=False
            if not bullet_p1[fire_p1_i]:
                continue
            bullet_p1[fire_p1_i][4]-=1
            bullet_p1[fire_p1_i] = shot_update(bullet_p1[fire_p1_i], 1)
            # if bullet_p2[i] is out of surface:
            # bullet_p1.remove(bullet_p1[i])

            if selected_p1 == 0:
                if hit((bullet_p1[fire_p1_i][0], bullet_p1[fire_p1_i][3] + 8, 16, 4), (686, coor_p2, 64, 64)):
                    hp_p2 -= 1
                    bullet_p1[fire_p1_i] = False
                if bullet_p1[fire_p1_i] and hit((bullet_p1[fire_p1_i][0], bullet_p1[fire_p1_i][3] + 52, 16, 4),
                                        (686, coor_p2, 64, 64)):  # [x,speed,image,coor]
                    hp_p2 -= 1
                    bullet_p1[fire_p1_i] = False
            if selected_p1 == 1:
                if hit((bullet_p1[fire_p1_i][0], bullet_p1[fire_p1_i][3] + 8+14, 24, 16), (686, coor_p2, 64, 64)):
                    hp_p2 -= 1
                    hp_p1 += 1
                    bullet_p1[fire_p1_i] = False

            if selected_p1 == 2:
                if hit((bullet_p1[fire_p1_i][0], bullet_p1[fire_p1_i][3] + 25, 7, 4),
                       (686, coor_p2, 64, 64)):  # [112,10,bullet_plane0_p1,coor]
                    hp_p2 -= 1
                    bullet_p1[fire_p1_i] = False
            if selected_p1 == 3:
                if hit((bullet_p1[fire_p1_i][0], coor_p1 + 28, 800, 8), (50, coor_p2, 64, 64)):
                    if laser_cd_p1<0 and life_p1:
                        hp_p2 -= 3 if laser_type_p1== 0 else 2 if laser_type_p1==3 else 1
                        laser_cd_p1 = lcd2
            if selected_p1 == 4:
                if hit((bullet_p1[fire_p1_i][0], bullet_p1[fire_p1_i][3] + 25, 7, 7),
                       (686, coor_p2, 64, 64)):  # [112,10,bullet_plane0_p1,coor]
                    hp_p2 -= 1
                    bullet_p1[fire_p1_i] = False
        for fire_p1_i in range(len(bullet_p2)):
            if not bullet_p2[fire_p1_i]:
                continue
            if bullet_p2[fire_p1_i][4]<0:
                bullet_p2[fire_p1_i]=False
            if not bullet_p2[fire_p1_i]:
                continue
            bullet_p2[fire_p1_i][4]-=1
            bullet_p2[fire_p1_i] = shot_update(bullet_p2[fire_p1_i], 2)
            # if bullet_p2[i]_p2 is out of surface:
            # bullet_p2.remove(bullet_p2[i])
            if selected_p2 == 0:
                if hit((bullet_p2[fire_p1_i][0], bullet_p2[fire_p1_i][3] + 8, 16, 4), (50, coor_p1, 64, 64)):
                    hp_p1 -= 1
                    bullet_p2[fire_p1_i] = False
                if bullet_p2[fire_p1_i] and hit((bullet_p2[fire_p1_i][0], bullet_p2[fire_p1_i][3] + 52, 64, 64),(50, coor_p1, 64, 64)):  # [x,speed,image,coor]
                    hp_p1 -= 1
                    bullet_p2[fire_p1_i] = False
            if selected_p2 == 1:
                if hit((bullet_p2[fire_p1_i][0], bullet_p2[fire_p1_i][3] + 8 +14, 16, 4), (50, coor_p1, 64, 64)):
                    hp_p1 -= 1
                    hp_p2 += 1
                    bullet_p2[fire_p1_i] = False
            if selected_p2 == 2:
                if hit((bullet_p2[fire_p1_i][0], bullet_p2[fire_p1_i][3] + 25, 7, 4), (50, coor_p1, 64, 64)):
                    hp_p1 -= 1
                    bullet_p2[fire_p1_i] = False
            if selected_p2 == 3:

                if hit((80, coor_p2 + 28, 800, 8), (50, coor_p1, 64, 64)):
                    if laser_cd_p2<0 and life_p2:
                        hp_p1 -= 3 if laser_type_p2 == 0 else 2 if laser_type_p2==3 else 1
                        laser_cd_p2=lcd1
            if selected_p2 == 4:

                if hit((bullet_p2[fire_p1_i][0], bullet_p2[fire_p1_i][3] + 25, 7, 7), (50, coor_p1, 64, 64)):
                    hp_p1 -= 1
                    bullet_p2[fire_p1_i] = False


        for fire_p1_i in range(hp_p1):
            surface.blit(heart, (7, fire_p1_i * -23 + 550))
        for fire_p1_i in range(hp_p2):
            surface.blit(heart, (757, fire_p1_i * -23 + 550))
        for fire_p1_i in range(bullet_num_p1):
            surface.blit(amo_p1, (7, fire_p1_i * 16 + 20))
        for fire_p1_i in range(bullet_num_p2):
            surface.blit(amo_p2, (775, fire_p1_i * 16 + 20))
        if hp_p1 <= 0:  # >   <
            life_p1 = False
        if hp_p2 <= 0:  # >   <
            life_p2 = False
        pygame.display.flip()
        laser_cd_p1 -= 1
        laser_cd_p2 -= 1
        # move update
        if True:
            if up_p1:
                coor_p1 -= speed_p1
            if down_p1:
                coor_p1 += speed_p1
            if up_p2:
                coor_p2 -= speed_p2
            if down_p2:
                coor_p2 += speed_p2
            if selected_p1 != 2 or plane2_passive:
                if coor_p1 > 570:  # >   <
                    coor_p1 = -30
                if coor_p1 < -30:
                    coor_p1 = 570
            else:
                if coor_p1 > 570:
                    timer -= 1
                elif coor_p1 < -30:
                    timer -= 1
                else:
                    timer = time_for_death_out_of_map
                #--
            if selected_p2 !=  2 or plane2_passive2:
                if coor_p2 < -30:
                    coor_p2 = 570
                if coor_p2 > 570:
                    coor_p2 = -30
            else:
                if coor_p2 > 570:
                    timer2 -= 1
                elif coor_p2 < -30:
                    timer2 -= 1
                else:
                    timer2 = time_for_death_out_of_map
        if timer < 0 :
            hp_p1 -= 1
            timer = time_for_death_out_of_map
        if timer2 < 0 :
            hp_p2 -= 1
            timer2 = time_for_death_out_of_map
        # ..fin.......

        if selected_p1==4:
            if bullet_num_p1==0:
                plane4_passive = True
            if bullet_num_p1==bullet_num[4] and plane4_passive == True:
                hp_p1=hp[4]
                plane4_passive = False
        if selected_p2==4:
            if bullet_num_p2==0:
                plane4_passive2 = True
            if bullet_num_p2==bullet_num[4] and plane4_passive2 == True:
                hp_p2=hp[4]
                plane4_passive2 = False
        events = pygame.event.get()
        if not events:
            events = [ev]
        for e in events:
            # up=True?pygame.event.get()
            if controle_net_2:
                print(controle_net_2)
            if True:
                if key_z(e) or controle_net_1 == "U":
                    up_p1 = True
                if key_s(e) or controle_net_1 == "D":
                    down_p1 = True
                if key_up(e) or controle_net_2 == "U":
                    up_p2 = True
                if key_down(e) or controle_net_2 == "D":
                    down_p2 = True
                if key_z_up(e) or controle_net_1 == "u":
                    up_p1 = False
                if key_s_up(e) or controle_net_1 == "d":
                    down_p1 = False
                if key_up_up(e) or controle_net_2 == "u":
                    up_p2 = False
                if key_down_up(e) or controle_net_2 == "d":
                    down_p2 = False
            # ..fin......
            if e.type == QUIT:
                #if server_controler:
                #    data_line_1.close()
                #    data_line_2.close()
                quit()
            if key_echap(e):
                return "mainpage"
            if (key_g(e) or controle_net_1 == "1") and bullet_num_p1>0 and life_p1:  # >   <
                bullet_num_p1-=1

                a = air_shot_p1[selected_p1][:]  # [112,10,bullet_plane0_p1]
                a.append(coor_p1)
                a.append(70)
                bullet_p1.append(a)
                laser_type_p1 += 1
                if laser_type_p1 == 4:
                    laser_type_p1 = 0
                sound[selected_p1].play()
            if (key_5(e) or controle_net_2 == "1") and bullet_num_p2 > 0 and life_p2:
                bullet_num_p2-=1
                b = air_shot_p2[selected_p2][:]  # [688,-10,bullet_plane0_p2]
                b.append(coor_p2)
                b.append(70)
                bullet_p2.append(b)
                laser_type_p2+=1
                if laser_type_p2==4:
                    laser_type_p2=0
                sound[selected_p2].play()
            if key_h(e) or controle_net_1 == "p":
                plane2_passive = not plane2_passive
            if key_9(e) or controle_net_2 == "p":
                plane2_passive2 = not plane2_passive2
            if key_space(e):
                hp_p1 = hp[selected_p1]
                hp_p2 = hp[selected_p2]
                bullet_num_p1 = bullet_num[selected_p1]
                bullet_num_p2 = bullet_num[selected_p2]
                laser_type_p1 = 0
                laser_type_p2 = 0
                life_p1 = True
                life_p2 = True


# ---------sound------------------
pygame.mixer.init()
pygame.mixer.music.load("0.mp3")
pygame.mixer.music.set_volume(music_volume)
pygame.mixer.music.play(-1)
sound1 = pygame.mixer.Sound("1.wav")
sound2 = pygame.mixer.Sound("2.wav")
sound3 = pygame.mixer.Sound("3.wav")
soundlaser = pygame.mixer.Sound("laser.mp3")
sound = [sound1,sound2,sound3,soundlaser,sound1]
sound1.set_volume(sound_volume)
sound2.set_volume(sound_volume)
sound3.set_volume(sound_volume)
soundlaser.set_volume(sound_volume)
#---------------------------
if server_controler:
    x.start()
    y.start()
page = "mainpage"
while True:
    if page == "mainpage":
        page = mainpage()
    if page == "settingpage":
        page = settingpage()
    if page == "selectpage":
        page, selected_p1, selected_p2 = selectpage()
    if page == "mappage":
        page,map_selected = mappage()
    if page == "gamepage":
        page = gamepage()

