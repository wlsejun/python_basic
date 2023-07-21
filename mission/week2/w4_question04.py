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

user = input('가위 바위 보 입력해주세요 : ')

if computer == user :
    print('나 :', user, '컴퓨터 : ', computer,  '비겼습니다.')
else :
    if computer == '가위' :
        if user == '바위' :
            print('나 :', user, '컴퓨터 : ', computer, '나 승리!')
        elif user == '보' :
            print('나 :', user, '컴퓨터 : ', computer, '컴퓨터 승리!')
    if computer == '바위' :
        if user == '보' :
            print('나 :', user, '컴퓨터 : ', computer, '나 승리!')
        elif user == '가위' :
            print('나 :', user, '컴퓨터 : ', computer, '컴퓨터 승리!')
    if computer == '보' :
        if user == '가위' :
            print('나 :', user, '컴퓨터 : ', computer, '나 승리!')
        elif user == '바위' :
            print('나 :', user, '컴퓨터 : ', computer, '컴퓨터 승리!')
    