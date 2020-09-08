import pygame
from pygame.sprite import Sprite
# sprite
# - group related element 
# - act on all group element at once

class Bullet(Sprite):
    '''A class to manage bullets fire from the ship'''

    def __init__(self,  ai_setting, screen, ship):
        '''create bullet shape object at ship position'''
        # super(Bullet, self).__init__() # python2.7 syntax
        super().__init__() # python3.x syntax
        self.screen = screen

        # create bullet rect a (0,0) then set current position
        self.rect = pygame.Rect(0, 0, ai_setting.bullet_width, ai_setting.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # store the bullet position at decimal value
        self.y = float(self.rect.y)

        self.color = ai_setting.bullet_color
        self.speed_factor = ai_setting.bullet_speed_factor

    
    def update(self):
        '''move the bullet up the screen'''
        # update the decimal position of the bullet -  moving bullet upward
        self.y -= self.speed_factor
        # update rect position
        self.rect.y = self.y


    def draw_bullet(self):
        '''Draw the bullet to the screen'''
        pygame.draw.rect(self.screen, self.color, self.rect)