#import random

#low= random.randint(9,22)
#high= random.randint(low,22)

#print (low)
#print (high)

#print ('the low number is:', low, '\nthe high number is:', high)


from turtle import *
color ('blue')
forward(100) 
left(60)
color ('red')
forward(100)
left(60)
color ('orange')
forward(100)
left(60)
color ('pink')
forward(100)
left(60)
color ('black')
forward(100)
left (60)
color ('green')
forward (100)


import pygame, sys


window = pygame.display.set_mode((400, 500)) 


BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)


pygame.draw.line(window,    BLUE, (50,   50), (250, 50), 4)
pygame.draw.line(window,    GREEN,(100, 250), (250, 50), 2)
pygame.draw.rect(window,    WHITE,(100, 250,   200, 75))
pygame.draw.circle(window,  RED,  (300, 250),  30, 0)
pygame.draw.ellipse(window, RED,  (200, 400,   40, 80), 1)
