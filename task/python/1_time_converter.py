# 3) **질문**: 12345초를 시간, 분, 초로 변환하세요.

def exchange_time1(second_f):
    hour = second_f // 3600
    second = second_f % 3600

    minute = second // 60
    second = second % 60
    
    print(f'{second_f}초는 {hour}시간 {minute}분 {second}초입니다.')

def exchange_time2(second_f):
    hour, second = divmod(second_f, 3600)
    minute, second = divmod(second, 60)
    
    print(f'{second_f}초는 {hour}시간 {minute}분 {second}초입니다.')

exchange_time2(12345)


