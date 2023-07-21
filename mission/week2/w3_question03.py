# 1. 나이와 지불 방법(카드, 현금)을 입력받는다. *예외처리 : 현금/카드로 입력하지 않은 경우
# 2. 나이 및 지불 방법에 따라 요금을 구분한다.
# 3. 입력받은 정보에 따른 요금을 출력한다.

age = int(input('나이를 입력해주세요 :'))
pay = input('현금/카드 중 지불 방법을 입력해주세요 :')

try:
    if age < 8 :
        cost = '무료'
    elif 8 <= age < 14 :
        if pay == '현금' :
            cost = 450
        elif pay == '카드' :
            cost = 450
    elif 14 <= age < 20 :
        if pay == '현금' :
            cost = 720
        elif pay == '카드' :
            cost = 1000
    elif 20 <= age < 75 :
        if pay == '현금' :
            cost = 1200
        elif pay == '카드' :
            cost = 1300
    else :
        cost = '무료'

except:
    print('Invalid value')

print('나이 :', age, '지불유형 :', pay, '버스요금 :', cost)

