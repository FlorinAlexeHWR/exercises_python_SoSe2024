import matplotlib.pyplot as plt
#Variablen definieren
r = 0.5
a = 1
n = 10
 

# Die Gleichung s_n als Liste definieren
s_n = []

term_sum = 0

for k in range(0, n):
    term = a * (r**k)
#hier geht es um eine Summe , deswegen benutzen wir den Operator +=

    term_sum += term
    s_n.append(term_sum)

plt.plot(s_n)

print(s_n)


 


