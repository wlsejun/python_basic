big = max("Hello world")
print(big)

# ============================
def greet(lang):
    if lang == "es":
        print("hola")
    elif lang == "fr":
        print("bonjour")
    else:
        print("hello")

greet("ko")

# ============================
def greet(lang):
    if lang == "es":
        return "Hola"
    elif lang == "fr":
        return "bongjour"
    else:
        return "hello"
print(greet("ko"), "sejun")
