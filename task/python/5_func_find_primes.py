# 3)  시작값, 끝값을 인자로 받아 그 사이의 소수를 리스트로 반환하는 find_primes 함수를 작성하세요.

def is_prime(num):
    
    return num > 1 and all(num % i !=0 for i in range(2, int(num**0.5)+1))

def find_primes(start, end):
    print([i for i in range(start, end+1) if is_prime(i)])

find_primes(1, 20)


#def is_prime(num):
    # if num < 2:
    #     return False
    # for i in range(2, int(num**0.5) + 1):
    #     if num%i == 0:
    #         return False
    # return True


