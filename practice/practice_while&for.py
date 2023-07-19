while True :
    line = input(">")
    if line[0] == "#" :
        continue
    elif line == "done" :
        break
    print(line)
print('done!')

# ----------------
friends = ['hyejin', 'sejun', 'yongho', 'sungsoo']
for friend in friends :
    print('hello', friend)
print('done')

# ----------------
largest_num = -1
print('before', largest_num)
num_list = [3, 41, 12, 9, 51, 7, 93]
for num in num_list :
    if num > largest_num :
        largest_num = num
    print(largest_num, num)
print('after', largest_num)

# -----------------
index = 0
subjects = ['국어', '영어', '수학', '컴퓨터', '데이터분석', '금융학', '경제학']
for subject in subjects :
    index = index + 1
    print(index, subject)
print('after', index)

# -----------------
start = 0
num_set = [1, 4, 6, 13, 36, 20, 93, 25]
for num in num_set :
    start = start + num
    print(start, num)
print('total', start)

# -----------------
count = 0
sum = 0
for value in [1, 4, 6, 13, 36, 20, 93, 25] :
    count = count + 1
    sum = sum + value
    print(count, sum)
print('count :', count, 'sum : ', sum, 'average : ', sum/count)

# -----------------
for value in [1, 4, 6, 13, 36, 20, 93, 25] :
    if value > 20 :
        print('large number', value)
print('done')

# ------리스트 안에 찾는 데이터 있는지 확인할 때----------
found = False
for value in [1, 4, 6, 13, 36, 20, 93, 25] :
    if value == 6 :
        found = True
        break
    print(found, value)
print('after', found)

# ------최솟값 구하기----------
smallest_num = None
number_set = [39, 50, 45, 23, 94, 35]
for num in number_set :
    if smallest_num == None :
        smallest_num = num
    elif num < smallest_num :
        smallest_num = num
    print(smallest_num, num)
print('smallest number :', smallest_num)



