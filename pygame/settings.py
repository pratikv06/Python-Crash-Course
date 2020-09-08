class Settings():
    '''A Class to store all settings for Alien Invasion'''

    def __init__(self):
        '''Initialize the game setting's'''
        self.screen_width = 1000
        self.screen_height = 680
        self.bg_color = (230, 230, 230)

        # ship speed
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # Bullet setting
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 3

        # Alien setting
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet direction: 1 = right, -1 = left
        self.fleet_direction = 1

        # How quick the gaem speed up
        self.speedup_scale = 1.1
        self.initialize_dynamic_setting()

        # scoring and score scaling
        self.alien_points = 5
        self.score_scaling = 1.5

    def initialize_dynamic_setting(self):
        '''Initialize setting that change throughout the game'''
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.fleet_direction = 1
        self.alien_points = 5

    def increase_speed(self):
        '''Increase game speed'''
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scaling)