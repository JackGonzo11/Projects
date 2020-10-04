#!/usr/bin/env python
from Maze_Generator import Maze
import pygame
# Pygame startup
val = input("Enter how big you want the maze to be ")
game = Maze(int(val))
pygame.init()
pygame.mixer.init
pygame.display.set_caption("Maze Generator")
isRunning = True
game.draw_maze()
print("done")
while isRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
            	isRunning = False  

        pygame.display.flip()