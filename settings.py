#defining  class to store and initialize the settings for the alien project
class Settings:
    def __init__(self):

        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230 ,230 ,230)

        #setting the speed of ship to 1.5 from 1 pixel on each pass through the loop
        self.ship_speed =1.5

        #Bullet settings
        self.bullet_speed = 1.0 
        self.bullet_width = 3 
        self.bullet_height = 15 
        self.bullet_color = (60, 60, 60)



