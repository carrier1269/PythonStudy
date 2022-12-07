'''import pandas as pd
import numpy as np

from pandas import Series, DataFrame

df = pd.DataFrame({'name':['이영원','윤성호','이순신','홍길동'],
                   '부서':['개발','제작','연구','개발']})
df2 = pd.DataFrame({'sname':['이갑숙','왕방울','이순신','갑순이'],
                    'proJ':['S','A','B','C']})

df=pd.DataFrame([''])
    
print(df,'\n')
print(df2)'''
import timeit
 
start_time = timeit.default_timer() # 시작 시간 체크



import numpy as np
import pandas as pd
'''
a=np.random.randint(1,10,size=(3,3))

print([a])

df = pd.DataFrame(a,columns=list("ABC"))

#print(df+df.loc[0])
print(df.add(df.loc[0]))
print(df.sub(df.loc[0]))
print(df.mul(df.loc[0]))
print(df.div(df.loc[0]))
print(df.floordiv(df.loc[0]))
print(df.mod(df.loc[0]))
print(df.pow(df.loc[0]))'''

'''dict_data = {"a":1, "b":2, "c":3, "d":4}
indexes = ['a','b','c','d','e','f','g']
obj = pd.Series(dict_data,dtype=np.float32,index=indexes,name="example_data")
print(obj)'''

'''raw_data = {'first_name':['jason','mark','bob'],'second_name':['bush','man','buggie']}
df = pd.DataFrame(raw_data,columns=['first_name','second_name'])
print(df)'''




'''df = pd.read_excel("c:/Users/최가인/Documents/파이썬연습.xlsx")
#con1 = df['영어']>=20
print(df.loc[['학과','이름']])'''

a=np.random.randint(1,10,size=(3,3))
df = pd.DataFrame(a,columns=list("ABCD"))
print(df)
 




































































terminate_time = timeit.default_timer() # 종료 시간 체크  
 
print("%f초 걸렸습니다." % (terminate_time - start_time))