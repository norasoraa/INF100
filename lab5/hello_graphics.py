from uib_inf100_graphics import *

TEXT = ' ,    ,\n{o,o}\n./)_)\n  " "    \n\nHello, Graphics!'

def redraw_all(app, canvas):
    canvas.create_text(app.width/2, app.height/2, text=TEXT)

run_app(width=400, height=200)



from uib_inf100_graphics import *

def redraw_all(app, canvas):
    # kode som tegner noe skal plasseres i denne blokken
    # `pass` er en kommando som gjør ingenting; en midlertidig plassholder. 
    pass  # erstatt denne linjen

run_app(width=400, height=200)



from uib_inf100_graphics import *

def redraw_all(app, canvas):
    # create_line(x0, y0, x1, y1, fill='black')
    # tegner en svart strek fra (x0, y0) to (x1, y1)
    canvas.create_line(25, 50, 200, 100, fill='black')
    canvas.create_line(250, 500, 20, 10, fill='blue')

run_app(width=400, height=200)



from uib_inf100_graphics import *

def redraw_all(app, canvas):
    # De fire første parameterne x_0, y_0, x_1 og y_1 representerer to
    # motstående hjørner i hyperrektangelet. Tenk på det som hjørnet til
    # venstre øverst etterfulgt av hjørnet til høyre nederst.
    canvas.create_rectangle(100, 50, app.width/2, app.height/2, fill='blue')

run_app(width=400, height=200)



from uib_inf100_graphics import *

def redraw_all(app, canvas):
    # De fleste tegne-funksjoner lar oss benytte valgfrie parametre
    # for å endre på tegningens utseende. Disse er skrevet på formen
    # parameter_navn=parameter_verdi, og kommer etter de posisjonelle
    # parameterne (som regel koordinater)

    # fill endrer fargen inni figuren
    canvas.create_rectangle(  0,   0, 150, 150, fill='yellow')
    # width endrer tykkelsen på kanten
    canvas.create_rectangle(100,  50, 250, 100, fill='orange', 
                            outline='black', width=5)
    # outline endrer fargen til kanten
    canvas.create_rectangle( 50, 100, 150, 200, fill='green',
                                                outline='red', width=3)
    # width=0 fjerner kanten fullstendig
    canvas.create_rectangle(125,  25, 175, 190, fill='purple', width=0)

run_app(width=400, height=200)



from uib_inf100_graphics import *

def redraw_all(app, canvas):
    # For å tegne ovaler, oppgir vi koordinatene til hyperrektangelet som 
    # omgir ovalen
    canvas.create_oval(100, 50, 300, 150, fill='yellow', outline='black')

    # For polygoner og linjer oppgir vi en rekke med (x, y) -koordinater
    # Linjer må ha to punkter
    canvas.create_line(100, 50, 150, 150, fill='red', width=5)

    # Polygoner må ha 3 eller flere punkter
    canvas.create_polygon(100, 30, 200, 50, 300, 30, 200, 10, 
                          fill='green', width = 5, outline='black')


    # For å skrive tekst, oppgir vi en enkelt koordinat som representerer
    # 'ankeret' til teksten. Vi må også ha selve teksten, og vi kan oppgi
    # font/skriftstørrelse om vi ønsker
    canvas.create_text(200, 100, text='INF100!',
                       fill='purple', font='Helvetica 26 bold underline')

    # Vi kan endre hva slags betydning anker-koordinatet har.
    # Prøv å sette ankeret til en av disse strengene:
    # 'n' 's' 'e' 'w' 'sw' 'nw' 'ne' 'se' 'center'
    canvas.create_text(200, 100, text='Grip dagen!', anchor='sw',
                       fill='darkBlue', font='Times 28 bold italic')

    # Her er en prikk som viser ankeret brukt til begge tekstene over
    canvas.create_oval(200 - 3, 100 - 3, 200 + 3, 100 + 3, fill="white")

run_app(width=400, height=200)



from uib_inf100_graphics import *

def redraw_all(app, canvas):
    # Fargen "Absolute Zero" har RGB -verdi #0048BA
    # Fargen "Acid green" har RGB -verdi #B0BF1A
    # https://en.wikipedia.org/wiki/List_of_colors:_A%E2%80%93F
    canvas.create_oval(100, 50, 300, 150,
                       fill='#0048BA', outline='#B0BF1A', width=10)


run_app(width=400, height=200)
