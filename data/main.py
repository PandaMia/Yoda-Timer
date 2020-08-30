import os, sys
import datetime
import pygame

from .button import *
from .timer import Timer
from .parameters import *
from .resource_path import *
from .text import *
from .images import *
from . import sounds

class YodaTimer(object):

    def __init__(self):
        pygame.display.set_caption('Yoda Timer')
        pygame.display.set_icon(yoda_icon)

        self.clock = pygame.time.Clock()

    def run_timer(self):

        timer = Timer()

        btn_start = RectButton(165, 60)
        btn_stop = RectButton(120, 60)
        btn_5min = RectButton(165, 60)
        btn_10min = RectButton(165, 60)
        btn_15min = RectButton(165, 60)
        btn_20min = RectButton(165, 60)
        btn_30min = RectButton(165, 60)
        btn_60min = RectButton(165, 60)

        btn_hour_plus = ArrowButton(85, 20)
        btn_min_plus = ArrowButton(85, 20)
        btn_sec_plus = ArrowButton(85, 20)
        btn_hour_minus = ArrowButton(85, 20)
        btn_min_minus = ArrowButton(85, 20)
        btn_sec_minus = ArrowButton(85, 20)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            display.blit(yoda_img, (0, 0))
            pygame.draw.rect(display, BROWN, (340, 97, 340, 83))

            timer_time = timer.get_time()
            print_text(f'{timer_time}', 345, 90, font_type=timer_font, font_size = 95)

            btn_start.draw(340, 240, 383, 250, 'Старт', action=timer.start_countdown, font_size=30)
            btn_start.draw(515, 240, 562, 250, 'Стоп', action=timer.stop_countdown, font_size=30)
            btn_5min.draw(340, 310, 381, 320, '5 мин', action=timer.set_time, arg=300, font_size=30)
            btn_10min.draw(515, 310, 545, 320, '10 мин', action=timer.set_time, arg=600, font_size=30)
            btn_15min.draw(340, 380, 371, 390, '15 мин', action=timer.set_time, arg=900, font_size=30)
            btn_20min.draw(515, 380, 545, 390, '20 мин', action=timer.set_time, arg=1200, font_size=30)
            btn_30min.draw(340, 450, 371, 460, '30 мин', action=timer.set_time, arg=1800, font_size=30)
            btn_60min.draw(515, 450, 557, 460, '1 час', action=timer.set_time, arg=3600, font_size=30)

            btn_hour_plus.draw(350, 87, action=timer.change_time, arg=3600)
            btn_min_plus.draw(467, 87, action=timer.change_time, arg=60)
            btn_sec_plus.draw(584, 87, action=timer.change_time, arg=1)
            btn_hour_minus.draw(350, 190, up=False, action=timer.change_time, arg=-3600)
            btn_min_minus.draw(467, 190, up=False, action=timer.change_time, arg=-60)
            btn_sec_minus.draw(584, 190, up=False, action=timer.change_time, arg=-1)

            if timer.delta.seconds <= 0 and timer.countdown:
                sounds.play_sound()
                timer.countdown = False
                pygame.time.delay(100)

            pygame.display.update()
            self.clock.tick()
