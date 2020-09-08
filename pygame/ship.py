import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    
    def __init__(self, screen, ai_setting):
        '''Initialize the ship and set it starting position'''
        super().__init__()
        self.screen = screen
        self.ai_setting = ai_setting

        # load the ship image and get it rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        # rect = rectangle
        # treat element as rectangle is efficient because, rectangle are simple shape
        self.screen_rect = self.screen.get_rect()

        # start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # Centering the element
        # - center, centerx, and centery
        # Edge of the screen
        #  - top, bottom, left, and right
        # For horizontal and vertical adjustment
        # - x and y coordinate from top-left corner

        # store a decimal value for the ship's center
        # Reason for using new variable - rect store only interger
        self.center = float(self.rect.centerx) 

        # movement flag
        self.moving_right = False
        self.moving_left = False

        

    def center_ship(self):
        '''Center the ship on the screen '''
        self.center = self.screen_rect.centerx


    def update(self):
        '''Update the ship position based on the movement flag'''
            
        # Updating center value and limiting the range
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_setting.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_setting.ship_speed_factor
        
        # Update ship position - rect.centerx
        self.rect.centerx = self.center
            

    def blitme(self):
        """Draw the ship at it current location"""
        self.screen.blit(self.image, self.rect)