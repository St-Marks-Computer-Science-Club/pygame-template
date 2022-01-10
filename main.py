import pygame
import sys

pygame.init()

window = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Please replace this text with the name of your app")

running = True 

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                # run code for a w key press
                print("w key pressed meaning up")

            if event.key == pygame.K_a:
                # run code for a a key press
                print("a key pressed meaning left")

            if event.key == pygame.K_s:
                # run code for a s key press
                print("s key pressed meaning down")

            if event.key == pygame.K_d:
                # run code for a d key press
                print("d key pressed meaning right")
                
    
    # write all code here


    pygame.display.update()