#!/usr/bin/env python

# import statements
import pygame
import time
import random
from Cell import Cell
random.seed()


class Maze:
	def __init__(self, r):
		# Maze window specs
		self.width = 1000                   
		self.height = 1000
		self.pygameScreen = pygame.display.set_mode((self.width, self.height))

		# define colors
		self.white = (255,255,255)
		self.green = (0, 255, 0)
		self.blue = (0, 0, 255)
		self.yellow = (255, 255, 0)
		self.black = (0, 0, 0)

		# define the Maze variables
		self.rows = r
		self.cols = r
		self.cellList = [[Cell(y,x,(1000/self.cols)) for x in range(self.cols)] for y in range(self.rows)]
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
				self.cellList[cell.x-1][cell.y].color = self.white									# sets the cell to the left as a path
				if(cell.y != self.rows-1) and (self.cellList[cell.x][cell.y+1].isVisited == False):	# (checks to see if the cell is on the bottom row) and (checks if the cell below has been visited)
						self.cellList[cell.x][cell.y+1].isVisited = True							# Marks the cell below as visited
						self.numCellsVisited += 1													# increment numCellsVisited
						self.cellList[cell.x][cell.y+1].isWall = True								# makes the cell below a wall
						self.cellList[cell.x][cell.y+1].solutionVisited = True

				if(cell.y != 0) and (self.cellList[cell.x][cell.y-1].isVisited == False):			# (checks to see if the cell is on the top row) and (checks if the cell above is visited)
						self.cellList[cell.x][cell.y-1].isVisited = True							# marks the cell above as visited
						self.numCellsVisited += 1													# increment numCellsVisited
						self.cellList[cell.x][cell.y-1].isWall = True								# makes the cell above a wall
						self.cellList[cell.x][cell.y-1].solutionVisited = True
				self.currentCell = self.cellList[cell.x-1][cell.y]									# moves current cell to cell to the left
				self.stack.append(self.currentCell)													# append current cell to stack
				self.currentCell.isVisited = True													# mark cell as visited
				self.numCellsVisited += 1

	# Function that moves the current cell left
	def move_up(self, cell):
		if(cell.y > 0) and (self.cellList[cell.x][cell.y-1].isVisited == False):					# (checks to see if the cell is on the top row) and (checks if the cell above has been visited)
				self.cellList[cell.x][cell.y-1].color = self.white									# sets the cell above as a path
				if(cell.x != 0) and (self.cellList[cell.x-1][cell.y].isVisited == False):			# (checks to see if the cell is on the left side) and (checks to see if the cell to the left is visited)
						self.cellList[cell.x-1][cell.y].isVisited = True							# marks cell to the left as visited
						self.numCellsVisited += 1													# increment numCellsVisited
						self.cellList[cell.x-1][cell.y].isWall = True								# makes the cell to the left a wall
						self.cellList[cell.x-1][cell.y].solutionVisited = True

				if(cell.x != self.cols-1) and (self.cellList[cell.x+1][cell.y].isVisited == False):	# (checks to see if the cell is on the far left side) and (checks to see if the cell to the right has been visited)
						self.cellList[cell.x+1][cell.y].isVisited = True							# marks cell to the right as visited
						self.numCellsVisited += 1													# increment numCellsVisited
						self.cellList[cell.x+1][cell.y].solutionVisited = True
						self.cellList[cell.x+1][cell.y].isWall = True								# makes the cell to the right a wall
				self.currentCell = self.cellList[cell.x][cell.y-1]									# moves current cell
				self.stack.append(self.currentCell)													# append current cell to stack
				self.currentCell.isVisited = True													# mark cell as visited
				self.numCellsVisited += 1

	# Function that moves the current cell down
	def move_right(self,cell):
		if(cell.x < self.cols-1) and (self.cellList[cell.x+1][cell.y].isVisited == False):			# (checks to see if the cell is on the far ride side) and (checks to see if the cell to the right has been visited)				
				self.cellList[cell.x+1][cell.y].color = self.white									# sets the cell to the right as a path
				if(cell.y != 0) and (self.cellList[cell.x][cell.y-1].isVisited == False):			# (checks if the cell is on the top row) and (checks if the cell above is visited)
						self.cellList[cell.x][cell.y-1].isVisited = True							# marks cell above as visited
						self.numCellsVisited += 1													# increment numCellsVisited
						self.cellList[cell.x][cell.y-1].isWall = True								# makes the cell above a wall
						self.cellList[cell.x][cell.y-1].solutionVisited = True

				if(cell.y != self.rows-1) and (self.cellList[cell.x][cell.y+1].isVisited == False):	# (checks if the cell is on the bottom row) and (checks if the cell below is visited)
						self.cellList[cell.x][cell.y+1].isVisited = True							# marks cell below as visited
						self.numCellsVisited += 1													# increment numCellsVisited
						self.cellList[cell.x][cell.y+1].solutionVisited = True
						self.cellList[cell.x][cell.y+1].isWall = True								# makes the cell below a wall
				self.currentCell = self.cellList[cell.x+1][cell.y]									# moves current cell
				self.stack.append(self.currentCell)													
				self.currentCell.isVisited = True													
				self.numCellsVisited += 1															

	# Function that moves the current cell right
	def move_down(self, cell):
		if(cell.y < self.rows-1) and (self.cellList[cell.x][cell.y+1].isVisited == False):			# (checks if the cell is on bottom row) and (checks if the cell below has been visited)				
				self.cellList[cell.x][cell.y+1].color = self.white									# sets the cell below as a path
				if(cell.x != 0) and (self.cellList[cell.x-1][cell.y].isVisited == False):			# (checks if the cell is on the far left side) and (checks if the cell to the left is visited)
						self.cellList[cell.x-1][cell.y].isVisited = True							# marks cell to the left as visited
						self.numCellsVisited += 1													# increment numCellsVisited
						self.cellList[cell.x-1][cell.y].isWall = True								# makes the cell to the left a wall
						self.cellList[cell.x-1][cell.y].solutionVisited = True

				if(cell.x != self.cols-1) and (self.cellList[cell.x+1][cell.y].isVisited == False): # (checks if the cell is on the far right side) and (checks if the cell to the right is visited)
						self.cellList[cell.x+1][cell.y].isVisited = True							# marks cell to the right as visited
						self.numCellsVisited += 1													# increment numCellsVisited
						self.cellList[cell.x+1][cell.y].solutionVisited = True
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
	# draws the maze using the pygame module
	def draw_maze(self):

		for r in self.cellList:
			for c in r:
				pygame.draw.rect(self.pygameScreen, c.color, (c.x*(1000/self.rows), c.y*(1000/self.cols), c.width, c.width))


'''
# Pygame startup
game = Maze(50)
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
'''
