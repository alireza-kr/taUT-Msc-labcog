import psychopy.visual
import psychopy.event
import psychopy. core
import random

win = psychopy.visual.Window (
    size = [400,400],
    units = "pix",
    fullscr = False,
    color = [1,1,1]
)

circle = psychopy.visual.Circle (
    win = win,
    units = "pix",
    radius = 20,
    fillColor = [0,0,0],
    lineColor = [-1,-1,-1],
    edges = 360
)

text = psychopy.visual.TextStim (
    win = win,
    text = "Ready? Start...",
    color = [-1,-1,-1]
)

line = psychopy.visual.Line (
    win = win,
    units = "pix",
    lineColor = [-1,-1,-1],
    start = [0,100],
    end = [0,-100]
)

position = ('left','right')
key = [['']]

text.draw()
win.update()
psychopy.event.waitKeys()

while (key[0][0]!='q'):
    cirPosition = random.choice(position)
    if (cirPosition=='left'):
        line.draw()
        circle.pos = [-100,0]
        circle.draw()
        win.update()
    elif (cirPosition=='right'):
        line.draw()
        circle.pos = [100,0]
        circle.draw()
        win.update()

    clock = psychopy.core.Clock()
    key = psychopy.event.waitKeys(keyList=['left','right','q'],timeStamped=clock)

    if (cirPosition!=key[0][0] and key[0][0]!='q'):
        text.text = "Wrong Answer!"
        text.draw()
        win.update()
        psychopy.core.wait(1)
    elif (cirPosition==key[0][0] and key[0][1]<0.5):
        text.text = "Good Job!"
        text.draw()
        win.update()
        print(key[0][1])
        psychopy.core.wait(1)
    elif (cirPosition==key[0][0] and key[0][1]>=0.5):
        text.text = "You are too slow!"
        text.draw()
        win.update()
        print(key[0][1])
        psychopy.core.wait(1)

win.close()
