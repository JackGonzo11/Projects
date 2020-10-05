#!/usr/bin/env python
from Maze_Generator import Maze
import pygame
from queue import PriorityQueue

class Depth_First_Search:
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
		self.maze.currentCell.color = self.maze.red

	def move_down(self):
		self.maze.currentCell = self.maze.cellList[self.maze.currentCell.x][self.maze.currentCell.y+1]
		self.maze.currentCell.solutionVisited = True
		self.solutionStack.append(self.maze.currentCell)
		self.maze.currentCell.color = self.maze.red

	def move_left(self):
		self.maze.currentCell = self.maze.cellList[self.maze.currentCell.x-1][self.maze.currentCell.y]
		self.maze.currentCell.solutionVisited = True
		self.solutionStack.append(self.maze.currentCell)
		self.maze.currentCell.color = self.maze.red

	def move_up(self):
		self.maze.currentCell = self.maze.cellList[self.maze.currentCell.x][self.maze.currentCell.y-1]
		self.maze.currentCell.solutionVisited = True
		self.solutionStack.append(self.maze.currentCell)
		self.maze.currentCell.color = self.maze.red

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

class Dijkstra:
	def __init__(self, maze):
		self.maze = maze
		self.dijkstra()
		self.get_shortest()

	def get_shortest(self):
		current = self.maze.endCell
		while (current != self.maze.cellList[0][0]):
			current.color = self.maze.yellow
			current = current.dijkstraPrev

	def dijkstra(self):
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
						temp = current.dijkstraDist + 1
						if (temp < cell.dijkstraDist):
							cell.dijkstraDist = temp
							cell.dijkstraPrev = current

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