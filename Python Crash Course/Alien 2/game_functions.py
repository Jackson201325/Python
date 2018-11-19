import sys
import pygame
from laser import Laser
from alien import Alien


def check_keydown_events(event, ai_settings, screen, ship, lasers):
    """Respond to keypress"""
    if event.key == pygame.K_UP:
        ship.move_up = True
    elif event.key == pygame.K_DOWN:
        ship.move_down = True
    elif event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_laser(ai_settings, screen, ship, lasers)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    """Respond to keypress"""
    if event.key == pygame.K_UP:
        ship.move_up = False
    elif event.key == pygame.K_DOWN:
        ship.move_down = False
    elif event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, lasers):
    """Respond to keypress and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, lasers)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def fire_laser(ai_settings, screen, ship, lasers):
    """Fire a laser if limit is not reached yet."""
    # Create a new laser and add it to the lasers group
    if len(lasers) < ai_settings.lasers_allowed:
        new_laser = Laser(ai_settings, screen, ship)
        lasers.add(new_laser)
        print("add laser")


def update_screen(ai_settings, screen, ship, aliens, lasers):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during wach pass through the loop
    screen.fill(ai_settings.bg_color)

    # Redraw all lasers behind ship and aliens.
    for laser in lasers.sprites():
        laser.draw_laser()
        print("update screen")
    ship.blitme()
    aliens.draw(screen)

    # Make the most recently drawn screen visible.
    pygame.display.flip()


def update_lasers(lasers):
    """Update position of lasers, and get rid of old lasers."""
    # Update laser positions.
    lasers.update()

    # Get rid of lasers that have disappeared.
    for laser in lasers.copy():
        if laser.rect.bottom <= 0:
            lasers.remove(laser)


def get_number_aliens_x(ai_settings, alien_width):
    """Determines the numver of aliens that fit in a row"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    """Determine the number of rows of aliens that fin on the screen."""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y/(2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """create an alien and place it in the place"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """Create a full fleet of aliens"""
    # Create an alien and find the number of aliens in a row
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # Create the first row of number_aliens_x
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def check_fleet_edges(ai_settings, aliens):
    """Respond appropriatley if any aliens hace reaclhed an edge"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """Drop the entire fleet and change fleet's direction"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def update_aliens(ai_settings, aliens):
    """
    Check if the fleet is at an edge,
    and then update the positions of all aliens in the fleet.
    """
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
