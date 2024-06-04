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


screen = pygame.display.set_mode((400,600))
pygame.display.set_caption("Let's Tetris")
block_size = 30

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


rotated_blocks = {k: rotate_clockwise(v) for k,v in blocks.items()}
running = True


while running:
    screen.fill(WHITE)

    # 블록 그리기 (회전 전)
    draw_block('I', blocks['I'], 30, 30)
    draw_block('O', blocks['O'], 150, 30)
    draw_block('T', blocks['T'], 270, 30)
    draw_block('S', blocks['S'], 30, 150)
    draw_block('Z', blocks['Z'], 150, 150)
    draw_block('J', blocks['J'], 270, 150)
    draw_block('L', blocks['L'], 30, 270)

    # 회전된 블록 그리기
    draw_block('I', rotated_blocks['I'], 30, 360)
    draw_block('O', rotated_blocks['O'], 150, 360)
    draw_block('T', rotated_blocks['T'], 270, 360)
    draw_block('S', rotated_blocks['S'], 30, 480)
    draw_block('Z', rotated_blocks['Z'], 150, 480)
    draw_block('J', rotated_blocks['J'], 270, 480)
    draw_block('L', rotated_blocks['L'], 30, 600)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()