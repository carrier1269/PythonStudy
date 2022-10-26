import numpy as np
from functools import reduce
'''
class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return ("my_dog의 이름은 {}이고, 나이는 {}살입니다.".format(self.name,self.age))
    

persons = [('GilDong','Hong',27),('Sunsin','Lee',46),('Yusin','Gim',34)]

print(sorted(persons,key=lambda info:info[2]))

lyrics = 'Half of my hear is in Havana'
sp = lyrics.split()
print(sp[0].upper())

for x in sp:
    print("('{}','{}')".format(x,x.upper()),end=' ')
print("\n")
n_list = [44, 66, 34, 24, 144, 98, 38, 568, 234, 345]

a = [x for x in n_list if x % 12 == 0]
print("new_list",a)

b = list(filter(lambda x : x%12==0, n_list))
print(b)'''
'''
new_list = []
n_list = [ -22.3, 29.44, 902.2, 45.7, -887.1, -56.3]

b= [x for x in n_list if x>0]
c= list(filter(lambda x : x>0, n_list))

print(b)

#for x in c:
#    print(x)
#    new_list.append(x)
#print(new_list)

def app(x):
    return x

new_list = list(map(app,c))
print(new_list)

'''
'''
n_list = [-22.3, 29.44, 902.2, 45.7, -887.1, -56.3]

max = max(n_list)
min = min(n_list)

print("최댓값 : {}".format(max))
print("최솟값 : {}".format(min))

def my_max(x):
    max1 = n_list[0]
    for x in n_list:
        if max1 < x:
            max1 = x
    return max1
def my_min(x):
    min1 = n_list[0]
    for x in n_list:
        if x < min1:
            min1 = x
    return min1

print("최댓값 : {}".format(my_max(n_list)))
print("최솟값 : {}".format(my_min(n_list)))
''''''
new_list = []

for x in range(1,101):
    if x % 6 == 0:
        new_list.append(x)
print(new_list)

new_list1 = list(filter(lambda x : x%6==0,range(1,101)))
print(new_list1)

new_list2 = [x for x in range(1,101) if x%6==0]
print(new_list2)'''

'''new_list = []

for x in range(1,101):
    if x%6 == 0 and x%7==0:
        new_list.append(x)
print(new_list)

new_list1 = list(filter(lambda x : x%6==0 and x%7==0,range(1,101)))
print(new_list1)

new_list2 = [x for x in range(1,101) if x%6==0 and x%7==0]
print(new_list2)'''


'''a = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
n_list = []
for x in a:
   new =  x.title()
   n_list.append(new)
print(n_list)'''

'''fruits = {'Apple':'사과', 'Strawberry':'딸기', 'Peach':'복숭아', 'Grape':'포도'}

n_list=[]
for x,y in fruits.items():
    a = str('{} = {}'.format(x,y))
    n_list.append(a)

def dtol(x,y):
    return str('{} = {}'.format(x,y))

print(n_list)

n_list1 = list(map(dtol,fruits.items()))

print(n_list1)'''

'''org_list = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(org_list.flatten())'''

