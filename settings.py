from typing import Any


class Settings :
    
    def __init__(self) :
        self.screen_width = 1200
        self.screen_height = 800

        self.bg_color = (230,230,230)

        self.ship_limit = 3  

        self.bullet_width = 8
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3

        self.fleet_drop_speed = 10

        self.speedup_scale = 1.3
        self.points_scale = 1.5

    def initialize_easy_mode(self):
        self.fleet_speed = 0.5
        self.fleet_direction = 1

        self.ship_speed = 5
        self.bullet_speed = 10

        self.alien_points = 50

    def initialize_normal_mode(self):
        self.fleet_speed = 1
        self.fleet_direction = 1

        self.ship_speed = 5
        self.bullet_speed = 10

        self.alien_points = 45

    def initialize_hard_mode(self):
        self.fleet_speed = 2
        self.fleet_direction = 1

        self.ship_speed = 5
        self.bullet_speed = 10

        self.alien_points = 40

    def increase_speed(self):
        self.fleet_speed *= self.speedup_scale
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points*self.points_scale)