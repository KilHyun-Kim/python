# StringTokenizer 만들기

## 토큰(Token)이란?
# 프로그램에서 다루는 최소 단위

## Tokenize란?
# 가장 작은 단위로 나누어 주는 일을 하는게 토크나이저.

## 왜 나누느냐?

# 나눠서 처리 해야하기 때문

## StringTokenizer란?
# 스트링을 나누어 주는 로직이 스트링 토크나이저 이다.


string = '1+2*(3-4)'
string2 = "13+24*(15-46.76)"
# 숫자와 괄호를 분리 해주는 식

def stringTokenizer(string, deli):

    # 1. 들어온 string 값을 원소들을 하나하나를 리스트에 원소로 넣는다.
    # -> [ "1", "+", "2", "*" ... ]
    # 2. 값이 두자리 수이거나 소수점일경우에도 하나하나 원소만을 넣기때문에
    # -> 단순 for로 append는 맞지않다.
    result = []
    accu = ""
    for chr in string2:
        # 특정 기호가 있을경우 result에 추가하는 로직 
        if chr in deli:
            # accu 가 공백이 아닐경우에만 result에 추가해주고 accu를 초기화 시킨다.
            if accu !="":
                result.append(accu)
                accu = ""
            result.append(chr)
        else:
            accu = accu + chr
            
    return result

# delimiter 값을 줌으로써 구분지을 연산자를 추가해줄 수도 있다.
result = stringTokenizer(string,"+-*/(){}^")
print(result)
