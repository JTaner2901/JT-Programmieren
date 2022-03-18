#######################################
# Juan-Taner Allerborn
# Python Kurs
# split() join()
# 17.03.2022
#######################################

print("The Real Slim Shady".split()) # Teil Elemente an der Stelle wo eine lücke ist (Weißraumzeichen)
# Und wandelt es in einer Liste um

# Nur die Zeilenumbrüche teilen
print("The Real \nSlim Shady".split('\n'))

# Nur Tabulatoren teilen
print("The \tReal Slim Shady".split('\t'))

# Mit Len Funktion gucken wie viele Wörter
print(len("Deine Eltern sind Geschwister".split(" ")))


names = ["Juan", "Jason", "Maxim", "Liana", "Jerome", "Caner"]
print(names) # Normal mit diesen schwulen Klammern
print(", ".join(names)) # Ohne schwulen klammern
