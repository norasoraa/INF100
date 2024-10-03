from uib_inf100_graphics import *

def app_started(app):
    # Modellen.
    # Denne funksjonen kalles én gang ved programmets oppstart.
    # Her skal vi __opprette__ variabler i som behøves i app.
    app.count = 0
    app.cx = app.width/2
    app.cy = app.height/2
    app.r = 50
    app.dx = -20
    app.dy = 5
    app.debug_mode = False

def timer_fired(app):
    # En kontroller.
    # Denne funksjonen kalles ca 10 ganger per sekund som standard.
    # Funksjonen kan __endre på__ eksisterende variabler i app.
    if app.debug_mode:
        return
    do_step(app)
 
def do_step(app):
    # Flytt
    app.cx += app.dx
    app.cy += app.dy

    # Snu retning hvis utenfor bounds
    if app.cx < app.r:
        app.cx = app.r
        app.dx = -app.dx
    if app.cx > app.width - app.r:
        app.cx = app.width - app.r
        app.dx = -app.dx
    if app.cy < app.r:
        app.cy = app.r
        app.dy = -app.dy
    if app.cy > app.height - app.r:
        app.cy = app.height - app.r
        app.dy = -app.dy

def mouse_pressed(app, event):
    app.cx, app.cy = event.x, event.y

def key_pressed(app, event):
    # En kontroller.
    # Denne funksjonen kalles hver gang brukeren trykker på tastaturet.
    # Funksjonen kan __endre på__ eksisterende variabler i app.
    #app.cpount += 1
    if event.key == "d":
        app.debug_mode = not app.debug_mode

    if event.key == "Space":
        do_step(app)
        
    print(event.key)
    if event.key == "Left" and app.cx > app.r:
        app.cx -= 10
        if app.cx < app.r:
            app.cx = app.r
    if event.key == "Right" and app.cx < app.width - app.r:
        app.cx += 10
        if app.cx > app.width - app.r:
            app.cx = app.width - app.r
    
    if event.key == "Up" and app.cy > app.r:
        app.cy -= 10
        if app.cy < app.r:
            app.cy = app.r
    if event.key == "Down" and app.cy < app.height - app.r:
        app.cy += 10
        if app.cy > app.height - app.r:
            app.cy = app.height - app.r


def redraw_all(app, canvas):
    # Visningen.
    # Denne funksjonen tegner vinduet. Funksjonen kalles hver gang
    # modellen har endret seg, eller vinduet har forandret størrelse.
    # Funksjonen kan __lese__ variabler fra app, men har ikke lov til
    # å endre på dem.
    canvas.create_oval(app.cx- app.r, app.cy - app.r, app.cx + app.r, app.cy + app.r, fill="green")
    canvas.create_rectangle(30, 30, 90, 90, fill = "blue")
    #canvas.create_text(app.width/2, app.height/2, text=f"{app.count}", font="Arial 60")
    if app.debug_mode:
        canvas.create_text(app.width/2, 40, text=f"{app.debug_mode= }", font="Arial 30")

run_app(width=500, height=400, title="Snake")
