from numpy import double
from numpy.core.fromnumeric import mean
import pandas as pd
# import random

pid='T'
name='Nandita'
env=1
dfi = pd.read_csv('data_env1.csv')

Avgreactiontime1 = dfi["Reaction time"].mean()
# print("Avgreactiontime1 = ", Avgreactiontime1)

Time = dfi["Time elapsed"].to_list()
map(double, Time)
Choice = dfi["Decision"].to_list()
TreeNo = dfi["Tree number"].to_list()
Rew = dfi["Cumulative reward per tree"].to_list()

Leavetime=[]
tree=[]
envi=[]
rew=[]
temp=0
trees1=0
for i in range(len(Time)):
    if Choice[i]=='leave':
        tree.append(TreeNo[i])
        trees1=TreeNo[i]
        rew.append(Rew[i])
        envi.append(env)
        Leavetime.append(Time[i]-temp)
        temp=Time[i]


AvgLeaveTime1=mean(Leavetime) - 4
# print("leavetime env1 avg =", AvgLeaveTime1)
TotalScoreEnv1=sum(rew)
AvgRewardPerTree1=mean(rew)
# print("TotalScoreEnv1=", TotalScoreEnv1)

########

env=2
dfi = pd.read_csv('data_env2.csv')

Avgreactiontime2 = dfi["Reaction time"].mean()
# print("Avgreactiontime2 = ", Avgreactiontime2)

Time = dfi["Time elapsed"].to_list()
map(double, Time)
Choice = dfi["Decision"].to_list()
TreeNo = dfi["Tree number"].to_list()
Rew = dfi["Cumulative reward per tree"].to_list()

Leavetime2=[]
rew2=[]
temp=0
trees2=0
for i in range(len(Time)):
    if Choice[i]=='leave':
        tree.append(TreeNo[i])
        trees2=TreeNo[i]
        rew.append(Rew[i])
        rew2.append(Rew[i])
        envi.append(env)
        Leavetime.append(Time[i]-temp)
        Leavetime2.append(Time[i]-temp)
        temp=Time[i]

AvgLeaveTime2=mean(Leavetime2) - 8
# print("leavetime env2 avg =", AvgLeaveTime1)
TotalScoreEnv2=sum(rew) - TotalScoreEnv1
AvgRewardPerTree2=mean(rew2)
# print("TotalScoreEnv2=", TotalScoreEnv2)

dict = {'Participant Name': name, 'Participant ID': pid, 'Environment': envi, 'Tree #': tree, 'Leave times': Leavetime, 'Reward': rew} 
     
df = pd.DataFrame(dict)
df_name =  "Pdata.csv"
df.to_csv(df_name)
print(df)

dict2 = {'Participant Name': name, 'Participant ID': pid,	'TotalScoreEnv1': TotalScoreEnv1,	'TotalScoreEnv2': TotalScoreEnv2,	'AvgReactionTime1': Avgreactiontime1,  'AvgReactionTime2': Avgreactiontime2, 'AvgLeavingTimeEnv1': AvgLeaveTime1, 'AvgLeavingTimeEnv2': AvgLeaveTime2, 'AvgRewardPerTree1':AvgRewardPerTree1, 'AvgRewardPerTree2':AvgRewardPerTree2, 'TotalTrees1': trees1, 'TotalTrees2': trees2}

df = pd.DataFrame(dict2, index=[0])
df_name =  "pmvtdata.csv"
df.to_csv(df_name)
print(df)

