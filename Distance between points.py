# 좌표평면 두 점 사이의 거리 구하는 알고리즘
import math


a = list(map(int,input("a 점의 좌표를 입력하시오. (x,y)").split()))
b = list(map(int,input("b 점의 좌표를 입력하시오. (x,y)").split()))


def distancePoints(a,b):
    d = math.sqrt(math.pow((a[0]-b[0]),2)+math.pow(a[1]-b[1],2))
    return d 
value = distancePoints(a,b)
print(value)
