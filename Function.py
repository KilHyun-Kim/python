# 함수?

'''
프로그램을 짤 때 효율을 높이기 위해서
특정 기능을 미리 만들어두고 이름을 붙여 사용
'''

# 함수 정의하기   인자값 / 리턴값
'''
def aa():
    print('hi');

def bb(x):   - arguments를 지정할 수 있음
    for i in range(x):
      print('hello')

def cc():    - input 으로 값을 받아서 사용할 수 있도록.
    n=int(input('n:'))
    print(n*2)
    return n*2
        
def dd(x,y):
    print(x*y)
    return x*y

'''


# 함수 호출하기



# *** 내장 모듈 ***
'''
python 에서 기본적으로 제공하는 기능
함수들을 모아서 묶어놓은 개념이라고 생각

'''

# math

'''
import math
math.ceil(2.1)
math.floor(2.1)
math.factorial(10)
math.sqrt(4)
math.pi

'''

# random

'''
import random

random.randint(1,5)  # 범위 내의 정수 랜덤값 생성
random.random()      # 0<= n <1 랜덤값 생성

li = ['a','b','c','d','e']
random.choice(li)    # 리스트 값 중 하나 랜덤 뽑기
random.sample(li,3)  # 리스트에서 랜덤 n개 뽑기
random.shuffle(li)   # 리스트 순서 랜덤 섞기

'''
