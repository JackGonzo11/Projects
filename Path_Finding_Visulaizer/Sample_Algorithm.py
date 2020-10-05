#!/usr/bin/env python

from Algorithm_Examples import *
from Maze_Generator import Maze
import pygame
import time

val = input("Enter how big you want the maze to be ")
game = Maze(int(val))
pygame.init()
pygame.mixer.init
pygame.display.set_caption("Maze Generator")
isRunning = True
#visualizer = Depth_First_Search(game)
#visualizer.depth_first_search()

visualizer = Dijkstra(game)

game.draw_maze()
while isRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
            	isRunning = False  
            
            # KEYBOARD EVENTS
            if event.type == pygame.KEYDOWN:
            	# escape key
            	if event.key == pygame.K_ESCAPE:
            		isRunning = False
        pygame.display.update()
