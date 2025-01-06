#Dancs Levente, Virágh Gergely 10.c Python első beadandó

#függvények a véletlenszámos feltöltéshez és az abszolútértékhez
import random, math

#menü

t = []
j=0
mukodes=True #logikai változó a menüvezérlés megfelelő működéséhez

print("A feladat:")
print("Egy görbe este után Részeg Aladár elindul hazafele. Mivel jól sikerült az este, így Aladár nem csak előre halad az idő elteltével, hanem olykor-olykor hátra fele is lép. A telefonján indulás előtt a túra GPS bekapcsolódott és felvette a lépéssorozatát.")

while mukodes==True:
    
    print("")

    print("1 - A feladat")
    print("2 - B feladat")
    print("3 - C feladat")
    print("4 - D feladat")
    print("5 - Tömb módosítása (elem hozzáadása, módosítása, törlése, feltöltés véletlen számokkal)")
    print("6 - Kilépés")

    valasztas = input()

    print("")

    if (valasztas=='1'):
        #1a

        print("Másnap ezt észrevette és kiértékelte. Hány százalékkal tett meg több utat, mint ha csak előre ment volna?")

        t_abs=[]

        i2=0

        for i2 in range(0,len(t),1):
            if t[i2]<0:
                t_abs.append(abs(t[i2]))
            else:
                t_abs.append(t[i2])

        i3=0
        lepesek=0

        for i3 in range(0,len(t),1):
            lepesek+=t[i3]

        i4=0
        lepesek_abszolut=0

        for i4 in range(0,len(t),1):
            lepesek_abszolut+=t_abs[i4]

        print(f'{round(((lepesek_abszolut-lepesek)/lepesek_abszolut*100),2)} százalékkal ment többet')

    elif (valasztas=='2'):
        #1b

        print("Melyik volt a leghosszabb lépéssorozat, amit előre ment?")

        t_lepessorozat=[]

        i5=0    

        haladas=0

        for i5 in range(0,len(t),1):
            if t[i5] >= 0:
                haladas+=1
            else:
                t_lepessorozat.append(haladas)
                haladas-=haladas

        i6=0                

        max=t_lepessorozat[0]

        for i6 in range(len(t_lepessorozat)):
            if max<t_lepessorozat[i6]:
                max=t_lepessorozat[i6]

        print(max)

    elif (valasztas=='3'):
        #1c

        print("Hány alkalommal tudott a legtöbbet haladni, azaz a legnagyobb lépéséből hány darab van. Figyelmen kívül hagyjuk, hogy azt épp előre vagy hátra teszi meg.")

        t_abs=[]

        i1=0

        for i1 in range(0,len(t),1):
            if t[i1]<0:
                t_abs.append(abs(t[i1]))
            else:
                t_abs.append(t[i1])

        maxlepes=t_abs[0]

        i7=0

        for i7 in range(len(t_abs)):
            if maxlepes<t_abs[i7]:
                maxlepes=t_abs[i7]

        i8=0
        maxlepes_szam=0

        for i8 in range(len(t_abs)):
            if t_abs[i8]==maxlepes:
                maxlepes_szam+=1

        print(f'{(maxlepes_szam)} db és {maxlepes} láb volt.')


    elif (valasztas=='4'):
        #1d

        print(" Volt-e olyan, amikor döntésképtelensége miatt nem tudott megmozdulni, azaz állt egyhelyben, mint a tejbetök?")

        i9=0
        t0=[]   

        for i9 in range(len(t)):
            if t[i9]==0:
                t0.append(i9)

        if len(t0)>0:
            print("igen.")
        else:
            print("nem.")  

    elif (valasztas=='5'):
        if len(t)>0:
            print("Tömb értéke: ")
            print(t)
        else:
            print("A tömb üres.")

        muvelet=input("h-Hozzáadás,m-Módositás,t-Törlés,v-Véletlenszámokkal feltöltés: ")
        if (muvelet=="h"):
            elem=int(input("Hozzáadadni kívánt elem: "))
            t.append(elem)
            print("")
            print("Tömb módosított értéke: ")
            print(t)

        elif (muvelet=="m"):
            sorsz=int(input("Módosítani kívánt elem: "))
            ertek=int(input("Új érték: "))
            t[sorsz]=ertek
            print("")
            print("Tömb módosított értéke: ")
            print(t)

        elif (muvelet=="t"):
            sorsz2=int(input("Törölni kívánt elem: "))
            t.pop(sorsz2)
            print("Elem törölve")
            print("")
            print("Tömb módosított értéke: ")
            print(t)

        elif (muvelet=="v"):
            n=int(input("Hozzáadni kívánt véletlen számok mennyisége: "))
            for j in range(0,n,1):
             t.append(random.randint(-10,10))
            print("Sikeres feltöltés")
            print("")
            print("Tömb módosított értéke: ")
            print(t)
            
        else:
            print("Érvénytelen művelet")

    elif (valasztas=='6'):
        mukodes=False

    else:
        print("Érvénytelen választás") 