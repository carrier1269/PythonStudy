'''def solution(arr, divisor):
    lst = []
    for x in range(len(arr)):
        if arr[x] % divisor == 0:
            lst.append(arr[x])
    answer = sorted(lst)
    if len(answer) != 0:
        return answer
    else:
        return [-1]'''

'''a = [3,4,1]
print(a.index(3))


def solution(cost, x):
    count = 0
    lst =[]
    countlst = [False] * len(cost)
    
    for a in cost:
        if countlst[cost.index(a)] == True:
            continue
        print("x = {}".format(x))
        print("a = {}".format(a))
        x = x-a
        print("수식 후 x {}".format(x))
        count += 2 ** cost.index(a)
        print("cindexa {}".format(cost.index(a)))
        countlst[cost.index(a)] = True
        print(countlst)
    return count

print(solution(a,8))'''
'''x=5
y=8
z=3
lst = []
for x in range(x,y+1):
    lst.append(x)
print(lst[0])
k = (lst.index(x) + lst.index(y) +z)/2
print(k)

if k != int(k):
    print('no')
else:
    print("yes")

print(lst)
print(type(lst.index(8)))





def solution(x, y, z):
    lst = []
    if x > y:
        x,y = y,x
    for x in range(x,y+1):
       lst.append(x)
    k = (lst[0]+lst[len(lst)-1]+z)/2
    
    if k != int(k):
        return -1
    else:
        return int(k)'''

a = [2,3,-1,0,-1]
b = str(a)
x = b.replace('-1','0')
print(x)
print(type(a[0]))
print(type(int(x[0])))