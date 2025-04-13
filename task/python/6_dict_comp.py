# 5)   ["apple", "banana", "cherry"]에서 각 단어의 길이를 딕셔너리로 만드세요. (딕셔너리 컴프리헨션 사용)

# 결과: {'apple': 5, 'banana': 6, 'cherry': 6}

fruits = ["apple", "banana", "cherry"]
result = {f: len(f) for f in fruits}
print(result)