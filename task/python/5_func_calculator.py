### **5. 함수 이해하기**
# 1)  두 수와 연산자(+, -, *, /)를 인자로 받아 계산하는 calculator 함수를 작성하세요.

def calculator(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b != 0: return a / b
    else:
        return "지원하지 않는 연산자입니다."

print(calculator(1, 4, '+'))