'''def solution(num1, num2):
    answer = 0
    answer = num1 - num2
    
    return answer'''
'''def solution(num1, num2):
        answer = num1/num2
    return int(answer)'''
'''def solution(num1, num2):
    answer = 0
    answer = num1 * num2
        return answer'''
'''def solution(num1, num2):
        if num1 == num2:
        return 1
    else:
        return -1'''
'''def solution(num1, num2):
        answer= num1%num2
        return answer'''
'''def solution(age):
    answer = 2022 - age +1
    return answer'''
'''def solution(angle):
    if angle > 0 and angle <90:
        answer = 1
    elif angle == 90:
        answer = 2
    elif angle > 90 and angle < 180:
        answer = 3
    elif angle == 180:
        answer = 4
    return answer'''
'''def solution(n):
    answer = 0
    for x in range(0,n+1):
        if x % 2 == 0:
            answer += x
    return answer'''
'''def solution(numbers):
    a = len(numbers)
    sum = 0
    for x in range(0,a):
       sum += numbers[x]
       answer = sum / a
    return answer'''
'''def solution(num1, num2):
    answer = 0
    answer=int(num1/num2*1000)
    return answer
def solution(array, n):
    answer = 0
    for x in array:
        if x == n:
            answer += 1
            
    return answer
def solution(n, k):
    a = int(n/10)
    b = k-a
    answer = n*12000+b*2000
    return answer
def solution(array, height):
    answer = 0
    for x in array:
        if x > height:
            answer += 1
    return answer
def solution(message):
    answer = len(message)*2
    return answer
def solution(n):
    a=n/7
    answer=0
    if a == int(a):
        answer = a
    else:
        answer = int(a)+1
    return answer
def solution(num_list):
    answer = []
    even = 0
    odd = 0
    for x in num_list:
        if x % 2 == 0:
            even += 1
        else:
            odd +=1
    answer = [even,odd]
    return answer
def solution(num_list):
    answer = list(reversed(num_list))
    return answer
def solution(strlist):
    answer = []
    for x in strlist:
        answer.append(len(x))
    return answer
def solution(slice, n):
    answer = 0
    a = n / slice
    if a == int(a):
        answer = a
    else:
        answer = int(a)+1
    return answer'''
'''def solution(my_string):
    answer = ''
    answer = my_string[::-1]
    return answer
def solution(numbers):
    answer = 0
    a = sorted(numbers, reverse = True)
    answer = a[0]*a[1]
    return answer
def solution(money):
    answer = []
    a = int(money / 5500)
    b = money - (a*5500)
    answer.append(a)
    answer.append(b)
    return answer
def solution(numbers, num1, num2):
    answer = []
    for x in range(num1,num2+1):
        answer.append(numbers[x])
    return answer
def solution(numbers):
    answer = []
    for x in numbers:
        answer.append(x*2)
    return answer
def solution(numbers):
    answer = []
    for x in numbers:
        answer.append(x*2)
    return answer
def solution(dot):
    answer = 0
    x = dot[0]
    y = dot[1]
    
    if x > 0 and y>0:
        answer = 1
    elif x > 0 and y<0:
        answer = 4
    elif x < 0 and y > 0:
        answer = 2
    elif x < 0 and y < 0:
        answer = 3
    return answer
def solution(my_string, letter):
    answer = ''
    for a in my_string:
        if a != letter:
            answer += a
    return answer
def solution(str1, str2):
    answer = 0
    if str2 in str1:
        answer = 1
    else:
        answer = 2
    return answer
def solution(sides):
    answer = 0
    a = sorted(sides,reverse = True)
    if a[0] < a[1] + a[2]:
        answer = 1
    else:
        answer = 2
    return answer
def solution(price):
    answer = 0
    if price < 100000:
        answer = price
    elif price >= 100000 and price < 300000:
        answer = price - price/100*5
    elif price >= 300000 and price < 500000:
        answer = price - price/100*10
    elif price >= 500000:
        answer = price - price/100*20
    return int(answer)
def solution(n):
    answer = []
    for x in range(1,n+1):
        if x % 2 == 1:
            answer.append(x)
    return answer
def solution(n):
    answer = 0
    a = str(n)
    for x in range(len(a)):
        answer += int(a[x])
        
    return answer
import math

def solution(n):
    answer = 0
    a = math.sqrt(n)
    if a == int(a):
        answer = 1
    else:
        answer = 2
    return answer
def solution(num):
    answer = ''
    if num % 2 == 0:
        answer = "Even"
    else:
        answer = "Odd"
    return answer
def solution(n):
    answer = 0
    for x in range(1,n+1):
        a = n/x
        if a == int(a):
            answer += a
    return answer
import numpy as np
def solution(arr):
    answer = 0
    a = np.array(arr)
    answer = np.mean(a)
    return answer
def solution(n):
    answer = 0
    a = str(n)
    for x in range(len(a)):
        answer += int(a[x])
    return answer
def solution(n):
    answer = []
    a = str(n)
    b = a[::-1]
    for x in range(len(a)):
        answer.append(int(b[x]))
    return answer'''
import math

def solution(n):
    answer = 0
    a = math.sqrt(n)
    if a == int(a):
        answer = (a+1)**2
    else:
        answer = -1
    return answer
def solution(s):
    answer = True
    a = 0
    b = 0
    for x in s:
        if x == 'p' or x == 'P':
            a += 1
        elif x == 'y' or x == 'Y':
            b += 1
    if a == b:
        return True
    else:
        return False
    return True
def solution(x):
    answer = True
    a = str(x)
    sum = 0
    for y in range(len(a)):
        sum += int(a[y])
    if x % sum == 0:
        return True
    else:
        return False
    return answer
def solution(x, n):
    answer = []
    for a in range(1,n+1):
        answer.append(a*x)
    return answer
def solution(n):
    answer = 0
    a = list(map(int,str(n)))
    b = sorted(a,reverse = True)
    c = [str(i) for i in b]
    d = "".join(c)
    answer = int(d)
    return answer
def solution(n):
    answer = 0
    a = []
    for s in range(1,n+1):
        a.append(s)
    for x in a:
        if n % x == 1:
            answer = x
            break
    return answer
def solution(n):
    answer = 0
    for x in range(1,n+1):
        if n % x == 1:
            return x
            break
