class GameStats():
    '''Track statistics for Alien Invasion'''

    def __init__(self, ai_setting):
        '''Initialize statistics'''
        self.ai_setting = ai_setting
        self.reset_stats()

        # start alien invasion in an inactive state
        self.game_active = False

        # Highscore never reset this
        self.high_score = 0


    def reset_stats(self):
        '''Initialize statistics that can change during the game'''
        self.ship_left = self.ai_setting.ship_limit
        self.score = 0
        self.level= 1   