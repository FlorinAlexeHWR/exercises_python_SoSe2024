a = 1
r = 0.5
s = 0
k = 0
grenzwert = 1/(1-r)
#epsilon ist eine kleine Zahl die verwendet wird, um die Konvergenz zu überprüfen
epsilon = 1e-10

while True:
    s += a * r**k
    k += 1
    print(s, end = " ")
    if (grenzwert - s) < epsilon: 
        break
    
        
