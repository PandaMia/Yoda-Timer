import sys
from .text import *
from .parameters import *

class Button(object):
    def __init__(self, width, height):
        self.inactive_clr = BLUE
        self.active_clr = LIGHT_BLUE
        self.width = width
        self.height = height

class RectButton(Button):
    def __init__(self, width, height):
        Button.__init__(self, width, height)

    def draw(self, x_btn, y_btn, x_msg, y_msg, message, action=None, arg=None, font_size=30):
        self.rect = pygame.Rect(x_btn, y_btn, self.width, self.height)

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if self.rect.collidepoint(mouse[0], mouse[1]):
            pygame.draw.rect(display, self.active_clr, self.rect)

            if click[0] == 1 and action is not None:
                if action == sys.exit:
                    pygame.quit()
                    sys.exit()
                elif arg is not None:
                    action(arg)
                else:
                    action()
        else:
            pygame.draw.rect(display, self.inactive_clr, self.rect)

        print_text(message=message, x=x_msg, y=y_msg, font_size=font_size)

class ArrowButton(Button):
    def __init__(self, width, height):
        Button.__init__(self, width, height)

    def draw(self, x, y, up=True, action=None, arg=None):
        first_point = (x, y)
        if up:
            second_point = (x+self.width//2, y-self.height)
        else:
            second_point = (x+self.width//2, y+self.height)
        third_point = (x+self.width, y)
        points = [first_point, second_point, third_point]

        self.polygon = pygame.draw.polygon(display, self.inactive_clr, points)
        pygame.draw.aalines(display, self.inactive_clr, False, points)

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if self.polygon.collidepoint(mouse[0], mouse[1]):
            pygame.draw.polygon(display, self.active_clr, points)
            pygame.draw.aalines(display, self.active_clr, False, points)

            if click[0] == 1 and action is not None:
                if action == sys.exit:
                    pygame.quit()
                    sys.exit()
                elif arg is not None:
                    action(arg)
                else:
                    action()
