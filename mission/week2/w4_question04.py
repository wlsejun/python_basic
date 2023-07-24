# 1. 컴퓨터의 선택 생성하기 - random 모듈 사용하기
# 2. 사용자의 선택 받기
# 3. 선택을 비교하고 결과 출력하기

import random
computer = random.randint(0,2)

if computer == 0 :
    computer = '가위'
elif computer == 1 :
    computer = '바위'
else :
    computer = '보'

my = input('가위 바위 보 입력해주세요 : ')

def rcp(my) :
    if computer == my :
        print('나 :', my, '\n', '컴퓨터 : ', computer,  '\n', '비겼습니다.')
    else :
        if computer == '가위' :
            if my == '바위' :
                print('나 :', my, '\n', '컴퓨터 : ', computer, '\n', '나 승리!')
            elif my == '보' :
                print('나 :', my, '\n', '컴퓨터 : ', computer, '\n', '컴퓨터 승리!')
        if computer == '바위' :
            if my == '보' :
                print('나 :', my, '\n', '컴퓨터 : ', computer, '\n', '나 승리!')
            elif my == '가위' :
                print('나 :', my, '\n', '컴퓨터 : ', computer, '\n', '컴퓨터 승리!')
        if computer == '보' :
            if my == '가위' :
                print('나 :', my, '\n', '컴퓨터 : ', computer, '\n', '나 승리!')
            elif my == '바위' :
                print('나 :', my, '\n', '컴퓨터 : ', computer, '\n', '컴퓨터 승리!')

rcp(my)
    