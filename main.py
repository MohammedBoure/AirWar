import pygame
from pygame.locals import QUIT
from image_handler import *
from keys import *
from sound_handler import *
from config import *
from server import *

class ev:
    type = 5

# -----colors--------------
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (180,20,20)

# -----------------------
size = (800, 600)
surface = pygame.display.set_mode(size)
clock = pygame.time.Clock()

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
    # ---fin------------------
    def hitt(point, rect):  # (x,y)    (a,b,c,d)
        x, y = point
        a, b, c, d = rect[0], rect[1], rect[2], rect[3]
        if a < x < a + c and b < y < b + d:
            return True
        return False

    def hit(rect1, rect2):
        x, y, dx, dy = rect1
        if hitt((x, y), rect2) or hitt((x + dx, y), rect2) or hitt((x, y + dy), rect2) or hitt((x + dx, y + dy), rect2):  # Fixed missing parenthesis
            return True
        return False

    def shot_update(bullet, p):  # bullet=[x,speed,image,coor] if selected=0
        if p == 1:
            if selected_p1 == 0:
                surface.blit(bullet[2], (bullet[0], bullet[3] + 8))
                surface.blit(bullet[2], (bullet[0], bullet[3] + 52))
                bullet[0] += bullet[1]
                return bullet
            elif selected_p1 == 1:
                surface.blit(bullet[2], (bullet[0], bullet[3] + 25))  # [112,10,bullet_plane0_p1]
                bullet[0] += bullet[1]
                return bullet
            elif selected_p1 == 2:
                surface.blit(bullet[2], (bullet[0], bullet[3] + 25))
                bullet[0] += bullet[1]
                return bullet
            elif selected_p1 == 3:
                if life_p1:
                    surface.blit(bullet[2], (bullet[0] - 45, coor_p1 + 21))
                    surface.blit(planes_images[selected_p1][0], (50, coor_p1))
                return bullet
            elif selected_p1 == 4:
                surface.blit(bullet[2], (bullet[0], bullet[3] + 25))
                bullet[0] += bullet[1]
                return bullet
        if p == 2:
            if selected_p2 == 0:
                surface.blit(bullet[2], (bullet[0], bullet[3] + 8))
                surface.blit(bullet[2], (bullet[0], bullet[3] + 52))
                bullet[0] += bullet[1]
                return bullet
            elif selected_p2 == 1:
                surface.blit(bullet[2], (bullet[0], bullet[3] + 25))
                bullet[0] += bullet[1]
                return bullet
            elif selected_p2 == 2:
                surface.blit(bullet[2], (bullet[0], bullet[3] + 25))
                bullet[0] += bullet[1]
                return bullet
            elif selected_p2 == 3:
                if life_p2:
                    surface.blit(bullet[2], (-65, coor_p2 + 22))
                    surface.blit(planes_images[selected_p2][1], (686, coor_p2))
                return bullet
            elif selected_p2 == 4:
                surface.blit(bullet[2], (bullet[0], bullet[3] + 32 - 7))
                bullet[0] += bullet[1]
                return bullet
            
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

if server_controler: #threading
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