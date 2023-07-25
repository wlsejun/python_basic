import random
computer_num = random.randint(0,2)
if computer_num == 0 : 
    computer = "가위"
elif computer_num == 1 : 
    computer = "바위"
elif computer_num == 2 : 
    computer = "보"

print("가위바위보 게임을 시작합니다.")
user = input("가위바위보 중 하나를 입력하세요")
while user != "가위" and user != "바위" and user != "보" : 
    user = input("가위바위보 중 하나를 다시 입력하세요")
    
while computer == user : 
    user = input("게임이 비겼습니다, 가위바위보 중 하나를 다시 입력하세요")
if computer == "가위" and user == "보" : 
    print("컴퓨터가 승리했습니다")
elif computer == "바위" and user == "가위" : 
    print("컴퓨터가 승리했습니다")
elif computer == "보" and user == "바위" : 
    print("컴퓨터가 승리했습니다")
elif computer == "보" and user == "가위" : 
    print("사용자가 승리했습니다")
elif computer == "가위" and user == "바위" : 
    print("사용자가 승리했습니다")
elif computer == "바위" and user == "보" : 
    print("사용자가 승리했습니다")
    