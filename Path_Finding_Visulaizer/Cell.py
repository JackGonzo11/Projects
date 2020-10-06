#!/usr/bin/env python
import pygame
import sys

class Cell:
	def __init__(self, xPos, yPos, scale):
		#initialize class variables for maze generator
		self.isWall = False
		self.height = scale
		self.width = scale
		self.color = (0, 0, 0)
		self.x = xPos
		self.y = yPos
		self.isVisited = False
		# initialize class variables used by dijkstra's algorithm
		self.solutionVisited = False
		self.dijkstraDist = sys.maxsize
		self.dijkstraPrev = None
		# initialize class variables used by A*
		self.adjacent = []
		self.aStarDist = 0

	# function that allows "<" in cell comparison. It looks at the dijkstraDist object for comparison
	def __lt__(self, obj):
		return self.dijkstraDist < obj.dijkstraDist
