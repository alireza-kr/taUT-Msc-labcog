import psychopy.visual
import psychopy.sound
import psychopy.event
import psychopy.core

win = psychopy.visual.Window (
    size = [400,400],
    units = "pix",
    fullscr = False,
    color = [1,1,1]
)

text = psychopy.visual.TextStim (
    win = win,
    text = "",
    units = "pix",
    height = 100,
    color = [-1,-1,-1]
)

for i in range(3):
    text.text = i+1
    text.draw()
    win.update()
    psychopy.sound.Sound("Audio/"+str(i+1)+".wav").play()
    psychopy.core.wait(psychopy.sound.Sound("Audio/"+str(i+1)+".wav").getDuration())

win.close()
