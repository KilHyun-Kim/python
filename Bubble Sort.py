# Bubble Sort

# 알고리즘에서 가장 첫번째로 나오는 알고리즘

'''
핵심로직

1. 첫번째꺼랑 두번째꺼랑 비교해서 두번째가 더 작으면 첫번째랑 자리를 바꿈
2. 
'''

numbers = [ 7, 3, 2, 9, 4]
first = numbers[0] # 7
second = numbers[1] # 3

print(first, second)

print(first > second) # true

# 자리바꾸기

first, second = second , first
print(first, second)



def bubbleSort(arr):
    for j in range(0,len(arr)-1):
        for i in range(j+1,len(arr)):
            if arr[j] > arr[i]:
                arr[j],arr[i] = arr[i], arr[j]
    return arr

result = bubbleSort(numbers)

print(result)
