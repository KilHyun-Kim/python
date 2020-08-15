# 단순 탐색 (Simple Search)
# 앞에서부터 원하는게 나올 때까지 하나하나 찾는다.

# 장점
# 만들기 쉽다.
# 정렬이 안되어있어도 된다.

# 단점
# 느리다
# 0(n)
# 10억개 최대 10억번

## 대안
# 이진탐색 (Binary Search)
# 0(log n)
# 10억개 - 2x번

arr = [ 1,2,3,4,5,6,7,8,9,10,11 ]

# 입력받은 숫자가 몇번째 인덱스에 있는지 찾는 Function 만들기

def simpleSearch(arr, targetNum):
    for i in range(0,len(arr)):
        if targetNum == arr[i]:
            return i
    return -1

print(simpleSearch(arr,8))
