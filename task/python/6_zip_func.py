# 3)  두 리스트 [1, 2, 3]과 [10, 20, 30]의 요소들을 짝지어 출력하세요.
# (zip 함수 사용)

# 결과:
# 1 10
# 2 20
# 3 30

a_list = [1, 2, 3]
b_list = [10, 20, 30]

for a, b in zip(a_list, b_list):
    print(f'{a} {b}')