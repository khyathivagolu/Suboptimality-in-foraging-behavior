#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.10),
    on Wed 07 Jul 2021 04:39:55 PM IST
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.10'
expName = 'untitled'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/home/khyathi/Desktop/surge/git uploads/Foraging task/foraging basic env 1/untitled_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "intro"
introClock = core.Clock()
introtext = visual.TextStim(win=win, name='introtext',
    text='//add text',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "startframe"
startframeClock = core.Clock()
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
square_2 = visual.ImageStim(
    win=win,
    name='square_2', 
    image='images/hollow.png', mask=None,
    ori=0, pos=(0, -0.2), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
tree1_2 = visual.ImageStim(
    win=win,
    name='tree1_2', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
tree2_2 = visual.ImageStim(
    win=win,
    name='tree2_2', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
tree3_2 = visual.ImageStim(
    win=win,
    name='tree3_2', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
tree4_2 = visual.ImageStim(
    win=win,
    name='tree4_2', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
tree5_2 = visual.ImageStim(
    win=win,
    name='tree5_2', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
tree6_2 = visual.ImageStim(
    win=win,
    name='tree6_2', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)

# Initialize components for Routine "rewardframe1"
rewardframe1Clock = core.Clock()
tree1_4 = visual.ImageStim(
    win=win,
    name='tree1_4', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
tree2_4 = visual.ImageStim(
    win=win,
    name='tree2_4', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
tree3_4 = visual.ImageStim(
    win=win,
    name='tree3_4', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
tree4_4 = visual.ImageStim(
    win=win,
    name='tree4_4', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
tree5_4 = visual.ImageStim(
    win=win,
    name='tree5_4', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
tree6_4 = visual.ImageStim(
    win=win,
    name='tree6_4', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
square_4 = visual.ImageStim(
    win=win,
    name='square_4', 
    image='images/hollow.png', mask=None,
    ori=0, pos=(0, -0.2), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
reward_2 = visual.TextStim(win=win, name='reward_2',
    text='default text',
    font='Arial',
    pos=(-0.6, -0.08), height=0.05, wrapWidth=None, ori=0, 
    color='green', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
resp = event.Mouse(win=win)
x, y = [None, None]
resp.mouseClock = core.Clock()
forward = visual.ImageStim(
    win=win,
    name='forward', 
    image='images/arrow.png', mask=None,
    ori=0, pos=(0.5, -0.2), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-9.0)
squaree = visual.ImageStim(
    win=win,
    name='squaree', 
    image='images/square.png', mask=None,
    ori=0, pos=(0.5, -0.2), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-10.0)
skip = event.Mouse(win=win)
x, y = [None, None]
skip.mouseClock = core.Clock()

# Initialize components for Routine "movetrees"
movetreesClock = core.Clock()
tree1_6 = visual.ImageStim(
    win=win,
    name='tree1_6', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
tree2_6 = visual.ImageStim(
    win=win,
    name='tree2_6', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
tree3_6 = visual.ImageStim(
    win=win,
    name='tree3_6', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
tree4_6 = visual.ImageStim(
    win=win,
    name='tree4_6', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
tree5_6 = visual.ImageStim(
    win=win,
    name='tree5_6', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
tree6_6 = visual.ImageStim(
    win=win,
    name='tree6_6', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
square_6 = visual.ImageStim(
    win=win,
    name='square_6', 
    image='images/hollow.png', mask=None,
    ori=0, pos=(0, -0.2), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)

# Initialize components for Routine "rewardframe2"
rewardframe2Clock = core.Clock()
tree1_5 = visual.ImageStim(
    win=win,
    name='tree1_5', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
tree2_5 = visual.ImageStim(
    win=win,
    name='tree2_5', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
tree3_5 = visual.ImageStim(
    win=win,
    name='tree3_5', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
tree4_5 = visual.ImageStim(
    win=win,
    name='tree4_5', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
tree5_5 = visual.ImageStim(
    win=win,
    name='tree5_5', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
tree6_5 = visual.ImageStim(
    win=win,
    name='tree6_5', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
square_5 = visual.ImageStim(
    win=win,
    name='square_5', 
    image='images/hollow.png', mask=None,
    ori=0, pos=(0, -0.2), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
reward_3 = visual.TextStim(win=win, name='reward_3',
    text='default text',
    font='Arial',
    pos=(0.6, -0.08), height=0.05, wrapWidth=None, ori=0, 
    color='green', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
resp_3 = event.Mouse(win=win)
x, y = [None, None]
resp_3.mouseClock = core.Clock()

# Initialize components for Routine "movetrees2"
movetrees2Clock = core.Clock()
tree1_10 = visual.ImageStim(
    win=win,
    name='tree1_10', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
tree2_10 = visual.ImageStim(
    win=win,
    name='tree2_10', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
tree3_10 = visual.ImageStim(
    win=win,
    name='tree3_10', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
tree4_10 = visual.ImageStim(
    win=win,
    name='tree4_10', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
tree5_10 = visual.ImageStim(
    win=win,
    name='tree5_10', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
tree6_10 = visual.ImageStim(
    win=win,
    name='tree6_10', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
square_10 = visual.ImageStim(
    win=win,
    name='square_10', 
    image='images/hollow.png', mask=None,
    ori=0, pos=(0, -0.2), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)

# Initialize components for Routine "rewardframe3"
rewardframe3Clock = core.Clock()
tree1_7 = visual.ImageStim(
    win=win,
    name='tree1_7', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
tree2_7 = visual.ImageStim(
    win=win,
    name='tree2_7', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
tree3_7 = visual.ImageStim(
    win=win,
    name='tree3_7', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
tree4_7 = visual.ImageStim(
    win=win,
    name='tree4_7', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
tree5_7 = visual.ImageStim(
    win=win,
    name='tree5_7', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
tree6_7 = visual.ImageStim(
    win=win,
    name='tree6_7', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
square_7 = visual.ImageStim(
    win=win,
    name='square_7', 
    image='images/hollow.png', mask=None,
    ori=0, pos=(0, -0.2), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
reward_4 = visual.TextStim(win=win, name='reward_4',
    text='default text',
    font='Arial',
    pos=(-0.6, -0.08), height=0.05, wrapWidth=None, ori=0, 
    color='green', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
resp_4 = event.Mouse(win=win)
x, y = [None, None]
resp_4.mouseClock = core.Clock()

# Initialize components for Routine "movetrees3"
movetrees3Clock = core.Clock()
tree1_11 = visual.ImageStim(
    win=win,
    name='tree1_11', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
tree2_11 = visual.ImageStim(
    win=win,
    name='tree2_11', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
tree3_11 = visual.ImageStim(
    win=win,
    name='tree3_11', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
tree4_11 = visual.ImageStim(
    win=win,
    name='tree4_11', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
tree5_11 = visual.ImageStim(
    win=win,
    name='tree5_11', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
tree6_11 = visual.ImageStim(
    win=win,
    name='tree6_11', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
square_11 = visual.ImageStim(
    win=win,
    name='square_11', 
    image='images/hollow.png', mask=None,
    ori=0, pos=(0, -0.2), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)

# Initialize components for Routine "rewardframe4"
rewardframe4Clock = core.Clock()
tree1_8 = visual.ImageStim(
    win=win,
    name='tree1_8', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
tree2_8 = visual.ImageStim(
    win=win,
    name='tree2_8', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
tree3_8 = visual.ImageStim(
    win=win,
    name='tree3_8', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
tree4_8 = visual.ImageStim(
    win=win,
    name='tree4_8', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
tree5_8 = visual.ImageStim(
    win=win,
    name='tree5_8', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
tree6_8 = visual.ImageStim(
    win=win,
    name='tree6_8', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
square_8 = visual.ImageStim(
    win=win,
    name='square_8', 
    image='images/hollow.png', mask=None,
    ori=0, pos=(0, -0.2), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
reward_5 = visual.TextStim(win=win, name='reward_5',
    text='default text',
    font='Arial',
    pos=(0.6, -0.08), height=0.05, wrapWidth=None, ori=0, 
    color='green', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
resp_5 = event.Mouse(win=win)
x, y = [None, None]
resp_5.mouseClock = core.Clock()

# Initialize components for Routine "movetrees2"
movetrees2Clock = core.Clock()
tree1_10 = visual.ImageStim(
    win=win,
    name='tree1_10', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
tree2_10 = visual.ImageStim(
    win=win,
    name='tree2_10', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
tree3_10 = visual.ImageStim(
    win=win,
    name='tree3_10', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
tree4_10 = visual.ImageStim(
    win=win,
    name='tree4_10', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
tree5_10 = visual.ImageStim(
    win=win,
    name='tree5_10', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
tree6_10 = visual.ImageStim(
    win=win,
    name='tree6_10', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
square_10 = visual.ImageStim(
    win=win,
    name='square_10', 
    image='images/hollow.png', mask=None,
    ori=0, pos=(0, -0.2), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)

# Initialize components for Routine "rewardframe5"
rewardframe5Clock = core.Clock()
tree1_9 = visual.ImageStim(
    win=win,
    name='tree1_9', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
tree2_9 = visual.ImageStim(
    win=win,
    name='tree2_9', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
tree3_9 = visual.ImageStim(
    win=win,
    name='tree3_9', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
tree4_9 = visual.ImageStim(
    win=win,
    name='tree4_9', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
tree5_9 = visual.ImageStim(
    win=win,
    name='tree5_9', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
tree6_9 = visual.ImageStim(
    win=win,
    name='tree6_9', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
square_9 = visual.ImageStim(
    win=win,
    name='square_9', 
    image='images/hollow.png', mask=None,
    ori=0, pos=(0, -0.2), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
reward_6 = visual.TextStim(win=win, name='reward_6',
    text='default text',
    font='Arial',
    pos=(-0.6, -0.08), height=0.05, wrapWidth=None, ori=0, 
    color='green', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
resp_6 = event.Mouse(win=win)
x, y = [None, None]
resp_6.mouseClock = core.Clock()

# Initialize components for Routine "movetrees3"
movetrees3Clock = core.Clock()
tree1_11 = visual.ImageStim(
    win=win,
    name='tree1_11', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
tree2_11 = visual.ImageStim(
    win=win,
    name='tree2_11', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
tree3_11 = visual.ImageStim(
    win=win,
    name='tree3_11', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
tree4_11 = visual.ImageStim(
    win=win,
    name='tree4_11', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
tree5_11 = visual.ImageStim(
    win=win,
    name='tree5_11', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
tree6_11 = visual.ImageStim(
    win=win,
    name='tree6_11', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
square_11 = visual.ImageStim(
    win=win,
    name='square_11', 
    image='images/hollow.png', mask=None,
    ori=0, pos=(0, -0.2), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)

# Initialize components for Routine "end"
endClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='The end~',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "intro"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
introComponents = [introtext]
for thisComponent in introComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
introClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "intro"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = introClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=introClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *introtext* updates
    if introtext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        introtext.frameNStart = frameN  # exact frame index
        introtext.tStart = t  # local t and not account for scr refresh
        introtext.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(introtext, 'tStartRefresh')  # time at next scr refresh
        introtext.setAutoDraw(True)
    if introtext.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > introtext.tStartRefresh + 3.0-frameTolerance:
            # keep track of stop time/frame for later
            introtext.tStop = t  # not accounting for scr refresh
            introtext.frameNStop = frameN  # exact frame index
            win.timeOnFlip(introtext, 'tStopRefresh')  # time at next scr refresh
            introtext.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "intro"-------
for thisComponent in introComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('introtext.started', introtext.tStartRefresh)
thisExp.addData('introtext.stopped', introtext.tStopRefresh)

# ------Prepare to start Routine "startframe"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse
mouse.clicked_name = []
gotValidClick = False  # until a click is received
tree1_2.setPos((0.5, 0.4))
tree2_2.setPos((-0.5, 0.2))
tree3_2.setPos((0.5, 0))
tree4_2.setPos((-0.5, -0.2))
tree5_2.setPos((0.5, -0.4))
tree6_2.setPos((-0.5, -0.6))
# keep track of which components have finished
startframeComponents = [mouse, square_2, tree1_2, tree2_2, tree3_2, tree4_2, tree5_2, tree6_2]
for thisComponent in startframeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
startframeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "startframe"-------
while continueRoutine:
    # get current time
    t = startframeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=startframeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *mouse* updates
    if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse.frameNStart = frameN  # exact frame index
        mouse.tStart = t  # local t and not account for scr refresh
        mouse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
        mouse.status = STARTED
        mouse.mouseClock.reset()
        prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
    if mouse.status == STARTED:  # only update if started and not finished!
        buttons = mouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                for obj in [square_2]:
                    if obj.contains(mouse):
                        gotValidClick = True
                        mouse.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    
    # *square_2* updates
    if square_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        square_2.frameNStart = frameN  # exact frame index
        square_2.tStart = t  # local t and not account for scr refresh
        square_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(square_2, 'tStartRefresh')  # time at next scr refresh
        square_2.setAutoDraw(True)
    
    # *tree1_2* updates
    if tree1_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        tree1_2.frameNStart = frameN  # exact frame index
        tree1_2.tStart = t  # local t and not account for scr refresh
        tree1_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(tree1_2, 'tStartRefresh')  # time at next scr refresh
        tree1_2.setAutoDraw(True)
    
    # *tree2_2* updates
    if tree2_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        tree2_2.frameNStart = frameN  # exact frame index
        tree2_2.tStart = t  # local t and not account for scr refresh
        tree2_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(tree2_2, 'tStartRefresh')  # time at next scr refresh
        tree2_2.setAutoDraw(True)
    
    # *tree3_2* updates
    if tree3_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        tree3_2.frameNStart = frameN  # exact frame index
        tree3_2.tStart = t  # local t and not account for scr refresh
        tree3_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(tree3_2, 'tStartRefresh')  # time at next scr refresh
        tree3_2.setAutoDraw(True)
    
    # *tree4_2* updates
    if tree4_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        tree4_2.frameNStart = frameN  # exact frame index
        tree4_2.tStart = t  # local t and not account for scr refresh
        tree4_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(tree4_2, 'tStartRefresh')  # time at next scr refresh
        tree4_2.setAutoDraw(True)
    
    # *tree5_2* updates
    if tree5_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        tree5_2.frameNStart = frameN  # exact frame index
        tree5_2.tStart = t  # local t and not account for scr refresh
        tree5_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(tree5_2, 'tStartRefresh')  # time at next scr refresh
        tree5_2.setAutoDraw(True)
    if tree5_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > tree5_2.tStartRefresh + 0-frameTolerance:
            # keep track of stop time/frame for later
            tree5_2.tStop = t  # not accounting for scr refresh
            tree5_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(tree5_2, 'tStopRefresh')  # time at next scr refresh
            tree5_2.setAutoDraw(False)
    
    # *tree6_2* updates
    if tree6_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        tree6_2.frameNStart = frameN  # exact frame index
        tree6_2.tStart = t  # local t and not account for scr refresh
        tree6_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(tree6_2, 'tStartRefresh')  # time at next scr refresh
        tree6_2.setAutoDraw(True)
    if tree6_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > tree6_2.tStartRefresh + 0-frameTolerance:
            # keep track of stop time/frame for later
            tree6_2.tStop = t  # not accounting for scr refresh
            tree6_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(tree6_2, 'tStopRefresh')  # time at next scr refresh
            tree6_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in startframeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "startframe"-------
for thisComponent in startframeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
x, y = mouse.getPos()
buttons = mouse.getPressed()
if sum(buttons):
    # check if the mouse was inside our 'clickable' objects
    gotValidClick = False
    for obj in [square_2]:
        if obj.contains(mouse):
            gotValidClick = True
            mouse.clicked_name.append(obj.name)
thisExp.addData('mouse.x', x)
thisExp.addData('mouse.y', y)
thisExp.addData('mouse.leftButton', buttons[0])
thisExp.addData('mouse.midButton', buttons[1])
thisExp.addData('mouse.rightButton', buttons[2])
if len(mouse.clicked_name):
    thisExp.addData('mouse.clicked_name', mouse.clicked_name[0])
thisExp.addData('mouse.started', mouse.tStart)
thisExp.addData('mouse.stopped', mouse.tStop)
thisExp.nextEntry()
thisExp.addData('square_2.started', square_2.tStartRefresh)
thisExp.addData('square_2.stopped', square_2.tStopRefresh)
thisExp.addData('tree1_2.started', tree1_2.tStartRefresh)
thisExp.addData('tree1_2.stopped', tree1_2.tStopRefresh)
thisExp.addData('tree2_2.started', tree2_2.tStartRefresh)
thisExp.addData('tree2_2.stopped', tree2_2.tStopRefresh)
thisExp.addData('tree3_2.started', tree3_2.tStartRefresh)
thisExp.addData('tree3_2.stopped', tree3_2.tStopRefresh)
thisExp.addData('tree4_2.started', tree4_2.tStartRefresh)
thisExp.addData('tree4_2.stopped', tree4_2.tStopRefresh)
thisExp.addData('tree5_2.started', tree5_2.tStartRefresh)
thisExp.addData('tree5_2.stopped', tree5_2.tStopRefresh)
thisExp.addData('tree6_2.started', tree6_2.tStartRefresh)
thisExp.addData('tree6_2.stopped', tree6_2.tStopRefresh)
# the Routine "startframe" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
reward1 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('reward.xlsx', selection='0:13'),
    seed=None, name='reward1')
thisExp.addLoop(reward1)  # add the loop to the experiment
thisReward1 = reward1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisReward1.rgb)
if thisReward1 != None:
    for paramName in thisReward1:
        exec('{} = thisReward1[paramName]'.format(paramName))

for thisReward1 in reward1:
    currentLoop = reward1
    # abbreviate parameter names if possible (e.g. rgb = thisReward1.rgb)
    if thisReward1 != None:
        for paramName in thisReward1:
            exec('{} = thisReward1[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "rewardframe1"-------
    continueRoutine = True
    # update component parameters for each repeat
    tree1_4.setPos((0.5, 0.4))
    tree2_4.setPos((-0.5, 0.2))
    tree3_4.setPos((0.5, 0))
    tree4_4.setPos((-0.5, -0.2))
    tree5_4.setPos((0.5, -0.4))
    tree6_4.setPos((-0.5, -0.6))
    reward_2.setText(rewardval1)
    # setup some python lists for storing info about the resp
    resp.x = []
    resp.y = []
    resp.leftButton = []
    resp.midButton = []
    resp.rightButton = []
    resp.time = []
    resp.clicked_name = []
    gotValidClick = False  # until a click is received
    # setup some python lists for storing info about the skip
    skip.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    rewardframe1Components = [tree1_4, tree2_4, tree3_4, tree4_4, tree5_4, tree6_4, square_4, reward_2, resp, forward, squaree, skip]
    for thisComponent in rewardframe1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    rewardframe1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "rewardframe1"-------
    while continueRoutine:
        # get current time
        t = rewardframe1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=rewardframe1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *tree1_4* updates
        if tree1_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            tree1_4.frameNStart = frameN  # exact frame index
            tree1_4.tStart = t  # local t and not account for scr refresh
            tree1_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(tree1_4, 'tStartRefresh')  # time at next scr refresh
            tree1_4.setAutoDraw(True)
        
        # *tree2_4* updates
        if tree2_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            tree2_4.frameNStart = frameN  # exact frame index
            tree2_4.tStart = t  # local t and not account for scr refresh
            tree2_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(tree2_4, 'tStartRefresh')  # time at next scr refresh
            tree2_4.setAutoDraw(True)
        
        # *tree3_4* updates
        if tree3_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            tree3_4.frameNStart = frameN  # exact frame index
            tree3_4.tStart = t  # local t and not account for scr refresh
            tree3_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(tree3_4, 'tStartRefresh')  # time at next scr refresh
            tree3_4.setAutoDraw(True)
        
        # *tree4_4* updates
        if tree4_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            tree4_4.frameNStart = frameN  # exact frame index
            tree4_4.tStart = t  # local t and not account for scr refresh
            tree4_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(tree4_4, 'tStartRefresh')  # time at next scr refresh
            tree4_4.setAutoDraw(True)
        
        # *tree5_4* updates
        if tree5_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            tree5_4.frameNStart = frameN  # exact frame index
            tree5_4.tStart = t  # local t and not account for scr refresh
            tree5_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(tree5_4, 'tStartRefresh')  # time at next scr refresh
            tree5_4.setAutoDraw(True)
        if tree5_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > tree5_4.tStartRefresh + 0-frameTolerance:
                # keep track of stop time/frame for later
                tree5_4.tStop = t  # not accounting for scr refresh
                tree5_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(tree5_4, 'tStopRefresh')  # time at next scr refresh
                tree5_4.setAutoDraw(False)
        
        # *tree6_4* updates
        if tree6_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            tree6_4.frameNStart = frameN  # exact frame index
            tree6_4.tStart = t  # local t and not account for scr refresh
            tree6_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(tree6_4, 'tStartRefresh')  # time at next scr refresh
            tree6_4.setAutoDraw(True)
        if tree6_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > tree6_4.tStartRefresh + 0-frameTolerance:
                # keep track of stop time/frame for later
                tree6_4.tStop = t  # not accounting for scr refresh
                tree6_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(tree6_4, 'tStopRefresh')  # time at next scr refresh
                tree6_4.setAutoDraw(False)
        
        # *square_4* updates
        if square_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            square_4.frameNStart = frameN  # exact frame index
            square_4.tStart = t  # local t and not account for scr refresh
            square_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(square_4, 'tStartRefresh')  # time at next scr refresh
            square_4.setAutoDraw(True)
        
        # *reward_2* updates
        if reward_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            reward_2.frameNStart = frameN  # exact frame index
            reward_2.tStart = t  # local t and not account for scr refresh
            reward_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(reward_2, 'tStartRefresh')  # time at next scr refresh
            reward_2.setAutoDraw(True)
        # *resp* updates
        if resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            resp.frameNStart = frameN  # exact frame index
            resp.tStart = t  # local t and not account for scr refresh
            resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp, 'tStartRefresh')  # time at next scr refresh
            resp.status = STARTED
            resp.mouseClock.reset()
            prevButtonState = resp.getPressed()  # if button is down already this ISN'T a new click
        if resp.status == STARTED:  # only update if started and not finished!
            buttons = resp.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [tree4_4]:
                        if obj.contains(resp):
                            gotValidClick = True
                            resp.clicked_name.append(obj.name)
                    x, y = resp.getPos()
                    resp.x.append(x)
                    resp.y.append(y)
                    buttons = resp.getPressed()
                    resp.leftButton.append(buttons[0])
                    resp.midButton.append(buttons[1])
                    resp.rightButton.append(buttons[2])
                    resp.time.append(resp.mouseClock.getTime())
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # *forward* updates
        if forward.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            forward.frameNStart = frameN  # exact frame index
            forward.tStart = t  # local t and not account for scr refresh
            forward.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(forward, 'tStartRefresh')  # time at next scr refresh
            forward.setAutoDraw(True)
        
        # *squaree* updates
        if squaree.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            squaree.frameNStart = frameN  # exact frame index
            squaree.tStart = t  # local t and not account for scr refresh
            squaree.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(squaree, 'tStartRefresh')  # time at next scr refresh
            squaree.setAutoDraw(True)
        # *skip* updates
        if skip.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            skip.frameNStart = frameN  # exact frame index
            skip.tStart = t  # local t and not account for scr refresh
            skip.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(skip, 'tStartRefresh')  # time at next scr refresh
            skip.status = STARTED
            prevButtonState = skip.getPressed()  # if button is down already this ISN'T a new click
        if skip.status == STARTED:  # only update if started and not finished!
            buttons = skip.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [squaree]:
                        if obj.contains(skip):
                            gotValidClick = True
                            skip.clicked_name.append(obj.name)
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in rewardframe1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "rewardframe1"-------
    for thisComponent in rewardframe1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    reward1.addData('tree1_4.started', tree1_4.tStartRefresh)
    reward1.addData('tree1_4.stopped', tree1_4.tStopRefresh)
    reward1.addData('tree2_4.started', tree2_4.tStartRefresh)
    reward1.addData('tree2_4.stopped', tree2_4.tStopRefresh)
    reward1.addData('tree3_4.started', tree3_4.tStartRefresh)
    reward1.addData('tree3_4.stopped', tree3_4.tStopRefresh)
    reward1.addData('tree4_4.started', tree4_4.tStartRefresh)
    reward1.addData('tree4_4.stopped', tree4_4.tStopRefresh)
    reward1.addData('tree5_4.started', tree5_4.tStartRefresh)
    reward1.addData('tree5_4.stopped', tree5_4.tStopRefresh)
    reward1.addData('tree6_4.started', tree6_4.tStartRefresh)
    reward1.addData('tree6_4.stopped', tree6_4.tStopRefresh)
    reward1.addData('square_4.started', square_4.tStartRefresh)
    reward1.addData('square_4.stopped', square_4.tStopRefresh)
    reward1.addData('reward_2.started', reward_2.tStartRefresh)
    reward1.addData('reward_2.stopped', reward_2.tStopRefresh)
    # store data for reward1 (TrialHandler)
    if len(resp.x): reward1.addData('resp.x', resp.x[0])
    if len(resp.y): reward1.addData('resp.y', resp.y[0])
    if len(resp.leftButton): reward1.addData('resp.leftButton', resp.leftButton[0])
    if len(resp.midButton): reward1.addData('resp.midButton', resp.midButton[0])
    if len(resp.rightButton): reward1.addData('resp.rightButton', resp.rightButton[0])
    if len(resp.time): reward1.addData('resp.time', resp.time[0])
    if len(resp.clicked_name): reward1.addData('resp.clicked_name', resp.clicked_name[0])
    reward1.addData('resp.started', resp.tStart)
    reward1.addData('resp.stopped', resp.tStop)
    reward1.addData('forward.started', forward.tStartRefresh)
    reward1.addData('forward.stopped', forward.tStopRefresh)
    reward1.addData('squaree.started', squaree.tStartRefresh)
    reward1.addData('squaree.stopped', squaree.tStopRefresh)
    # store data for reward1 (TrialHandler)
    x, y = skip.getPos()
    buttons = skip.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        for obj in [squaree]:
            if obj.contains(skip):
                gotValidClick = True
                skip.clicked_name.append(obj.name)
    reward1.addData('skip.x', x)
    reward1.addData('skip.y', y)
    reward1.addData('skip.leftButton', buttons[0])
    reward1.addData('skip.midButton', buttons[1])
    reward1.addData('skip.rightButton', buttons[2])
    if len(skip.clicked_name):
        reward1.addData('skip.clicked_name', skip.clicked_name[0])
    reward1.addData('skip.started', skip.tStart)
    reward1.addData('skip.stopped', skip.tStop)
    # the Routine "rewardframe1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'reward1'


# set up handler to look after randomisation of conditions etc
pos1 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('pos.xlsx'),
    seed=None, name='pos1')
thisExp.addLoop(pos1)  # add the loop to the experiment
thisPos1 = pos1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPos1.rgb)
if thisPos1 != None:
    for paramName in thisPos1:
        exec('{} = thisPos1[paramName]'.format(paramName))

for thisPos1 in pos1:
    currentLoop = pos1
    # abbreviate parameter names if possible (e.g. rgb = thisPos1.rgb)
    if thisPos1 != None:
        for paramName in thisPos1:
            exec('{} = thisPos1[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "movetrees"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    tree1_6.setPos((0.5, tree1_p))
    tree2_6.setPos((-0.5, tree2_n))
    tree3_6.setPos((0.5, tree3_p))
    tree4_6.setPos((-0.5, tree4_n))
    tree5_6.setPos((0.5, tree5_p))
    tree6_6.setPos((-0.5, tree6_n))
    # keep track of which components have finished
    movetreesComponents = [tree1_6, tree2_6, tree3_6, tree4_6, tree5_6, tree6_6, square_6]
    for thisComponent in movetreesComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    movetreesClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "movetrees"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = movetreesClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=movetreesClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *tree1_6* updates
        if tree1_6.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            tree1_6.frameNStart = frameN  # exact frame index
            tree1_6.tStart = t  # local t and not account for scr refresh
            tree1_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(tree1_6, 'tStartRefresh')  # time at next scr refresh
            tree1_6.setAutoDraw(True)
        if tree1_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > tree1_6.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                tree1_6.tStop = t  # not accounting for scr refresh
                tree1_6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(tree1_6, 'tStopRefresh')  # time at next scr refresh
                tree1_6.setAutoDraw(False)
        
        # *tree2_6* updates
        if tree2_6.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            tree2_6.frameNStart = frameN  # exact frame index
            tree2_6.tStart = t  # local t and not account for scr refresh
            tree2_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(tree2_6, 'tStartRefresh')  # time at next scr refresh
            tree2_6.setAutoDraw(True)
        if tree2_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > tree2_6.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                tree2_6.tStop = t  # not accounting for scr refresh
                tree2_6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(tree2_6, 'tStopRefresh')  # time at next scr refresh
                tree2_6.setAutoDraw(False)
        
        # *tree3_6* updates
        if tree3_6.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            tree3_6.frameNStart = frameN  # exact frame index
            tree3_6.tStart = t  # local t and not account for scr refresh
            tree3_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(tree3_6, 'tStartRefresh')  # time at next scr refresh
            tree3_6.setAutoDraw(True)
        if tree3_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > tree3_6.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                tree3_6.tStop = t  # not accounting for scr refresh
                tree3_6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(tree3_6, 'tStopRefresh')  # time at next scr refresh
                tree3_6.setAutoDraw(False)
        
        # *tree4_6* updates
        if tree4_6.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            tree4_6.frameNStart = frameN  # exact frame index
            tree4_6.tStart = t  # local t and not account for scr refresh
            tree4_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(tree4_6, 'tStartRefresh')  # time at next scr refresh
            tree4_6.setAutoDraw(True)
        if tree4_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > tree4_6.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                tree4_6.tStop = t  # not accounting for scr refresh
                tree4_6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(tree4_6, 'tStopRefresh')  # time at next scr refresh
                tree4_6.setAutoDraw(False)
        
        # *tree5_6* updates
        if tree5_6.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            tree5_6.frameNStart = frameN  # exact frame index
            tree5_6.tStart = t  # local t and not account for scr refresh
            tree5_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(tree5_6, 'tStartRefresh')  # time at next scr refresh
            tree5_6.setAutoDraw(True)
        if tree5_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > tree5_6.tStartRefresh + 0-frameTolerance:
                # keep track of stop time/frame for later
                tree5_6.tStop = t  # not accounting for scr refresh
                tree5_6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(tree5_6, 'tStopRefresh')  # time at next scr refresh
                tree5_6.setAutoDraw(False)
        
        # *tree6_6* updates
        if tree6_6.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            tree6_6.frameNStart = frameN  # exact frame index
            tree6_6.tStart = t  # local t and not account for scr refresh
            tree6_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(tree6_6, 'tStartRefresh')  # time at next scr refresh
            tree6_6.setAutoDraw(True)
        if tree6_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > tree6_6.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                tree6_6.tStop = t  # not accounting for scr refresh
                tree6_6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(tree6_6, 'tStopRefresh')  # time at next scr refresh
                tree6_6.setAutoDraw(False)
        
        # *square_6* updates
        if square_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            square_6.frameNStart = frameN  # exact frame index
            square_6.tStart = t  # local t and not account for scr refresh
            square_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(square_6, 'tStartRefresh')  # time at next scr refresh
            square_6.setAutoDraw(True)
        if square_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > square_6.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                square_6.tStop = t  # not accounting for scr refresh
                square_6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(square_6, 'tStopRefresh')  # time at next scr refresh
                square_6.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in movetreesComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "movetrees"-------
    for thisComponent in movetreesComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    pos1.addData('tree1_6.started', tree1_6.tStartRefresh)
    pos1.addData('tree1_6.stopped', tree1_6.tStopRefresh)
    pos1.addData('tree2_6.started', tree2_6.tStartRefresh)
    pos1.addData('tree2_6.stopped', tree2_6.tStopRefresh)
    pos1.addData('tree3_6.started', tree3_6.tStartRefresh)
    pos1.addData('tree3_6.stopped', tree3_6.tStopRefresh)
    pos1.addData('tree4_6.started', tree4_6.tStartRefresh)
    pos1.addData('tree4_6.stopped', tree4_6.tStopRefresh)
    pos1.addData('tree5_6.started', tree5_6.tStartRefresh)
    pos1.addData('tree5_6.stopped', tree5_6.tStopRefresh)
    pos1.addData('tree6_6.started', tree6_6.tStartRefresh)
    pos1.addData('tree6_6.stopped', tree6_6.tStopRefresh)
    pos1.addData('square_6.started', square_6.tStartRefresh)
    pos1.addData('square_6.stopped', square_6.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'pos1'


# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=3, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    reward2 = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('reward.xlsx', selection='0:11'),
        seed=None, name='reward2')
    thisExp.addLoop(reward2)  # add the loop to the experiment
    thisReward2 = reward2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisReward2.rgb)
    if thisReward2 != None:
        for paramName in thisReward2:
            exec('{} = thisReward2[paramName]'.format(paramName))
    
    for thisReward2 in reward2:
        currentLoop = reward2
        # abbreviate parameter names if possible (e.g. rgb = thisReward2.rgb)
        if thisReward2 != None:
            for paramName in thisReward2:
                exec('{} = thisReward2[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "rewardframe2"-------
        continueRoutine = True
        # update component parameters for each repeat
        tree1_5.setPos((0.5, 0.2))
        tree2_5.setPos((-0.5, 0))
        tree3_5.setPos((0.5, -0.2))
        tree4_5.setPos((-0.5, -0.4))
        tree5_5.setPos((0.5, -0.6))
        tree6_5.setPos((-0.5, 0.4))
        reward_3.setText(rewardval2)
        # setup some python lists for storing info about the resp_3
        resp_3.clicked_name = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        rewardframe2Components = [tree1_5, tree2_5, tree3_5, tree4_5, tree5_5, tree6_5, square_5, reward_3, resp_3]
        for thisComponent in rewardframe2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        rewardframe2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "rewardframe2"-------
        while continueRoutine:
            # get current time
            t = rewardframe2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=rewardframe2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *tree1_5* updates
            if tree1_5.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree1_5.frameNStart = frameN  # exact frame index
                tree1_5.tStart = t  # local t and not account for scr refresh
                tree1_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree1_5, 'tStartRefresh')  # time at next scr refresh
                tree1_5.setAutoDraw(True)
            
            # *tree2_5* updates
            if tree2_5.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree2_5.frameNStart = frameN  # exact frame index
                tree2_5.tStart = t  # local t and not account for scr refresh
                tree2_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree2_5, 'tStartRefresh')  # time at next scr refresh
                tree2_5.setAutoDraw(True)
            
            # *tree3_5* updates
            if tree3_5.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree3_5.frameNStart = frameN  # exact frame index
                tree3_5.tStart = t  # local t and not account for scr refresh
                tree3_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree3_5, 'tStartRefresh')  # time at next scr refresh
                tree3_5.setAutoDraw(True)
            
            # *tree4_5* updates
            if tree4_5.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree4_5.frameNStart = frameN  # exact frame index
                tree4_5.tStart = t  # local t and not account for scr refresh
                tree4_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree4_5, 'tStartRefresh')  # time at next scr refresh
                tree4_5.setAutoDraw(True)
            
            # *tree5_5* updates
            if tree5_5.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree5_5.frameNStart = frameN  # exact frame index
                tree5_5.tStart = t  # local t and not account for scr refresh
                tree5_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree5_5, 'tStartRefresh')  # time at next scr refresh
                tree5_5.setAutoDraw(True)
            
            # *tree6_5* updates
            if tree6_5.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree6_5.frameNStart = frameN  # exact frame index
                tree6_5.tStart = t  # local t and not account for scr refresh
                tree6_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree6_5, 'tStartRefresh')  # time at next scr refresh
                tree6_5.setAutoDraw(True)
            
            # *square_5* updates
            if square_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                square_5.frameNStart = frameN  # exact frame index
                square_5.tStart = t  # local t and not account for scr refresh
                square_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(square_5, 'tStartRefresh')  # time at next scr refresh
                square_5.setAutoDraw(True)
            
            # *reward_3* updates
            if reward_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                reward_3.frameNStart = frameN  # exact frame index
                reward_3.tStart = t  # local t and not account for scr refresh
                reward_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(reward_3, 'tStartRefresh')  # time at next scr refresh
                reward_3.setAutoDraw(True)
            # *resp_3* updates
            if resp_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                resp_3.frameNStart = frameN  # exact frame index
                resp_3.tStart = t  # local t and not account for scr refresh
                resp_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(resp_3, 'tStartRefresh')  # time at next scr refresh
                resp_3.status = STARTED
                resp_3.mouseClock.reset()
                prevButtonState = resp_3.getPressed()  # if button is down already this ISN'T a new click
            if resp_3.status == STARTED:  # only update if started and not finished!
                buttons = resp_3.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        for obj in [tree3_5]:
                            if obj.contains(resp_3):
                                gotValidClick = True
                                resp_3.clicked_name.append(obj.name)
                        if gotValidClick:  # abort routine on response
                            continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in rewardframe2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "rewardframe2"-------
        for thisComponent in rewardframe2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        reward2.addData('tree1_5.started', tree1_5.tStartRefresh)
        reward2.addData('tree1_5.stopped', tree1_5.tStopRefresh)
        reward2.addData('tree2_5.started', tree2_5.tStartRefresh)
        reward2.addData('tree2_5.stopped', tree2_5.tStopRefresh)
        reward2.addData('tree3_5.started', tree3_5.tStartRefresh)
        reward2.addData('tree3_5.stopped', tree3_5.tStopRefresh)
        reward2.addData('tree4_5.started', tree4_5.tStartRefresh)
        reward2.addData('tree4_5.stopped', tree4_5.tStopRefresh)
        reward2.addData('tree5_5.started', tree5_5.tStartRefresh)
        reward2.addData('tree5_5.stopped', tree5_5.tStopRefresh)
        reward2.addData('tree6_5.started', tree6_5.tStartRefresh)
        reward2.addData('tree6_5.stopped', tree6_5.tStopRefresh)
        reward2.addData('square_5.started', square_5.tStartRefresh)
        reward2.addData('square_5.stopped', square_5.tStopRefresh)
        reward2.addData('reward_3.started', reward_3.tStartRefresh)
        reward2.addData('reward_3.stopped', reward_3.tStopRefresh)
        # store data for reward2 (TrialHandler)
        x, y = resp_3.getPos()
        buttons = resp_3.getPressed()
        if sum(buttons):
            # check if the mouse was inside our 'clickable' objects
            gotValidClick = False
            for obj in [tree3_5]:
                if obj.contains(resp_3):
                    gotValidClick = True
                    resp_3.clicked_name.append(obj.name)
        reward2.addData('resp_3.x', x)
        reward2.addData('resp_3.y', y)
        reward2.addData('resp_3.leftButton', buttons[0])
        reward2.addData('resp_3.midButton', buttons[1])
        reward2.addData('resp_3.rightButton', buttons[2])
        if len(resp_3.clicked_name):
            reward2.addData('resp_3.clicked_name', resp_3.clicked_name[0])
        reward2.addData('resp_3.started', resp_3.tStart)
        reward2.addData('resp_3.stopped', resp_3.tStop)
        # the Routine "rewardframe2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'reward2'
    
    
    # set up handler to look after randomisation of conditions etc
    pos2 = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('pos.xlsx'),
        seed=None, name='pos2')
    thisExp.addLoop(pos2)  # add the loop to the experiment
    thisPos2 = pos2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPos2.rgb)
    if thisPos2 != None:
        for paramName in thisPos2:
            exec('{} = thisPos2[paramName]'.format(paramName))
    
    for thisPos2 in pos2:
        currentLoop = pos2
        # abbreviate parameter names if possible (e.g. rgb = thisPos2.rgb)
        if thisPos2 != None:
            for paramName in thisPos2:
                exec('{} = thisPos2[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "movetrees2"-------
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        tree1_10.setPos((0.5, tree2_n))
        tree2_10.setPos((-0.5, tree3_p))
        tree3_10.setPos((0.5, tree4_n))
        tree4_10.setPos((-0.5, tree5_p))
        tree5_10.setPos((0.5, tree6_n))
        tree6_10.setPos((-0.5, tree1_p))
        # keep track of which components have finished
        movetrees2Components = [tree1_10, tree2_10, tree3_10, tree4_10, tree5_10, tree6_10, square_10]
        for thisComponent in movetrees2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        movetrees2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "movetrees2"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = movetrees2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=movetrees2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *tree1_10* updates
            if tree1_10.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree1_10.frameNStart = frameN  # exact frame index
                tree1_10.tStart = t  # local t and not account for scr refresh
                tree1_10.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree1_10, 'tStartRefresh')  # time at next scr refresh
                tree1_10.setAutoDraw(True)
            if tree1_10.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree1_10.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    tree1_10.tStop = t  # not accounting for scr refresh
                    tree1_10.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree1_10, 'tStopRefresh')  # time at next scr refresh
                    tree1_10.setAutoDraw(False)
            
            # *tree2_10* updates
            if tree2_10.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree2_10.frameNStart = frameN  # exact frame index
                tree2_10.tStart = t  # local t and not account for scr refresh
                tree2_10.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree2_10, 'tStartRefresh')  # time at next scr refresh
                tree2_10.setAutoDraw(True)
            if tree2_10.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree2_10.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    tree2_10.tStop = t  # not accounting for scr refresh
                    tree2_10.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree2_10, 'tStopRefresh')  # time at next scr refresh
                    tree2_10.setAutoDraw(False)
            
            # *tree3_10* updates
            if tree3_10.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree3_10.frameNStart = frameN  # exact frame index
                tree3_10.tStart = t  # local t and not account for scr refresh
                tree3_10.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree3_10, 'tStartRefresh')  # time at next scr refresh
                tree3_10.setAutoDraw(True)
            if tree3_10.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree3_10.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    tree3_10.tStop = t  # not accounting for scr refresh
                    tree3_10.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree3_10, 'tStopRefresh')  # time at next scr refresh
                    tree3_10.setAutoDraw(False)
            
            # *tree4_10* updates
            if tree4_10.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree4_10.frameNStart = frameN  # exact frame index
                tree4_10.tStart = t  # local t and not account for scr refresh
                tree4_10.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree4_10, 'tStartRefresh')  # time at next scr refresh
                tree4_10.setAutoDraw(True)
            if tree4_10.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree4_10.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    tree4_10.tStop = t  # not accounting for scr refresh
                    tree4_10.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree4_10, 'tStopRefresh')  # time at next scr refresh
                    tree4_10.setAutoDraw(False)
            
            # *tree5_10* updates
            if tree5_10.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree5_10.frameNStart = frameN  # exact frame index
                tree5_10.tStart = t  # local t and not account for scr refresh
                tree5_10.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree5_10, 'tStartRefresh')  # time at next scr refresh
                tree5_10.setAutoDraw(True)
            if tree5_10.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree5_10.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    tree5_10.tStop = t  # not accounting for scr refresh
                    tree5_10.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree5_10, 'tStopRefresh')  # time at next scr refresh
                    tree5_10.setAutoDraw(False)
            
            # *tree6_10* updates
            if tree6_10.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree6_10.frameNStart = frameN  # exact frame index
                tree6_10.tStart = t  # local t and not account for scr refresh
                tree6_10.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree6_10, 'tStartRefresh')  # time at next scr refresh
                tree6_10.setAutoDraw(True)
            if tree6_10.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree6_10.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    tree6_10.tStop = t  # not accounting for scr refresh
                    tree6_10.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree6_10, 'tStopRefresh')  # time at next scr refresh
                    tree6_10.setAutoDraw(False)
            
            # *square_10* updates
            if square_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                square_10.frameNStart = frameN  # exact frame index
                square_10.tStart = t  # local t and not account for scr refresh
                square_10.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(square_10, 'tStartRefresh')  # time at next scr refresh
                square_10.setAutoDraw(True)
            if square_10.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > square_10.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    square_10.tStop = t  # not accounting for scr refresh
                    square_10.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(square_10, 'tStopRefresh')  # time at next scr refresh
                    square_10.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in movetrees2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "movetrees2"-------
        for thisComponent in movetrees2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        pos2.addData('tree1_10.started', tree1_10.tStartRefresh)
        pos2.addData('tree1_10.stopped', tree1_10.tStopRefresh)
        pos2.addData('tree2_10.started', tree2_10.tStartRefresh)
        pos2.addData('tree2_10.stopped', tree2_10.tStopRefresh)
        pos2.addData('tree3_10.started', tree3_10.tStartRefresh)
        pos2.addData('tree3_10.stopped', tree3_10.tStopRefresh)
        pos2.addData('tree4_10.started', tree4_10.tStartRefresh)
        pos2.addData('tree4_10.stopped', tree4_10.tStopRefresh)
        pos2.addData('tree5_10.started', tree5_10.tStartRefresh)
        pos2.addData('tree5_10.stopped', tree5_10.tStopRefresh)
        pos2.addData('tree6_10.started', tree6_10.tStartRefresh)
        pos2.addData('tree6_10.stopped', tree6_10.tStopRefresh)
        pos2.addData('square_10.started', square_10.tStartRefresh)
        pos2.addData('square_10.stopped', square_10.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'pos2'
    
    
    # set up handler to look after randomisation of conditions etc
    reward3 = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('reward.xlsx', selection='0:13'),
        seed=None, name='reward3')
    thisExp.addLoop(reward3)  # add the loop to the experiment
    thisReward3 = reward3.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisReward3.rgb)
    if thisReward3 != None:
        for paramName in thisReward3:
            exec('{} = thisReward3[paramName]'.format(paramName))
    
    for thisReward3 in reward3:
        currentLoop = reward3
        # abbreviate parameter names if possible (e.g. rgb = thisReward3.rgb)
        if thisReward3 != None:
            for paramName in thisReward3:
                exec('{} = thisReward3[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "rewardframe3"-------
        continueRoutine = True
        # update component parameters for each repeat
        tree1_7.setPos((0.5, 0))
        tree2_7.setPos((-0.5, -0.2))
        tree3_7.setPos((0.5, -0.4))
        tree4_7.setPos((-0.5, -0.6))
        tree5_7.setPos((0.5, 0.4))
        tree6_7.setPos((-0.5, 0.2))
        reward_4.setText(rewardval3)
        # setup some python lists for storing info about the resp_4
        resp_4.clicked_name = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        rewardframe3Components = [tree1_7, tree2_7, tree3_7, tree4_7, tree5_7, tree6_7, square_7, reward_4, resp_4]
        for thisComponent in rewardframe3Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        rewardframe3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "rewardframe3"-------
        while continueRoutine:
            # get current time
            t = rewardframe3Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=rewardframe3Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *tree1_7* updates
            if tree1_7.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree1_7.frameNStart = frameN  # exact frame index
                tree1_7.tStart = t  # local t and not account for scr refresh
                tree1_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree1_7, 'tStartRefresh')  # time at next scr refresh
                tree1_7.setAutoDraw(True)
            
            # *tree2_7* updates
            if tree2_7.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree2_7.frameNStart = frameN  # exact frame index
                tree2_7.tStart = t  # local t and not account for scr refresh
                tree2_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree2_7, 'tStartRefresh')  # time at next scr refresh
                tree2_7.setAutoDraw(True)
            
            # *tree3_7* updates
            if tree3_7.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree3_7.frameNStart = frameN  # exact frame index
                tree3_7.tStart = t  # local t and not account for scr refresh
                tree3_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree3_7, 'tStartRefresh')  # time at next scr refresh
                tree3_7.setAutoDraw(True)
            
            # *tree4_7* updates
            if tree4_7.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree4_7.frameNStart = frameN  # exact frame index
                tree4_7.tStart = t  # local t and not account for scr refresh
                tree4_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree4_7, 'tStartRefresh')  # time at next scr refresh
                tree4_7.setAutoDraw(True)
            
            # *tree5_7* updates
            if tree5_7.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree5_7.frameNStart = frameN  # exact frame index
                tree5_7.tStart = t  # local t and not account for scr refresh
                tree5_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree5_7, 'tStartRefresh')  # time at next scr refresh
                tree5_7.setAutoDraw(True)
            
            # *tree6_7* updates
            if tree6_7.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree6_7.frameNStart = frameN  # exact frame index
                tree6_7.tStart = t  # local t and not account for scr refresh
                tree6_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree6_7, 'tStartRefresh')  # time at next scr refresh
                tree6_7.setAutoDraw(True)
            
            # *square_7* updates
            if square_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                square_7.frameNStart = frameN  # exact frame index
                square_7.tStart = t  # local t and not account for scr refresh
                square_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(square_7, 'tStartRefresh')  # time at next scr refresh
                square_7.setAutoDraw(True)
            
            # *reward_4* updates
            if reward_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                reward_4.frameNStart = frameN  # exact frame index
                reward_4.tStart = t  # local t and not account for scr refresh
                reward_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(reward_4, 'tStartRefresh')  # time at next scr refresh
                reward_4.setAutoDraw(True)
            # *resp_4* updates
            if resp_4.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                resp_4.frameNStart = frameN  # exact frame index
                resp_4.tStart = t  # local t and not account for scr refresh
                resp_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(resp_4, 'tStartRefresh')  # time at next scr refresh
                resp_4.status = STARTED
                resp_4.mouseClock.reset()
                prevButtonState = resp_4.getPressed()  # if button is down already this ISN'T a new click
            if resp_4.status == STARTED:  # only update if started and not finished!
                buttons = resp_4.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        for obj in [tree2_7]:
                            if obj.contains(resp_4):
                                gotValidClick = True
                                resp_4.clicked_name.append(obj.name)
                        if gotValidClick:  # abort routine on response
                            continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in rewardframe3Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "rewardframe3"-------
        for thisComponent in rewardframe3Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        reward3.addData('tree1_7.started', tree1_7.tStartRefresh)
        reward3.addData('tree1_7.stopped', tree1_7.tStopRefresh)
        reward3.addData('tree2_7.started', tree2_7.tStartRefresh)
        reward3.addData('tree2_7.stopped', tree2_7.tStopRefresh)
        reward3.addData('tree3_7.started', tree3_7.tStartRefresh)
        reward3.addData('tree3_7.stopped', tree3_7.tStopRefresh)
        reward3.addData('tree4_7.started', tree4_7.tStartRefresh)
        reward3.addData('tree4_7.stopped', tree4_7.tStopRefresh)
        reward3.addData('tree5_7.started', tree5_7.tStartRefresh)
        reward3.addData('tree5_7.stopped', tree5_7.tStopRefresh)
        reward3.addData('tree6_7.started', tree6_7.tStartRefresh)
        reward3.addData('tree6_7.stopped', tree6_7.tStopRefresh)
        reward3.addData('square_7.started', square_7.tStartRefresh)
        reward3.addData('square_7.stopped', square_7.tStopRefresh)
        reward3.addData('reward_4.started', reward_4.tStartRefresh)
        reward3.addData('reward_4.stopped', reward_4.tStopRefresh)
        # store data for reward3 (TrialHandler)
        x, y = resp_4.getPos()
        buttons = resp_4.getPressed()
        if sum(buttons):
            # check if the mouse was inside our 'clickable' objects
            gotValidClick = False
            for obj in [tree2_7]:
                if obj.contains(resp_4):
                    gotValidClick = True
                    resp_4.clicked_name.append(obj.name)
        reward3.addData('resp_4.x', x)
        reward3.addData('resp_4.y', y)
        reward3.addData('resp_4.leftButton', buttons[0])
        reward3.addData('resp_4.midButton', buttons[1])
        reward3.addData('resp_4.rightButton', buttons[2])
        if len(resp_4.clicked_name):
            reward3.addData('resp_4.clicked_name', resp_4.clicked_name[0])
        reward3.addData('resp_4.started', resp_4.tStart)
        reward3.addData('resp_4.stopped', resp_4.tStop)
        # the Routine "rewardframe3" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'reward3'
    
    
    # set up handler to look after randomisation of conditions etc
    pos3 = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('pos.xlsx'),
        seed=None, name='pos3')
    thisExp.addLoop(pos3)  # add the loop to the experiment
    thisPos3 = pos3.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPos3.rgb)
    if thisPos3 != None:
        for paramName in thisPos3:
            exec('{} = thisPos3[paramName]'.format(paramName))
    
    for thisPos3 in pos3:
        currentLoop = pos3
        # abbreviate parameter names if possible (e.g. rgb = thisPos3.rgb)
        if thisPos3 != None:
            for paramName in thisPos3:
                exec('{} = thisPos3[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "movetrees3"-------
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        tree1_11.setPos((0.5, tree1_p))
        tree2_11.setPos((-0.5, tree2_n))
        tree3_11.setPos((0.5, tree3_p))
        tree4_11.setPos((-0.5, tree4_n))
        tree5_11.setPos((0.5, tree5_p))
        tree6_11.setPos((-0.5, tree6_n))
        # keep track of which components have finished
        movetrees3Components = [tree1_11, tree2_11, tree3_11, tree4_11, tree5_11, tree6_11, square_11]
        for thisComponent in movetrees3Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        movetrees3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "movetrees3"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = movetrees3Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=movetrees3Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *tree1_11* updates
            if tree1_11.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree1_11.frameNStart = frameN  # exact frame index
                tree1_11.tStart = t  # local t and not account for scr refresh
                tree1_11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree1_11, 'tStartRefresh')  # time at next scr refresh
                tree1_11.setAutoDraw(True)
            if tree1_11.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree1_11.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    tree1_11.tStop = t  # not accounting for scr refresh
                    tree1_11.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree1_11, 'tStopRefresh')  # time at next scr refresh
                    tree1_11.setAutoDraw(False)
            
            # *tree2_11* updates
            if tree2_11.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree2_11.frameNStart = frameN  # exact frame index
                tree2_11.tStart = t  # local t and not account for scr refresh
                tree2_11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree2_11, 'tStartRefresh')  # time at next scr refresh
                tree2_11.setAutoDraw(True)
            if tree2_11.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree2_11.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    tree2_11.tStop = t  # not accounting for scr refresh
                    tree2_11.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree2_11, 'tStopRefresh')  # time at next scr refresh
                    tree2_11.setAutoDraw(False)
            
            # *tree3_11* updates
            if tree3_11.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree3_11.frameNStart = frameN  # exact frame index
                tree3_11.tStart = t  # local t and not account for scr refresh
                tree3_11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree3_11, 'tStartRefresh')  # time at next scr refresh
                tree3_11.setAutoDraw(True)
            if tree3_11.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree3_11.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    tree3_11.tStop = t  # not accounting for scr refresh
                    tree3_11.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree3_11, 'tStopRefresh')  # time at next scr refresh
                    tree3_11.setAutoDraw(False)
            
            # *tree4_11* updates
            if tree4_11.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree4_11.frameNStart = frameN  # exact frame index
                tree4_11.tStart = t  # local t and not account for scr refresh
                tree4_11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree4_11, 'tStartRefresh')  # time at next scr refresh
                tree4_11.setAutoDraw(True)
            if tree4_11.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree4_11.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    tree4_11.tStop = t  # not accounting for scr refresh
                    tree4_11.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree4_11, 'tStopRefresh')  # time at next scr refresh
                    tree4_11.setAutoDraw(False)
            
            # *tree5_11* updates
            if tree5_11.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree5_11.frameNStart = frameN  # exact frame index
                tree5_11.tStart = t  # local t and not account for scr refresh
                tree5_11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree5_11, 'tStartRefresh')  # time at next scr refresh
                tree5_11.setAutoDraw(True)
            if tree5_11.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree5_11.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    tree5_11.tStop = t  # not accounting for scr refresh
                    tree5_11.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree5_11, 'tStopRefresh')  # time at next scr refresh
                    tree5_11.setAutoDraw(False)
            
            # *tree6_11* updates
            if tree6_11.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree6_11.frameNStart = frameN  # exact frame index
                tree6_11.tStart = t  # local t and not account for scr refresh
                tree6_11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree6_11, 'tStartRefresh')  # time at next scr refresh
                tree6_11.setAutoDraw(True)
            if tree6_11.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree6_11.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    tree6_11.tStop = t  # not accounting for scr refresh
                    tree6_11.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree6_11, 'tStopRefresh')  # time at next scr refresh
                    tree6_11.setAutoDraw(False)
            
            # *square_11* updates
            if square_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                square_11.frameNStart = frameN  # exact frame index
                square_11.tStart = t  # local t and not account for scr refresh
                square_11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(square_11, 'tStartRefresh')  # time at next scr refresh
                square_11.setAutoDraw(True)
            if square_11.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > square_11.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    square_11.tStop = t  # not accounting for scr refresh
                    square_11.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(square_11, 'tStopRefresh')  # time at next scr refresh
                    square_11.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in movetrees3Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "movetrees3"-------
        for thisComponent in movetrees3Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        pos3.addData('tree1_11.started', tree1_11.tStartRefresh)
        pos3.addData('tree1_11.stopped', tree1_11.tStopRefresh)
        pos3.addData('tree2_11.started', tree2_11.tStartRefresh)
        pos3.addData('tree2_11.stopped', tree2_11.tStopRefresh)
        pos3.addData('tree3_11.started', tree3_11.tStartRefresh)
        pos3.addData('tree3_11.stopped', tree3_11.tStopRefresh)
        pos3.addData('tree4_11.started', tree4_11.tStartRefresh)
        pos3.addData('tree4_11.stopped', tree4_11.tStopRefresh)
        pos3.addData('tree5_11.started', tree5_11.tStartRefresh)
        pos3.addData('tree5_11.stopped', tree5_11.tStopRefresh)
        pos3.addData('tree6_11.started', tree6_11.tStartRefresh)
        pos3.addData('tree6_11.stopped', tree6_11.tStopRefresh)
        pos3.addData('square_11.started', square_11.tStartRefresh)
        pos3.addData('square_11.stopped', square_11.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'pos3'
    
    
    # set up handler to look after randomisation of conditions etc
    reward4 = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('reward.xlsx', selection='0:13'),
        seed=None, name='reward4')
    thisExp.addLoop(reward4)  # add the loop to the experiment
    thisReward4 = reward4.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisReward4.rgb)
    if thisReward4 != None:
        for paramName in thisReward4:
            exec('{} = thisReward4[paramName]'.format(paramName))
    
    for thisReward4 in reward4:
        currentLoop = reward4
        # abbreviate parameter names if possible (e.g. rgb = thisReward4.rgb)
        if thisReward4 != None:
            for paramName in thisReward4:
                exec('{} = thisReward4[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "rewardframe4"-------
        continueRoutine = True
        # update component parameters for each repeat
        tree1_8.setPos((0.5, 0.2))
        tree2_8.setPos((-0.5, 0))
        tree3_8.setPos((0.5, -0.2))
        tree4_8.setPos((-0.5, -0.4))
        tree5_8.setPos((0.5, -0.6))
        tree6_8.setPos((-0.5, 0.4))
        reward_5.setText(rewardval4)
        # setup some python lists for storing info about the resp_5
        resp_5.clicked_name = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        rewardframe4Components = [tree1_8, tree2_8, tree3_8, tree4_8, tree5_8, tree6_8, square_8, reward_5, resp_5]
        for thisComponent in rewardframe4Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        rewardframe4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "rewardframe4"-------
        while continueRoutine:
            # get current time
            t = rewardframe4Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=rewardframe4Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *tree1_8* updates
            if tree1_8.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree1_8.frameNStart = frameN  # exact frame index
                tree1_8.tStart = t  # local t and not account for scr refresh
                tree1_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree1_8, 'tStartRefresh')  # time at next scr refresh
                tree1_8.setAutoDraw(True)
            
            # *tree2_8* updates
            if tree2_8.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree2_8.frameNStart = frameN  # exact frame index
                tree2_8.tStart = t  # local t and not account for scr refresh
                tree2_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree2_8, 'tStartRefresh')  # time at next scr refresh
                tree2_8.setAutoDraw(True)
            
            # *tree3_8* updates
            if tree3_8.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree3_8.frameNStart = frameN  # exact frame index
                tree3_8.tStart = t  # local t and not account for scr refresh
                tree3_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree3_8, 'tStartRefresh')  # time at next scr refresh
                tree3_8.setAutoDraw(True)
            
            # *tree4_8* updates
            if tree4_8.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree4_8.frameNStart = frameN  # exact frame index
                tree4_8.tStart = t  # local t and not account for scr refresh
                tree4_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree4_8, 'tStartRefresh')  # time at next scr refresh
                tree4_8.setAutoDraw(True)
            
            # *tree5_8* updates
            if tree5_8.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree5_8.frameNStart = frameN  # exact frame index
                tree5_8.tStart = t  # local t and not account for scr refresh
                tree5_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree5_8, 'tStartRefresh')  # time at next scr refresh
                tree5_8.setAutoDraw(True)
            
            # *tree6_8* updates
            if tree6_8.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree6_8.frameNStart = frameN  # exact frame index
                tree6_8.tStart = t  # local t and not account for scr refresh
                tree6_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree6_8, 'tStartRefresh')  # time at next scr refresh
                tree6_8.setAutoDraw(True)
            
            # *square_8* updates
            if square_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                square_8.frameNStart = frameN  # exact frame index
                square_8.tStart = t  # local t and not account for scr refresh
                square_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(square_8, 'tStartRefresh')  # time at next scr refresh
                square_8.setAutoDraw(True)
            
            # *reward_5* updates
            if reward_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                reward_5.frameNStart = frameN  # exact frame index
                reward_5.tStart = t  # local t and not account for scr refresh
                reward_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(reward_5, 'tStartRefresh')  # time at next scr refresh
                reward_5.setAutoDraw(True)
            # *resp_5* updates
            if resp_5.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                resp_5.frameNStart = frameN  # exact frame index
                resp_5.tStart = t  # local t and not account for scr refresh
                resp_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(resp_5, 'tStartRefresh')  # time at next scr refresh
                resp_5.status = STARTED
                resp_5.mouseClock.reset()
                prevButtonState = resp_5.getPressed()  # if button is down already this ISN'T a new click
            if resp_5.status == STARTED:  # only update if started and not finished!
                buttons = resp_5.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        for obj in [tree3_5]:
                            if obj.contains(resp_5):
                                gotValidClick = True
                                resp_5.clicked_name.append(obj.name)
                        if gotValidClick:  # abort routine on response
                            continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in rewardframe4Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "rewardframe4"-------
        for thisComponent in rewardframe4Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        reward4.addData('tree1_8.started', tree1_8.tStartRefresh)
        reward4.addData('tree1_8.stopped', tree1_8.tStopRefresh)
        reward4.addData('tree2_8.started', tree2_8.tStartRefresh)
        reward4.addData('tree2_8.stopped', tree2_8.tStopRefresh)
        reward4.addData('tree3_8.started', tree3_8.tStartRefresh)
        reward4.addData('tree3_8.stopped', tree3_8.tStopRefresh)
        reward4.addData('tree4_8.started', tree4_8.tStartRefresh)
        reward4.addData('tree4_8.stopped', tree4_8.tStopRefresh)
        reward4.addData('tree5_8.started', tree5_8.tStartRefresh)
        reward4.addData('tree5_8.stopped', tree5_8.tStopRefresh)
        reward4.addData('tree6_8.started', tree6_8.tStartRefresh)
        reward4.addData('tree6_8.stopped', tree6_8.tStopRefresh)
        reward4.addData('square_8.started', square_8.tStartRefresh)
        reward4.addData('square_8.stopped', square_8.tStopRefresh)
        reward4.addData('reward_5.started', reward_5.tStartRefresh)
        reward4.addData('reward_5.stopped', reward_5.tStopRefresh)
        # store data for reward4 (TrialHandler)
        x, y = resp_5.getPos()
        buttons = resp_5.getPressed()
        if sum(buttons):
            # check if the mouse was inside our 'clickable' objects
            gotValidClick = False
            for obj in [tree3_5]:
                if obj.contains(resp_5):
                    gotValidClick = True
                    resp_5.clicked_name.append(obj.name)
        reward4.addData('resp_5.x', x)
        reward4.addData('resp_5.y', y)
        reward4.addData('resp_5.leftButton', buttons[0])
        reward4.addData('resp_5.midButton', buttons[1])
        reward4.addData('resp_5.rightButton', buttons[2])
        if len(resp_5.clicked_name):
            reward4.addData('resp_5.clicked_name', resp_5.clicked_name[0])
        reward4.addData('resp_5.started', resp_5.tStart)
        reward4.addData('resp_5.stopped', resp_5.tStop)
        # the Routine "rewardframe4" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'reward4'
    
    
    # set up handler to look after randomisation of conditions etc
    pos2_2 = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('pos.xlsx'),
        seed=None, name='pos2_2')
    thisExp.addLoop(pos2_2)  # add the loop to the experiment
    thisPos2_2 = pos2_2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPos2_2.rgb)
    if thisPos2_2 != None:
        for paramName in thisPos2_2:
            exec('{} = thisPos2_2[paramName]'.format(paramName))
    
    for thisPos2_2 in pos2_2:
        currentLoop = pos2_2
        # abbreviate parameter names if possible (e.g. rgb = thisPos2_2.rgb)
        if thisPos2_2 != None:
            for paramName in thisPos2_2:
                exec('{} = thisPos2_2[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "movetrees2"-------
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        tree1_10.setPos((0.5, tree2_n))
        tree2_10.setPos((-0.5, tree3_p))
        tree3_10.setPos((0.5, tree4_n))
        tree4_10.setPos((-0.5, tree5_p))
        tree5_10.setPos((0.5, tree6_n))
        tree6_10.setPos((-0.5, tree1_p))
        # keep track of which components have finished
        movetrees2Components = [tree1_10, tree2_10, tree3_10, tree4_10, tree5_10, tree6_10, square_10]
        for thisComponent in movetrees2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        movetrees2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "movetrees2"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = movetrees2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=movetrees2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *tree1_10* updates
            if tree1_10.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree1_10.frameNStart = frameN  # exact frame index
                tree1_10.tStart = t  # local t and not account for scr refresh
                tree1_10.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree1_10, 'tStartRefresh')  # time at next scr refresh
                tree1_10.setAutoDraw(True)
            if tree1_10.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree1_10.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    tree1_10.tStop = t  # not accounting for scr refresh
                    tree1_10.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree1_10, 'tStopRefresh')  # time at next scr refresh
                    tree1_10.setAutoDraw(False)
            
            # *tree2_10* updates
            if tree2_10.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree2_10.frameNStart = frameN  # exact frame index
                tree2_10.tStart = t  # local t and not account for scr refresh
                tree2_10.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree2_10, 'tStartRefresh')  # time at next scr refresh
                tree2_10.setAutoDraw(True)
            if tree2_10.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree2_10.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    tree2_10.tStop = t  # not accounting for scr refresh
                    tree2_10.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree2_10, 'tStopRefresh')  # time at next scr refresh
                    tree2_10.setAutoDraw(False)
            
            # *tree3_10* updates
            if tree3_10.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree3_10.frameNStart = frameN  # exact frame index
                tree3_10.tStart = t  # local t and not account for scr refresh
                tree3_10.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree3_10, 'tStartRefresh')  # time at next scr refresh
                tree3_10.setAutoDraw(True)
            if tree3_10.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree3_10.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    tree3_10.tStop = t  # not accounting for scr refresh
                    tree3_10.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree3_10, 'tStopRefresh')  # time at next scr refresh
                    tree3_10.setAutoDraw(False)
            
            # *tree4_10* updates
            if tree4_10.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree4_10.frameNStart = frameN  # exact frame index
                tree4_10.tStart = t  # local t and not account for scr refresh
                tree4_10.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree4_10, 'tStartRefresh')  # time at next scr refresh
                tree4_10.setAutoDraw(True)
            if tree4_10.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree4_10.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    tree4_10.tStop = t  # not accounting for scr refresh
                    tree4_10.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree4_10, 'tStopRefresh')  # time at next scr refresh
                    tree4_10.setAutoDraw(False)
            
            # *tree5_10* updates
            if tree5_10.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree5_10.frameNStart = frameN  # exact frame index
                tree5_10.tStart = t  # local t and not account for scr refresh
                tree5_10.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree5_10, 'tStartRefresh')  # time at next scr refresh
                tree5_10.setAutoDraw(True)
            if tree5_10.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree5_10.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    tree5_10.tStop = t  # not accounting for scr refresh
                    tree5_10.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree5_10, 'tStopRefresh')  # time at next scr refresh
                    tree5_10.setAutoDraw(False)
            
            # *tree6_10* updates
            if tree6_10.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree6_10.frameNStart = frameN  # exact frame index
                tree6_10.tStart = t  # local t and not account for scr refresh
                tree6_10.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree6_10, 'tStartRefresh')  # time at next scr refresh
                tree6_10.setAutoDraw(True)
            if tree6_10.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree6_10.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    tree6_10.tStop = t  # not accounting for scr refresh
                    tree6_10.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree6_10, 'tStopRefresh')  # time at next scr refresh
                    tree6_10.setAutoDraw(False)
            
            # *square_10* updates
            if square_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                square_10.frameNStart = frameN  # exact frame index
                square_10.tStart = t  # local t and not account for scr refresh
                square_10.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(square_10, 'tStartRefresh')  # time at next scr refresh
                square_10.setAutoDraw(True)
            if square_10.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > square_10.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    square_10.tStop = t  # not accounting for scr refresh
                    square_10.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(square_10, 'tStopRefresh')  # time at next scr refresh
                    square_10.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in movetrees2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "movetrees2"-------
        for thisComponent in movetrees2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        pos2_2.addData('tree1_10.started', tree1_10.tStartRefresh)
        pos2_2.addData('tree1_10.stopped', tree1_10.tStopRefresh)
        pos2_2.addData('tree2_10.started', tree2_10.tStartRefresh)
        pos2_2.addData('tree2_10.stopped', tree2_10.tStopRefresh)
        pos2_2.addData('tree3_10.started', tree3_10.tStartRefresh)
        pos2_2.addData('tree3_10.stopped', tree3_10.tStopRefresh)
        pos2_2.addData('tree4_10.started', tree4_10.tStartRefresh)
        pos2_2.addData('tree4_10.stopped', tree4_10.tStopRefresh)
        pos2_2.addData('tree5_10.started', tree5_10.tStartRefresh)
        pos2_2.addData('tree5_10.stopped', tree5_10.tStopRefresh)
        pos2_2.addData('tree6_10.started', tree6_10.tStartRefresh)
        pos2_2.addData('tree6_10.stopped', tree6_10.tStopRefresh)
        pos2_2.addData('square_10.started', square_10.tStartRefresh)
        pos2_2.addData('square_10.stopped', square_10.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'pos2_2'
    
    
    # set up handler to look after randomisation of conditions etc
    reward5 = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('reward.xlsx', selection='0:12'),
        seed=None, name='reward5')
    thisExp.addLoop(reward5)  # add the loop to the experiment
    thisReward5 = reward5.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisReward5.rgb)
    if thisReward5 != None:
        for paramName in thisReward5:
            exec('{} = thisReward5[paramName]'.format(paramName))
    
    for thisReward5 in reward5:
        currentLoop = reward5
        # abbreviate parameter names if possible (e.g. rgb = thisReward5.rgb)
        if thisReward5 != None:
            for paramName in thisReward5:
                exec('{} = thisReward5[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "rewardframe5"-------
        continueRoutine = True
        # update component parameters for each repeat
        tree1_9.setPos((0.5, 0))
        tree2_9.setPos((-0.5, -0.2))
        tree3_9.setPos((0.5, -0.4))
        tree4_9.setPos((-0.5, -0.6))
        tree5_9.setPos((0.5, 0.4))
        tree6_9.setPos((-0.5, 0.2))
        reward_6.setText(rewardval5)
        # setup some python lists for storing info about the resp_6
        resp_6.clicked_name = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        rewardframe5Components = [tree1_9, tree2_9, tree3_9, tree4_9, tree5_9, tree6_9, square_9, reward_6, resp_6]
        for thisComponent in rewardframe5Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        rewardframe5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "rewardframe5"-------
        while continueRoutine:
            # get current time
            t = rewardframe5Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=rewardframe5Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *tree1_9* updates
            if tree1_9.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree1_9.frameNStart = frameN  # exact frame index
                tree1_9.tStart = t  # local t and not account for scr refresh
                tree1_9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree1_9, 'tStartRefresh')  # time at next scr refresh
                tree1_9.setAutoDraw(True)
            
            # *tree2_9* updates
            if tree2_9.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree2_9.frameNStart = frameN  # exact frame index
                tree2_9.tStart = t  # local t and not account for scr refresh
                tree2_9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree2_9, 'tStartRefresh')  # time at next scr refresh
                tree2_9.setAutoDraw(True)
            
            # *tree3_9* updates
            if tree3_9.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree3_9.frameNStart = frameN  # exact frame index
                tree3_9.tStart = t  # local t and not account for scr refresh
                tree3_9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree3_9, 'tStartRefresh')  # time at next scr refresh
                tree3_9.setAutoDraw(True)
            
            # *tree4_9* updates
            if tree4_9.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree4_9.frameNStart = frameN  # exact frame index
                tree4_9.tStart = t  # local t and not account for scr refresh
                tree4_9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree4_9, 'tStartRefresh')  # time at next scr refresh
                tree4_9.setAutoDraw(True)
            
            # *tree5_9* updates
            if tree5_9.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree5_9.frameNStart = frameN  # exact frame index
                tree5_9.tStart = t  # local t and not account for scr refresh
                tree5_9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree5_9, 'tStartRefresh')  # time at next scr refresh
                tree5_9.setAutoDraw(True)
            
            # *tree6_9* updates
            if tree6_9.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree6_9.frameNStart = frameN  # exact frame index
                tree6_9.tStart = t  # local t and not account for scr refresh
                tree6_9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree6_9, 'tStartRefresh')  # time at next scr refresh
                tree6_9.setAutoDraw(True)
            
            # *square_9* updates
            if square_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                square_9.frameNStart = frameN  # exact frame index
                square_9.tStart = t  # local t and not account for scr refresh
                square_9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(square_9, 'tStartRefresh')  # time at next scr refresh
                square_9.setAutoDraw(True)
            
            # *reward_6* updates
            if reward_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                reward_6.frameNStart = frameN  # exact frame index
                reward_6.tStart = t  # local t and not account for scr refresh
                reward_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(reward_6, 'tStartRefresh')  # time at next scr refresh
                reward_6.setAutoDraw(True)
            # *resp_6* updates
            if resp_6.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                resp_6.frameNStart = frameN  # exact frame index
                resp_6.tStart = t  # local t and not account for scr refresh
                resp_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(resp_6, 'tStartRefresh')  # time at next scr refresh
                resp_6.status = STARTED
                resp_6.mouseClock.reset()
                prevButtonState = resp_6.getPressed()  # if button is down already this ISN'T a new click
            if resp_6.status == STARTED:  # only update if started and not finished!
                buttons = resp_6.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        for obj in [tree2_7]:
                            if obj.contains(resp_6):
                                gotValidClick = True
                                resp_6.clicked_name.append(obj.name)
                        if gotValidClick:  # abort routine on response
                            continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in rewardframe5Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "rewardframe5"-------
        for thisComponent in rewardframe5Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        reward5.addData('tree1_9.started', tree1_9.tStartRefresh)
        reward5.addData('tree1_9.stopped', tree1_9.tStopRefresh)
        reward5.addData('tree2_9.started', tree2_9.tStartRefresh)
        reward5.addData('tree2_9.stopped', tree2_9.tStopRefresh)
        reward5.addData('tree3_9.started', tree3_9.tStartRefresh)
        reward5.addData('tree3_9.stopped', tree3_9.tStopRefresh)
        reward5.addData('tree4_9.started', tree4_9.tStartRefresh)
        reward5.addData('tree4_9.stopped', tree4_9.tStopRefresh)
        reward5.addData('tree5_9.started', tree5_9.tStartRefresh)
        reward5.addData('tree5_9.stopped', tree5_9.tStopRefresh)
        reward5.addData('tree6_9.started', tree6_9.tStartRefresh)
        reward5.addData('tree6_9.stopped', tree6_9.tStopRefresh)
        reward5.addData('square_9.started', square_9.tStartRefresh)
        reward5.addData('square_9.stopped', square_9.tStopRefresh)
        reward5.addData('reward_6.started', reward_6.tStartRefresh)
        reward5.addData('reward_6.stopped', reward_6.tStopRefresh)
        # store data for reward5 (TrialHandler)
        x, y = resp_6.getPos()
        buttons = resp_6.getPressed()
        if sum(buttons):
            # check if the mouse was inside our 'clickable' objects
            gotValidClick = False
            for obj in [tree2_7]:
                if obj.contains(resp_6):
                    gotValidClick = True
                    resp_6.clicked_name.append(obj.name)
        reward5.addData('resp_6.x', x)
        reward5.addData('resp_6.y', y)
        reward5.addData('resp_6.leftButton', buttons[0])
        reward5.addData('resp_6.midButton', buttons[1])
        reward5.addData('resp_6.rightButton', buttons[2])
        if len(resp_6.clicked_name):
            reward5.addData('resp_6.clicked_name', resp_6.clicked_name[0])
        reward5.addData('resp_6.started', resp_6.tStart)
        reward5.addData('resp_6.stopped', resp_6.tStop)
        # the Routine "rewardframe5" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'reward5'
    
    
    # set up handler to look after randomisation of conditions etc
    pos3_2 = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('pos.xlsx'),
        seed=None, name='pos3_2')
    thisExp.addLoop(pos3_2)  # add the loop to the experiment
    thisPos3_2 = pos3_2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPos3_2.rgb)
    if thisPos3_2 != None:
        for paramName in thisPos3_2:
            exec('{} = thisPos3_2[paramName]'.format(paramName))
    
    for thisPos3_2 in pos3_2:
        currentLoop = pos3_2
        # abbreviate parameter names if possible (e.g. rgb = thisPos3_2.rgb)
        if thisPos3_2 != None:
            for paramName in thisPos3_2:
                exec('{} = thisPos3_2[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "movetrees3"-------
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        tree1_11.setPos((0.5, tree1_p))
        tree2_11.setPos((-0.5, tree2_n))
        tree3_11.setPos((0.5, tree3_p))
        tree4_11.setPos((-0.5, tree4_n))
        tree5_11.setPos((0.5, tree5_p))
        tree6_11.setPos((-0.5, tree6_n))
        # keep track of which components have finished
        movetrees3Components = [tree1_11, tree2_11, tree3_11, tree4_11, tree5_11, tree6_11, square_11]
        for thisComponent in movetrees3Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        movetrees3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "movetrees3"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = movetrees3Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=movetrees3Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *tree1_11* updates
            if tree1_11.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree1_11.frameNStart = frameN  # exact frame index
                tree1_11.tStart = t  # local t and not account for scr refresh
                tree1_11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree1_11, 'tStartRefresh')  # time at next scr refresh
                tree1_11.setAutoDraw(True)
            if tree1_11.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree1_11.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    tree1_11.tStop = t  # not accounting for scr refresh
                    tree1_11.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree1_11, 'tStopRefresh')  # time at next scr refresh
                    tree1_11.setAutoDraw(False)
            
            # *tree2_11* updates
            if tree2_11.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree2_11.frameNStart = frameN  # exact frame index
                tree2_11.tStart = t  # local t and not account for scr refresh
                tree2_11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree2_11, 'tStartRefresh')  # time at next scr refresh
                tree2_11.setAutoDraw(True)
            if tree2_11.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree2_11.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    tree2_11.tStop = t  # not accounting for scr refresh
                    tree2_11.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree2_11, 'tStopRefresh')  # time at next scr refresh
                    tree2_11.setAutoDraw(False)
            
            # *tree3_11* updates
            if tree3_11.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree3_11.frameNStart = frameN  # exact frame index
                tree3_11.tStart = t  # local t and not account for scr refresh
                tree3_11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree3_11, 'tStartRefresh')  # time at next scr refresh
                tree3_11.setAutoDraw(True)
            if tree3_11.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree3_11.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    tree3_11.tStop = t  # not accounting for scr refresh
                    tree3_11.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree3_11, 'tStopRefresh')  # time at next scr refresh
                    tree3_11.setAutoDraw(False)
            
            # *tree4_11* updates
            if tree4_11.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree4_11.frameNStart = frameN  # exact frame index
                tree4_11.tStart = t  # local t and not account for scr refresh
                tree4_11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree4_11, 'tStartRefresh')  # time at next scr refresh
                tree4_11.setAutoDraw(True)
            if tree4_11.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree4_11.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    tree4_11.tStop = t  # not accounting for scr refresh
                    tree4_11.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree4_11, 'tStopRefresh')  # time at next scr refresh
                    tree4_11.setAutoDraw(False)
            
            # *tree5_11* updates
            if tree5_11.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree5_11.frameNStart = frameN  # exact frame index
                tree5_11.tStart = t  # local t and not account for scr refresh
                tree5_11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree5_11, 'tStartRefresh')  # time at next scr refresh
                tree5_11.setAutoDraw(True)
            if tree5_11.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree5_11.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    tree5_11.tStop = t  # not accounting for scr refresh
                    tree5_11.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree5_11, 'tStopRefresh')  # time at next scr refresh
                    tree5_11.setAutoDraw(False)
            
            # *tree6_11* updates
            if tree6_11.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree6_11.frameNStart = frameN  # exact frame index
                tree6_11.tStart = t  # local t and not account for scr refresh
                tree6_11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree6_11, 'tStartRefresh')  # time at next scr refresh
                tree6_11.setAutoDraw(True)
            if tree6_11.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree6_11.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    tree6_11.tStop = t  # not accounting for scr refresh
                    tree6_11.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree6_11, 'tStopRefresh')  # time at next scr refresh
                    tree6_11.setAutoDraw(False)
            
            # *square_11* updates
            if square_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                square_11.frameNStart = frameN  # exact frame index
                square_11.tStart = t  # local t and not account for scr refresh
                square_11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(square_11, 'tStartRefresh')  # time at next scr refresh
                square_11.setAutoDraw(True)
            if square_11.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > square_11.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    square_11.tStop = t  # not accounting for scr refresh
                    square_11.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(square_11, 'tStopRefresh')  # time at next scr refresh
                    square_11.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in movetrees3Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "movetrees3"-------
        for thisComponent in movetrees3Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        pos3_2.addData('tree1_11.started', tree1_11.tStartRefresh)
        pos3_2.addData('tree1_11.stopped', tree1_11.tStopRefresh)
        pos3_2.addData('tree2_11.started', tree2_11.tStartRefresh)
        pos3_2.addData('tree2_11.stopped', tree2_11.tStopRefresh)
        pos3_2.addData('tree3_11.started', tree3_11.tStartRefresh)
        pos3_2.addData('tree3_11.stopped', tree3_11.tStopRefresh)
        pos3_2.addData('tree4_11.started', tree4_11.tStartRefresh)
        pos3_2.addData('tree4_11.stopped', tree4_11.tStopRefresh)
        pos3_2.addData('tree5_11.started', tree5_11.tStartRefresh)
        pos3_2.addData('tree5_11.stopped', tree5_11.tStopRefresh)
        pos3_2.addData('tree6_11.started', tree6_11.tStartRefresh)
        pos3_2.addData('tree6_11.stopped', tree6_11.tStopRefresh)
        pos3_2.addData('square_11.started', square_11.tStartRefresh)
        pos3_2.addData('square_11.stopped', square_11.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'pos3_2'
    
    thisExp.nextEntry()
    
# completed 3 repeats of 'trials'


# ------Prepare to start Routine "end"-------
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
endComponents = [text]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
            text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
