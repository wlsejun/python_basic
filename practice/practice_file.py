# ---파일 열고 읽는 법 : 첫번째 방법---
fhand = open('파일명')   #파일의 개찰구 역할
for line in fhand :    #한줄씩 반복적으로 받아 옴
    line = line.rstrip()  #개행문자(\n) 지우기_줄바꿈 지우기
    if not line.startswith('From') :
        continue
    print(line)

# ---파일 열고 읽는 법 : 두번째 방법---
fhand = open('파일명')
for line in fhand :
    line = line.rstrip()
    if not '@naver.com' in line :
        continue
    print(line)

# ---여러 파일 열 수 있게---
fname = input('Enter the file name : ')
try :
    fhand = open(fname)
except :
    print('File cannot be opended : ', fname)
    quit()    #파일이 없을 경우 여기서 종료시킴. 아래 코드는 실행안함.

count = 0
for line in fhand :
    if line.startswith('Subject') :
        count = count + 1
print('There were', count, 'subject lines in', fname)

