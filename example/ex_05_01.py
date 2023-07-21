str = 'X-DSPAM-Confidence: 0.8475'

number = str.find(':')
# print(number)
peace = str[number+2 :]
# print(peace)
value = float(peace)
print(value)
print(type(value))

# ---------------------------------

words = 'Connect Foundation'
if 'F' in words:
    words.lower()
    words[7] = '&'
else :
    print(words)
print(words)

# ---------------------------------

words = 'Connect Foundation'
if 'F' in words:
    words = words.lower()  # words에 소문자 변환 결과를 저장
    words = words.replace(words[7], '&')  # 리스트를 다시 문자열로 변환하여 words에 할당
else:
    print(words)

print(words)