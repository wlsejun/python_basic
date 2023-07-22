# 1. 월급을 입력받는다.
# 2. 세전 연봉을 구한다. __(월급 * 12)
# 3. 세금을 구한다. __(세전연봉 * 세전연봉 구간에 맞는 세율)
# 4. 세후 연봉을 구한다. __(세전 연봉 - 세금)
# 5. 세전 연봉과 세후 연봉을 출력한다.

# 함수로 만들기

m_pay = float(input('월급(단위 : 만원)을 입력해주세요 :'))

try:
    monthly_payment = m_pay * 12
except:
    print('Invalid value')

if monthly_payment <= 1200 :
    tax = monthly_payment * 0.06
elif monthly_payment <= 4600 :
    tax = monthly_payment * 0.15
elif monthly_payment <= 8800 :
    tax = monthly_payment * 0.24
elif monthly_payment <= 15000 :
    tax = monthly_payment * 0.35
elif monthly_payment <= 30000 :
    tax = monthly_payment * 0.38
elif monthly_payment <= 50000 :
    tax = monthly_payment * 0.40
else :
    tax = monthly_payment * 0.42

yearly_payment = monthly_payment - tax

print('세전연봉 :', monthly_payment, '\n', '세후연봉 :', yearly_payment)