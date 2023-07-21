data = 'From sejun.kim@naver.com Sat July  5 09:14:16 2023'
atpos = data.find('@')
print(atpos)
sppos = data.find(' ', atpos)
print(sppos)
print(data[atpos +1 : sppos])
