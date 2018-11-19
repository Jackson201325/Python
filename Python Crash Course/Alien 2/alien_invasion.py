import pygame
from pygame.sprite import Group
from alien import Alien
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # Initialize game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship
    ship = Ship(ai_settings, screen)

    # Make an alien
    alien = Alien(ai_settings, screen)

    # Make a group to store bullets, and a group of aliens
    lasers = Group()
    aliens = Group()

    # Create a flee of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Set the background color.
    bg_color = (230, 230, 230)

    # Start the main loop for the game
    while True:

        # Watch for keyboard and mouse event
        gf.check_events(ai_settings, screen, ship, lasers)

        ship.update()
        gf.update_lasers(lasers)
        gf.update_aliens(ai_settings, aliens)

        # Redraw the screen during each pass through the loop
        gf.update_screen(ai_settings, screen, ship, aliens, lasers)

        # Make the mos recently drawn screen visible.
        pygame.display.flip()


run_game()
