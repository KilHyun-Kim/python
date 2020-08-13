# 정렬

# Selection Sort (선택적 정렬)

'''
li = [8,6,4,1,2,3,5,10,9,7]

for i in range(len(li)):
    m_index = i
    print(li)
    for j in range(i,len(li)):
        if li[j] < li[m_index]:
            m_index=j
    li[i],li[m_index] = li[m_index],li[i]
'''





# Bubble Sort (버블 정렬)

li = [ 8,6,4,1,2,3,5,10,9,7 ]

for i in range(len(li)):
    print(li)
    for j in range(len(li)-i-1):
        if li[j] > li[j+1]:
            li[j],li[j+1] = li[j+1], li[j]
