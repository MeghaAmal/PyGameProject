import pygame

#to group related elements on the game and act on all grouped elements at once
from pygame.sprite import Sprite

#class to define firing of bullets from the ship 

class Bullet(Sprite):
    
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0, 0) and then set correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Storing of bullet's position as a decimal  
        self.y = float(self.rect.y)

    def update(self):
        #manages the movement of bullet's position when fired the y corordinate decreases as it moves up
        self.y -= self.settings.bullet_speed  
        # Update the rect position.
        self.rect.y = self.y
        
    def draw_bullet(self):
        #Draw the bullet to the screen
        pygame.draw.rect(self.screen, self.color, self.rect)

