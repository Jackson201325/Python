class Settings():
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize game' settings."""

        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship Settings
        self.ship_limit = 3

        # Bullets Settings
        self.bullet_speed_factor = 6
        self.bullet_width = 500
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 7

        # Aliens Settings
        self.fleet_drop_speed = 10

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change through out the game"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # Fleet direction of 1 representright and -1 left
        self.fleet_direction = 1


    def increase_speed(self):
        """Increase speed settings"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
