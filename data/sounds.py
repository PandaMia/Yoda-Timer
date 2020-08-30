import pygame
from .resource_path import *

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.init()

clock_sound = pygame.mixer.Sound(resource_path(os.path.join('resourses', 'sounds', 'clock.wav')))
clock_sound.set_volume(0.8)

def play_sound():
    pygame.mixer.Sound.play(clock_sound)
