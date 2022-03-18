#######################################
# Juan-Taner Allerborn
# Python Kurs
# islower(), isupper, lower() und upper()
# 17.03.2022
#######################################

passwort = "Passwort123"
print(passwort.islower()) # Überprüft ob der String nur Kleinbuchstaben ab
print(passwort.isupper()) # Prüft ob er nur Großbuchstaben hat
test = "Der Gordon ist Bernhard"
print(test.lower()) # Alles Klein geschrieben
print(test.upper()) # Alles Groß geschrieben


print("\n##############################")
password_incorrect = True
while password_incorrect:
    password = input("Passwort eingeben (Groß- und Kleinbuchstaben)")
    if password.isupper() or password.islower():
        continue
    else:
        password_incorrect = False
        print("Passwort wurde aktzeptiert...")