def buchstaben_ändern(string, buchstabe):
    vokale = "aeiouöäüß"
    geänderte_strings = [] #Eine liste, die die modifizierten buchstaben speichern wird
    
    for vokal in vokale: #Für jeden Vokal in "vokale" wird eine neue Version des Strings erzeugt
        neuer_string = "" #ist ein leerer String, der Zeichenweise aufgebaut wird.
        for char in string:#Durchlaufen des Originalstrings
           
            if char.lower() == buchstabe.lower(): #durchlauf des Originalstrings
                neuer_string += vokal #wenn char dem zu ersetzenden buchstabe entspricht, wird der aktuelle vokal 'vokal' hinzugefügt
            else:
                neuer_string += char #ansonsten wird char unverändert hinzugefügt
        geänderte_strings.append(neuer_string) #Der neu erzeugte String wird zur Liste 'geänderte_strings' hinzugefügt und gespeichert
        
    for geänderte_strings in geänderte_strings:
        print(geänderte_strings) #am Ende wird jeder modifizierte String in der liste 'geänderte_strings' ausgegeben


#Beispielaufrufe aus der Aufgabe
buchstaben_ändern(string="banana", buchstabe="a")
buchstaben_ändern(string="Wie geht es Ihnen", buchstabe="a")
