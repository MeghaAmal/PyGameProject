import pygame.font

#class to report scoring information
class Scoreboard:
    def __init__(self, ai_game):
        #Initialize scorekeeping attributes 
        self.screen = ai_game.screen 
        self.screen_rect = self.screen.get_rect() 
        self.settings = ai_game.settings 
        self.stats = ai_game.stats
        
        # Font settings for scoring information. 
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        
        # Prepare the initial score image. 
        self.prep_score()

    # to turn score to image
    def prep_score(self):
        rounded_score = round(self.stats.score, -1) 
        score_str = "{:,}".format(rounded_score)
        #score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True,self.text_color, self.settings.bg_color)
        # Display the score at the top right of the screen. 
        self.score_rect = self.score_image.get_rect() 
        self.score_rect.right = self.screen_rect.right - 20 
        self.score_rect.top = 20
    
    #Draw score to the screen.
    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)


