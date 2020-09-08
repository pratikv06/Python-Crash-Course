import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

def check_keydown_events(event, ai_setting, screen, ship, bullets):
    '''Check for key press - Start Moving'''
    if event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_RIGHT:
        # Move ship to the right
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # move ship to the left
        ship.moving_left = True

    elif event.key in [pygame.K_SPACE, pygame.K_UP]:
        # Create a bullet and add it to bullet group 
        fire_bullet(ai_setting, screen, ship, bullets)      

def check_keyup_events(event, ship):
    '''Check for key releases - Stop Moving'''
    if event.key == pygame.K_RIGHT:
        # Stop right movement of ship
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        # Stop left movement of ship
        ship.moving_left = False

def check_events(ai_setting, screen, aliens, ship, bullets, stats, sb, play_button):
    # Watch for the keyboard or mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_setting, screen, aliens, bullets, ship, stats, sb, play_button, mouse_x, mouse_y)
        elif event.type == pygame.KEYDOWN:
            # key press event
            check_keydown_events(event, ai_setting, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            # key release event
            check_keyup_events(event, ship)

def check_play_button(ai_setting, screen, aliens, bullets, ship, stats, sb, play_button, mouse_x, mouse_y):
    '''start new game when the player clicks play'''
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Reset the game setting
        ai_setting.initialize_dynamic_setting()

        # Hide mouse cursor
        pygame.mouse.set_visible(False)
        # resetting the game statistics
        stats.reset_stats()
        stats.game_active = True

        # Reset scoreboard
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        # Empty the list of aliens and bullets
        aliens.empty()
        bullets.empty()

        # create a new fleet and center the ship
        create_fleet(ai_setting, screen, aliens, ship)
        ship.center_ship()

def update_screen(ai_setting, screen, ship, bullets, aliens, stats, sb, play_button):
    '''Set bg color, update image position, flip screen'''
    # redrawing the screen during the each pass through the loop   
    screen.fill(ai_setting.bg_color)

    # Redraw bullets behind the ship
    for bullet in bullets.sprites():
        bullet.draw_bullet()
  
    # Redisplay ship on screen
    ship.blitme()
    
    # redisplay alein on screen
    # aliens.blitme()
    aliens.draw(screen)

    # display game score
    sb.show_scoreboard()

    # Draw button on screen
    if not stats.game_active:
        play_button.draw_button()

    # make the most recenlty drawn screen visible
    pygame.display.flip()

def fire_bullet(ai_setting, screen, ship, bullets):
    # Fire bullet if limit not reached
    # Create a bullet and add it to bullet group 
    if len(bullets) < ai_setting.bullet_allowed:
        new_bullet = Bullet(ai_setting, screen, ship)
        bullets.add(new_bullet)

def update_bullets(ai_setting, screen, ship, aliens, bullets, stats ,sb):
    '''Update position of bullet and removing the old bullets'''
    # fire bullets
    bullets.update()
    # removing disappeared bullet from memory
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    # Check for any bullets that have hit aliens
    check_bullet_alien_collision(ai_setting, screen, ship, aliens, bullets, stats, sb)
    
def check_bullet_alien_collision(ai_setting, screen, ship, aliens, bullets, stats, sb):
    '''Resond to bullet-alien collision'''
    # Check for any bullets that have hit aliens
    # If so, get rid of bullet and alien
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    # updating score after collision
    if collisions:
        for aleins in collisions.values():
            stats.score += ai_setting.alien_points * len(aliens)
            sb.prep_score()

    # updating hogh score 
    check_high_score(stats, sb)

    # check for all alien destroy
    if len(aliens) == 0:
        # Destroy existing bullets and create new fleets
        bullets.empty()
        ai_setting.increase_speed()

        # increase level 
        stats.level += 1
        sb.prep_level()

        create_fleet(ai_setting, screen, aliens, ship)

def get_number_alien_x(ai_setting, alien_width):
    '''Determine the number of aliens that fit in a row'''
    avaiable_space_x = ai_setting.screen_width - 2*alien_width
    number_alien_x = avaiable_space_x // (2*alien_width)
    return number_alien_x

def get_number_rows(ai_setting, ship_height, alien_height):
    '''Determine the number of rows of aliens that fit on the screen'''
    available_space_y = (ai_setting.screen_height - (3* alien_height) - ship_height)
    number_rows = available_space_y // (2* alien_height)
    return number_rows

def create_alien(ai_setting, screen, aliens, alien_number, row_number):
    '''create an alien and place it in the row'''
    alien = Alien(ai_setting, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2* alien_width* alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2* alien.rect.height* row_number
    aliens.add(alien)

def create_fleet(ai_setting, screen, aliens, ship):
    '''Create a full fleet of aliens'''
    # Create a alien and find the number of aliens in a row
    # spacing between each alien is equal to one alien width
    alien = Alien(ai_setting, screen)
    number_alien_x = get_number_alien_x(ai_setting, alien.rect.width)
    number_rows = get_number_rows(ai_setting, ship.rect.height, alien.rect.height)
    
    # Create fleet of alien
    for row_number in range(number_rows):
        #  Creating in row of alien
        for alien_number in range(number_alien_x):
            # Create a alien and place it in the row
            create_alien(ai_setting, screen, aliens, alien_number, row_number)

def check_fleet_edges(ai_setting, aliens):
    '''Respond appropriately if any alien have reached an edges'''
    for alien in aliens.sprites():
        if alien.check_edge():
            change_fleet_direction(ai_setting, aliens)
            break

def change_fleet_direction(ai_setting, aliens):
    '''Drop the entire fleet and change the fleet's diretion'''
    for alien in aliens.sprites():
        alien.rect.y += ai_setting.fleet_drop_speed
    ai_setting.fleet_direction *= -1

def ship_hit(ai_setting, stats, sb, screen, ship, aliens, bullets):
    '''Respond to ship being hit by alien'''
    # Decrement ships left
    if stats.ship_left > 0:
        stats.ship_left -= 1

        # update scoreboard
        sb.prep_ships()

        # Empty all the aliens and the bullets
        aliens.empty()
        bullets.empty()

        # Create a new fleet and center the ship
        create_fleet(ai_setting, screen, aliens, ship)
        ship.center_ship()

        # Pause
        sleep(1.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_alien_bottom(ai_setting, stats, sb, screen, ship, aliens, bullets):
    '''check if any alien have reached the bottom'''
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # treat this same as alien hit the ship
            ship_hit(ai_setting, stats, sb, screen, ship, aliens, bullets)
            break

def update_aliens(ai_setting, stats, sb, screen, ship, aliens, bullets):
    '''check if fleet is at edge and Update the position of all alien in the fleet'''
    check_fleet_edges(ai_setting, aliens)
    aliens.update()

    # Looking for alien-ship collision
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_setting, stats, sb, screen, ship, aliens, bullets)

    # Looking for alien-bottom collosion
    check_alien_bottom(ai_setting, stats, sb, screen, ship, aliens, bullets)

def check_high_score(stats, sb):
    '''check to see if there a new high score'''
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()



