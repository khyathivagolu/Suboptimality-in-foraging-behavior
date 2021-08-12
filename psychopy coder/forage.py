import psychopy.visual
import psychopy.event
import psychopy.core

clock = psychopy.core.Clock()

win = psychopy.visual.Window(
    size=[1920, 1080],
    units="pix",
    fullscr=False,
    color="#FBEBD3"
)

road = psychopy.visual.Rect(
    win=win,
    units="pix",
    width=750,
    height=1080,
    fillColor="#F8CA93",
    lineColor="#F8CA93"
)

circle = psychopy.visual.Circle(
    win=win,
    units="pix",
    radius=60,
    pos=[0,-270],
    lineWidth = 5,
    fillColor="#F8CA93",
    lineColor=[-1, -1, -1],
    edges=128
)

tree1 = psychopy.visual.ImageStim(
    win=win,
    image="images/tree.png",
    units="pix",
    pos=[480,-270],
    size=200
)

tree2 = psychopy.visual.ImageStim(
    win=win,
    image="images/tree.png",
    units="pix",
    pos=[-480,0],
    size=200
)

tree3 = psychopy.visual.ImageStim(
    win=win,
    image="images/tree.png",
    units="pix",
    pos=[480,270],
    size=200
)

road.draw()
circle.draw()
tree1.draw()
tree2.draw()
tree3.draw()

win.flip()

psychopy.event.waitKeys()
psychopy.core.wait(1.0)
circle.fillColor="#96C75F"
road.draw()
circle.draw()
tree1.draw()
tree2.draw()
tree3.draw()
win.flip()
# psychopy.core.wait(1.0)

psychopy.event.waitKeys()

circle.fillColor="#F8CA93"
road.draw()
circle.draw()
tree1.draw()
tree2.draw()
tree3.draw()
win.flip()
# print(clock.getTime())

psychopy.event.waitKeys()

# keep_going = True
y1 = -270
y2 = 0
y3 = 270
c=0

while c<=270:

    if c<150:
        tree1.pos=[480,y1]
        tree1.draw()
    if c>150:
        tree2.pos=[-480,y2+150]
        tree2.draw()

    tree3.pos=[480,y3]
    y1=y1-1
    y2=y2-1
    y3=y3-1
    c=c+1
    road.draw()
    circle.draw()
    # tree2.draw()
    tree3.draw()

    win.flip()

    # keys = psychopy.event.getKeys()

    # if len(keys) > 0:
    #     keep_going = False

win._getFrame().save('forage.png')
win.close()