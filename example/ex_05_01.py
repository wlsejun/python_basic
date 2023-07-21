str = 'X-DSPAM-Confidence: 0.8475'

number = str.find(':')
# print(number)
peace = str[number+2 :]
# print(peace)
value = float(peace)
print(value)
print(type(value))