a = '123'
type(a)
b = int(a)
print(type(b))
print(b)
print(a)
print(a + 1)
print(int(a)+1)

c = 'hello world'
d = int(c)

who = input("what's your name?")
print('Welcome', who)

who = input("who are u?")
print('hello', who)

#유럽식 층수를 입력받는다.
#입력받은 유럽식 층수를 int(정수)형으로 변환해준다. -> input 함수는 '문자열'을 반환
#입력받은 유럽식 층수에서 1을 더해준다. -> = 미국식 층수
#미국식 층수를 출력한다..
europe_floor = input("what's floor in your country?")
american_floor = int(europe_floor) +1
print('US floor : ', american_floor)