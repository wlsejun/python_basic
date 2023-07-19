# ---------------Syntax Error-------------------
# Syntax Error_Example01
x = 6
if x > 5
print("x > 5")

# Syntax Error_Debugging01
x = 6
if x > 5:
    print("x > 5")

# Syntax Error_Example02
name = input("what's your name?")
print("hello, name)
# Syntax Error_Debugging02
name = input("what's your name?")
print("hello", name)

# ---------------Value Error-------------------
# Value Error_Example01
language = "english"
lan_code = int(language)

# Value Error_Debugging01
language = "010324"
lan_code = int(language)
print(lan_code)

# ---------------Type Error-------------------
# Type Error_Example01
myName = "Lisa"
myAge = 27
me = myName + myAge

# Type Error_Debugging01
myName = "Lisa"
myAge = "27"
me = myName + myAge
print("I'm", me)

I'm Lisa 27
