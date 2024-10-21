import numpy as np
import matplotlib.pyplot as plt
import math as m

file1 = open("data.txt", "r")
data = file1.readlines()
file1.close()
max_x=0
min_x=0
max_y=0
min_y=0
lines=0
for line in data:
    k=list(map(float,line[0:-1].split(" ")))
    if (lines%2 == 0):
        max_x=max(max_x, max(k))
        min_x=min(min_x, min(k))
    else:
        max_y=max(max_y, max(k))
        min_y=min(min_y, min(k))
    lines+=1
cols = 2
rows = m.ceil(lines/4)
print(min_x, max_x, min_y, max_y)

f=open("data.txt","r")
axis = plt.figure(figsize=(10,8),constrained_layout=True).subplots(rows, cols)
for i in range (lines//2):
    x=list(map(float,f.readline()[0:-1].split(" ")))
    y=list(map(float,f.readline()[0:-1].split(" ")))
    axis[i//2, i%2].grid(which='minor', linewidth=0.3, linestyle='--')
    axis[i//2, i%2].minorticks_on()
    axis[i//2, i%2].grid()
    axis[i//2, i%2].set_xticks(np.linspace(round(min_x), round(max_x-1), 4))
    axis[i//2, i%2].set_yticks(np.linspace(round(-10), round(10), 11))
    axis[i//2, i%2].axis([min_x-1, max_x+1, min_y-1, max_y+1])
    axis[i//2, i%2].plot(x, y)
    axis[i//2, i%2].set_title("График № %i " %int(i+1))
plt.savefig('task2.png')
plt.show()

