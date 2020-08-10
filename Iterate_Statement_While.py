# 반복문 while

'''
while 조건:
 실행 코드

* 조건이 참일때 = 반복실행
* 조건이 거짓일때 = 반복종료

print('a 가 0보다 같거나 크면 실행, 작으면 정지')
a = int(input('a:'))
while a>=0:
 print('실행')
 a = int(input('a:'))

'''

# 무한루프


# n번 반복하기
'''
n = int(input('n:'))

while n:
     print(n)
     n = n-1
     
n 을 0 으로 만들어서 false 가 됐을때 종료하니까 n번 반복된다
'''  

# ~까지 반복하기

# (1) 1~10까지 숫자 반복하기

'''
 n = 1
 while n <= 10 :
  print(n)
  n = n + 1
'''

# (2) yes 를 입력하면 반복하기

'''
text = 'yes'

while text == 'yes':
 text=input('yes 입력 시 반복')

print('종료')

'''

# (3) e 또는 E 가 입력될 때까지 반복하기

'''
text = input('e 또는 E 입력 시 종료')
 while text!='e' and text!='E':
  text = input('e 또는 E 입력 시 종료')
print('종료')

'''
