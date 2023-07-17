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
if birth_m == time_m :
	if birth_d < time_d : 
    age = age -1

print(age)