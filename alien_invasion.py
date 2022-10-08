import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


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

        #create an instance of Ship class with argument self so as to refer to current instance
        self.ship = Ship(self)

        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        #Start the main loop for the game.
        while True:
            self._check_events()
            # to update the ships position based on the player's input 
            self.ship.update()
            self._update_bullets()
            self._update_aliens()

            self._update_screen()

    #included helper method to simplify code on check_events
    def _check_events(self):  
            # keyboard and mouse events.
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
                   
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

    #included helper method to simplify code on bullet updates
    def _update_bullets(self):
        #Update position of bullets 
        self.bullets.update()
        #to remove old bullets
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0: 
                self.bullets.remove(bullet)

    #Managing  the movement and position of  aliens in  fleet
    def _update_aliens(self):
        #check if the fleet is at an edge and then update alien position accordingly
        self._check_fleet_edges()
        self.aliens.update()

    #Create the fleet of aliens
    def _create_fleet(self):
        # Make an alien and find the number of aliens in a row. 
        #this alien is not added to the fleet
        alien = Alien(self) 
        #alien_width = alien.rect.width
        alien_width, alien_height = alien.rect.size
        # Spacing between each alien is equal to one alien width.
        available_space_x = self.settings.screen_width - (2*alien_width)
        number_aliens_x = available_space_x // (2*alien_width)

        # Determine the number of rows of aliens that fit on the screen.
        ship_height = self.ship.rect.height 
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height) 
        number_rows = available_space_y // (2 * alien_height)

        # Create the full fleet of aliens. 
        for row_number in range(number_rows):
            # Create  first row of aliens.
            for alien_number in range(number_aliens_x):
                #self._create_alien(alien_number)
                self._create_alien(alien_number, row_number)

    #helper method 
    #def _create_alien(self, alien_number):
    def _create_alien(self, alien_number,row_number):
        #Create an alien and place it in the row.
        alien = Alien(self)
        #alien_width = alien.rect.width
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    #method to implement if the fleet has reached the edge
    def _check_fleet_edges(self):
        for alien in self.aliens.sprites(): 
            if alien.check_edges():
                self._change_fleet_direction() 
                break

    #Drop the entire fleet and change the fleet's direction            
    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed 
        self.settings.fleet_direction *= -1
 




    #included helper method to simplify code on screen updates
    def _update_screen(self):
        # code to include the baackground color to the screen
        self.screen.fill(self.settings.bg_color)

        #drawing of ship to the screen to make it appear at top of background
        self.ship.blitme()

        #to draw all fired bullets on screen , bullets.sprites has a list of all sprites in the group bullets
        for bullet in self.bullets.sprites(): 
            bullet.draw_bullet()
        #to make the alien appear in screen using group's draw method
        self.aliens.draw(self.screen)
        # Make the most recently drawn screen visible.
        pygame.display.flip()
            
if __name__ == '__main__':
    # Make a game instance, and run the game. 
    ai = AlienInvasion()
    ai.run_game()
