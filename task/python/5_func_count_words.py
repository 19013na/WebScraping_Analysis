# 2)  문자열을 인자로 받아 단어 수를 반환하는 count_words 함수를 작성하세요.
# 결과: 단어 수: 5

def count_words(sentence):
    print(f'단어 수: {len(sentence.split())}')

count_words("Hello  python")
count_words("hi hi hi hi")