from uib_inf100_graphics import *

def get_color(value):
    if value < 0:
        return "cyan"
    if value == 0:
        return "lightgray"
    if value > 0:
        return "orange"


def draw_board(canvas, x1, y1, x2, y2, board, debug_mode):
    rows = len(board)
    cols = len(board[0])
    cell_width = (x2-x1)/cols
    cell_hight = (y2-y1)/rows
    for row in range(rows):
        for col in range(cols):
            color = get_color(board[row][col])
            cell_x1 = x1 + cell_width * col
            cell_y1 = y1 + cell_hight * row
            cell_x2 = cell_x1 + cell_width
            cell_y2 = cell_y1 + cell_hight
            canvas.create_rectangle(cell_x1, cell_y1, cell_x2, cell_y2, fill = color)
            if debug_mode == True:
                cell_mid_x = (cell_x1 + cell_x2) / 2
                cell_mid_y = (cell_y1 + cell_y2) / 2
                canvas.create_text(cell_mid_x, cell_mid_y, text=f"{row},{col}\n{board[row][col]}")


def app_started(app):
    app.board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0,-1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 2, 3, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    app.debug_mode = True
    
    app.head_pos = (3,4)
    
    app.snake_size = 3
    app.direction = "east"
    
    app.state = "active"

    app.timer_delay = 200 # milliseconds


def get_next_head_position(head_row, head_col, direction):
    if direction == "north":
        head_row -= 1
    if direction == "south":
        head_row += 1
    if direction == "east":
        head_col += 1
    if direction == "west":
        head_col -= 1
    return (head_row,head_col)


def subtract_one_from_all_positives(grid):
    rows = len(grid)
    cols = len(grid[0])
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] > 0:
                grid[row][col] -= 1


import random
def add_apple_at_random_location(grid):
    row = random.choice(range(len(grid)))
    col = random.choice(range(len(grid[0])))
    while grid[row][col] != 0:
        row = random.choice(range(len(grid)))
        col = random.choice(range(len(grid[0])))
    else:
        grid[row][col] -= 1


def is_legal_move(row, col, board):
    if row >= len(board) or col >= len(board[0]):
        return False
    if row < 0 or col < 0:
        return False
    if board[row][col] > 0:
        return False
    else:
        return True


def move_snake(app):
    app.head_pos = get_next_head_position(app.head_pos[0], app.head_pos[1], app.direction)
    row, col = app.head_pos
    if is_legal_move(row ,col , app.board) == False:
        app.state = "gameover"
        return
    if app.board[row][col] == -1:
        app.snake_size += 1
        add_apple_at_random_location(app.board)
    else:
        subtract_one_from_all_positives(app.board)
    app.board[row][col] = app.snake_size


def timer_fired(app):
    if app.debug_mode == False and app.state == "active":
        move_snake(app)


def key_pressed(app, event):
    if event.key == "d":
        app.debug_mode = not app.debug_mode
    if app.state == "gameover":
        return 
    if event.key == "Space":
        move_snake(app)
    if event.key == "Up":
        app.direction = "north"
    if event.key == "Down":
        app.direction = "south"
    if event.key == "Left":
        app.direction = "west"
    if event.key == "Right":
        app.direction = "east"


def redraw_all(app, canvas):
    board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 9,10,11, 0,-1, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 6, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 1, 2, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    if app.state == "gameover":
        canvas.create_text(app.width/2, app.height/2, text=f'{"Game Over"}', font="Arial 40")
        return
    draw_board(canvas, 25, 25, app.width-25, app.height-25, app.board, app.debug_mode)
    if app.debug_mode == True:
        canvas.create_text(app.width/2, 25/2, text=f'{app.head_pos=} {app.snake_size=} {app.direction=} {app.state=}')
    

run_app(width=500, height=400, title="Snake")
