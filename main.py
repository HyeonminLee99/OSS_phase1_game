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

cell_size = 20
cols = 20
rows = 30
maxfps = 30

screen = pygame.display.set_mode((cell_size*cols,cell_size*rows))
pygame.display.set_caption("Let's Tetris")
block_size = 30

cur_block = None
next_block = None
game_over = False
paused = False

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


def draw_block(block_type , block_position , offset_x , offset_y) :
    for pos in block_position :
        x = pos[0] * block_size + offset_x
        y = pos[1] * block_size + offset_y
        pygame.draw.rect(screen , colors[block_type], (x,y,block_size ,block_size))


def rotate_clockwise(block_positions) :
    return [(y,-x) for x,y in block_positions]


def remove_row(board , row) :
    del board[row]
    return [[0 for i in range(cols)]] + board

def new_stone() :
    if cur_block is None :
        cur_block = blocks[rand(len(blocks))]
        next_block = blocks[rand(len(blocks))]

    cur_block = next_block
    next_block = blocks[rand(len(blocks))]


def check_collision(board, block , offset) :
    off_x , off_y = offset
    for cy, row in enumerate(blcok) :
        for cx, cell in enumerate(row) :
            try:
                if cell and board[cy+off_y][cx+off_x] :
                    return True
            except IndexError:
                return True
    return False
"""
def move(board,step) :
    if not game_over and not paused :
        new_x = cur_block + step

        if new_x < 0 :
            new_x = 0
        if new_x > cols - len(cur_block) :
            new_x = cols - len(cur_block)
        if not check_collision(board , )

"""

    



pygame.time.set_timer(pygame.USEREVENT +1 , 1000)
rotated_blocks = {k: rotate_clockwise(v) for k,v in blocks.items()}
running = True



pygame.quit()
sys.exit()