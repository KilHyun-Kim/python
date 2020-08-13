# 중첩 for 문



# 주사위


'''
a = int(input('a:'))
b = int(input('b:'))

for i in range(1,a+1):
    for j in range(1,b+1):
        print(i,j)
'''

# 구구단
'''
for i in range(2,10):
    for j in range(1,10):
        print('{}*{}={}'.format(i,j,i*j))
    print()
'''

# 행렬 만들기

'''
li = [[1,2,3,4,],[5,6,7,8]]

for i in range(len(li)): # 2 i = 0,1
    for j in range(len(li[i])): # 4 j = 0, 1, 2, 3
        print(li[i][j], end=' ')
    print()
'''
