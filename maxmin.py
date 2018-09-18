import random
ls=[]
for j in range(10):
    szam=random.randint(1,100)
    ls.append(szam)
max=ls[0]
min=ls[0]
for i in ls:
    if i>max:
        max=i
    elif i<min:
        min=i
print(ls)
print('Min=',min)
print('Max=',max)