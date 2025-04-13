# 1) **질문**: 반지름 5인 원의 넓이를 계산하세요. (공식: 넓이 = π × 반지름², π=3.14)

import math

def calculate_circle(radius):
    area = math.pi * radius ** 2
    print(f'{area:.1f}')

calculate_circle(5)