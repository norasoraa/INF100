from uib_inf100_graphics import *

def draw_stripes_vertical(app, canvas, lines):
    for i in range(lines):
        canvas.create_line((app.width/3)*(i+1), app.height/9, (app.width/3)*(i+1), app.height-(app.height/9), fill='red', width=5)

def draw_steps(app, canvas, steps):
    for i in range(steps):
        canvas.create_line(app.width/3, app.height/9+(app.height/9)*(i+1), app.width-(app.width/3), app.height/9+(app.height/9)*(i+1), fill='red', width=5)



def redraw_all(app, canvas):
    draw_stripes_vertical(app, canvas, 2)
    draw_steps(app, canvas, 6)

run_app(width=300, height=400)