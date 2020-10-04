#!/usr/bin/env python

import pygame

class Cell:
	def __init__(self, xPos, yPos, scale):
		self.isVisited = False
		self.solutionVisited = False
		self.isWall = False
		self.height = scale
		self.width = scale
		self.color = (0, 0, 0)
		self.x = xPos
		self.y = yPos