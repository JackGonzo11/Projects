#!/usr/bin/env python
from Maze_Generator import Maze
import pygame
# Pygame startup
val = input("Enter how big you want the maze to be(x rows and x columns )")
pixels = input("Enter how big you want window to be (X # of pixels by X # of pixels)")
game = Maze(int(val),int(pixels))
pygame.init()
pygame.mixer.init
pygame.display.set_caption("Maze Generator")
isRunning = True
game.draw_maze()
while isRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
            	isRunning = False  

        pygame.display.flip()