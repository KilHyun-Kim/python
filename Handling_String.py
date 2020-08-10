# String Index

'''
text = 'abc'
print(text[-1])
text에서 index 번호를 적을때 양수의경우 정순으로 음수의경우 뒷자리부터 -1로 시작한다.

only integers
'''

# String Slice

'''
text = 'abcde fg hijk'
print(text[0:8:2])

문자열[시작점:끝점+1:구간]
* 음수 가능
* 구간에 -1을 넣을 경우 반대로 출력 text[8:0:-1]  - 사용값 테스트해야함

문자열[시작점:] : 시작점부터 끝까지
문자열[:끝점] : 끝점부터 맨앞까지
문자열[:] : 전체 불러오기
문자열[::-1] : 문자를 거꾸로 전체 출력
'''

# String Method


# 출력 지정 : format(a,b,c...)
'''
text = 'abcde {} {}'
print(text.format('ABC', 123)
'''

# replace(a,b)
'''
replace(대체할곳, 대체할값)
'''

# split(a)
'''
text = 'abcde A/B/C A.B.C
a,b,c = text.split('나눌곳의 기준')
'''

# join()
'''
text = 'abcde'
print('/'.join(text))
값 하나하나에 /를 추가함 a/b/c/d/e
'''

# count(a)
'''
개수를 알 수 있음
text.count('갯수 확인할값')
'''

# strip(a) / lstrip(a) / rstrip(a)

'''
아무값을 넣지 않을경우 공백을 제거한다
strip(a) : a 값을 양쪽에 모두 제거한다
lstrip(a) : a 값을 왼쪽에 모두 제거
rstrip(a) : a 값을 오른쪽에 모두 제거
'''

# 인덱스 찾기 find(a) / rfind(a) / index(a) / rindex(a)
'''
1. find ?
find(a) : a 를 왼쪽에서부터 찾아서 위치값 반환
rfind(a) : a 를 오른쪽에서부터 찾아서 위치값 반환
없는것을 찾을 경우 -1을 return (index와 차이점)

- 맨처음 값을 찾았을 경우 하나만 찾고 끝
2. index ?
index(a) : a 를 왼쪽에서부터 찾아서 위치값 반환
rindex(a) : a 를 오른쪽에서부터 찾아서 위치값 반환
없는것을 찾을 경우 error 를 return (find와 차이점)

- 맨처음 값을 찾았을 경우 하나만 찾고 끝
'''


# 확인하기 isalpha() / isdigit() / isalnum() / isupper() / islower()

'''
isalpha ?
isdigit ?
isalnum ?
isupper ?
islower ?
'''


# 대/소문자 만들기 upper() / lower()

# 0 채우기 : zfill()
'''
앞쪽에 0을 채워야할 경우 사용
.zfill(채워야할 자리수)
'''
