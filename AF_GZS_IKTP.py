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

    print(colored(f"(1.) {kuszob} küszöb van.", "light_magenta"))

elif (valasztas=='2'):
    hegycsucssz=0

    for i in range(1,len(mlist)-1):
        if mlist[i]>mlist[i-1] and mlist[i]>mlist[i+1]:
            hegycsucssz+=1
            
    print(colored(f"(2.) Összesen {hegycsucssz} hegycsúcs.", "light_magenta"))

elif (valasztas=='3'):
    talalat=False  
    for i in range(len(mlist)-1):
        if mlist[i] == mlist[i+1]:
            talalat=True
            print(colored(f"(3.) {i+1} mérési ponton nyereg van!", "light_magenta"))

    if not (talalat):
        print(colored("(3.) Nincs nyereg pont!", "light_magenta"))

elif (valasztas=='4'):
    szkulonb=[]
    for i in range(len(mlist)-1):
        szkulonb.append(mlist[i+1]-mlist[i])

    maxszkulonb=max(szkulonb)
    maxpozi=szkulonb.index(maxszkulonb)
    print(colored(f"(4.) {maxszkulonb} m volt a legnagyobb szintkülönbség a {maxpozi+ 1}. és {maxpozi + 2}. mérési pont között.", "light_magenta"))

elif (valasztas=='5'):
    if (not mlist):
        print(colored("A lista üres, nem lehet módosítani vagy törölni.", "red"))
    else:
        print(colored("\nJelenlegi lista:", "light_red"))
        for number in mlist:
            print(colored(number, "light_green"), end=", ")
        print(5)

        poziin=input(colored("Add meg a módosítani vagy törölni kívánt elem poziciojat (0-tól kezdve): ", "light_green"))

        if (poziin=="" or not poziin.isnumeric()):
            print(colored("\nÉrvénytelen pozicio! Csak számot adjon meg.", "red"))
        else:
            pozi=int(poziin)
            if (0<=pozi<len(mlist)):
                muvelet=input(colored("[m]", "light_yellow")+" - Módosítás\n"+colored("[t]", "red")+" - Törlés\n").lower()

                if (muvelet=="m"):
                    ujertek=int(input(colored("Add meg az új értéket: ", "light_green")))
                    mlist[pozi]=ujertek
                    print("\nAz új lista értéke:")
                    for number in (mlist):
                        print(colored(number, "light_green"), end=", ")
                    print()                