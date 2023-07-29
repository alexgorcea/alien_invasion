import sys

import pygame

from time import sleep

from settings import Settings
from ship import Ship
from bullets import Bullet
from aliens import Alien
from game_stats import GameStats
from scoreboard import ScoreBoard
from start_button import Button

class AlienInvasion:

    def __init__(self):
        pygame.init()

        self.game_active = False

        self.clock = pygame.time.Clock()

        self.settings = Settings()

        self.screen = pygame.display.set_mode( (0,0), pygame.FULLSCREEN)

        self.settings.screen_height = self.screen.get_rect().height
        self.settings.screen_width = self.screen.get_rect().width

        self.screen_rect = self.screen.get_rect()

        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self.stats = GameStats(self)
        self.score = ScoreBoard(self)

        self._create_fleet()

        self._create_difficulty_buttons()


    def run_game(self):

        while True:
            self._check_events()

            if self.game_active == True :
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            
            self._update_events()
            self.clock.tick(60)

    def _update_events(self) :

        self.screen.fill(self.settings.bg_color)

        if not self.game_active :
            self.easy_mode.draw_b()
            self.normal_mode.draw_b()
            self.hard_mode.draw_b()

        else:
            for bullet in self.bullets.sprites() :
                bullet.draw_bullet()

            self.ship.blitme()

            self.aliens.draw(self.screen)

            self.score.show_score()

            self.score.show_score()

        pygame.display.flip()

    def _check_events(self) :
        for event in pygame.event.get():

            if event.type == pygame.QUIT :
                sys.exit()
            elif event.type == pygame.KEYDOWN :
                self.key_down_events(event)
            elif event.type == pygame.KEYUP :
                self.key_up_events(event)    
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_buttons(mouse_pos)

    def key_down_events(self, event) :

        if event.key == pygame.K_RIGHT :
            self.ship.moving_r = True
        elif event.key == pygame.K_LEFT :
            self.ship.moving_l = True
        elif event.key == pygame.K_SPACE :
            self._fire_bullet()
        elif event.key == pygame.K_q :
            sys.exit()
        elif event.key == pygame.K_1 :
            self._start_game()
            self.settings.initialize_easy_mode()
        elif event.key == pygame.K_2 :
            self._start_game()
            self.settings.initialize_normal_mode()
        elif event.key == pygame.K_3 :
            self._start_game()
            self.settings.initialize_hard_mode()

    
    def key_up_events(self, event) :

        if event.key == pygame.K_RIGHT :
            self.ship.moving_r = False
        elif event.key == pygame.K_LEFT :
            self.ship.moving_l = False

    def _fire_bullet(self) :
        if len(self.bullets) < self.settings.bullets_allowed :
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self) :
        self.bullets.update()
        for bullet in self.bullets.copy() :
            if bullet.rect.bottom <= 0 :
                self.bullets.remove(bullet)

        self._check_alien_bullets_collide()

    def _create_fleet(self):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        current_x, current_y = alien_width, 2*alien_height

        while current_y < (self.settings.screen_height - 4*alien_height) :

            while current_x < (self.settings.screen_width - 2*alien_width) :
                self._create_alien(current_x,current_y)
                current_x += 2*alien_width

            current_x = alien_width
            current_y += 2*alien_height

    def _create_alien(self,x_position, y_position) :
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.y = y_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _update_aliens(self) :
        self.check_fleet_edges()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship, self.aliens) :
            self._ship_hit()
        self._check_aliens_bottom()
    
    def check_fleet_edges(self) :
        for alien in self.aliens.sprites():
            if alien.check_edges() :
                self.change_fleet_direction()   
                break

    def change_fleet_direction(self) :
        for alien in self.aliens.sprites() :
            alien.rect.y += self.settings.fleet_drop_speed
            alien.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_alien_bullets_collide(self) :
        collisions = pygame.sprite.groupcollide(self.bullets,self.aliens,False,True)
        if not self.aliens :
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            self.stats.level +=1
            self.score.prep_level()

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.score.prep_score()
            self.score.check_high_score()


    def _ship_hit(self) :
        if self.stats.ships_left > 1 :
            print('Ship has been hit !!!')
            self.stats.ships_left -= 1
            self.score.prep_ships()

            self.bullets.empty()
            self.aliens.empty()

            self._create_fleet()
            self.ship.center_ship()

            sleep(0.5)

        else :
            if self.stats.high_score < self.stats.score:
                self.stats.high_score = self.stats.score
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self) :
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height :
                self._ship_hit()
                
    def _check_buttons(self,pos):
        if self.easy_mode.rect.collidepoint(pos):
            self._start_game()
            self.settings.initialize_easy_mode()
            self.prep_stats()
        
        elif self.normal_mode.rect.collidepoint(pos):
            self._start_game()
            self.settings.initialize_normal_mode()
            self.prep_stats()

        elif self.hard_mode.rect.collidepoint(pos):
            self._start_game()
            self.settings.initialize_hard_mode()
            self.prep_stats()
            
    def _reset_game(self):
        self.aliens.empty()
        self.bullets.empty()
        self._create_fleet()
        self.stats.reset_stats()
        self.ship.center_ship()
        self.score.prep_score()

    def _start_game(self):
        if self.game_active == False:
            self.game_active = True
            self._reset_game()
            pygame.mouse.set_visible(False)

    def _create_difficulty_buttons(self):

        self.easy_button_position = self.screen_rect.centerx - 500
        self.easy_mode = Button(self,'Play Easy Mode',self.easy_button_position)

        self.normal_mode = Button(self,'Play Normal Mode', self.screen_rect.centerx)

        self.hard_button_position = self.screen_rect.centerx + 500
        self.hard_mode = Button(self,'Play Hard Mode', self.hard_button_position)
    
    def prep_stats(self):
        self.score.prep_level()
        self.score.prep_score()
        self.score.prep_ships()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()