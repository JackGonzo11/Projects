#!/usr/bin/env python

# import statements
import pygame
import time
import random
import math
from Cell import Cell
random.seed()


class Maze:
	def __init__(self, r, window_size):
		# Maze window specs
		self.width = window_size                   
		self.height = window_size
		self.pygameScreen = pygame.display.set_mode((self.width, self.height))

		# define colors
		self.white = (255,255,255)
		self.green = (0, 255, 0)
		self.blue = (0, 0, 255)
		self.yellow = (255, 255, 0)
		self.black = (0, 0, 0)
		self.red = (255, 0, 0)

		# define the Maze variables
		self.rows = r
		self.cols = r
		self.cellList = [[Cell(y,x,(window_size/self.cols)) for x in range(self.cols)] for y in range(self.rows)]
		self.stack = []
		self.currentCell = self.cellList[0][0]
		self.endCell = self.cellList[self.rows-1][self.cols-1]
		self.numCellsVisited = 0
		
		# Initialize maze
		self.create_maze()
		self.currentCell = self.cellList[0][0]

	# Function that moves the current cell up
	def move_left(self, cell):
		if(cell.x > 0) and (self.cellList[cell.x-1][cell.y].isVisited == False):					# (checks to make sure the current cell isnt on the far left) and (if the cell to the left has been visited)
				self.cellList[cell.x-1][cell.y].color = self.white
				if(cell.y != self.rows-1) and (self.cellList[cell.x][cell.y+1].isVisited == False):	# (checks to see if the cell is on the bottom row) and (checks if the cell below has been visited)
						self.cellList[cell.x][cell.y+1].isVisited = True							# Marks the cell below as visited
						self.numCellsVisited += 1													# increment numCellsVisited
						self.cellList[cell.x][cell.y+1].isWall = True								# makes the cell below a wall
						self.cellList[cell.x][cell.y+1].solutionVisited = True

				if(cell.y != 0) and (self.cellList[cell.x][cell.y-1].isVisited == False):			# (checks to see if the cell is on the top row) and (checks if the cell above is visited)
						self.cellList[cell.x][cell.y-1].isVisited = True							# marks the cell above as visited
						self.numCellsVisited += 1													# increment numCellsVisited
						self.cellList[cell.x][cell.y-1].isWall = True								# makes the cell above a wall
				self.currentCell = self.cellList[cell.x-1][cell.y]									# moves current cell to cell to the left
				self.stack.append(self.currentCell)													# append current cell to stack
				self.currentCell.isVisited = True													# mark cell as visited
				self.numCellsVisited += 1

	# Function that moves the current cell left
	def move_up(self, cell):
		if(cell.y > 0) and (self.cellList[cell.x][cell.y-1].isVisited == False):					# (checks to see if the cell is on the top row) and (checks if the cell above has been visited)
				self.cellList[cell.x][cell.y-1].color = self.white
				if(cell.x != 0) and (self.cellList[cell.x-1][cell.y].isVisited == False):			# (checks to see if the cell is on the left side) and (checks to see if the cell to the left is visited)
						self.cellList[cell.x-1][cell.y].isVisited = True							# marks cell to the left as visited
						self.numCellsVisited += 1													# increment numCellsVisited
						self.cellList[cell.x-1][cell.y].isWall = True								# makes the cell to the left a wall
						self.cellList[cell.x-1][cell.y].solutionVisited = True						# marks the wall as visited in the solution

				if(cell.x != self.cols-1) and (self.cellList[cell.x+1][cell.y].isVisited == False):	# (checks to see if the cell is on the far left side) and (checks to see if the cell to the right has been visited)
						self.cellList[cell.x+1][cell.y].isVisited = True							# marks cell to the right as visited
						self.numCellsVisited += 1													# increment numCellsVisited
						self.cellList[cell.x+1][cell.y].solutionVisited = True						# marks the wall as visited in the solution
						self.cellList[cell.x+1][cell.y].isWall = True								# makes the cell to the right a wall
				self.currentCell = self.cellList[cell.x][cell.y-1]									# moves current cell
				self.stack.append(self.currentCell)													# append current cell to stack
				self.currentCell.isVisited = True													# mark cell as visited
				self.numCellsVisited += 1

	# Function that moves the current cell down
	def move_right(self,cell):
		if(cell.x < self.cols-1) and (self.cellList[cell.x+1][cell.y].isVisited == False):			# (checks to see if the cell is on the far ride side) and (checks to see if the cell to the right has been visited)
				self.cellList[cell.x+1][cell.y].color = self.white	
				if(cell.y != 0) and (self.cellList[cell.x][cell.y-1].isVisited == False):			# (checks if the cell is on the top row) and (checks if the cell above is visited)
						self.cellList[cell.x][cell.y-1].isVisited = True							# marks cell above as visited
						self.numCellsVisited += 1													# increment numCellsVisited
						self.cellList[cell.x][cell.y-1].isWall = True								# makes the cell above a wall
						self.cellList[cell.x][cell.y-1].solutionVisited = True						# marks the wall as visited in the solution

				if(cell.y != self.rows-1) and (self.cellList[cell.x][cell.y+1].isVisited == False):	# (checks if the cell is on the bottom row) and (checks if the cell below is visited)
						self.cellList[cell.x][cell.y+1].isVisited = True							# marks cell below as visited
						self.numCellsVisited += 1													# increment numCellsVisited
						self.cellList[cell.x][cell.y+1].solutionVisited = True						# marks the wall as visited in the solution
						self.cellList[cell.x][cell.y+1].isWall = True								# makes the cell below a wall
				self.currentCell = self.cellList[cell.x+1][cell.y]									# moves current cell
				self.stack.append(self.currentCell)													
				self.currentCell.isVisited = True													
				self.numCellsVisited += 1															

	# Function that moves the current cell right
	def move_down(self, cell):
		if(cell.y < self.rows-1) and (self.cellList[cell.x][cell.y+1].isVisited == False):			# (checks if the cell is on bottom row) and (checks if the cell below has been visited)	
				self.cellList[cell.x][cell.y+1].color = self.white
				if(cell.x != 0) and (self.cellList[cell.x-1][cell.y].isVisited == False):			# (checks if the cell is on the far left side) and (checks if the cell to the left is visited)
						self.cellList[cell.x-1][cell.y].isVisited = True							# marks cell to the left as visited
						self.numCellsVisited += 1													# increment numCellsVisited
						self.cellList[cell.x-1][cell.y].isWall = True								# makes the cell to the left a wall
						self.cellList[cell.x-1][cell.y].solutionVisited = True						# marks the wall as visited in the solution

				if(cell.x != self.cols-1) and (self.cellList[cell.x+1][cell.y].isVisited == False): # (checks if the cell is on the far right side) and (checks if the cell to the right is visited)
						self.cellList[cell.x+1][cell.y].isVisited = True							# marks cell to the right as visited
						self.numCellsVisited += 1													# increment numCellsVisited
						self.cellList[cell.x+1][cell.y].solutionVisited = True						# marks the wall as visited in the solution
						self.cellList[cell.x+1][cell.y].isWall = True								# makes the cell to the right a wall
				self.currentCell = self.cellList[cell.x][cell.y+1]									# moves current cell
				self.stack.append(self.currentCell)
				self.currentCell.isVisited = True
				self.numCellsVisited += 1

	# checks if the path has lead to a dead end
	def popable(self, cell): 
		result = True
		if(cell.y != self.rows-1) and (self.cellList[cell.x][cell.y+1].isVisited == False):			# Checks to see if the cell is on the bottom, and if the cell below is visited
			result = False
		if(cell.x != self.cols-1) and (self.cellList[cell.x+1][cell.y].isVisited == False):			# Checks to see if the cell is on the far right side, and if the cell on the right is visited
			result = False
		if(cell.y != 0) and (self.cellList[cell.x][cell.y-1].isVisited == False):					# Checks to see if the cell is on the top, and if the cell above is visited
			result = False
		if(cell.x != 0) and (self.cellList[cell.x-1][cell.y].isVisited == False):					# Checks to see if the cell is on the far left side, and if the cell to the left is visited
			result = False
		return result

	# checks to see if 98% of the cells have been visited
	def check_finished(self):
		return self.numCellsVisited < self.rows*self.cols*.98
	
	#initializes adjacencies of each cell
	def set_adjacenties_and_dist(self, cell):
		dist = math.sqrt((cell.x ** 2)+(cell.y ** 2))
		cell.aStarDist = dist
		if(cell.x != self.cols-1) and (not self.cellList[cell.x+1][cell.y].isWall): # checks if the cell to the right is on the edge and is not a wall
			cell.adjacent.append(self.cellList[cell.x+1][cell.y])
		if(cell.x != 0) and (not self.cellList[cell.x-1][cell.y].isWall): # checks if the cell to the left is on the edge and is not a wall
			cell.adjacent.append(self.cellList[cell.x-1][cell.y])
		if(cell.y != self.rows-1) and (not self.cellList[cell.x][cell.y+1].isWall): # checks if the cell below is on the edge and is not a wall
			cell.adjacent.append(self.cellList[cell.x][cell.y+1])
		if(cell.y != 0) and (not self.cellList[cell.x][cell.y-1].isWall): # checks if the cell above is on the edge and is not a wall
			cell.adjacent.append(self.cellList[cell.x][cell.y-1])
	
	# Initializes all of the cells and creates a path
	def create_maze(self):
		self.currentCell.color = self.green				# specify starting cell
		self.currentCell.isVisited = True
		self.numCellsVisited += 1
		self.stack.append(self.currentCell)

		self.endCell.color = self.blue					# specify end cell
		self.endCell.isVisited = True
		self.numCellsVisited += 1

		while(self.check_finished()):					# loop to create the maze using backtracking algorithm
			randomNum = random.randrange(0,4)

			if(self.popable(self.currentCell)):			# checks to see if the maze has hit a dead end
				if(len(self.stack) > 1):
					self.stack.pop()
					self.currentCell = self.stack[-1]
			if(randomNum == 0):							# determines which way to move via the random library
				self.move_up(self.currentCell)			# the reason there are two movements is to create paths
				self.move_up(self.currentCell)
			elif(randomNum == 1):
				self.move_right(self.currentCell)
				self.move_right(self.currentCell)
			elif(randomNum == 2):
				self.move_down(self.currentCell)
				self.move_down(self.currentCell)
			elif(randomNum == 3):
				self.move_left(self.currentCell)
				self.move_left(self.currentCell)

		#loop through all the cells and set their adjacencies
		for r in self.cellList:
			for c in r:
				if(c.isWall == False):
					self.set_adjacenties_and_dist(c)

	# draws the maze using the pygame module
	def draw_maze(self):

		for r in self.cellList:
			for c in r:
				if (c.isWall == False):
					pygame.draw.rect(self.pygameScreen, c.color, (c.x*(self.height/self.rows), c.y*(self.width/self.cols), c.width, c.width))
