

def steigung_funktion(Koordinaten):
    x1, y1, x2, y2 = Koordinaten
    if x2-x1 == 0:
        print("Die Steigung ist nicht definiert")
    else:
        m_formel = (y2-y1) / (x2-x1)
        print("Die Steigung der Geraden beträgt", m_formel)
        
Koordinaten = [1,1,2,4]

steigung_funktion(Koordinaten)
   




