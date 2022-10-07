import pygame

#class to define ship's behavior 
class Ship:

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        # settings attribute for ship
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #loads ship image
        self.image = pygame.image.load('images/ship.bmp')

        #get ship's rectangle surface
        self.rect = self.image.get_rect()

        # positioning of the ship to the bottom center of the screen 
        self.rect.midbottom = self.screen_rect.midbottom

        # attribute that can hold decimal value (ship's horizontal position) since rect.x holds only integer part
        self.x = float(self.rect.x)


        #right movement flag
        self.moving_right = False
        #left movement flag
        self.moving_left = False

    #method to change position of ship if Flag is true 
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left >0: 
            self.x -= self.settings.ship_speed

        # Update rect object from self.x. 
        self.rect.x = self.x
    
    #method to draw the image to the screen position specified by self.rect
    def blitme(self):
        self.screen.blit(self.image, self.rect)