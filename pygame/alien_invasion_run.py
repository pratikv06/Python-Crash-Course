import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import ScoreBoard


def run_game():
    '''Initialize game and create a screen object '''

    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode((ai_setting.screen_width,ai_setting.screen_height))
    # screen object is called surface
    # surface is a part of screen where game element is displayed
    pygame.display.set_caption("Alien Invasion")

    # Make Ship
    ship = Ship(screen, ai_setting)

    # make group to store bullet in
    bullets = Group()

    # Make a single alien
    # aliens = Alien(ai_setting, screen)
   
    # Group of alien 
    aliens = Group()
    # create a fleet of an alien
    gf.create_fleet(ai_setting, screen, aliens, ship)

    # creating an instance to store game statistics and scoreboard
    stats = GameStats(ai_setting)
    sb = ScoreBoard(ai_setting, screen, stats)

    # Make play button
    play_button = Button(ai_setting, screen, "Play")
    # start the main loop for the game
    while True:
        # Watch for the keyboard or mouse events
        gf.check_events(ai_setting, screen, aliens, ship, bullets, stats, sb, play_button)

        # check for game active
        if stats.game_active:
            # Changing ship position 
            ship.update()

            # fire bullets
            gf.update_bullets(ai_setting, screen, ship, aliens, bullets, stats, sb)

            # move alien 
            gf.update_aliens(ai_setting, stats, sb, screen, ship, aliens, bullets)
        
        # Update scren element - bg color, ship position, flip screen
        gf.update_screen(ai_setting, screen, ship, bullets, aliens, stats, sb, play_button)


run_game()