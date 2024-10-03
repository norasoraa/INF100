from uib_inf100_graphics import *

def redraw_all(app, canvas):
    canvas.create_rectangle(320, 330, 290, 410, fill='pink', outline ='black') #fot bak venstre
    canvas.create_line(320, 410, 290, 410, fill='black', width = 5)
    canvas.create_rectangle(370, 330, 340, 410, fill='pink', outline ='black') #fot bak høyre
    canvas.create_line(370, 410, 340, 410, fill='black', width = 5)
    canvas.create_rectangle(145, 370, 185, 440, fill='pink', outline ='black') #fot venstre
    canvas.create_line(145, 440, 185, 440, fill='black', width = 5)
    canvas.create_rectangle(260, 370, 220, 440, fill='pink', outline ='black') #fot høyre
    canvas.create_line(260, 440, 220, 440, fill='black', width = 5)
    canvas.create_line(440, 250, 370, 275, fill='pink', width = 8) #hale
    canvas.create_line(441, 248, 410, 290, fill='pink', width = 8) #hale
    canvas.create_line(385, 230, 412, 293, fill='pink', width = 8) #hale
    canvas.create_oval(100, 175, 380, 400, fill='pink', outline='black') #kropp
    

    canvas.create_oval(100, 20, 300, 200, fill='pink', outline='black') #hode
    canvas.create_polygon(170, 160, 200, 185, 230, 160, 200, 160, 
                          fill='black', width = 5, outline='black') #munn
    canvas.create_line(170, 160, 230, 160, fill='white', width = 5) #tenner
    canvas.create_oval(190, 168, 222, 185, fill='red', outline='red') #tunge
    canvas.create_oval(150, 95, 250, 160, fill='pink', outline='black') #nese
    canvas.create_oval(170, 115, 185, 140, fill='black', outline='black') #nesebor venstre
    canvas.create_oval(215, 115, 230, 140, fill='black', outline='black') #nesebor høyre
    canvas.create_oval(215, 65, 240, 90, fill='white', outline='black') #øye høyre
    canvas.create_oval(221, 71, 234, 84, fill='black', outline='light blue', width = 4) #øye høyre
    canvas.create_line(160, 80, 185, 80, fill='black', width = 5) #øye venstre
    canvas.create_rectangle(100, 30, 150, 70, fill='pink', outline ='black') #øre venstre
    canvas.create_rectangle(300, 30, 250, 70, fill='pink', outline ='black') #øre høyre
        
run_app(width=480, height=460)