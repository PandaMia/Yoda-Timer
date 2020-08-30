import pygame
from .parameters import display, DIGITS
from .resource_path import *

pygame.font.init()

timer_font = resource_path(os.path.join('resourses', 'font', 'LCD1.ttf'))
text_font = resource_path(os.path.join('resourses', 'font', 'DroidSans.ttf'))

def print_text(message, x, y, font_color = (255, 255, 255), font_type = text_font, font_size = 30):
    font = pygame.font.Font(font_type, font_size)
    text = font.render(message, True, font_color)
    display.blit(text, (x, y))
