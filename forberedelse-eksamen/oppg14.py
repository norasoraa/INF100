from uib_inf100_graphics import *

def app_started(app):
    app.rows = 5
    app.cols = 8
    app.margin = 50 # margin rundt rutenettet
    app.peker = (-1, -1) # (row, col) for valgt rute, (-1,-1) for ingen
    app.poeng = 0
    app.mudvarp = muldvarp_at_random_location(app)



import random
def muldvarp_at_random_location(app):
    row = random.choice(range(5))
    col = random.choice(range(8))
    while app[row][col] != 0:
        row = random.choice(range(5))
        col = random.choice(range(8))
    else:
        app[row][col] -= 1

def point_in_grid(app, x, y):
    # returner True hvis piksel-koordinatet (x, y) er på innsiden av
    # rutenettet slik det blir tegnet i visningen.
    return ((app.margin <= x <= app.width-app.margin) and
            (app.margin <= y <= app.height-app.margin))

def get_cell(app, x, y):
    # "visning-til-modell"
    # returnerer (row, col) for ruten hvor piksel-koordnatet (x, y) hører hjemme,
    # eller (-1, -1) hvis koodinatet er utenfor rutenettet
    if (not point_in_grid(app, x, y)):
        return (-1, -1)
    grid_width  = app.width - 2*app.margin
    grid_height = app.height - 2*app.margin
    cell_width  = grid_width / app.cols
    cell_height = grid_height / app.rows

    # Merk: vi trenger å konvertere til int her; det er ikke 
    # tilstrekkelig å benytte //, siden x, y, eller app.margin kan
    # være flyttall, og da vil også // returnere flyttall
    row = int((y - app.margin) / cell_height)
    col = int((x - app.margin) / cell_width)

    return (row, col)

def get_cell_bounds(app, row, col):
    # "modell-til-visning"
    # returnerer (x0, y0, x1, y1), piksel-koordinater for hjørnene til
    # den gitte ruten
    grid_width  = app.width - 2*app.margin
    grid_height = app.height - 2*app.margin
    column_width = grid_width / app.cols
    row_height = grid_height / app.rows
    x0 = app.margin + col * column_width
    x1 = app.margin + (col+1) * column_width
    y0 = app.margin + row * row_height
    y1 = app.margin + (row+1) * row_height
    return (x0, y0, x1, y1)

def mouse_pressed(app, event):
    (row, col) = get_cell(app, event.x, event.y)
    # velg denne ruten med mindre den allerede er valgt
    if (app.selection == (row, col)):
        app.selection = (-1, -1)
    else:
        app.selection = (row, col)

def redraw_all(app, canvas):
    # tegn alle rutene
    for row in range(app.rows):
        for col in range(app.cols):
            (x0, y0, x1, y1) = get_cell_bounds(app, row, col)
            fill = "orange" if (app.selection == (row, col)) else "cyan"
            canvas.create_rectangle(x0, y0, x1, y1, fill=fill)
    canvas.create_text(app.width/2, 25/2, text=f'Poeng: {app.poeng}')

run_app(width=400, height=300)