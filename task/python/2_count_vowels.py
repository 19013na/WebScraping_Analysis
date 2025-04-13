# 4) **질문**: "Python is awesome"에서 모음(a, e, i, o, u)의 개수를 세세요.
# 결과: 모음 개수 : 6

def count_vowels(sentence):
    # for i in sentence:
    #     if i in 'aeiou':
    #         count += 1

    count = sum(map(lambda i: i in 'aeiou', sentence))

    print(count)

count_vowels("Python is awesome")