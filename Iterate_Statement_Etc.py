# 기타 제어문

# continue : 해당 단계만 건너뛰고 다음 단계로 간다
'''
for i in range(1,11):
    if i==5:
        continue
    print(i)
-> 1,2,3,4,6,7,8,9,10
'''

# break : 중간에 빠져나감
'''
for i in range(1,11):
    if i==5:
        break
    print(i)
-> 1,2,3,4
'''

# pass : 아무것도 하지않음

'''
for i in range(1,11):
    if i==5:
        pass
    print(i)
-> 1~10 까지 다나옴 (아무것도 변하지않음)

-> Python 은 다른 언어와 다르게 아무 값을 넣지 않을경우 에러를 반환한다
-> 그리하여 나중에 추가한다던지 할경우 pass를 넣어서 에러를 없애준
'''
