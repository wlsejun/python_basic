name = "sejun"
try:
    print("start")
    int_name = int(name)
    print("second")
except:
    int_name = -1

print("Done", int_name)


# ============현실적인 예시============
user_num = input("enter your phone number :")
try:
    num = int(user_num) 
except:                #예외발생 시 실행
    num = -1
if num > 0:
    print("your number is", num)
else:
    print("Error : not a number")