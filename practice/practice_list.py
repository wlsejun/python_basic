friends = ['yonghou', 2, 'hyejin']

for i in range(len(friends)):
    friend = friends[i]
    print('hello', friend)
print(friends)
friends[1] = 'hi'
print(friends)
frined = 'Byun'
x = frined.lower()
print(x)


print(range(4))
print(range(len(friends)))

for i in range(3):
    print(i)

stuff = list()
stuff.append('book')
stuff.append('good')
print(stuff)

#average 구하기
total = 0
count = 0
while True :
    num = input('Enter a number :')
    if num == 'done' : 
        break
    value = float(num)
    total = total + value
    count = count +1

average = total/count
print('average :', average)


# 더 많은 메모리를 차지함.
numlist = list()
while True :
    inp = input('Enter a number :')
    if inp == 'done' :
        break
    value = float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print('avarage :', average)

#split
truth = 'God is Good all the time'
word = truth.split()
print(word)

truth = 'God / is / good'
word = truth.split('/')
print(word)


fhand = open('파일명')
for line in fhand :
    line = line.rstrip()
    if not line.startswith('From') :
        continue
    words = line.split()
    print(words[2])


line = 'From sjgood97@naver.com Sat Jul 24 09:14:33 2023'
words = line.split()
email = words[1].split('@')
print(email)

