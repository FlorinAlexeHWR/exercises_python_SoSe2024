def vokon_zählen(text):
    vokale = "aeiouäüöß"
    #erstmal vokale und konsonanten = 0
    anzahl_vokale = 0
    anzahl_konsonanten = 0
    #for-schleife
    for buchstaben in text.lower():
        if buchstaben.isalpha():
            if buchstaben in vokale:
                anzahl_vokale += 1
            else:
                anzahl_konsonanten += 1
#hier wird eine f-String benutzt
    print(f"Es gibt {anzahl_vokale} Vokale und {anzahl_konsonanten} Konsonanten.")
#Beispiele
print(vokon_zählen("Berlin"))

print (vokon_zählen("HI, &%/ BerliN!!"))

print (vokon_zählen("qwrtzpsdfghjklyxcvbnm"))

#alternativlösung
#def vokon_zählen(wort):
    #vokalen = "aeiou"
    #wort_lower = wort.lower()
    
    #buchstaben = [i for i in wort_lower if i.isalpha()]
    #vokalen = [k for k in work_lower if k in vokalen]
    