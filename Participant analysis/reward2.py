from numpy import double
from numpy.core.fromnumeric import mean
import pandas as pd
# import random

dfi = pd.read_csv('totalpdata.csv')

sno= dfi['Participant Serial No'].to_list()
name = dfi['Participant Name'].to_list()
pid = dfi['Participant ID'].to_list()
env = dfi['Environment'].to_list()
leavetime=dfi['Leave times'].to_list()
map(double, leavetime)

l1=[]
l2=[]
names=[]
aleavetime1=[]
aleavetime2=[]
flag=0
for i in range(len(dfi)):
    if env[i]==1:
        if flag:
            l1.append(leavetime[i])
        flag=1
    if env[i]==2:
        l2.append(leavetime[i])
    if i>1 and sno[i-1]==0:
        flag=0
        aleavetime1.append(mean(l1)-4)
        aleavetime2.append(mean(l2)-8)
        names.append(name[i])
        l1=[]
        l2=[]

print(aleavetime1)
print(aleavetime2)



dict2 = {'Participant Name': names,	'aleavetime1':aleavetime1,'aleavetime2':aleavetime2 }

df = pd.DataFrame(dict2)
df_name =  "ans.csv"
df.to_csv(df_name)
print(df)

    


# Avgreactiontime1 = dfi["Reaction time"].mean()
# # print("Avgreactiontime1 = ", Avgreactiontime1)

# Time = dfi["Time elapsed"].to_list()
# map(double, Time)
# Choice = dfi["Decision"].to_list()
# TreeNo = dfi["Tree number"].to_list()
# Rew = dfi["Cumulative reward per tree"].to_list()

# Leavetime=[]
# tree=[]
# envi=[]
# rew=[]
# temp=0
# trees1=0
# for i in range(len(Time)):
#     if Choice[i]=='leave':
#         tree.append(TreeNo[i])
#         trees1=TreeNo[i]
#         rew.append(Rew[i])
#         envi.append(env)
#         Leavetime.append(Time[i]-temp)
#         temp=Time[i]


# AvgLeaveTime1=mean(Leavetime) - 4
# # print("leavetime env1 avg =", AvgLeaveTime1)
# TotalScoreEnv1=sum(rew)
# AvgRewardPerTree1=mean(rew)
# # print("TotalScoreEnv1=", TotalScoreEnv1)

# ########

# env=2
# dfi = pd.read_csv('data_env2.csv')

# Avgreactiontime2 = dfi["Reaction time"].mean()
# # print("Avgreactiontime2 = ", Avgreactiontime2)

# Time = dfi["Time elapsed"].to_list()
# map(double, Time)
# Choice = dfi["Decision"].to_list()
# TreeNo = dfi["Tree number"].to_list()
# Rew = dfi["Cumulative reward per tree"].to_list()

# Leavetime2=[]
# rew2=[]
# temp=0
# trees2=0
# for i in range(len(Time)):
#     if Choice[i]=='leave':
#         tree.append(TreeNo[i])
#         trees2=TreeNo[i]
#         rew.append(Rew[i])
#         rew2.append(Rew[i])
#         envi.append(env)
#         Leavetime.append(Time[i]-temp)
#         Leavetime2.append(Time[i]-temp)
#         temp=Time[i]

# AvgLeaveTime2=mean(Leavetime2) - 8
# # print("leavetime env2 avg =", AvgLeaveTime1)
# TotalScoreEnv2=sum(rew) - TotalScoreEnv1
# AvgRewardPerTree2=mean(rew2)
# # print("TotalScoreEnv2=", TotalScoreEnv2)

# dict = {'Participant Name': name, 'Participant ID': pid, 'Environment': envi, 'Tree #': tree, 'Leave times': Leavetime, 'Reward': rew} 
     
# df = pd.DataFrame(dict)
# df_name =  "Pdata.csv"
# df.to_csv(df_name)
# print(df)


