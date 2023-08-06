Vowels="aeiou"or"AEIOU"
result=""
Alphabet=input("Plase Enter Your Alphabet: ")
for char in Alphabet:
    if    char not in Vowels:
        result += "." + char.lower()
        print(result)