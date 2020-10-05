#!/usr/bin/env python

import pygame
import sys

class Cell:
	def __init__(self, xPos, yPos, scale):
		self.adjacent = []
		self.isVisited = False
		self.dijkstraDist = sys.maxsize
		self.dijkstraPrev = None
		self.aStarDist = 0
		self.solutionVisited = False
		self.isWall = False
		self.height = scale
		self.width = scale
		self.color = (0, 0, 0)
		self.x = xPos
		self.y = yPos

	def __lt__(self, obj):
		return self.dijkstraDist < obj.dijkstraDist
