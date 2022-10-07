import sys
import pygame
# import Settings class from settings.py
from settings import Settings
# import Ship class from ship.py
from ship import Ship
# import Bullet class from bullet.py
from bullet import Bullet


#Overall class to manage game assets and behavior.
class AlienInvasion:
    def __init__(self):
    #Initializng  game, and creation of game resources.
        pygame.init()

        self.settings = Settings()

        #setting the screen to full screen
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) 
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        #method to manually set up the screen width and height 
        # self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height)) 
        pygame.display.set_caption("Alien Invasion") 

        #create an instance of Ship class with argument self so as to refer to currnt instance

        self.ship = Ship(self)

        #enabling background color 
        #self.bg_color = (230,230,230)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
    #Start the main loop for the game.
        while True:
            self._check_events()
            # to update the ships position based on the player's input 
            self.ship.update()
            self.bullets.update()
            #to remove old bullets
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0: 
                    self.bullets.remove(bullet)
            #print(len(self.bullets))

            self._update_screen()

    #included helper method to simplify code on check_events
    def _check_events(self):  
            # keyboard and mouse events.
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                    # # to check if right key is pressed
                    # if event.key == pygame.K_RIGHT:
                    #     #move the ship to the right
                    #     #self.ship.rect.x += 1
                    #     #setting the moving_right to TRUE when right arrow key is clicked instead of directly increasing with 1 
                    #     self.ship.moving_right =True
                    # elif event.key == pygame.K_LEFT: 
                    #     self.ship.moving_left = True

                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
                    # if event.key == pygame.K_RIGHT:
                    #     #setting the moving_right to FALSE when right arrow key is released
                    #      self.ship.moving_right =False
                    # elif event.key == pygame.K_LEFT: 
                    #     self.ship.moving_left = False
                       
    def _check_keydown_events(self, event):
        #respond to keypresses
        # to check if right key is pressed
        if event.key == pygame.K_RIGHT:
            #setting the moving_right to TRUE when right arrow key is clicked instead of directly increasing with 1 
            self.ship.moving_right =True
        elif event.key == pygame.K_LEFT: 
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE: 
            self._fire_bullet()


    def _check_keyup_events(self, event): 
        #Respond to key releases
          if event.key == pygame.K_RIGHT:
            #setting the moving_right to FALSE when right arrow key is released
            self.ship.moving_right =False
          elif event.key == pygame.K_LEFT: 
            self.ship.moving_left = False

    def _fire_bullet(self):
        #checking if number of existing bullets before creating a new bullet 
        if len(self.bullets) < self.settings.bullets_allowed:
            #Creating  new bullet and adding it to  bullets group
            new_bullet = Bullet(self) 
            self.bullets.add(new_bullet)

    #included helper method to simplify code on screen updates
    def _update_screen(self):
            # code to include the baackground color to the screen
            self.screen.fill(self.settings.bg_color)

            #drawing of ship to the screen to make it appear at top of background
            self.ship.blitme()

            #to draw all fired bullets on screen , bullets.sprites has a list of all sprites in the group bullets
            for bullet in self.bullets.sprites(): 
                bullet.draw_bullet()


            # Make the most recently drawn screen visible.
            pygame.display.flip()
            
if __name__ == '__main__':
    # Make a game instance, and run the game. 
    ai = AlienInvasion()
    ai.run_game()
