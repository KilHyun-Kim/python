
# 문자열 처리

# 띄어쓰기 없애기

'''
text = input('text')

for i in text:
    if i != ' ':
     print(i,end='')
'''     

# 대소문자 바꾸어 출력하기

'''
text = input('text')

for i in text:
    if i.isupper():
        print(i.lower(),end='')
    elif i.islower():
        print(i.upper(), end='')
    else:
        print(i,end='')
'''

# 이름 찾기

name=['김철수','김영희', '홍길동', '이김놀','최길현']

for i in name:
    if '김' in i:
        print(i)
