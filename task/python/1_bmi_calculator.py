# 2)  **질문**: 사용자로부터 체중(kg)과 키(cm)를 입력받아 BMI를 계산하세요.

# (공식: BMI = 체중(kg) / (키(m)²))

# 결과: 체중(kg): 70

# 키(cm): 175

# BMI: 22.9

def user_inform(weight, height):
    height_m = height/100
    bmi = weight / (height_m ** 2)
    print(f'{bmi:.1f}')

user_inform(70, 175)