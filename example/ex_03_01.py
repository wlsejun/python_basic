sh = input("Enter hours :")
sr = input("Enter rate :")

try:
    fh = float(sh)
    fr = float(sr)

except:
    fh = -1
    fr = -1

if fh > 0 and fr > 0:
    if fh > 40:
        print("over time")
        reg = fh * fr
        otp = (fh - 40) * (fr * 0.5)
        pay = reg + otp
    else :
        print("regular time")
        pay = fh * fr

    print("Total pay:", pay)
else :
    print("not number")
