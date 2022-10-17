import numpy as np
import random
import sys

def hit(map, x_0, y_0, R):
    damage = 0
    for y in range(max(y_0 - R, 0), min(y_0 + R + 1, 100)):
        for x in range(max(x_0 - R, 0), min(x_0 + R + 1, 100)):
            if (x - x_0)**2 + (y - y_0)**2 <= R**2:
                damage += map[y, x]
    return damage

# #генерим данные
# n=100
# f = open('trgts.txt','w')
# for i in range(0,n):
#     for j in range(0,n):
#         if random.randint(0,100)==1:
#             f.write (str(i)+' '+str(j)+' '+ str(random.randint(1,100))+'\n')

# f.close()

name = sys.argv[1]
R = int(sys.argv[2])
#R = 10
#name = 'trgts.txt'
map = np.zeros((100, 100))


pts = np.loadtxt(name, int)


for x, y, w in pts:
    map[y, x] += w

coord_x = -1
coord_y = -1
damage_max = 0

for y in range(100):
    for x in range(100):
        damage = hit(map, x, y, R)
        if damage > damage_max:
            damage_max = damage
            coord_x = x
            coord_y = y

print(damage_max, coord_x, coord_y)
