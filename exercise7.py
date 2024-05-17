def buchstaben_zählen(text):
    aufzählen = 0
    for buchstaben in text:
#isalpha() method returns True if all characters are alphabeit letter!!! Also keine sonderzeichen oder zahlen
        if buchstaben.isalpha():
            aufzählen += 1
            
    return aufzählen
 #Beispielaufrufe   
print(buchstaben_zählen("Hallo, Berlin"))
print(buchstaben_zählen("Hallo, Berlin%&6!"))
            
        
    
#Eine andere Lösung ohne "isalpha"
#def buchstaben_zählen(wort):
    #alphabet = "abcefghjklmnopqrstuvwxyzäöüß$"
    #wort_lower = wort.lower ()
    #wort_list = list(wort_lower)
    #wort_letter = [buchstabe for buchstabe in wort_list if buchstabe in]
    #prin(len("wort_letter"))
    
#buchstaben_zählen("Hallo, Berlin!!!")