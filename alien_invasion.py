import sys
import pygame
from settings import Settings

#Overall class to manage game assets and behavior.
class AlienInvasion:
    def __init__(self):
    #Initializng  game, and creation of game resources.
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height)) 
        pygame.display.set_caption("Alien Invasion") 

        #enabling background color 
        #self.bg_color = (230,230,230)
    def run_game(self):
    #Start the main loop for the game.
        while True:
            # keyboard and mouse events.
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    sys.exit()
            # code to include the baackground color to the screen
            self.screen.fill(self.settings.bg_color)
            # Make the most recently drawn screen visible.
            pygame.display.flip()
if __name__ == '__main__':
    # Make a game instance, and run the game. 
    ai = AlienInvasion()
    ai.run_game()
