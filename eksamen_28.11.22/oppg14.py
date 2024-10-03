from uib_inf100_graphics import *

def app_started(app):
    app.racket_x = app.width//2
    app.racket_y = app.height//2
    app.racket_height = 25
    app.dx = -4
    app.dy = 5
    app.is_paused = False
    app.timer_delay = 25 # millisekunder

def key_pressed(app, event):
    if event.key == "p":
        app.is_paused = not app.is_paused
    elif event.key == "s":
        do_step(app)

def timer_fired(app):
    if not app.is_paused:
        do_step(app)

def do_step(app):
    # Flytt horisontalt
    app.racket_x += app.dx

    # Sjekk om firkanten har gått utenfor lerretet, og hvis ja, snu
    # retning; men flytt også firkanten til kanten (i stedet for å gå
    # forbi). Merk: det finnes andre, mer sofistikerte måter å håndtere
    # at rektangelet går forbi kanten...
    if app.racket_x < 0:
        # snu retningen!
        app.racket_x = 0
        app.dx = -app.dx
    elif app.racket_x > app.width - app.racket_height:
        app.racket_x = app.width - app.racket_height
        app.dx = -app.dx
    
    # Flytt vertikalt på samme måte
    app.racket_y += app.dy
    if app.racket_y < 0:
        # snu retningen!
        app.racket_y = 0
        app.dy = -app.dy
    elif app.racket_y > app.height - app.racket_height:
        app.racket_y = app.height - app.racket_height
        app.dy = -app.dy

def redraw_all(app, canvas):
    # tegn firkanten
    canvas.create_oval(
        app.racket_x,
        app.racket_y,
        app.racket_x + app.racket_height,
        app.racket_y + app.racket_height,
        fill="yellow",
    )
    # tegn teksten
    canvas.create_text(
        app.width/2, 20,
        text="Trykk 'p' for å sette på pause",
    )
    canvas.create_text(
        app.width/2, 40,
        text="Trykk 's' for å gjør et enkelt steg",
    )

run_app(width=400, height=150)
