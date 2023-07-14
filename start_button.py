import pygame.font

class Button:
    def __init__(self,ai_game,msg,position_x):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.width = 300
        self.height = 50
        self.text_color = (255,255,255)
        self.button_color = (0,0,0)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0,0, self.width,self.height)
        self.rect.centerx = position_x
        self.rect.centery = self.screen_rect.centery

        self._prep_msg(msg,position_x)

    def _prep_msg(self,msg, position_x):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()

        self.msg_image_rect.centery = self.rect.centery
        self.msg_image_rect.centerx = position_x

    def draw_b(self):
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)