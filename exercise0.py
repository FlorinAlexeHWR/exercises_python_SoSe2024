P = 1 # Principal
t = 1 # Time
i = 1 # Interest
n = 60 * 24 * 265
A = P * (1 + i/n)**(t*n) # Calculation 
print(A)

from math import exp

def carg_berechnung(AK, EK, t):
    AK_abs = abs(AK)
    EK_abs = abs(EK)
    cagr = ((EK/AK_abs)**(1/t)-1) # * 100
    return cagr

cagr_berechnung(100, 700, 30)






    


