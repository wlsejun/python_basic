def computepay(hours, rate) :
    print("computepay", hours, rate)
    if hours > 40:
        print("over time")
        reg = hours * rate
        otp =  (hours - 40) * (rate * 0.5)
        pay = reg + otp
    else :
        print("regular time")
        pay = hours * rate
    return pay

sh = input("Enter hours :")
sr = input("Enter rate :")

try:
    fh = float(sh)
    fr = float(sr)

except:
    print("not number")
    quit() #아래 코드는 실행시키지 않을 때

total_pay = computepay(fh, fr)

print("Total pay:", total_pay)