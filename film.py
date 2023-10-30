

film_bewertungen = {}
print("\n")
# Filmtitel und ihre Bewertungen in das Wörterbuch eingefügt.
film_bewertungen = {
    "The Silence of the Lambs": 9.3,
    "The Matrix": 9.2,
    "Inception": 9.0,
    "The social Network": 8.9,
    "Schindler's List": 8.9,
    "Disaster Movie": 1.0,
    "The Last Airbender": 2.1,
    "Jack and Jill": 3.3
}


# Funktion durchschnittliche_bewertung(wörterbuch), die die durchschnittliche Bewertung aller Filme im Wörterbuch berechnet und zurückgibt.
def durchschnittliche_bewertung(wörterbuch):
    bewertungen = wörterbuch.values()
    durchschnitt = sum(bewertungen) / len(bewertungen)
    return durchschnitt

# Funktion höchste_bewertung(wörterbuch), die den Filmtitel mit der höchsten Bewertung zurückgibt.
def höchste_bewertung(wörterbuch):
    höchste_bewertung = max(wörterbuch, key=wörterbuch.get)
    return höchste_bewertung

# Funktion filme_ab_6(wörterbuch), die eine Liste der Filmtitel zurückgibt, die eine Bewertung von 6 oder höher haben.
def filme_ab_6(wörterbuch):
    filme = [film for film, bewertung in wörterbuch.items() if bewertung >= 6]
    return filme

# ein weiterer Film mit Bewertung und aktualisierem Wörterbuch.
film_bewertungen["Inception"] = 9.0

# Ausgabe des Wörterbuchs, um sicherzustellen, dass die Bewertungen aktualisiert wurden.
print(film_bewertungen)
print("\n")
# Verwendung der oben definierten Funktionen
print("Die durchschnittliche Bewertung aller Filme beträgt:", durchschnittliche_bewertung(film_bewertungen))
print("\n")
print("Der Film mit der höchsten Bewertung ist:", höchste_bewertung(film_bewertungen))
print("\n")
print("Filme mit einer Bewertung von 6 oder höher sind:", filme_ab_6(film_bewertungen))
print("\n")