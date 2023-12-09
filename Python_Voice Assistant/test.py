# import pygame
# import os

# # Initialize pygame
# pygame.init()

# # Initialize pygame mixer
# pygame.mixer.init()

# def turnon_sound():
#     try:
#         pygame.mixer.music.load("startup.mp3")
#         pygame.mixer.music.play()
#     except pygame.error as e:
#         print(f"Error loading or playing the sound: {e}")

# # Call the turnon_sound function
# turnon_sound()

import pygame
import os

# Suppress welcome message
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

# Initialize pygame
pygame.init()

# Initialize pygame mixer
pygame.mixer.init()

# Load and play a simple sound
pygame.mixer.Sound("startup.mp3").play()

# Keep the program running for a while to allow the sound to play
pygame.time.delay(5000)