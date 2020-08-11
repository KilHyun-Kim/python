# Tuple


# 튜플 만들기
'''
tu = ()
tu = tuple()
튜플은 빈 괄호이다
변경이 불가능 하다
'''

# 튜플 인덱스


# 튜플 활용

'''
tu = ('a','b','c')
tu.index('c')
'b' in tu
len(tu)
tu.count('a') // 개수 세기

'''


# 변수 할당하기
'''
num = (5,7,9)
n1,n2,n3 = num  
개수를 딱 맞춰서 대입해줘야함

'''


# 값 교환하기
'''

a = 'hello'
b = 'world'
(a,b) = (b,a)
값 교환시 다른 변수를 할당해주지 않아도 간단하게 교환 가능
'''

# 리스트 -> 튜플
'''

li = [ . . . ]
tuple(li)
'''
# 튜플 -> 리스트
'''
tu = ('a','b','c')
list(tu)

'''


### set ###

# 세트 만들기

'''
se = set()
se = {} # 사용 불가능
'''

# 세트 특징 ( 순서, 중복 없음 )
'''
a = { 1, 4, 6, 8 }
b = { 2,4, 1,2,3}
따라서 , index 값은 불러올 수 없음
'''


# 세트 활용

'''

add 추가하기
remove 삭제하기
1 in a 확인하기
len(a) 길이
sum(a) 합
min(a) 최소값
max(a) 최대값

list(a) 리스트로 변환
tuple(A) 튜플로 변환

'''

# 세트만의 활용
'''
 a = { 1,2,3 }
 b = { 2,3,4 }

 a&b   # 교집합
 a|b   # 합집합
 a-b   # 차집합
 a^b   # 대칭 차집합

 이러한 변화가 가능하다.
'''


### Dictionary ###

# 특징
'''
 dic = { 키:값 , 키:값, 키:값 }

'''

# 딕셔너리 만들기

'''
 dic = {}
 dic = dict()
'''

# 딕셔너리 특징

'''
index를 가져올때 순서를 넣는것이 아니라, 키값을 넣어줘서 확인할 수 있다.

dic = {'kor':80, 'eng': 90 , 'mat': 77 }
print(dic['kor'])

'''

# 딕셔너리 활용

'''
del dic['mat']  # 삭제하기
dic.clear()     # 전체 삭제
'eng' in dic    # 확인하기 ( 키 기준 )
len(dic)        # 전체 개수

dic.keys()      # 모든 키 얻기
dic.values()    # 모든 값 얻기
dic.items()     # 모든 순서쌍 얻기

tuple(dic)
list(dic)
set(dic)
# 위의 세개를 사용할 경우 키값만 가져올 수 있다. values 값을 원할경우 dic.values()를 사용한 후 넣는다


# 딕셔너리로 만들기

li = [ 'ab', 'cd' , 'ef' ]
dict(li)
 => li = { 'a':'b', 'c':'d', 'e':'f' }
이런식으로 되는데
순서쌍의 개수가 안맞을경우 에러를 반환하게 된다.
'''
