import pygame


class Ship():
    def __init__(self, ai_settings, screen):
        """Initialize the ship and set its starting position"""
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal calue for the ship's center
        self.center = float(self.rect.centerx)
        self.center2 = float(self.rect.centery)

        # Move flag
        self.moving_right = False
        self.moving_left = False
        self.move_up = False
        self.move_down = False

    def update(self):
        """Update the ship's position based on the movement flag"""
        # Update ship's center value, not the rectangle
        if self.move_up and self.rect.top > 0:
            self.center2 -= self.ai_settings.ship_speed_factor
        if self.move_down and self.rect.bottom < self.screen_rect.bottom:
            self.center2 += self.ai_settings.ship_speed_factor
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # Update rectangle object from self.center
        self.rect.centerx = self.center
        self.rect.centery = self.center2

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
