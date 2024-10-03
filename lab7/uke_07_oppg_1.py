from uib_inf100_graphics import *

def draw_grid(canvas, x1, y1, x2, y2, color_grid):
    """ Tegner et rutenett med farger. Rutenettet er avgrenset av (x1, y1)
    i hjørnet til venstre oppe, og av (x2, y2) til høyre nede. Listen
    color_grid er en 2D-liste med strenger som representerer farger."""
    rows = len(color_grid)
    cols = len(color_grid[0])
    cell_width = (x2-x1)/cols
    cell_hight = (y2-y1)/rows
    for row in range(rows):
        for col in range(cols):
            cell_x1 = x1 + cell_width * col
            cell_y1 = y1 + cell_hight * row
            cell_x2 = cell_x1 + cell_width
            cell_y2 = cell_y1 + cell_hight
            canvas.create_rectangle(cell_x1, cell_y1, cell_x2, cell_y2, fill = color_grid[row][col])
    

def redraw_all(app, canvas):
    # Et 3x3 rutenett med innebygde farger
    draw_grid(canvas, 50, 20, 130, 100, [
        ["red", "green", "blue"],
        ["yellow", "pink", "cyan"],
        ["black", "gray", "orange"],
    ])

    # Et sjakkbrett
    draw_grid(canvas, 150, 20, 350, 100, [
        ["white", "black"] * 4,
        ["black", "white"] * 4,
    ] * 4)

    # En 2D-liste med kun én rad
    draw_grid(canvas, 50, 120, 350, 180, [
        ['#00c', '#01c', '#02c', '#03c', '#04c', '#05c', '#06c', '#07c',
         '#08c', '#09c', '#0ac', '#0bc', '#0cc', '#0dc', '#0ec', '#0fc']
    ])

run_app(width=400, height=200)
