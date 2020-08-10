# 메소드

# .split()
'''
text = input('날짜 입력 yyyy.mm.dd')
y,m,d = text.split('.')
print(text,y,m,d)
'''

# map(함수, 집합 형태-iterable 객체)
# a,b,c = map(int,['1','2','3'])


# map + split Ex
'''
text = input('a b c 값 입력')
text = text.split()
a,b,c = map(int,text)
print(a,b,c, a+b+c)
'''
# a,b,c = map(int,input('a b c 값 입력').split()) 위의 코드와 동일


# 숫자 출력하기
# print(x,'과',y,'의 합은',x+y'이다') not 추천 - 형태에따라 띄어쓰기가 되기때문

# format()
'''
x = 3
y = 5
print('{}과 {}의 합은 {}이다.'.format(x,y,x+y)) - format 활용하여 사용하기
'''

# 산술연산자 메소드

'''
반올림 : round()
절대값 : abs()
제곱 : pow()
나눗셈 : divmod(a,b)
x,y = divmod(7,2)
x에는 몫 , y 에는 나머지
최대값 : max()
최소값 : min()
합 : sum(집합형태:Iterable)
'''
