# 2)  [10, 20, 30, 40, 50]에서 30보다 큰 수만 필터링하세요.
# (filter 함수 사용)

# 결과: [40, 50]

#List Comprehension 방식
#print([i for i in [10, 20, 30, 40, 50] if i>30])

# filter 함수 사용 방식
print(list(filter(lambda i : i>30, [10, 20, 30, 40, 50])))
