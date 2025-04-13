#4) 구구단 3단을 출력하세요.

def gugudan(num):
    for i in range(1,10):
        print(f'{num} x {i} = {num*i}')
    
    # 방법 2
    #print("\n".join([f'{num} x {i} = {num*i}' for i in range(1, 10)]))

    # 방법 3
    #print("\n".join(map(lambda i: f'{num} x {i} = {num*i}', range(1, 10))))


gugudan(3)