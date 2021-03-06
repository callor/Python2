'''
Created on 2017. 8. 22.
@author: callor
'''
'''
산술연산자, 논리연산자 
    ALU : Arithmetic Logic Unit
    
관계연산자, 비교연산자, 논리연산자를 이용해서
프로그램의 흐름을 변경하는 목적
'''
x = 3

# x 가 10 이하이면
if x <= 10 :
    print("맞다")
else :
    print("틀리다")

# x 가 10 미만이면    
if x < 10 :
    print("x는 한자리 숫자 입니다")

# x가 10 이상이고, x 100 미만인가?
if x >= 10 and x < 100 :
    print("x는 두자리 숫자 입니다")
    
if x > 100 or x < 1000 :
    print("모든 범위 숫자")
    
if x != 10 :
    print("x는 10이 아니다")
    
'''
만약 x 값이 1이면 곱셈연산을 하고
    아이면 덧셈연산을 하는 코드
'''
a = 3
b = 4

# 반복문 내에서나 코드상의 어떤 흐름이
# x 값이 1인경우를 건너 뛰는경우가 발생할수도 있다라고 가정
if x == 1 :
    print(a * b)
else :
    print(a + b)

# 위 코드보다 다소 안전한 코드    
if x != 1 :
    print(a + b)
    print(a / b)
else :
    print(a * b)

# 한줄로 쓰기
# if 문 다음에 다른 statement 가 한줄만 필요할때
if x == 1 : print(a * b)

# 다중 선택문
if x == 1 : print(a * b)
elif x == 2 : print(a / b)
elif x == 3 : print(a + b)
else : print("없음")

if x == 9 :
    pass # 아무것도 하지 말고 건너 뛰기
else :
    print(x)











