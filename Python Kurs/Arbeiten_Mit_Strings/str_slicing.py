#######################################
# Juan-Taner Allerborn
# Python Kurs
# Arbeiten mit Strings (Slicing)
# 17.03.2022
#######################################

test_string ="The Motherfucking MC"
print(len(test_string))
print(test_string[0])

# Wie bei Listen 'Teilstring zurückgeben'
print(test_string[4:16])

# In Variabel speichern
slicing = test_string[4:]
print(slicing)

# Überprüfen (true/false)
print("MC" in test_string)
print("gay" not in test_string)