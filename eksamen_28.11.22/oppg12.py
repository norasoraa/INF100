from uib_inf100_graphics import *

def draw_turns(app, canvas, turns):
    canvas.create_line((app.width/10), app.height/2, (app.width/10), app.height-app.height/4, fill='green', width=5)
    canvas.create_line((app.width-(app.width/10)*3), app.height/2, (app.width-(app.width/10)*3), app.height/4, fill='green', width=5)
    canvas.create_line((app.width-(app.width/10)*3), app.height/2, (app.width-(app.width/10)*2), app.height/2, fill='green', width=5)
    canvas.create_oval((app.width-(app.width/10)*2.5), app.height/2.5, (app.width-(app.width/10)*1.5), app.height-(app.height/2.5), fill='green', width=5, outline='green')

    for i in range(1,turns):
        canvas.create_line((app.width/10)+((app.width/10)*(i)), app.height/4, (app.width/10)+((app.width/10)*(i)), app.height-app.height/4, fill='green', width=5)
    for i in range(0,turns,2):
        canvas.create_line((app.width/10)+((app.width/10)*(i)), app.height-app.height/4, (app.width/10)+((app.width/10)*(i+1)), app.height-app.height/4, fill='green', width=5)
    for i in range(1,turns,2):
        canvas.create_line((app.width/10)+((app.width/10)*(i)), app.height/4, (app.width/10)+((app.width/10)*(i+1)), app.height/4, fill='green', width=5)

def redraw_all(app, canvas):
    draw_turns(app, canvas, 6)

run_app(width=400, height=200)