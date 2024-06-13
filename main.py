import random
import pygame, sys


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
CYAN = (0, 255, 255)
PURPLE = (128, 0, 128)


cell_size = 20
cols = 15
rows = 20
score_width = 150
maxfps = 60


blocks = {
    'I': [(0, 1), (1, 1), (2, 1), (3, 1)],
    'O': [(1, 0), (2, 0), (1, 1), (2, 1)],
    'T': [(1, 0), (0, 1), (1, 1), (2, 1)],
    'S': [(1, 0), (2, 0), (0, 1), (1, 1)],
    'Z': [(0, 0), (1, 0), (1, 1), (2, 1)],
    'J': [(0, 0), (0, 1), (1, 1), (2, 1)],
    'L': [(2, 0), (0, 1), (1, 1), (2, 1)]
}


colors = {
    'I': RED,
    'O': GREEN,
    'T': BLUE,
    'S': YELLOW,
    'Z': ORANGE,
    'J': CYAN,
    'L': PURPLE
}


pygame.init()
screen = pygame.display.set_mode((cell_size * cols + score_width, cell_size * rows))
pygame.display.set_caption("Let's Tetris")
block_size = 20
font = pygame.font.Font(None , 36)

def draw_start_button(screen , text = "Start") :
    button_text = font.render(text, True, BLACK)
    button_rect = pygame.Rect((cell_size * cols + score_width) // 2 - 50, (cell_size * rows) // 2 - 25, 100, 50)
    pygame.draw.rect(screen, WHITE, button_rect)
    screen.blit(button_text, (button_rect.x + (100 - button_text.get_width()) // 2, button_rect.y + (50 - button_text.get_height()) // 2))
    return button_rect


def draw_block(block_type, block_position, offset_x, offset_y):
    for pos in block_position:
        x = pos[0] * block_size + offset_x
        y = pos[1] * block_size + offset_y
        pygame.draw.rect(screen, colors[block_type], (x, y, block_size, block_size))


def draw_board(board, screen):
    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(screen, colors[cell], (x * cell_size, y * cell_size, cell_size, cell_size))
            pygame.draw.rect(screen, WHITE, (x * cell_size, y * cell_size, cell_size, cell_size), 1)


def level_display(screen , level) :
    level_text = font.render(f"Level {level}" , True , WHITE)
    screen.blit(level_text ,  (screen.get_width() // 2 - level_text.get_width() // 2, (cell_size * rows) // 2 - 60))
    pygame.display.flip()
    pygame.time.wait(1000)


def gameover_display(screen) :
    gameover_text = font.render("Game Over" , True , WHITE)
    screen.blit(gameover_text ,  (screen.get_width() // 2 - gameover_text.get_width() // 2, (cell_size * rows) // 2 - 60))
    pygame.display.flip()
    pygame.time.wait(2000)



def rotate_clockwise(block_shape):
    return [(y, -x) for x, y in block_shape]


def clear_row(board):
    new_board = [row for row in board if any(cell == 0 for cell in row)]
    cleared_rows = rows - len(new_board)
    return [[0 for _ in range(cols)] for _ in range(cleared_rows)] + new_board, cleared_rows


def update_board(board, block, offset, block_type):
    off_x, off_y = offset
    for pos in block:
        x = pos[0] + off_x
        y = pos[1] + off_y
        if y >= 0:
            board[y][x] = block_type
    return board


def new_block():
    block_type = random.choice(list(blocks.keys()))
    return block_type, blocks[block_type]


def check_collision(board, block, offset):
    off_x, off_y = offset
    for pos in block:
        x = pos[0] + off_x
        y = pos[1] + off_y
        if x < 0 or x >= cols or y >= rows:
            return True
        if y >= 0 and board[y][x]:
            return True
    return False


def main() :
    game_over = False
    paused = False
    board = [[0 for _ in range(cols)] for _ in range(rows)]
    cur_block, cur_shape = new_block()
    cur_pos = [cols // 2, 0]
    clock = pygame.time.Clock()

    fall_time = 0
    fall_speed = 0.1

    move_speed = 0.08
    move_time = 0

    score = 0
    level = 1
    line_cleared = 0


    start = False
    while not start :
        screen.fill(BLACK)
        buttun_rect = draw_start_button(screen)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if buttun_rect.collidepoint(event.pos):
                    start = True

    level_display(screen , level)

    while not game_over:
        screen.fill(BLACK)

        dt = clock.tick(maxfps) / 1000
        fall_time += dt
        move_time += dt

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = not paused
                if not paused:
                    ########################################
                    ############### PHASE 2 ################
                    ########################################
                    # if event.key == pygame.K_LEFT:
                    #     if not check_collision(board, cur_shape, (cur_pos[0] - 1, cur_pos[1])):
                    #         cur_pos[0] -= 1
                    # if event.key == pygame.K_RIGHT:
                    #     if not check_collision(board, cur_shape, (cur_pos[0] + 1, cur_pos[1])):
                    #         cur_pos[0] += 1
                    # if event.key == pygame.K_DOWN:
                    #     if not check_collision(board, cur_shape, (cur_pos[0], cur_pos[1] + 1)):
                    #         cur_pos[1] += 1
                    ########################################
                    ############### PHASE 2 ################
                    ########################################
                    if event.key == pygame.K_RSHIFT or event.key == pygame.K_LSHIFT:
                        rotated_shape = rotate_clockwise(cur_shape)
                        if not check_collision(board, rotated_shape, cur_pos):
                            cur_shape = rotated_shape
                    ########################################
                    ############### PHASE 2 ################
                    ########################################
                    if event.key == pygame.K_SPACE:
                        while not check_collision(board, cur_shape, (cur_pos[0], cur_pos[1] + 1)):
                            cur_pos[1] += 1
                    ########################################
                    ############### PHASE 2 ################
                    ########################################

        keys = pygame.key.get_pressed()
        if not paused:
            if keys[pygame.K_LEFT] and move_time >= move_speed:
                if not check_collision(board, cur_shape, (cur_pos[0] - 1, cur_pos[1])):
                    cur_pos[0] -= 1
                move_time = 0
            if keys[pygame.K_RIGHT] and move_time >= move_speed:
                if not check_collision(board, cur_shape, (cur_pos[0] + 1, cur_pos[1])):
                    cur_pos[0] += 1
                move_time = 0
            ########################################
            ############### PHASE 2 ################
            ########################################
            if keys[pygame.K_DOWN] and move_time >= move_speed:
                if not check_collision(board, cur_shape, (cur_pos[0], cur_pos[1]+1)):
                    cur_pos[1] += 1
                move_time = 0
            ########################################
            ############### PHASE 2 ################
            ########################################
            if fall_time >= fall_speed:
                fall_time = 0
                if not check_collision(board, cur_shape, (cur_pos[0], cur_pos[1] + 1)):
                    cur_pos[1] += 1
                else:
                    board = update_board(board, cur_shape, cur_pos, cur_block)
                    board, cleared_rows = clear_row(board)
                    line_cleared += cleared_rows
                    score += cleared_rows*100

                    if line_cleared >= level *10 :
                        level += 1
                        fall_speed = max(0.1 , fall_speed - 0.05)
                        level_display(screen , level)
                            
                    cur_block, cur_shape = new_block()
                    cur_pos = [cols // 2, 0]
                    if check_collision(board, cur_shape, cur_pos):
                        game_over = True
                        break

                        
        draw_board(board, screen)
        draw_block(cur_block, cur_shape, cur_pos[0] * cell_size, cur_pos[1] * cell_size)

        if paused:
            text = font.render("Paused", True, WHITE)
            screen.blit(text, (screen.get_width() // 2 - text.get_width() // 2, screen.get_height() // 2 - text.get_height() // 2))


        score_text = font.render(f"Score: {score}", True, WHITE)
        level_text = font.render(f"Level: {level}", True, WHITE)
        screen.blit(score_text, (cell_size * cols + 10, 10))
        screen.blit(level_text, (cell_size * cols + 10, 50))
        

        pygame.display.flip()
        clock.tick(maxfps)


    gameover_display(screen)

    restart = False
    while not restart :
        screen.fill(BLACK)
        button_rect = draw_start_button(screen , "Restart")
        pygame.display.flip()


        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_rect.collidepoint(event.pos):
                        restart = True



if __name__ == "__main__" :
    main()