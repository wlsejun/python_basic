#그와 비슷하게 법 개정 전 한국 나이를 미국 나이로 변환하는 프로그램을 코딩
#birth = int(input('생일이 지났습니까? 맞으면 0, 틀리면 -1 :'))
# 20살, 10월 10일, 대답에는 -1이 적혀야 한다
name = input('이름 :')
kor_age = int(input('한국 나이 : '))
# 미국식 나이 = 한국식 나이 + birth
birth = int(input('생일이 지났습니까? 맞으면 0, 틀리면 -1 : '))
print(name,'의 미국 나이는 %d살 입니다.'%(kor_age + birth))