# Works with IDLE STFU

import statistics

b = []
print ("Ingrese 9999 para detener")

while True:
    a = input("Ingrese los numeros: ")
    a = int(a)
    if a == 9999:
        break
    else:
        b.append(a)

print (b)
c = statistics.mode(b)
d = statistics.median(b)
e = statistics.median_grouped(b)

print("The mode is: ",c)
print("The Median is: ",d)
print("The median_grouped: ",e)
