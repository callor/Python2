'''
Created on 2017. 8. 24.
@author: callor
'''
'''
모듈은 비슷한 기능들을 모아둔 파일
1. 함수모음
    호출하는 곳에서 import 를 실행하고
    필요에 따라 모듈에 포함된 함수를 호출
    
2. 스크립트 모음
    호출하는 곳에서 import를 실행하면
    실행함과 동시에 모듈의 코드가 실행되는 방식
'''
# 기존 2.x 방식의 import 방식
import modules01.ScDev # 스크립트 테스트 용으로 사용
import modules01.FunDev # 함수를 사용하기 위한 준비

print(modules01.FunDev.f1(10,20))













