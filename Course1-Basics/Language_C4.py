def greet(lang):
    if lang == "ES":
        return "Hola"
    elif lang == "EN":
        return "Hello"
    elif lang == "FR":
        return "Bonjour"
    else : 
        return "N/A"


x = input("Lenguaje: ")
y = greet(x)
print(y,"Carlos")

