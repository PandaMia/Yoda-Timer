import datetime
import pygame

class Timer(object):

    def __init__(self):
        self.delta = datetime.timedelta(seconds=300)
        self.time = datetime.datetime.now() + self.delta
        self.countdown = False

    def set_time(self, seconds):
        self.delta = datetime.timedelta(seconds=seconds)
        self.time = datetime.datetime.now() + self.delta

    def change_time(self, seconds):
        self.delta += datetime.timedelta(seconds=seconds)
        self.time = datetime.datetime.now() + self.delta
        pygame.time.delay(150)

    def get_time(self):
        curr_time = datetime.datetime.now()
        if self.countdown:
            self.delta = self.time - curr_time
        seconds = self.delta.seconds
        hour = seconds // 3600
        minute = seconds // 60 % 60
        second = seconds % 60
        delta = datetime.time(hour=hour, minute=minute, second=second)
        return delta

    def start_countdown(self):
        if self.delta.seconds > 0:
            self.time = datetime.datetime.now() + self.delta
            self.countdown = True

    def stop_countdown(self):
        self.countdown = False
