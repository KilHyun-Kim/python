# 가장 많이 등장하는 알파벳의 개수 구하기
# Ex) mouse => 1, test => 2, hello => 2

# high_frequency_letter

word = "aaabbc"

def highFrequencyLetterCount(word):

    values = {}
    for alphabet in word:
        # word 길이만큼 시행 (for)
        # values 딕셔너리에 키값을 word의 alphabet으로 주고 None일경우에 1값을 추가해준다.
        # 1이 아닐경우에 +1 씩 올려주어서 알파벳 개수에 따라서 값을 추가해준다.
         if values.get(alphabet) == None:
            values[alphabet] = 1
         else:
            values[alphabet] += 1
         print("values=>", values)
    # 개수를 저장하기 위한 변수
    maxValue = -1
    for key in values:
        # key 값과 values 값을 확인한후,
        print("key=>", key, "value=>",values[key])
        # values[key] values값과 maxValue값을 비교한뒤
        # 전체적으로 for를 시키면서 제일 큰값을 maxValue에 계속 저장한다.
        if values[key] > maxValue:
            maxValue= values[key]
    # 마지막으로 maxValue에는 개수가 가장 많은 값이 저장되게 된다.
    return maxValue

result = highFrequencyLetterCount(word)

print(result)
