from image_handler import *

music_volume = 0.04
sound_volume = 0.07

HOST = "192.168.43.144"
PORT = 8000

server_controler = False

speed = [10, 8, 15, 7, 14]  #{plane0,plane1,...}
basic_cd = [40, 70, 25, 350, 60] #{plane0,plane1,...}
hp = [5, 5, 3, 7, 3]   #{plane0,plane1,...}
bullet_num = [4, 3, 6, 1, 12] #{plane0,plane1,...}
lcd1,lcd2=(15,15)
time_for_death_out_of_map=100 #for plane2 pacive

# ---------planes info-------

laser_p2,laser_p1=0,0
fire_p1=[fire1_p1,fire2_p1]#from images_handler file
fire_p2=[fire1_p2,fire2_p2]#from images_handler file
maps_images = [map1,map2,map3,map4,map5,map6,map7,map8]#from images_handler file
planes_images = [[plane0_p1, plane0_p2], [plane1_p1, plane1_p2], [plane2_p1, plane2_p2], [plane3_p1, plane3_p2], [plane4_p1, plane4_p2]]#from images_handler file
air_shot_p1 = [[112, 20, bullet_plane0_p1], [112, 40, bullet_plane1_p1], [112, 25, bullet_plane2_p2], [112,0,laser_p1],[112,25,bullet_plane4_p1]]  # [x,speed,image]#from images_handler file
air_shot_p2 = [[688, -20, bullet_plane0_p2], [688, -40, bullet_plane1_p2], [688, -25, bullet_plane2_p2], [668,0,laser_p2], [668,-25,bullet_plane4_p2]]#from images_handler file
lasers_p2=[l,ll,lll,llll] #from images_handler file
lasers_p1=[k,kk,kkk,kkkk]#from images_handler file
