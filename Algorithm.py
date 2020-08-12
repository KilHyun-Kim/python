# Argorithm

'''
1) 합 구하기
# 숫자 n을 입력받아 1~n 까지 합 구하기

n = int(input('n:'))
s = 0

for i in range(1,n+1):
    s = s + i

print(s)
'''

'''

2) 곱 구하기

# 숫자 n 을 입력받아 1~n 까지 곱 구하기


n = int(input('n:'))
s = 1

for i in range(1,n+1):
    s = s * i

print(s)

3) 숫자 누적하기

# 0 을 입력할때까지 반복해서 숫자를 입력받아 합 구하기

n = int(input('n값을 입력하시오 0 을 넣을 시 '))
s=0

while n:
    s= s + n
    print(s)
    n= int(input('n값을 입력하시오 0 을 넣을 시 끝'))

'''

# 약수와 배수 판별
'''

# 숫자 a,b를 입력받아 b가 a의 약수인지 확인하기 (a>=b)

a = int(input('a:'))
b = int(input('b:'))
if a>=b:
    if a%b == 0:
        print('약수입니다')
    else:
        print('약수가 아닙니다')
else:
    print('a가 b보다 작습니다')

'''

# 약수 구하기

'''
n = int(input('n:'))
s = []
for i in range (1,n+1):
    if n%i == 0:
        s.append(i)
print(s)
'''

# 배수 구하기
'''
n = int(input('n:'))
s = []
for i in range(1,101):
    if i%n ==0:
      s.append(i)
print(s)
'''


# 문자 체크

# 긴 문장(text)과 한 문자 (t)를 입력받아
# t가 text안에 포함되어 있는지 확인하기
'''
text= input('text:')
t = input('t:')

check = False
s = 0
for i in text:
    if i == t :
        check = True
        s += 1
print(s)
'''
# 숫자 체크
# 5개의 숫자를 입력받아 리스트를 만들고
# n을 입력받아 리스트 값에 n이 있는지 확인

'''
num = list(map(int,input('5개의 숫자를 입력해주세요.').split()))
n = int(input('확인할 값'))
check = False

for i in range(0,len(num)):
    if num[i] == n:
        check = True
        break
if check:
    print('존재')
else:
    print('없습니다')
'''



# 개수 구하기

# 약수의 개수 구하기
# n을 입력받아 n의 약수의 개수 구하기

'''
n = int(input('n:'))

li = []

for i in range(1,n+1):
    if n%i == 0 :
        li.append(i)
print(len(li))
'''

# O X 개수 구하기
'''
n = list(input('text:'))

print(n.count('o')) # 사용하면 됨

o_count = 0
x_count = 0

for i in n:
    if i=='o':
        o_count += 1
    elif:
        x_count += 1
print(o_count)
print(x_count)
'''

# 평균 이상 개수 구하기
# 여러개의 숫자를 입력 받아 평균을 구하고
# 평균 이상의 숫자 개수 구하기

num = list(map(int,input('num:').split()))

avg = sum(num)/len(num)

check = 0

for i in num:
    if i>= avg:
        check += 1

print(avg)  # 평균값
print(check)# 평균보다 큰 숫자의 개수



