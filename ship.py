import pygame

#class to define ship's behavior 
class Ship:

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #loads ship image
        self.image = pygame.image.load('images/ship.bmp')

        #get ship's rectangle surface
        self.rect = self.image.get_rect()

        # positioning of the ship to the bottom center of the screen 
        self.rect.midbottom = self.screen_rect.midbottom

    #method to draw the image to the screen position specified by self.rect
    def blitme(self):
        self.screen.blit(self.image, self.rect)