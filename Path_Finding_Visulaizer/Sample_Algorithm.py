#!/usr/bin/env python

from Algorithm_Examples import *
from Maze_Generator import Maze
import pygame
import time

print("------------------------------------------------------------------\n Welcome to the pathfinding algorithm maze solver! \n Choose one of the ooptions below by typing its corresponding number")
print("1. Depth First Search \n2. Dijkstra \n3. A*")
choice = input("------------------------------------------------------------------\n")
val = input("Enter how big you want the maze to be(x rows and x columns )")
pixels = input("Enter how big you want window to be (X # of pixels by X # of pixels)")
game = Maze(int(val),int(pixels))
pygame.init()
pygame.mixer.init
pygame.display.set_caption("Maze Generator")
isRunning = True

if (int(choice) == 1):
	visualizer = Depth_First_Search(game)
	visualizer.depth_first_search()
elif (int(choice) == 2):
	visualizer = Dijkstra(game)
elif (int(choice) == 3):
	visualizer = AStar(game)

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
