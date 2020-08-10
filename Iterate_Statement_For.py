# 반복문 for 

'''
 for 변수 in 열거형 :
  실행 코드

열거형 데이터를 하나씩 변수 값에 대입하며 실행
'''

'''
 range 함수
  숫자의 범위와 증감값을 정하며
  규칙적인 수들의 집합으로 만들어주는 함수
  
'''

# for  문
'''
for i in range(10):
    print(i)
'''

# 1에서 n까지 출력

'''
n = int(input('n:'))
 for i in range(1,n+1):
     print(i)
'''

# a 에서 b 까지 출력
'''
a,b = map(int,input('a,b:').split())

for i in range(a,b+1)
    print(i)
'''

# n에서 0까지 출력
'''
n=int(input('n:'))

for i in range(n,-1,-1)
    print(i)
    
