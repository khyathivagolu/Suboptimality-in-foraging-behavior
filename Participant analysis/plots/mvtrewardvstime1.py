import numpy as np
import matplotlib.pyplot as plt
import random
import pandas as pd

plt.style.use('seaborn-darkgrid')

dfi = pd.read_csv('alldata.csv')

AvgLeavingTimeEnv1 = dfi["AvgLeavingTimeEnv1"].to_list()
AvgLeavingTimeEnv2 = dfi["AvgLeavingTimeEnv2"].to_list()
Y=[]
env=[]
for i in range(1,38):
    if i<=19:
        env.append(random.randint(0,50))
        Y.append(AvgLeavingTimeEnv1[i-1])
    else:
        env.append(random.randint(100,150))
        Y.append(AvgLeavingTimeEnv2[i-20])


# Artists = ['Georg Solti','','Quincy Jones', 'Alison Krauss', 'Pierre Boulez', '', 'Vladimir Horowitz', '', 'Jay-Z', 'Vince Gill', '', 'Kanye West', '', 'Henry Mancini', '', 'Al Schmitt', 'Bruce Springsteen', 'Paul McCartney', 'Leonard Bernstein', 'Jay David Saks', 'Willie Nelson', '', '']
# noms = [74,79,80,42,67,67,45,72,80,47,46,70,74,72,37,36,50,79,63,53,52,50,50]
# wins = [31,28,28,27,26,25,25,25,23,22,22,22,25,20,20,20,20,18,16,13,10,12,10]
# nvsw = [2.38,2.82,2.85,1.56,2.57,2.68,1.8,2.88,3.47,2.13,2.09,3.18,2.96,3.6,1.85,1.8,2.5,4.39,3.94,4.07,5.2,4.16,5]

# fig = plt.figure(figsize = (8, 6))

# plt.text(noms[1]-3,wins[1]-1,'Beyoncé',fontsize=9)
# plt.text(noms[7]-3,wins[7]-1,'John Williams',fontsize=9)


# for i,type in enumerate(Artists):
#     x = noms[i]
#     y = wins[i]
#     plt.scatter(x, y, s=60, color='white', edgecolor='lightgrey' )
#     plt.text(x+0.5, y+0.5, type, fontsize=9)

plt.scatter(env, Y, s=60, cmap='ocean', edgecolor='lightgrey' )
# plt.scatter(AvgLeavingTimeEnv1, env, s=60, c=nvsw, cmap='ocean', edgecolor='lightgrey' )
plt.xlabel('Nominations')
plt.ylabel('Wins')
plt.title('Artists with most nominations vs most wins')

plt.tight_layout()
# plt.savefig("NomvWin.png", bbox_inches ="tight")

plt.show()
