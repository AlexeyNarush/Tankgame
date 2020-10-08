import settings
from color import *
import threading
import pygame
import time

#Tank class with settings and functions 
class Tank:
    # Main patameters of tanks
	def __init__(self, coorX, coorY, img, direct, r):
		self.X = coorX
		self.Y = coorY
		self.img = img
		self.simg = img 
		self.sheald = 0
		self.hp = 3
		self.direct = direct
		self.reverse = r
		self.drive = False
	# Moving functions for tanks
	def move(self, direct, screen, grid, boxes, enemy):
		if (direct == 1):
			self.img = pygame.transform.rotate(self.simg, 180)
		if (direct == 2):
			self.img = pygame.transform.rotate(self.simg, 90)
		if (direct == 3):
			self.img = self.simg
		if (direct == 4):
			self.img = pygame.transform.rotate(self.simg, -90)
		if (direct != self.direct):
			self.direct = direct
			return
		if self.drive == False:
			self.thread = threading.Thread(target=self.smoothmove, args = (screen, grid, boxes, enemy))
			self.thread.start()	
	# Function  to make tank move smooth 
	def smoothmove(self, screen, grid, boxes , enemy):
		dx = 0
		dy = 0
		if (self.direct == 1):
			dy = self.reverse
		if (self.direct == 2):
			dx = -self.reverse
		if (self.direct == 3):
			dy = -self.reverse
		if (self.direct == 4):
			dx = self.reverse
		x = self.X + dx * 50 
		y = self.Y + dy * 50
		# This part of code not letting tank to go throught boxes and each other 
		if (enemy.X, enemy.Y) == (x, y):
			return
		for i in boxes:
			if (i.X, i.Y) == (x, y):
				return
		if (x < 0 or y < 0 or x > settings.height - settings.block or y > settings.width - settings.block):
			return
		self.drive = True
		i = 1
		# Function prevents tank image from stucking and redraws the grid
		while (i <= 50):
			circB = pygame.draw.rect(screen, BLACK, (self.X, self.Y, settings.block, settings.block))
			grid.draw(screen)
			pygame.display.update(pygame.Rect(self.X, self.Y, settings.block, settings.block))
			self.X += dx
			self.Y += dy
			screen.blit(self.img, (self.X, self.Y))
			i += 1
			pygame.display.update(pygame.Rect(self.X, self.Y, settings.block, settings.block))
		self.drive = False
		return
	# Ment to give sheald to hited player and protect him from getting hit again instantly 
	def Sheald(self,):
		stime = time.time()
		self.sheald = 2
		while (time.time() - stime < 2):
			self.sheald = 2 - (time.time() - stime)
		self.sheald = 0
	




	



