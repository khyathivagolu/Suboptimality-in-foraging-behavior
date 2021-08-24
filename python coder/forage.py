from time import time
import psychopy.visual
import psychopy.event
import psychopy.core
import numpy as np
import pandas as pd
import random
# class psychopyeventMouse(visible=True, newPos=None, win=None)

clock = psychopy.core.Clock()
globalclock = psychopy.core.Clock()

win = psychopy.visual.Window(
    size=[1920, 1080],
    units="pix",
    fullscr=False,
    color="#FBEBD3"  # sand
)

road = psychopy.visual.Rect(
    win=win,
    units="pix",
    width=725,
    height=1080,
    fillColor="#F8CA93",
    lineColor="#F8CA93"  # road
)

sqStay = psychopy.visual.Rect(
    win=win,
    units="pix",
    width=175,
    height=200,
    fillColor="#FBEBD3",
    pos=[480, -270],
    lineWidth=4,
    lineColor="#FBEBD3"
    # lineColor=[-1, -1, -1]  # road
)

sqLeave = psychopy.visual.Rect(
    win=win,
    units="pix",
    width=120,
    height=120,
    fillColor="#FBEBD3",
    pos=[-480, -270],
    lineWidth=4,
    lineColor=[-1, -1, -1]  # road
)

arrow = psychopy.visual.ImageStim(
    win=win,
    image="images/arrow.png",
    units="pix",
    pos=[-480, -270],
    size=60
)

circle = psychopy.visual.Circle(
    win=win,
    units="pix",
    radius=60,
    pos=[0, -270],
    lineWidth=5,
    fillColor="#F8CA93",  # road
    lineColor=[-1, -1, -1],
    edges=128
)

rew = psychopy.visual.TextStim(
    win=win,
    # text="+8",
    color="#7AAE47",
    height=35,
    pos=[480+120, -270+100]
)

intro = psychopy.visual.TextStim(
    win=win,
    text="Hey there! \n Welcome to the patch foraging task. \n Click the spacebar to start.",
    color=[-1,-1,-1],
    height=40,
    pos=[0,0]
)

outro = psychopy.visual.TextStim(
    win=win,
    # text="Time up! Thank you for participating!",
    color=[-1,-1,-1],
    height=40,
    pos=[0,0]
)

Mouse = psychopy.event.Mouse(
    visible=True, 
    newPos=None, 
    win=win
    )

tree = [0, 1, 2, 3, 4, 5]
x = [-480, 480]
y = [-540, -270, 0, 270, 540, 810]
r = [7,6,5,4,3,2,1]

for i in range(6):
    tree[i] = psychopy.visual.ImageStim(
        win=win,
        image="images/tree.png",
        units="pix",
        pos=[x[i % 2], y[i]],
        size=200
    )

rewardcollected=[]
treeNo=[]
decision=[]
reactiontime=[] #between center click and stay or leave click

intro.draw()
win.flip()

psychopy.event.waitKeys(keyList='space')

sqStay.draw()
sqLeave.draw()
arrow.draw()
for i in range(6):
    tree[i].draw()
road.draw()
circle.draw()
win.flip()

k=0
timeleft=True
totaltime=60*2
mouseclick=0
globalclock.reset()
curtree=1                          #current tree
while timeleft:

    travelTime = 4
    totalDist = 270
    speed = totalDist/travelTime #speed in pixel/sec

    wait1=True
    sval=85
    eval=95
    r = random.randint(sval,eval+5)
    wait2=True
    while wait1 and timeleft:

        if globalclock.getTime() > totaltime:           #termination
            print(globalclock.getTime(), " Time up!1")
            timeleft=False

        while wait2 and timeleft:
            if globalclock.getTime() > totaltime:           #termination
                print(globalclock.getTime(), " Time up!2")
                timeleft=False

            if Mouse.isPressedIn(shape=circle):
                Mouse.clickReset()
                psychopy.core.wait(1.0)
                circle.fillColor = "#96C75F" #green
                sqStay.draw()
                sqLeave.draw()
                arrow.draw()
                for i in range(6):
                    tree[i].draw()
                road.draw()
                circle.draw()
                win.flip()
                wait2=False
    
        if Mouse.isPressedIn(shape=sqStay, buttons=[0]):        
            # mouseclick=mouseclick+1
            buttons, times = Mouse.getPressed(getTime=True)
            # print(buttons, "hii", times)
            Mouse.clickReset()

            rew.pos = [x[(k+1)%2]+80, -270+100]
            rew.text = str('+') + str(r)
            rewardcollected.append(r)
            treeNo.append(curtree)
            decision.append('stay')
            reactiontime.append(times[0])
            sval=sval-10
            eval=eval-10
            if(sval>=0):
                r=random.randint(sval,eval)
            else:
                r=0

            circle.fillColor = "#F8CA93" #road
            sqStay.draw()           #reward appears
            sqLeave.draw()
            arrow.draw()
            for i in range(6):
                tree[i].draw()
            road.draw()
            circle.draw()
            rew.draw()
            win.flip()

            psychopy.core.wait(0.5)

            sqStay.draw()           #reward disappears
            sqLeave.draw()
            arrow.draw()
            for i in range(6):
                tree[i].draw()
            road.draw()
            circle.draw()
            win.flip()
            
            # clock.reset()
            # psychopy.core.wait(0.5)
            # print("stay=",mouseclick)
            # buttons, times = Mouse.getPressed(getTime=True)
            wait2=True
            # psychopy.event.clearEvents() #get rid of other, unprocessed events
            # wait1=False

        if Mouse.isPressedIn(shape=sqLeave, buttons=[0]):            #Leave patch
            # mouseclick=mouseclick+1
            buttons, times = Mouse.getPressed(getTime=True)
            Mouse.clickReset()

            curtree=curtree+1
            rewardcollected.append(0)
            treeNo.append(curtree)
            decision.append('leave')
            reactiontime.append(times[0])
            # psychopy.event.clearEvents() #get rid of other, unprocessed events

            sqStay.draw()
            sqLeave.draw()
            arrow.draw()
            for i in range(6):
                tree[i].draw()
            road.draw()
            circle.draw()
            win.flip()

            # print("leave=",mouseclick)
            # buttons, times = Mouse.getPressed(getTime=True)
            # print(buttons, "hii", times)
            # Mouse.clickReset()
            wait1=False

    circle.fillColor = "#F8CA93" #road
    sqStay.draw()
    sqLeave.draw()
    arrow.draw()
    for i in range(6):
        tree[i].draw()
    road.draw()
    circle.draw()
    win.flip()
    clock.reset()
    
    while clock.getTime() < travelTime and timeleft:  # travel time = 4s

        if globalclock.getTime() > totaltime:           #termination
            print(globalclock.getTime(), " Time up!3")
            timeleft=False
        
        # sqStay.draw()
        # sqLeave.draw()

        for i in range(6):
            dist = speed*clock.getTime()
            tree[i].pos = [x[i % 2], y[i]-dist]
            if(y[i] == -810):
                y[i] = 810
            tree[i].draw()

        road.draw()
        circle.draw()
        win.flip()
        # print(clock.getTime())
    for i in range(6):
        if(y[i] > -810):
            y[i] = y[i]-totalDist
        else:
            y[i] = 810
        tree[i].draw()
    sqStay.pos = [x[k%2], -270]
    sqLeave.pos = [x[(k+1)%2], -270]
    arrow.pos = [x[(k+1)%2], -270]

    sqStay.draw()
    sqLeave.draw()
    arrow.draw()
    road.draw()
    circle.draw()
    for i in range(6):
        tree[i].draw()
    win.flip()
    # psychopy.core.wait(1.0)
    # psychopy.event.mouseClick()
    # Mouse.getPressed()
        
    k=k+1
    if globalclock.getTime() > totaltime:           #termination
        print(globalclock.getTime(), " Time up!4")
        timeleft=False

totalReward = sum(rewardcollected)

outro.text="Time up! Thank you for participating! \n Your score = " + str(totalReward)

outro.draw()
win.flip()
psychopy.core.wait(5.0)

# print(*rewardcollected, sep = ", ")
# # print("\n")
# print(*treeNo, sep = ", ")
print("Total reward = ", totalReward)

data = []
rewardPerTree=[]

for i in range(len(rewardcollected)):

    data.append(
        [
            treeNo[i],
            decision[i],
            reactiontime[i],
            rewardcollected[i]
        ]
    )

print(np.matrix(data))

# np.savetxt(
#     "data.csv",
#     data,
#     delimiter=", "
# )

# dictionary of lists 
dict = {'Tree number': treeNo, 'Decision': decision, 'Reaction time': reactiontime, 'Reward': rewardcollected} 
     
df = pd.DataFrame(dict)
  
# saving the dataframe
df.to_csv('data.csv')

win._getFrame().save('forage.png')
win.close()
