#그와 비슷하게 법 개정 전 한국 나이를 미국 나이로 변환하는 프로그램을 코딩
#birth = int(input('생일이 지났습니까? 맞으면 0, 틀리면 -1 :'))
# 20살, 10월 10일, 대답에는 -1이 적혀야 한다
name = input('이름 :')
kor_age = int(input('한국 나이 : '))
# 미국식 나이 = 한국식 나이 + birth
birth = int(input('생일이 지났습니까? 맞으면 0, 틀리면 -1 : '))
print(name,'의 미국 나이는 %d살 입니다.'%(kor_age + birth))



# =====================아래는 추가로 피드백 받고 싶은 코드입니다====================
birth_year=input('when did you born?')
birth_month=input('when is your birth month?')
birth_day=input('when is your birth date?')
birth_y=int(birth_year)
birth_m=int(birth_month)
birth_d=int(birth_day)
time_y=int(now.year)
time_m=int(now.month)
time_d=int(now.day)
age=time_y-birth_y
if birth_m > time_m :
    age = age-1
else :
    if (birth_m == time_m) and (birth_d  >time_d) :
        age = age -1
    else :
        age = age
print(age)
int(input('생일에 언제세요 : '))