import os
# os.environ["SDL_VIDEODRIVER"]= "dummy"
# os.environ['SDL_VIDEODRIVER']='windib'
# os.environ["SDL_VIDEODRIVER"] = "directfb"
import random
import time
import pygame
pygame.font.init() #allows us to use font after we initialize it here

# creating sandbox size
width,height = 900,700

# enemy carebears
happy_carebear = pygame.image.load(os.path.join('./assets','pixel_ship_red_small.png'))
# happy_carebear = pygame.image.load('./assets/pixel_ship_red_small.png') #the same as above

# player ship
yellow_ship = pygame.image.load(os.path.join('./assets','pixel_ship_yellow.png'))

#lasers
blue_laser = pygame.image.load(os.path.join('./assets','pixel_laser_blue.png'))
red_laser = pygame.image.load(os.path.join('./assets','pixel_laser_red.png'))
green_laser = pygame.image.load(os.path.join('./assets','pixel_laser_green.png'))
yellow_laser = pygame.image.load(os.path.join('./assets','pixel_laser_yellow.png'))

#background, using pygame.transform.scale to adjust the width,height as defined in variables above.
background = pygame.transform.scale(pygame.image.load('./assets/background-black.png'),(width,height))


# win initiliazes the game window, it will disappear if there is no condition to keep it open, the for loop in pygame.event.get()
# keeps this window open
win = pygame.display.set_mode((width,height))  

def main():
    run = True  
    FPS = 60 # FPS is used to check for events/collisions 60 times a second
    game_level = 1
    life = 3
    main_font = pygame.font.Font(pygame.font.get_default_font(),23)

    clockinit = pygame.time.Clock()

    def update_window():
        win.blit(background, (0,0))
        #drawing text, rgb 255 max ; format for .render is(text,antialias(1 default), color)
        life_label = main_font.render(f'Lives Left: {life}',1,(255,100,0))
        level = main_font.render(f'Level: {game_level}',1,(255,100,0))

        win.blit(life_label,(18,15))
        win.blit(level, (width - level.get_width()-18,15))
        pygame.display.update()

    while run:
        clockinit.tick(FPS)
        update_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # if player presses the 'x' icon to close, this allows the game to close
                run= False

main()