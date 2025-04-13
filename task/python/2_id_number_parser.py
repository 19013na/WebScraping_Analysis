
# 2) **질문**: 주민등록번호 "901212-1234567"에서 생년월일을 추출하세요.
# (형식: "1990년 12월 12일")

def id_number_parser(date):
    year = date[:2]
    month = date[2:4]
    day = date[4:6]

    if date[7] == "1" or date[7] == "2":
        year = "19" + year
    else:
        year = "20" + year

    print(f'{year}년 {month}월 {day}일')


id_number_parser("901212-1234567")