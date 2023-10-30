print("\n")
produkte = [
    ("Laptop", 899.99, 4.6, True),
    ("Smartphone", 549.99, 4.2, True),
    ("Tablet", 299.99, 3.9, False),
    ("Kopfhörer", 149.99, 4.8, True),
    ("Maus", 19.99, 4.1, True),
]

verfügbare_produkte = [produkt[0] for produkt in produkte if produkt[3]]
print("Folgende Produkte sind vorrätig:")
for produkt in verfügbare_produkte:
    print(produkt)
print("\n")

gut_und_günstig = [produkt[0] for produkt in produkte if produkt[1] < 50 and produkt[2] >= 4]
print(f"Das ist das günstigste und gut bewertetes Produkt; {gut_und_günstig}")

print("\n")

durchschnittspreis = sum([produkt[1] for produkt in produkte]) / len(produkte)
print(f"Der Durchschnittspreis aller Produkte ist: {durchschnittspreis:.2f}€")

print("\n")

teuerstes_produkt = max(produkte, key=lambda produkt: produkt[1])
print(f"Das teuerste Produkt ist: {teuerstes_produkt[0]}")

print("\n")
