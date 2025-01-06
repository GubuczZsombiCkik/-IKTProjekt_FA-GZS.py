# Fulop Aron, Gubucz Zsombor Python első beadandó

from termcolor import colored
import random


mlist=[101, 138, 112, 121, 176, 163, 123, 210, 226]

menu = [
    ("Küszöbök számolása"),
    ("Hegyek (hegycsúcsok) számolása"),
    ("Nyereg pont keresése"),
    ("Legnagyobb szintkülönbség keresése"),
    ("Lista módosítása (hozzáadás, törlés, módosítás)"),
    ("Kilépés!"),
]

menuv=True

for i in range(len(menu)):
    print(colored(f"{i+1}-{menu[i]}", "yellow"))

valasztas = input(colored("Választás: ", "light_cyan"))

if (valasztas=='1'):
    kuszob=0
    maxm=mlist[0]

    for i in range(1,len(mlist)):
        if mlist[i]>maxm:
            kuszob+= 1
            maxm=mlist[i]
