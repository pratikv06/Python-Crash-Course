import pygame.font
from pygame.sprite import Group
from ship import Ship

class ScoreBoard():
    '''A Class to report scoring information'''

    def __init__(self, ai_setting, screen, stats):
        '''Initialize scorekeeping attributes'''
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_setting = ai_setting
        self.stats = stats

        # Font setting for scoring information
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Preparing initial score image
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()




    def show_scoreboard(self):
        '''Draw scoreboard on screen'''
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    def prep_score(self):
        '''Turn the score into render image'''
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        score_str = "Score: " + str(score_str)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_setting.bg_color)

        # Display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20    

    def prep_high_score(self):
        '''Turn the highscore into a rendered image'''
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        high_score_str = "High Score: "+ str(high_score_str)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_setting.bg_color)

        # Center the high score at the top of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top  

    def prep_level(self):
        '''Turn level into rendered image'''
        level_str = "level: " + str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.ai_setting.bg_color)

        # position the level below the score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        '''show how many ship left'''
        self.ships = Group()
        for ship_number in range(self.stats.ship_left):
            ship = Ship(self.screen, self.ai_setting)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)