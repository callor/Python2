'''
Created on 2017. 8. 24.
Exec Module
@author: callor
'''
# Exec Module
#     실제 작업을 진행하는 module
#     함수, 스크립트문, 변수들이 선언되고 사용되는 곳
#
# 모듈에 포함된 모둔 함수를 import
from modules01.FunDev import *

# FuncDev에 선언되어 있는
# __name__ 의 내용이 현재파일이름인 "modules01.FuncDev"으로 변경
# FunDev에 포함된 함수중 f1을 호출

# 스크립트
print(f1(10,20))

# paramF 함수를 호출하면서
# 3개의 매개변수를 보낸다.
# 2개는 일반 숫자형 변수이고
# 1개는 list ( Collection, Array ) 변수를 보냈다.
num1 = 10
num2 = 20
list = [1,2,3,4,5,6,7,8,9,0,"A"]

print("함수 호출전 변수 값들")
print(num1)
print(num2)
print(list)
print(num1,num2,list)
print("---------------------")

paramF(10,20,list)

# 일반변수(숫자, 문자열)는 함수내부에서 값을 변경해도
# 원본 변수내용은 변하지 않는다
#     immutable
print("함수 호출후 변수 값들")
print(num1)
print(num2)

# Array들은 함수내부에서 변경(append,del, update) 되면
# 원본의 내용도 변경이 되어 버린다.
#     mutable
print(list)
print(num1,num2,list)
print("--------------------")

# 모듈중에서 필요한 함수만 import
from modules01.FunDev import f2
 
  
