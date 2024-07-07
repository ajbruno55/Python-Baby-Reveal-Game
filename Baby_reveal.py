import pygame
import random
from time import sleep
from baby import Baby
from poop import Poop

# Initialize game window
pygame.init()

# Initialize sound capability and add sound effects from folder
pygame.mixer.init()
fart_sound = pygame.mixer.Sound('/Users/alexbruno/Desktop/Baby Reveal Game/fart.mp3')
win_sound = pygame.mixer.Sound('/Users/alexbruno/Desktop/Baby Reveal Game/win.wav')
wahwah_sound = pygame.mixer.Sound('/Users/alexbruno/Desktop/Baby Reveal Game/wah_wah.mp3')

# Display/clock settings
screen = pygame.display.set_mode((1300,500))
caption = pygame.display.set_caption("Baby Reveal Game")

clock = pygame.time.Clock()

# Loading crib image to blit on screen and setting randomness to y coordinate
crib_image = pygame.image.load('/Users/alexbruno/Desktop/Baby Reveal Game/crib.png')
crib_resized = pygame.transform.scale(crib_image, (100,100))
crib_y = random.randint(1,350)

def create_poop():
    """Function to create a new turd on screen.
    Creates poops coming in at random y coordinates to add randomness"""
    new_poop = Poop(1300, random.randint(50,450))
    poop_group.add(new_poop)
    return new_poop

# Creating poop group to hold poop sprites
poop_group = pygame.sprite.Group()
poop = create_poop()
poop_group.add(poop)

# Creating baby group to hold baby sprites and adding a single baby 
baby_group = pygame.sprite.Group()
baby = Baby(50, 250)
baby_group.add(baby)

# To hold font display for winning game
# Also variables to hold Girl/Boy reveal text and Pink/Blue Background colors
font = pygame.font.SysFont(None, 200)
boy_text = "IT'S A BOY!!!"
girl_text = "IT'S A GIRL!!!"
boy_color = (140,216,240)
girl_color = (255,175,205)
white = (255,255,255)
black = (0,0,0)
color_store = [white, girl_color]
color_index = 0
flash_interval = 0.4
flashing = True

# Flags to detect movement and game state
running = True
moving_down = False
moving_up = False
game_won = False
game_lost = False

# Flags to detect poop on screen and add more poop
poop1_on_screen = True
poop2_on_screen = True
poop3_on_screen = True
poop4_on_screen = True

# Flag for dramatic effect before moving to game won or game lost screen
# then will set to false after so it moves out of the pause
delay = True

# main game loop
while running:
    # event loop
    # makes baby move up and down at reponse to up/down arrows
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                moving_up = True
            elif event.key == pygame.K_DOWN:
                moving_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                moving_up = False
            elif event.key == pygame.K_DOWN:
                moving_down = False
   
   # Light green background
    screen.fill((144, 238, 144))

    # Move baby as indicated by the user input events in event loop
    if not game_won and not game_lost:
        if moving_down:
            for baby in baby_group:
                baby.move_down()  
        if moving_up:
            for baby in baby_group:
                baby.move_up()

     # Detect if baby makes it in the crib, triggers game won loop 
        if baby.rect.x >= 1220 and (crib_y - 15) <= baby.rect.y <= (crib_y + 15):
            win_sound.play()
            game_won = True

        # Collision detection between baby and poop
        # game lost/sound effect if it happens
        if pygame.sprite.spritecollideany(baby, poop_group):
            fart_sound.play()
            game_lost = True

        # If baby misses crib then game lost, wah wah sound effect plays
        if baby.rect.x >= 1270:
            wahwah_sound.play()
            game_lost = True    

     # Keep baby moving right and poop coming at baby
        baby.update()
        poop_group.update()

    # Adding more poops at random coordinates to fire at the baby
        if poop.rect.x < random.randint(950,1050) and poop1_on_screen:
            new_poop = create_poop()
            poop1_on_screen = False
        if poop.rect.x < random.randint(550,650) and poop2_on_screen:
            new_poop = create_poop()
            poop2_on_screen = False
        if poop.rect.x < random.randint(350,450) and poop3_on_screen:
            new_poop = create_poop()
            poop3_on_screen = False
        if poop.rect.x < random.randint(150,250) and poop4_on_screen:
            new_poop = create_poop()
            poop4_on_screen = False

    # Draw poop and baby to the screen 
        baby_group.draw(screen)
        poop_group.draw(screen)

    # Blit crib to screen at random y coordinate 
        screen.blit(crib_resized, (1200, crib_y))
    
    
    # Clear screen and let the user know they lost
    elif game_lost:
        if delay:
            sleep(2)
            delay = False
        screen.fill(black) 
        text = font.render("Try again.", True, white)
        text_rect = text.get_rect(center=(1300 // 2, 500 // 2))
        screen.blit(text, text_rect)

    # clear screen and let the user know they won
    elif game_won:
        if delay:
            sleep(3)
            delay = False

        # Reveal screen to contain reveal text and flashing pink or blue background  
        color_index = (color_index + 1) % len(color_store)
        screen.fill(color_store[color_index]) 
        text = font.render(girl_text, True, black)
        text_rect = text.get_rect(center=(1300 // 2, 500 // 2))
        screen.blit(text, text_rect)
        sleep(flash_interval)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()