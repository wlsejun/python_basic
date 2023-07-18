sh = input("Enter hours :")
sr = input("Enter rate :")

try:
    fh = float(sh)
    fr = float(sr)

except:
    print("not number")
    quit() #아래 코드는 실행시키지 않을 때

if fh > 40:
    print("over time")
    reg = fh * fr
    otp = (fh - 40) * (fr * 0.5)
    pay = reg + otp
else :
    print("regular time")
    pay = fh * fr

print("Total pay:", pay)
