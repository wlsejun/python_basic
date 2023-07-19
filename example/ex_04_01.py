count = 0
total = 0
while True :
    number = input('Enter a number :')
    if number == 'done':
        break
    try:
        float_num = float(number)
    except:
        print('Invalid input')
        continue

    count = count + 1
    total = total + float_num
print('total :', total, 'count :', count, 'average :', total/count)