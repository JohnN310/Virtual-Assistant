import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up display
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Fighting Game")

# Load the new background image
new_background = pygame.image.load("background.png")
new_background = pygame.transform.scale(new_background, (width, height))

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Players
p1 = pygame.image.load("warrior.png")
p2 = pygame.image.load("warrior2.png")
p1 = pygame.transform.scale(p1, (100, 100))
p2 = pygame.transform.scale(p2, (100, 100))
player1 = p1.get_rect()
player2 = p1.get_rect()
# Set initial positions
player1.x = 70  # Set the desired x-coordinate for player 1
player1.y = 300  # Set the desired y-coordinate for player 1
player2.x = 650  # Set the desired x-coordinate for player 2
player2.y = 300  # Set the desired y-coordinate for player 2

# Punches
punch1 = pygame.image.load("sword.png")
punch2 = pygame.image.load("sword2.png")
punch1 = pygame.transform.scale(punch1, (100, 100))
punch2 = pygame.transform.scale(punch2, (100, 100))
punch_speed = 10  # Adjust the speed as needed
punch1_active = False
punch2_active = False
# Create Rect objects for the punches
punch1_rect = punch1.get_rect()
punch2_rect = punch2.get_rect()

# Health points
health1 = 70
health2 = 70

# Shields
# Load the shield images
shield1_image = pygame.image.load("shield.png")
shield2_image = pygame.image.load("shield2.png")
shield1_image = pygame.transform.scale(shield1_image, (100, 100))
shield2_image = pygame.transform.scale(shield2_image, (100, 100))
shield1_active = False
shield2_active = False
shield1 = pygame.Rect(0, 0, 100, 100)
shield2 = pygame.Rect(0, 0, 100, 100)

# Load a custom font
font1 = pygame.font.Font("fonts/kenyancoffeebd.ttf", 36)
# Create text objects for options
continue_text = font1.render("Continue Playing", True, (192, 192, 192))
quit_text = font1.render("Quit", True, (192, 192, 192))
next_round_text = font1.render("Next Round", True, (192, 192, 192))

# Main game loop
clock = pygame.time.Clock()
movement_clock = pygame.time.Clock()  # Separate clock for movement
running = True
game_active = False
countdown = 3  # Countdown time in seconds
fight_duration = 3  # Fight duration in seconds
current_fight_time = 0
countdown_font = pygame.font.Font("fonts/Orbitron.ttf", 90)
timer_font = pygame.font.Font("fonts/Orbitron.ttf", 25)  # Font for the timer
fight_font=pygame.font.Font("fonts/alfa_pinoy_font_by_maypakialam-d3071b3.ttf", 74)
fight_text_screen=fight_font.render("Fight!", True, (228, 28, 28))

# Game over
font = pygame.font.Font("fonts/BLENDER BRUSH.ttf", 74)
game_over_text = font.render("Game Over", True, (255, 48, 48))
# Continue game
continue_text_screen=font.render("Continue", True, (204, 102, 0))
# Next Round
next_round_text_screen=font.render("Next Round", True, (255, 255, 48))

while running:
    screen.blit(new_background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if game_active: 
        # Player movement and punch
        movement_clock.tick(120)  # Set the frame rate for movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            player1.x -= 5
        if keys[pygame.K_d]:
            player1.x += 5
        if keys[pygame.K_w]:
            player1.y -= 5
        if keys[pygame.K_s]:
            player1.y += 5
        if keys[pygame.K_LEFT]:
            player2.x -= 5
        if keys[pygame.K_RIGHT]:
            player2.x += 5
        if keys[pygame.K_UP]:
            player2.y -= 5
        if keys[pygame.K_DOWN]:
            player2.y += 5

        if keys[pygame.K_f]:
            punch1_rect.topleft = (player1.x+60, player1.y)
            punch1_active = True
        else:
            punch1_active= False
        if keys[pygame.K_SLASH]:
            punch2_rect.topleft = (player2.x-80, player2.y)
            punch2_active = True
        else:
            punch2_active= False
        
        if keys[pygame.K_LSHIFT]:
            shield1.topright = (player1.x+40, player1.y)
            shield1_active = True
        else:
            shield1_active = False

        if keys[pygame.K_RSHIFT]:
            shield2.topleft = (player2.x-60, player2.y)
            shield2_active = True
        else:
            shield2_active = False

            # Check for collisions
        if player1.colliderect(player2):
            player1.x += random.randint(10, 20)
            player2.x -= random.randint(10, 20)

            # Update punches
        if punch1_active:
            if punch1_rect.x > width:
                punch1_active = False
                punch1_rect.x = -100
        if punch2_active:
            if punch2_rect.x < -100:
                punch2_active = False
                punch2_rect.x = width

        if punch1_rect.colliderect(player2) and not shield2_active:
            punch1_rect.x += punch_speed
            health2 -= 0.1
            if health2 <= 0:
                current_fight_time=fight_duration+1
                
        if punch2_rect.colliderect(player1) and not shield1_active:
            punch2_rect.x += punch_speed
            health1 -= 0.1
            if health1 <= 0:
                current_fight_time=fight_duration+1  

        # Draw players
        screen.blit(p1, player1)
        screen.blit(p2, player2)

        # Draw health bars
        pygame.draw.rect(screen, GREEN, (player1.x, player1.y - 10, health1, 5))
        pygame.draw.rect(screen, GREEN, (player2.x, player2.y - 10, health2, 5))

        # Draw shields
        if shield1_active:
            screen.blit(shield1_image,shield1.topright)
        if shield2_active:
            screen.blit(shield2_image,shield2.topleft)
                
        #Draw swords
        if punch1_active:
            screen.blit(punch1,punch1_rect.topleft)
        if punch2_active:
            screen.blit(punch2,punch2_rect.topleft)    

        #Draw timer
        timer_text = timer_font.render(f"Time: {int(fight_duration - current_fight_time)}", True, (255, 255, 255))
        timer_rect = timer_text.get_rect(topright=(width - 10, 10))
        screen.blit(timer_text, timer_rect)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate for timer
        clock.tick(60)

        # Update the fight timer
        current_fight_time += clock.get_time() / 1000  # Convert to seconds

        #Check if the fight time has exceeded the duration
        if current_fight_time >= fight_duration:
            current_fight_time = 0  
            # Delay before quitting
            continue_rect=continue_text.get_rect()
            quit_rect=quit_text.get_rect()
            next_rect=next_round_text.get_rect()
            continue_rect.x=250
            continue_rect.y=250
            next_rect.x=250
            next_rect.y=300
            quit_rect.x=250
            quit_rect.y=350
            if health1>0 and health2>0:
                screen.blit(continue_text, continue_rect)
            screen.blit(quit_text, quit_rect)
            screen.blit(next_round_text, next_rect)
            pygame.display.flip()
            pygame.time.delay(3000)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button
                    if continue_rect.collidepoint(event.pos):
                        screen.blit(new_background, (0, 0))
                        pygame.display.flip()
                        game_active = False
                        screen.blit(continue_text_screen, (width // 2 - game_over_text.get_width() // 2, height // 2 - game_over_text.get_height() // 2))
                        pygame.display.flip()
                        pygame.time.delay(2000)
                    elif quit_rect.collidepoint(event.pos):
                        screen.blit(new_background, (0, 0))
                        pygame.display.flip()
                        game_active = False
                        screen.blit(game_over_text, (width // 2 - game_over_text.get_width() // 2, height // 2 - game_over_text.get_height() // 2))
                        pygame.display.flip()
                        pygame.time.delay(2000)
                        pygame.quit()
                    elif next_rect.collidepoint(event.pos):
                        screen.blit(new_background, (0, 0))
                        pygame.display.flip()
                        game_active = False
                        screen.blit(next_round_text_screen, (width // 2 - game_over_text.get_width() // 2, height // 2 - game_over_text.get_height() // 2))
                        pygame.display.flip()
                        pygame.time.delay(2000)
                        health1=70
                        health2=70
                        player1.x = 70  # Set the desired x-coordinate for player 1
                        player1.y = 300  # Set the desired y-coordinate for player 1
                        player2.x = 650  # Set the desired x-coordinate for player 2
                        player2.y = 300  # Set the desired y-coordinate for player 2
    else:
        # Draw countdown on the screen
        countdown_text = countdown_font.render(str(countdown), True, (255, 255, 255))
        countdown_rect = countdown_text.get_rect(center=(width // 2, height // 2))
        screen.blit(countdown_text, countdown_rect)
        pygame.display.flip()

        # Countdown logic
        if countdown > 0:
            pygame.time.delay(1000)  # Delay for 1 second
            countdown -= 1
        else:
            countdown=3
            screen.blit(new_background, (0, 0))
            pygame.display.flip()
            game_active = True
            screen.blit(fight_text_screen, fight_text_screen.get_rect(center=(width // 2, height // 2)))
            pygame.display.flip()
            pygame.time.delay(2000)
            
        # Cap the frame rate
        clock.tick(1)  # Cap at 1 frame per second for countdown

# Display "Game Over"
screen.blit(game_over_text, (width // 2 - game_over_text.get_width() // 2, height // 2 - game_over_text.get_height() // 2))
pygame.display.flip()

# Delay before quitting
pygame.time.delay(2000)

# Clean up and quit
pygame.quit()