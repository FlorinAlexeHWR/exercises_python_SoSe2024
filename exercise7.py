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
            
        
    
