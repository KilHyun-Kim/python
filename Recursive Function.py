# 재귀 (recursive)
# 재귀는 자기 자신을 호출 하는 것을 말한다.

## 재귀함수 (recursive function)
# 재귀함수는 자기 자신을 호출하는 함수 이다.



## 재귀함수 만들기

# *** 탈출조건, 끝나는 조건이 꼭 들어가야 한다.


arr = [ 7,3,2,9 ]

def sum(arr, accu):
    # arr의 배열이 비었을경우 accu를 반환
    if(len(arr) ==0 ): return accu
   
    # 위의 if에 걸리지 않으면 arr의 값 만큼 계속 재귀하여 함수가 반복됨
    return sum(arr, accu + arr.pop())
  

print('result => ',sum(arr,0))
