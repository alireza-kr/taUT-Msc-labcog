import psychopy.visual
import psychopy.event

win = psychopy.visual.Window(
    size = [600,600],
    units = "pix",
    fullscr = False,
    color = [1,1,1]
)

circle = psychopy.visual.Circle(
    win = win,
    units = "pix",
    radius = 20,
    fillColor = [0,0,0],
    lineColor = [-1,-1,-1],
    edges = 360
)

circle.draw()
win.update()

key = ''

while (key!='q'):
    key = psychopy.event.waitKeys(keyList=['left','right','up','down','q'])[0]
    if(key=='left'):
        circle.pos = [-50,0]
        circle.draw()
        win.update()
    elif(key=='right'):
        circle.pos = [50,0]
        circle.draw()
        win.update()
    elif(key=='up'):
        circle.pos = [0,50]
        circle.draw()
        win.update()
    elif(key=='down'):
        circle.pos = [0,-50]
        circle.draw()
        win.update()
    elif(key=='q'):
        win.close()
