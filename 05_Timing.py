import psychopy.visual
import psychopy.event
import psychopy.info

win = psychopy.visual.Window(
    size = [600,600],
    units = "pix",
    fullscr = False,
    color = [1,1,1]
)

circle = psychopy.visual.Circle(
    win = win,
    units = "pix",
    radius = 100,
    fillColor = [0,0,0],
    lineColor = [-1,-1,-1],
    edges = 3
)

currentInfo = psychopy.info.RunTimeInfo(win=win,refreshTest='grating')
screenIFI = round(float(currentInfo['windowRefreshTimeAvg_ms']),2)   #Screen Inter-Frame Interval
screenFPS = round(1000/screenIFI, 2)                                 #Screen Frame Per Second

print(currentInfo)

numStim = 10
durStim = 500   #in ms
numFramesStim = int(durStim/screenIFI)
numFramesOff = int(screenFPS - numFramesStim)

for i in range(numStim):
    for j in range(numFramesStim):
        circle.radius = 100
        circle.draw()
        win.update()
    for j in range(numFramesOff):
        circle.radius = 0
        circle.draw()
        win.update()
    circle.edges += 1

win.close()
