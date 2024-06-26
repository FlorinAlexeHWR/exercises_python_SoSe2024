# Schreiben Sie eine Funktion buchstaben_häufigkeit(), die eine String annimmt und die Anzahl der einzelnen Buchstaben in der String zurückgibt. Mit anderen Worten, die Funktion berechnet die Häufigkeit jedes Buchstabens in der String. Die Funktion berücksichtigt nur Buchstaben und keine Zahlen oder Sonderzeichen. Groß- und Kleinbuchstaben werden als der gleiche Buchstabe betrachtet. Die Funktion gibt ein Dictionary mit Buchstaben als Schlüssel (key) die Buchstabenhäufigkeit als Wert (value) zurück. Achtung! Das von der Funktion zurückgegebene Dictionary ist alphabetisch geordnet.

# buchstaben_häufigkeit("123Wie g&eht es Ihnen%$?")

# {'e': 4, 'g': 1, 'h': 2, 'i': 2, 'n': 2, 's': 1, 't': 1, 'w': 1}
# PS. Wenn Sie noch etwas Zeit haben, plotten Sie ein Histogramm mit den Schlüsseln (die Buchstaben) auf der horizontalen Achse und den Werten (die Häufigkeit) auf der vertikalen Achse, plt.bar(). Zuerst müssen Sie matplotlib importieren

import matplotlib.pyplot as plt

def buchstaben_häufigkeit(x):
    mein_d = {}
    for buchstabe in x.lower():
        if buchstabe.isalpha():
            
            if buchstabe not in mein_d:
                mein_d[buchstabe] = 1
                
            else:
                mein_d[buchstabe] += 1
                
    mein_d_sorted = dict(sorted(mein_d.items()))
    
    return mein_d_sorted
bh_dict = buchstaben_häufigkeit(x="123Wie geht es Ihnen$$§")

plt.bar(bh_dict.keys(), bh_dict.values())