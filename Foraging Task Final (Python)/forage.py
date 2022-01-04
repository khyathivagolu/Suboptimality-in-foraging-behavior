import psychopy.visual
import psychopy.event
import psychopy.core
import pandas as pd
import random

clock = psychopy.core.Clock()
globalclock = psychopy.core.Clock()

win = psychopy.visual.Window(
    size=[1920, 1080],
    units="pix",
    fullscr=True,
    color="#FBEBD3"             # sand
)

road = psychopy.visual.Rect(
    win=win,
    units="pix",
    width=725,
    height=1080,
    fillColor="#F8CA93",
    lineColor="#F8CA93"         # road
)

sqStay = psychopy.visual.Rect(
    win=win,
    units="pix",
    width=175,
    height=200,
    fillColor="#FBEBD3",
    pos=[480, -270],
    lineWidth=4,
    lineColor="#FBEBD3"         # road      
)

sqLeave = psychopy.visual.Rect(
    win=win,
    units="pix",
    width=120,
    height=120,
    fillColor="#FBEBD3",
    pos=[-480, -270],
    lineWidth=4,
    lineColor=[-1, -1, -1]      # road
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
    fillColor="#F8CA93",        # road
    lineColor=[-1, -1, -1],
    edges=128
)

rew = psychopy.visual.TextStim(
    win=win,
    color="#7AAE47",
    height=35,
    pos=[480+120, -270+100]
)

intro = psychopy.visual.TextStim(
    win=win,
    text="Welcome to the patch foraging task. \n Before proceeding to the game, please fill out the survey if you haven't already. \n Once that's done, press the spacebar to continue.",
    color=[-1,-1,-1],
    wrapWidth=700,
    height=35,
    pos=[0,0]
)

outro = psychopy.visual.TextStim(
    win=win,
    color=[-1,-1,-1],
    wrapWidth=800,
    height=35,
    pos=[0,0]
)

Mouse = psychopy.event.Mouse(
    visible=True, 
    newPos=None, 
    win=win
    )

intro.draw()
win.flip()
psychopy.event.waitKeys(keyList='space')

rules1 = psychopy.visual.TextStim(
    win=win,
    text="RULES!",
    color=[-1,-1,-1],
    height=35,
    pos=[0,400]
)
rules1.draw()
win.flip()
psychopy.core.wait(0.5)

rules2 = psychopy.visual.TextStim(
    win=win,
    text="Click the circular box at the center and wait for it to turn green. \n ",
    color=[-1,-1,-1],
    height=30,
    wrapWidth=400,
    pos=[-270,285]
)

rules1.draw()
rules2.draw()
win.flip()
psychopy.core.wait(1.0)

bcircleimg = psychopy.visual.Circle(
    win=win,
    units="pix",
    radius=60,
    pos=[120, 295],
    lineWidth=5,
    fillColor="#FBEBD3",        # road
    lineColor=[-1, -1, -1],
    edges=128
)

gcircleimg = psychopy.visual.Circle(
    win=win,
    units="pix",
    radius=60,
    pos=[420, 295],
    lineWidth=5,
    lineColor = "#7AAE47",
    fillColor = "#96C75F",
    edges=128
)

sarrow = psychopy.visual.ImageStim(
    win=win,
    image="images/arrow.png",
    units="pix",
    ori=90,
    pos=[270, 295],
    size=50
)

rules1.draw()
rules2.draw()
bcircleimg.draw()
gcircleimg.draw()
sarrow.draw()
win.flip()
psychopy.core.wait(1.0)

rules3 = psychopy.visual.TextStim(
    win=win,
    text="Then, on each trial, you either choose to stay at the tree you are at or leave the current tree and travel to a new tree. \n To stay -> click on the tree \n To leave -> click on the box on the opposite side of the tree",
    color=[-1,-1,-1],
    height=30,
    wrapWidth=1250,
    pos=[0,130]
)

demoimage = psychopy.visual.ImageStim(
    win=win,
    image="images/rules.png",
    units="pix",
    pos=[0, -60],
    size=[1050,160]
)

rules1.draw()
rules2.draw()
bcircleimg.draw()
gcircleimg.draw()
sarrow.draw()
demoimage.draw()
rules3.draw()
win.flip()
psychopy.core.wait(1.0)

rules4 = psychopy.visual.TextStim(
    win=win,
    text="As you keep picking from the same tree repeatedly, the number of berries you pick (your reward) at each attempt will go down as you will be depleting this tree.",
    color=[-1,-1,-1],
    height=30,
    wrapWidth=1250,
    pos=[0,-190]
)

rules1.draw()
rules2.draw()
bcircleimg.draw()
gcircleimg.draw()
sarrow.draw()
demoimage.draw()
rules3.draw()
rules4.draw()
win.flip()
psychopy.core.wait(1.0)

rules5 = psychopy.visual.TextStim(
    win=win,
    text="You can choose to leave the current tree to travel to a new tree at any time. When you do that, you will need to wait while you travel to the next tree where you can start picking berries again.",
    color=[-1,-1,-1],
    height=30,
    wrapWidth=1250,
    pos=[0,-300]
)

rules1.draw()
rules2.draw()
bcircleimg.draw()
gcircleimg.draw()
sarrow.draw()
demoimage.draw()
rules3.draw()
rules4.draw()
rules5.draw()
win.flip()
psychopy.core.wait(1.0)

rules6 = psychopy.visual.TextStim(
    win=win,
    text="Press the spacebar to continue.",
    color=[-1,-1,-1],
    height=30,
    wrapWidth=1250,
    pos=[0,-390]
)

rules1.draw()
rules2.draw()
bcircleimg.draw()
gcircleimg.draw()
sarrow.draw()
demoimage.draw()
rules3.draw()
rules4.draw()
rules5.draw()
rules6.draw()
win.flip()
psychopy.core.wait(1.0)

psychopy.event.waitKeys(keyList='space')

rules6 = psychopy.visual.TextStim(
    win=win,
    text="On each trial when you click on the tree, the number of berries you collected will appear on the screen.",
    color=[-1,-1,-1],
    height=30,
    wrapWidth=550,
    pos=[-270,300]
)

demoimage2 = psychopy.visual.ImageStim(
    win=win,
    image="images/rules2.png",
    units="pix",
    pos=[320, 300],
    size=[200,200]
)

rules6.draw()
demoimage2.draw()
win.flip()
psychopy.core.wait(1.0)

rules7 = psychopy.visual.TextStim(
    win=win,
    bold=True,
    text="You must play one session of the foraging game, which will consist of two blocks. The environment will change between these blocks.",
    color=[-1,-1,-1],
    height=30,
    wrapWidth=1250,
    pos=[0,100]
)
rules6.draw()
demoimage2.draw()
rules7.draw()
win.flip()
psychopy.core.wait(1.0)

rules8 = psychopy.visual.TextStim(
    win=win,
    bold=True,
    text="Your goal is to collect as many berries as you can in the given time.",
    color=[-1,-1,-1],
    height=35,
    wrapWidth=700,
    pos=[0,-20]
)
rules6.draw()
demoimage2.draw()
rules7.draw()
rules8.draw()
win.flip()
psychopy.core.wait(1.0)

rules9 = psychopy.visual.TextStim(
    win=win,
    bold=True,
    text="There are unlimited number of trees in the environment, but a finite amount of time (two minutes in each of the two environments). Try and collect as many berries as you can in that time.",
    color=[-1,-1,-1],
    height=30,
    wrapWidth=1250,
    pos=[0,-150]
)
rules6.draw()
demoimage2.draw()
rules7.draw()
rules8.draw()
rules9.draw()
win.flip()
psychopy.core.wait(1.0)

rules10 = psychopy.visual.TextStim(
    win=win,
    bold=True,
    text="Press the spacebar to proceed to the game. You cannot quit in between. If you face any issues while playing the game, finish the trial and replay from the start. \n Good luck!",
    color=[-1,-1,-1],
    height=30,
    wrapWidth=1250,
    pos=[0,-290]
)
rules6.draw()
demoimage2.draw()
rules7.draw()
rules8.draw()
rules9.draw()
rules10.draw()
win.flip()
psychopy.core.wait(1.0)

######################################################################################################################################

tree = [0, 1, 2, 3, 4, 5]
x = [-480, 480]
y = [-540, -270, 0, 270, 540, 810]

for i in range(6):
    tree[i] = psychopy.visual.ImageStim(
        win=win,
        image="images/tree.png",
        units="pix",
        pos=[x[i % 2], y[i]],
        size=200
    )

rewardcollected=[]          # on that click
treeNo=[]                   # corresponding tree
decision=[]                 # stay or leave
reactiontime=[]             # between center click and decision
cumReward=[]
cumRewardpertree=[]
timeElapsed=[]


# intro.draw()
# win.flip()

psychopy.event.waitKeys(keyList='space')

sqStay.draw()
sqLeave.draw()
arrow.draw()
for i in range(6):
    tree[i].draw()
road.draw()
circle.draw()
win.flip()

k=0             # counter
timeleft=True
totaltime=60*2
mouseclick=0
globalclock.reset()
curtree=1    
treerewsofar=0
totalrewsofar=0

while timeleft:

    travelTime = 4
    totalDist = 270
    speed = totalDist/travelTime        # speed in pixel/sec

    wait1=True
    sval=85
    eval=95
    r = random.randint(sval,eval+5)
    wait2=True
    while wait1 and timeleft:

        if globalclock.getTime() > totaltime:               # termination
            timeleft=False

        while wait2 and timeleft:
            if globalclock.getTime() > totaltime:           # termination
                timeleft=False

            if Mouse.isPressedIn(shape=circle):

                Mouse.clickReset()
                circle.lineColor = "#7AAE47"                # green
                sqStay.draw()
                sqLeave.draw()
                arrow.draw()
                for i in range(6):
                    tree[i].draw()
                road.draw()
                circle.draw()
                win.flip()
                psychopy.core.wait(1.0)
                circle.fillColor = "#96C75F"                # green "#96C75F"
                sqStay.draw()
                sqLeave.draw()
                arrow.draw()
                for i in range(6):
                    tree[i].draw()
                road.draw()
                circle.draw()
                win.flip()
                wait2=False
    
        if Mouse.isPressedIn(shape=sqStay, buttons=[0]):            # stay in the same patch
            buttons, times = Mouse.getPressed(getTime=True)
            timeElapsed.append(globalclock.getTime())
            Mouse.clickReset()

            rew.pos = [x[(k+1)%2]+80, -270+100]
            rew.text = str('+') + str(r)
            rewardcollected.append(r)
            treeNo.append(curtree)
            decision.append('stay')
            reactiontime.append(times[0])
            treerewsofar=treerewsofar+r
            totalrewsofar=totalrewsofar+r
            cumReward.append(totalrewsofar)
            cumRewardpertree.append(treerewsofar)
            # timeElapsed.append(globalclock.getTime())
            sval=sval-10
            eval=eval-10
            if(sval>=0):
                r=random.randint(sval,eval)
            else:
                r=0

            circle.fillColor = "#F8CA93"    # road
            circle.lineColor = "#000000"    # black
            sqStay.draw()                   # reward appears
            sqLeave.draw()
            arrow.draw()
            for i in range(6):
                tree[i].draw()
            road.draw()
            circle.draw()
            rew.draw()
            win.flip()

            psychopy.core.wait(0.5)

            sqStay.draw()                   # reward disappears
            sqLeave.draw()
            arrow.draw()
            for i in range(6):
                tree[i].draw()
            road.draw()
            circle.draw()
            win.flip()

            wait2=True

        if Mouse.isPressedIn(shape=sqLeave, buttons=[0]):            # leave the patch
            buttons, times = Mouse.getPressed(getTime=True)
            timeElapsed.append(globalclock.getTime())
            Mouse.clickReset()

            curtree=curtree+1
            rewardcollected.append(0)
            treeNo.append(curtree-1)
            decision.append('leave')
            reactiontime.append(times[0])
            cumReward.append(totalrewsofar)
            cumRewardpertree.append(treerewsofar)
            treerewsofar=0

            sqStay.draw()
            sqLeave.draw()
            arrow.draw()
            for i in range(6):
                tree[i].draw()
            road.draw()
            circle.draw()
            win.flip()

            wait1=False

    circle.fillColor = "#F8CA93"    # road
    circle.lineColor = "#000000"    # black
    sqStay.draw()
    sqLeave.draw()
    arrow.draw()
    for i in range(6):
        tree[i].draw()
    road.draw()
    circle.draw()
    win.flip()
    clock.reset()
    
    while clock.getTime() < travelTime and timeleft:        # travel time = 4s

        if globalclock.getTime() > totaltime:               # termination
            timeleft=False

        for i in range(6):
            dist = speed*clock.getTime()
            tree[i].pos = [x[i % 2], y[i]-dist]
            if(y[i] == -810):
                y[i] = 810
            tree[i].draw()

        road.draw()
        circle.draw()
        win.flip()
        
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

    k=k+1

    if globalclock.getTime() > totaltime:                   # termination
        timeleft=False

totalReward = sum(rewardcollected)
print("Total reward for 1st environment = ", totalReward)

outro.text="Time up! \n Your score for the 1st environment = " + str(totalReward) + "\nPress the spacebar to enter the 2nd environment!"

outro.draw()
win.flip()
psychopy.event.waitKeys(keyList='space')

# data collection

dict = {'Tree number': treeNo, 'Time elapsed': timeElapsed, 'Decision': decision, 'Reaction time': reactiontime, 'Reward': rewardcollected, 'Cumulative reward per tree': cumRewardpertree, 'Total cumulative reward': cumReward} 
     
df = pd.DataFrame(dict)
df_name =  "data_env1.csv"
df.to_csv(df_name)

######################################################################################################################################

tree = [0, 1, 2, 3]
x = [-480, 480]
y = [-810,-270, 270, 810]
# x = [-480, 480]
# y = [-540, -270, 0, 270, 540, 810]

for i in range(4):
    tree[i] = psychopy.visual.ImageStim(
        win=win,
        image="images/tree.png",
        units="pix",
        pos=[x[i % 2], y[i]],
        size=200
    )

rewardcollected=[]          # on that click
treeNo=[]                   # corresponding tree
decision=[]                 # stay or leave
reactiontime=[]             # between center click and decision
cumReward=[]
cumRewardpertree=[]
timeElapsed=[]

sqLeave.pos = [-480,-270]
sqStay.pos = [480,-270]
arrow.pos = [-480,-270]

sqStay.draw()
sqLeave.draw()
arrow.draw()
for i in range(4):
    tree[i].draw()
road.draw()
circle.draw()
win.flip()

k=0
timeleft=True
totaltime=60*2
mouseclick=0
globalclock.reset()
curtree=1                           #current tree
treerewsofar=0
totalrewsofar=0

while timeleft:

    travelTime = 8
    totalDist = 270*2
    speed = totalDist/travelTime    # speed in pixel/sec

    wait1=True
    sval=85
    eval=95
    r = random.randint(sval,eval+5)
    wait2=True
    while wait1 and timeleft:

        if globalclock.getTime() > totaltime:                   # termination
            timeleft=False

        while wait2 and timeleft:
            if globalclock.getTime() > totaltime:               # termination
                timeleft=False

            if Mouse.isPressedIn(shape=circle):
                Mouse.clickReset()
                circle.lineColor = "#7AAE47"                    # green
                sqStay.draw()
                sqLeave.draw()
                arrow.draw()
                for i in range(4):
                    tree[i].draw()
                road.draw()
                circle.draw()
                win.flip()
                psychopy.core.wait(1.0)
                circle.fillColor = "#96C75F"                    # green
                sqStay.draw()
                sqLeave.draw()
                arrow.draw()
                for i in range(4):
                    tree[i].draw()
                road.draw()
                circle.draw()
                win.flip()
                wait2=False
    
        if Mouse.isPressedIn(shape=sqStay, buttons=[0]):        # stay in the same patch
            buttons, times = Mouse.getPressed(getTime=True)
            timeElapsed.append(globalclock.getTime())
            Mouse.clickReset()

            rew.pos = [x[(k+1)%2]+80, -270+100]
            rew.text = str('+') + str(r)
            rewardcollected.append(r)
            treeNo.append(curtree)
            decision.append('stay')
            reactiontime.append(times[0])
            treerewsofar=treerewsofar+r
            totalrewsofar=totalrewsofar+r
            cumReward.append(totalrewsofar)
            cumRewardpertree.append(treerewsofar)
            # timeElapsed.append(globalclock.getTime())
            sval=sval-10
            eval=eval-10
            if(sval>=0):
                r=random.randint(sval,eval)
            else:
                r=0

            circle.fillColor = "#F8CA93"    # road
            circle.lineColor = "#000000"    # black
            sqStay.draw()                   # reward appears
            sqLeave.draw()
            arrow.draw()
            for i in range(4):
                tree[i].draw()
            road.draw()
            circle.draw()
            rew.draw()
            win.flip()

            psychopy.core.wait(0.5)

            sqStay.draw()                   # reward disappears
            sqLeave.draw()
            arrow.draw()
            for i in range(4):
                tree[i].draw()
            road.draw()
            circle.draw()
            win.flip()
            wait2=True

        if Mouse.isPressedIn(shape=sqLeave, buttons=[0]):            # leave the patch
            buttons, times = Mouse.getPressed(getTime=True)
            timeElapsed.append(globalclock.getTime())
            Mouse.clickReset()

            curtree=curtree+1
            rewardcollected.append(0)
            treeNo.append(curtree-1)
            decision.append('leave')
            reactiontime.append(times[0])
            cumReward.append(totalrewsofar)
            cumRewardpertree.append(treerewsofar)
            treerewsofar=0

            sqStay.draw()
            sqLeave.draw()
            arrow.draw()
            for i in range(4):
                tree[i].draw()
            road.draw()
            circle.draw()
            win.flip()
            wait1=False

    circle.fillColor = "#F8CA93"    # road
    circle.lineColor = "#000000"    # black
    sqStay.draw()
    sqLeave.draw()
    arrow.draw()
    for i in range(4):
        tree[i].draw()
    road.draw()
    circle.draw()
    win.flip()
    clock.reset()
    
    while clock.getTime() < travelTime and timeleft:        # travel time = 8s

        if globalclock.getTime() > totaltime:               # termination
            timeleft=False

        for i in range(4):
            dist = speed*clock.getTime()
            tree[i].pos = [x[i % 2], y[i]-dist] 
            if(y[i] == -1350):
                y[i] = 810
            tree[i].draw()

        road.draw()
        circle.draw()
        win.flip()

    for i in range(4):
        if(y[i] > -1350):
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
    for i in range(4):
        tree[i].draw()
    win.flip()
        
    k=k+1
    if globalclock.getTime() > totaltime:                   # termination
        timeleft=False

totalReward = sum(rewardcollected)
print("Total reward for 2nd environment = ", totalReward)

outro.text="Time up! \n Your score for the 2nd environment= " + str(totalReward) + "\nThank you for participating! :D"

outro.draw()
win.flip()
psychopy.core.wait(5.0)

dict = {'Tree number': treeNo, 'Time elapsed': timeElapsed, 'Decision': decision, 'Reaction time': reactiontime, 'Reward': rewardcollected, 'Cumulative reward per tree': cumRewardpertree, 'Total cumulative reward': cumReward} 
     
df = pd.DataFrame(dict)
df_name = "data_env2.csv"
df.to_csv(df_name)

win.close()

