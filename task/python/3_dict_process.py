# 2) **질문**: 
# {"name": "John", "age": 30} 딕셔너리에서 "age"의 값을 출력하세요.
# {"math": 90, "science": 85, "history": 78} 딕셔너리에서 모든 과목명을 출력하세요.
# 딕셔너리 {'apple': 3, 'banana': 5}에서 apple의 값을 2 증가시키세요.

# 결과:  
# 나이: 30
# 과목들: ['math', 'science', 'history']
# {'apple': 5, 'banana': 5}


introduction = {"name": "John", "age": 30}
score = {"math": 90, "science": 85, "history": 78}
fruit = {'apple': 3, 'banana': 5}

print(f'나이: {introduction["age"]}')

print(f'과목들: {list(score.keys())}')
#subject = list(map(lambda i : i, score.keys()))

fruit.update({"apple" : fruit["apple"] + 2})
#fruit.update(apple = fruit["apple"] + 2)

print(fruit)
