#!/usr/bin/env python
from Maze_Generator import Maze
import pygame
from queue import PriorityQueue

# Depth Frist Search Class
class Depth_First_Search:
	def __init__(self, maze):
		self.maze = maze
		self.solutionStack = []

	# Checks if (The cell is on the right side) and if (the cell to the right is a wall) and if (the cell to the right is visited)
	def check_right(self):
		return	(self.maze.currentCell.x < self.maze.cols-1) and self.maze.cellList[self.maze.currentCell.x+1][self.maze.currentCell.y].isWall == False and (self.maze.cellList[self.maze.currentCell.x+1][self.maze.currentCell.y].solutionVisited == False)

	# Checks if (The cell below is on the bottom row) and if (the cell below is a wall) and if (the cell below is visited)
	def check_down(self):
		return	(self.maze.currentCell.y < self.maze.rows-1) and (self.maze.cellList[self.maze.currentCell.x][self.maze.currentCell.y+1].isWall == False) and (self.maze.cellList[self.maze.currentCell.x][self.maze.currentCell.y+1].solutionVisited == False)

	# Checks if (The cell is on the left side) and if (the cell to the left is a wall) and if (the cell to the left is visited)
	def check_left(self):
		return	(self.maze.currentCell.x != 0) and (self.maze.cellList[self.maze.currentCell.x-1][self.maze.currentCell.y].isWall == False) and (self.maze.cellList[self.maze.currentCell.x-1][self.maze.currentCell.y].solutionVisited == False)

	# Checks if (The cell above is on the top row) and if (the cell above is a wall) and if (the cell above is visited)
	def check_up(self):
		return	(self.maze.currentCell.y != 0) and (self.maze.cellList[self.maze.currentCell.x][self.maze.currentCell.y-1].isWall == False) and (self.maze.cellList[self.maze.currentCell.x][self.maze.currentCell.y-1].solutionVisited == False)

	# Moves the current cell right and changes certain variables
	def move_right(self):
		self.maze.currentCell = self.maze.cellList[self.maze.currentCell.x+1][self.maze.currentCell.y]	# moves the currrent cell to the right
		self.maze.currentCell.solutionVisited = True													# marks the current cell as visited
		self.solutionStack.append(self.maze.currentCell)												# appends the current cell onto the solution stack
		self.maze.currentCell.color = self.maze.yellow													# sets the current cells color to yellow

	# Moves the current cell down and changes certain variables
	def move_down(self):
		self.maze.currentCell = self.maze.cellList[self.maze.currentCell.x][self.maze.currentCell.y+1]	# moves the currrent cell down
		self.maze.currentCell.solutionVisited = True													# marks the current cell as visited
		self.solutionStack.append(self.maze.currentCell)												# appends the current cell onto the solution stack
		self.maze.currentCell.color = self.maze.yellow													# sets the current cells color to yellow

	# Moves the current cell left and changes certain variables
	def move_left(self):
		self.maze.currentCell = self.maze.cellList[self.maze.currentCell.x-1][self.maze.currentCell.y]	# moves the currrent cell to the left
		self.maze.currentCell.solutionVisited = True													# marks the current cell as visited
		self.solutionStack.append(self.maze.currentCell)												# appends the current cell onto the solution stack
		self.maze.currentCell.color = self.maze.yellow													# sets the current cells color to yellow

	# Moves the current cell up and changes certain variables
	def move_up(self):
		self.maze.currentCell = self.maze.cellList[self.maze.currentCell.x][self.maze.currentCell.y-1]	# moves the currrent cell up
		self.maze.currentCell.solutionVisited = True													# marks the current cell as visited
		self.solutionStack.append(self.maze.currentCell)												# appends the current cell onto the solution stack
		self.maze.currentCell.color = self.maze.yellow													# sets the current cells color to yellow

	# function to implement the depth first search algorithm
	def depth_first_search(self):
		self.maze.currentCell.solutionVisited = True													# marks starting cell as visited
		self.solutionStack.append(self.maze.currentCell)												# appends the starting cell to the solution stack
		while (self.maze.currentCell != self.maze.endCell):												# loop while the current cell is not the end cell
			if (self.check_right()):																	# checks if the current cell can move a certain direction
				self.move_right()																		# if possible, it moves
			elif (self.check_down()):
				self.move_down()
			elif (self.check_left()):
				self.move_left()
			elif (self.check_up()):
				self.move_up()
			else:																						# if the current cell cannot move anywhere
				self.maze.currentCell.color = self.maze.white											# changes the color of the current cell to white
				self.solutionStack.pop()																# pop the current cell from the stack
				self.maze.currentCell = self.solutionStack[-1]											# sets the current cell to the top of the solution stack
		self.maze.endCell.color = self.maze.blue														# resets the ending cell to the color blue

# Implement the Dijkstra class
class Dijkstra:
	def __init__(self, maze):
		self.maze = maze
		self.dijkstra()
		self.get_shortest()

	# function to backtrack from the end to the beginning to find the shortest path to the exit
	def get_shortest(self):
		current = self.maze.endCell									# initializes current to the last cell in the maze
		while (current != self.maze.cellList[0][0]):				# loops until current is the starting cell
			current.color = self.maze.yellow						# sets the color of current to yellow
			current = current.dijkstraPrev							# sets the current to the cells prev
		self.maze.endCell.color = self.maze.blue					# resets the end cells color to blue

	# function to implement Dijkstr'a algorithm
	def dijkstra(self):
		self.maze.currentCell.dijkstraDist = 0						# sets the distance of the starting cell to 0
		q = []														# creates a list
		for r in self.maze.cellList:								# loops through every path in the maze
			for c in r:
				current = c
				if (c.isWall == False):
					q.append(current)								# appends each path to q
		while(len(q) != 0):											# loops until q is empty
			q.sort()												# sorts q so that the minimum value is at the front
			current = q.pop(0)										# removes the smallest cell
			current.solutionVisited = True							# marks it as visited
			if (current == self.maze.endCell):						# if the cell is the end cell
				break												# completed!
			else:													# otherwise...
				for cell in current.adjacent:						# for each adjacent cell
					if (cell.solutionVisited == True):				# if the adjacent cell is visited
						continue									# continue, nothing happens
					else:							
						temp = current.dijkstraDist + 1				# else, temp = current cells distance and add 1... This will become the new dijkstraDist
						if (temp < cell.dijkstraDist):				# if this new distance is < the current cells distance
							cell.dijkstraDist = temp				# the adjacent cells distance = temp
							cell.dijkstraPrev = current 			# sets a pointer from the cell it came from for solution purposes


'''
The AStar class is exactly the same as dijkstra's except for one difference.
It adds the distance of each cell to the end cell as a factor in dijkstraDist.
By doing this, the algorithm prioritizes moves that get closer to the end cell and pushes cells that move furthur away from the goal down in the queue.
This is implemented by using pythagorean theorm to calculate the distance... sqrt(a^2 + b^2)
'''
class AStar:
	def __init__(self, maze):
		self.maze = maze
		self.a_star()
		self.get_shortest()


	def get_shortest(self):
		current = self.maze.endCell
		while (current != self.maze.cellList[0][0]):
			current.color = self.maze.yellow
			current = current.dijkstraPrev
		self.maze.endCell.color = self.maze.blue

	def a_star(self):
		self.maze.currentCell.dijkstraDist = 0
		q = []
		for r in self.maze.cellList:
			for c in r:
				current = c
				if (c.isWall == False):
					q.append(current)
		while(len(q) != 0):
			q.sort()
			current = q.pop(0)
			current.solutionVisited = True
			if (current == self.maze.endCell):
				break
			else:
				for cell in current.adjacent:
					if (cell.solutionVisited == True):
						continue
					else:
						temp = current.dijkstraDist + 1 + current.aStarDist
						if (temp < cell.dijkstraDist):
							cell.dijkstraDist = temp
							cell.dijkstraPrev = current
		self.maze.endCell.color = self.maze.blue