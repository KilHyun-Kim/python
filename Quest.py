# 탐색

# 선형 탐색

'''

li = [1,6,4,2,3,10,8,7,5,9]
n = int(input('1~10'))

for i in range(len(li)):
    if li[i] == n:
        print(i)    # 몇번째에 존재하는지 index 값을 반환
        break
'''


# 이진 탐색

# 중간값을 기준으로 작고 큼을 비교함으로 탐색하는 방법

'''
li = [1,3,5,6,8,9,13,15,17,19]
n = int(input('1,3,5,6,8,9,13,15,17,19'))

s_index = 0
e_index = len(li) - 1

while s_index <= e_index:
    m_index = (s_index + e_index) // 2
    if n <li[m_index]:
        e_index = m_index -1
    elif n > li[m_index]:
        s_index = m_index + 1
    else:
        print(m_index)
        break
'''
