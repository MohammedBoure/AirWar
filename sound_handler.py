import pygame
from config import music_volume,sound_volume

pygame.mixer.init()
pygame.mixer.music.load("sound/0.mp3")
pygame.mixer.music.set_volume(music_volume)
pygame.mixer.music.play(-1)
sound1 = pygame.mixer.Sound("sound/1.wav")
sound2 = pygame.mixer.Sound("sound/2.wav")
sound3 = pygame.mixer.Sound("sound/3.wav")
soundlaser = pygame.mixer.Sound("sound/laser.mp3")
sound = [sound1,sound2,sound3,soundlaser,sound1]
sound1.set_volume(sound_volume)
sound2.set_volume(sound_volume)
sound3.set_volume(sound_volume)
soundlaser.set_volume(sound_volume)