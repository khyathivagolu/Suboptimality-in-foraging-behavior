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
map(double, AvgLeaveTime1)
map(double, AvgLeaveTime2)

totavglt1 = mean(AvgLeaveTime1)
totavglt2 = mean(AvgLeaveTime2)

mlt1=[]
mlt2=[]
for i in range(len(dfi)):
   mlt1.append(abs(AvgLeaveTime1[i]-totavglt1))
   mlt2.append(abs(AvgLeaveTime2[i]-totavglt2))

print(mlt1)
print(mlt2)