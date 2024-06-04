from random import randrange as rand
import pygame, sys

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
ORANGE = (255,165,0)
CYAN = (0,255,255)
PURPLE = (128,0,128)

blocks = {
    'I' : [(0,1) , (1,1) , (2,1) , (3,1)],
    'O' : [(1,0) , (2,0) , (1,1) , (2,1)],
    'T' : [(1,0) , (0,1) , (1,1) , (2,1)],
    'S' : [(1,0) , (2,0) , (0,1) , (1,1)],
    'Z' : [(0,0) , (1,0) , (1,1) , (2,1)],
    'J' : [(0,0) , (0,1) , (1,1) , (2,1)],
    'L' : [(2,0) , (0,1) , (1,1) , (2,1)]
}



colors = {
    'I' : RED,
    'O' : GREEN,
    'T' : BLUE,
    'S' : YELLOW,
    'Z' : ORANGE,
    'J' : CYAN,
    'L' : PURPLE
}