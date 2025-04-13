# 2) **질문**: 1부터 100까지의 숫자 중 3의 배수의 합을 구하세요.
# 결과: 3의 배수의 합: 1683


def multiple_sum(num):
    
    result = sum(i for i in range(1, 101) if(i%num == 0))

    #result = 0
    # for i in range(1, 101):
    #     if(i % num == 0): result += i

    print(f'{num}의 배수의 합: {result}')


multiple_sum(3)