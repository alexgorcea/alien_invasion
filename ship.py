import pygame


class Ship:

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        self.moving_r = False
        self.moving_l = False

    def update(self):
        if self.moving_r and self.rect.right < self.screen_rect.right :
            self.x += self.settings.ship_speed
        elif self.moving_l and self.rect.left > self.screen_rect.left :
            self.x -= self.settings.ship_speed
        
        self.rect.x = self.x

    
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self) :
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)