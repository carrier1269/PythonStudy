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

'''numbers = [2,8,6,4,3,1,4,6,2]

def first_odd(numbers):
    a = sorted(numbers)
    for x in a:
        if(x != 1 and (x-1)%2==0):
            return x
            break

print('처음으로 나타나는 홀수는 :', first_odd(numbers))'''

'''numbers = [1,2,3,4,5,6,7,8,9,10,12,14,16]

def reverse_generator(numbers):
    a = sorted(numbers,reverse=True)
    for x in a:
        yield x

for num in reverse_generator(numbers):
    print(num, end=' ')

for a in reverse_generator(numbers):
    if((a-1)%2 == 0):
        print(a) 
        break'''

'''print(np.array([0, 0, 0, 0, 0 ,0, 0 ,0 ,0 ,0]))
print(np.zeros(10))'''
'''
a = np.array([23,45,67,7,2,30,34,82])
print("최댓값 : {}".format(a.max()))
print("최솟값 : {}".format(a.min()))
print("평균값 : {}".format(a.mean()))

b = np.random.randint(0,100,size = 10)
print("b = {}".format(b))
print("최댓값 : {}".format(b.max()))
print("최솟값 : {}".format(b.min()))
print("평균값 : {}".format(b.mean()))

print(type(a))
print(type(b))

''''''

a = np.arange(1,11)
print(a)
b=sorted(a,reverse=True)
print(b)
c=np.array(b).reshape(2,5)
print(c)
d=c.reshape(5,2)
print(d)
'''
'''
a = np.arange(1,17).reshape(4,4)
print(a)

b = np.random.rand(10)
print(b)
print(b.max())
print(b.min())
print(b.mean())'''

'''n = int(input("n을 입력하시오 :"))
d = np.arange(1,n*n+1).reshape(n,n)%2
print(d)
d[1:3,1:3] = 0
print(d)
'''
'''n = int(input("2이상의 수 n을 입력하시오 :"))
d = np.ones((n,n))
d[1:-1,1:-1] = 0
print(d)

b = d[0:2,:]
print(b)
'''
a = np.array([1,2,3,4,5,6,7])
print(a[::-2])