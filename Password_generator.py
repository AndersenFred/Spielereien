import random
import numpy as np
while(True):
    try:
        x = int(input('Wie Viele Stellen?\n'))
        if x <= 0:
            raise ValueError
        try:
            print('Bei {} Stellen gibt es {}e{} Möglichkeiten für ein Passwort'.format(x, str((126-33)**x)[0],int(np.log(float((126-33)**x))/np.log(10))))
            if(x)>60:
                print('Das ist mehr als Atome im sichtbaren Universum')
        except(OverflowError):
            pass
    except(ValueError):
        print('Ungültige Eingabe')
    else:
        break
s = []
name = input('Unter welchem Namen soll es gespeichert werden?\nWenn es nicht gespeichert werden soll ohne Eingabe Enter dücken\n')
for i in range(x):
    s.append(chr((int(random.random()*1000)%(126-33)+33)))
j = ""
for i in s:
        j+=i
if name != "":
    name+='.txt'
    f = open(name,'a')
    f.write(j)
    f.close()
print(j)
input('Zum Beenden Enter drücken\n')
