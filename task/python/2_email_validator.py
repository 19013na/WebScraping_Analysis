
# 3) **질문**: 입력된 이메일 주소가 유효한지 검사하세요. (조건: @와 . 포함)
# 결과: 이메일 주소: user@example.com -> # 유효함
# 이메일 주소: user@example -> # 유효하지 않음


def email_validator(email):
    if email[-4:] == '.com' and '@' in email:
        print("유효함")
    else:
        print("유효하지 않음")

email_validator("user@example.com")
email_validator("user@example")
