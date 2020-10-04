#!/usr/bin/env python
from Maze_Generator import Maze
import pygame
class Solution_Visualizer:
	def __init__(self, maze):
		self.maze = maze
		self.solutionStack = []

	def check_right(self):
		return	(self.maze.currentCell.x < self.maze.cols-1) and self.maze.cellList[self.maze.currentCell.x+1][self.maze.currentCell.y].isWall == False and (self.maze.cellList[self.maze.currentCell.x+1][self.maze.currentCell.y].solutionVisited == False)

	def check_down(self):
		return	(self.maze.currentCell.y < self.maze.rows-1) and (self.maze.cellList[self.maze.currentCell.x][self.maze.currentCell.y+1].isWall == False) and (self.maze.cellList[self.maze.currentCell.x][self.maze.currentCell.y+1].solutionVisited == False)

	def check_left(self):
		return	(self.maze.currentCell.x != 0) and (self.maze.cellList[self.maze.currentCell.x-1][self.maze.currentCell.y].isWall == False) and (self.maze.cellList[self.maze.currentCell.x-1][self.maze.currentCell.y].solutionVisited == False)

	def check_up(self):
		return	(self.maze.currentCell.y != 0) and (self.maze.cellList[self.maze.currentCell.x][self.maze.currentCell.y-1].isWall == False) and (self.maze.cellList[self.maze.currentCell.x][self.maze.currentCell.y-1].solutionVisited == False)

	def move_right(self):
		self.maze.currentCell = self.maze.cellList[self.maze.currentCell.x+1][self.maze.currentCell.y]
		self.maze.currentCell.solutionVisited = True
		self.solutionStack.append(self.maze.currentCell)
		self.maze.currentCell.color = self.maze.yellow

	def move_down(self):
		self.maze.currentCell = self.maze.cellList[self.maze.currentCell.x][self.maze.currentCell.y+1]
		self.maze.currentCell.solutionVisited = True
		self.solutionStack.append(self.maze.currentCell)
		self.maze.currentCell.color = self.maze.yellow

	def move_left(self):
		self.maze.currentCell = self.maze.cellList[self.maze.currentCell.x-1][self.maze.currentCell.y]
		self.maze.currentCell.solutionVisited = True
		self.solutionStack.append(self.maze.currentCell)
		self.maze.currentCell.color = self.maze.yellow

	def move_up(self):
		self.maze.currentCell = self.maze.cellList[self.maze.currentCell.x][self.maze.currentCell.y-1]
		self.maze.currentCell.solutionVisited = True
		self.solutionStack.append(self.maze.currentCell)
		self.maze.currentCell.color = self.maze.yellow

	def depth_first_search(self):
		self.maze.currentCell.solutionVisited = True
		self.solutionStack.append(self.maze.currentCell)
		while (self.maze.currentCell != self.maze.endCell):
			if (self.check_right()):
				self.move_right()
			elif (self.check_down()):
				self.move_down()
			elif (self.check_left()):
				self.move_left()
			elif (self.check_up()):
				self.move_up()
			else:
				self.maze.currentCell.color = self.maze.white
				self.solutionStack.pop()
				self.maze.currentCell = self.solutionStack[-1]
		self.maze.endCell.color = self.maze.blue

game = Maze(10)
pygame.init()
pygame.mixer.init
pygame.display.set_caption("Maze Generator")
isRunning = True
visualizer = Solution_Visualizer(game)
visualizer.depth_first_search()

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
