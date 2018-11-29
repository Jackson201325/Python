import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from ship import Ship
import game_functions as gf


def run_game():
    # Initialize pygame, settings, and screen object.

    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Create and instance to store the game statistics
    stats = GameStats(ai_settings)

    # Make a ship
    ship = Ship(ai_settings, screen)

    # Make a Group to store bullets
    bullets = Group()

    # Make a group that stores aliens
    aliens = Group()

    # Create the flee of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    while True:

        gf.check_events(ai_settings, screen, ship, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
