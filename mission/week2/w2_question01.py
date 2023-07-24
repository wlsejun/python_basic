# 1. 학생의 이름과 점수를 입력 받는다.
# 2. grader 함수를 만들고 if문을 사용하여 점수 범위를 나눈다.
# 3. 해당 점수범위에 맞는 학점을 출력한다.
# 4. 학생이름, 점수, 학점을 출력한다.


name = input('What your name?')
score = input('Enter your score :')

try:
    std_score = float(score)
except:
    print('Not a number')

def grader(name, std_score) :

    if std_score > 100 :
        print('Invalid value')
    elif std_score >= 95 :
        grade = 'A+'
    elif std_score >= 94 :
        grade = 'A'
    elif std_score >= 89 :
        grade = 'B+'
    elif std_score >= 84 :
        grade = 'B'
    elif std_score >= 79 :
        grade = 'C+'
    elif std_score >= 74 :
        grade = 'C'
    elif std_score >= 69 :
        grade = 'D+'
    elif std_score >= 64 :
        grade = 'D'
    else :
        grade = 'F'

    print('학생이름 : ', name, '\n', '점수 :', std_score, '\n', '학점 :', grade)

grader(name, std_score)
