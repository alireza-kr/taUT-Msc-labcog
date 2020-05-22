#from psychopy import visual, event
import psychopy.visual
import psychopy.event

win = psychopy.visual.Window(
    size = [600,600],
    fullscr = False,
    color = [1,1,1]
)

text = psychopy.visual.TextStim(
    win = win,
    text = "Hello, world!",
    color = [-1,-1,-1]
)

#Draw the text on the win, but it will not be shown until the win will be updated
text.draw()

#For showing the text on the screen, win must be updated
win.update()
#win.flip()

#Wait unit some keys pressed
psychopy.event.waitKeys()


text.color = [2,2,2]
text.pos = [0,-0.5]
text.draw()

win.update()

psychopy.event.waitKeys()


win.close()
