from numpy import double
from numpy.core.fromnumeric import mean
import pandas as pd

dfi = pd.read_csv('pmvtdata.csv')

name = dfi['Participant Name'].to_list()
pid = dfi['Participant ID'].to_list()
TotalScoreEnv1 = dfi['TotalScoreEnv1'].to_list()
TotalScoreEnv2 = dfi['TotalScoreEnv2'].to_list()
Avgreactiontime1 = dfi['AvgReactionTime1'].to_list()
Avgreactiontime2 = dfi['AvgReactionTime2'].to_list()
AvgLeaveTime1 = dfi['AvgLeavingTimeEnv1'].to_list()
AvgLeaveTime2 = dfi['AvgLeavingTimeEnv2'].to_list()

for i in range(len(name)):
    rt=Avgreactiontime1[i]
    
        