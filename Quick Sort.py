
# 정렬 - 버블, 선택, 삽입, 병합, 퀵정렬

# 퀵정렬

'''
하나의 리스트를 피벗(pivot)을 기준으로 두 개의 비균등한 크기로 분할하고
분할된 부분 리스트를 정렬한 다음,
두 개의 정렬된 부분 리스트를 합하여 전체가 정렬된 리스트가 되게하는 방법
'''

numbers = [ 40,35,27,50,75 ]

def quickSort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [ number for number in array[1:] if number <= pivot]
        greater = [ number for number in array[1:] if number > pivot ]
        return quickSort(less) + [pivot] + quickSort(greater)
# return 에서 quickSort를 재귀함수로 걸어주어 계속해서 결과를 만족할 때까지 함수를 동작시켜준다.

result = quickSort(numbers)
print(result)

