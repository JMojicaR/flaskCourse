nombre = input("Introduce tu nombre: ")
letter = nombre[0]
upper_letter = letter.upper()
#has_lower_case = any(c.islower() for c in nombre)
print(letter == upper_letter)