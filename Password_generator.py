import random
import numpy as np
def generator(x):
    j = ""
    for i in range(x):
        j+=(chr((int(random.random()*94)+33)))
    return j

if __name__ == '__main__':

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
            continue
        break
    j = generator(x)
    name = input('Unter welchem Namen soll es gespeichert werden?\nWenn es nicht gespeichert werden soll ohne Eingabe Enter dücken\n')
    if name != "":
        name+='.txt'
        f = open(name,'a')
        f.write(j)
        f.close()
    print(j)
    input('Zum Beenden Enter drücken\n')
