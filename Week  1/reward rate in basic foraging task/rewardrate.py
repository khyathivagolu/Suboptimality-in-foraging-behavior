
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-darkgrid')

x = np.arange(0,15)

y1 = np.array([7.07,6.56,5.91,5.35,5.2,4.76,4.31,3.92,3.42,2.89,2.4,1.72,1.06,0.13,0])
y2 = np.array([6.57,5.9,5.62,5.1,4.57,3.99,3.11,2.14,1.36,1.16,0.75,0.26,0,0,0])
y3 = np.array([7.2,6.7,5.99,5.08,4.46,3.98,3.32,2.77,1.97,1.36,0.95,0.39,0,0,0])
y4 = np.array([7.06,6.92,6.25,5.52,5.1,4.43,3.88,3.35,2.98,2.25,1.29,0.98,0.23,0,0])
y5 = -x*(7/14) + 7


fig = plt.figure(figsize = (8, 6))

plt.plot(x, y1, marker='o', linewidth=1, label='Round 1, Bush 1')
plt.plot(x, y2, marker='o', linewidth=1, label='Round 1, Bush 2')
plt.plot(x, y3, marker='o', linewidth=1, label='Round 2, Bush 1')
plt.plot(x, y4, marker='o', linewidth=1, label='Round 2, Bush 2')
plt.plot(x, y5, marker='o', linewidth=4, label='Linear reference')


plt.xlabel('trial no.')
plt.ylabel('reward value')
  

plt.title('Trends in reward values in the foraging task')

plt.legend()

plt.tight_layout()
plt.savefig("View.png", bbox_inches ="tight")
plt.show()

