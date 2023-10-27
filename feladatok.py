def feladat1():
    x = 0
    while x < 150:
        print(x, end="; ")
        x += 2
    print(x)


def feladat2():
    x = 0
    szamok = 0
    while x < 11:
        szam = float(input("Szám: "))
        if szam % 3 == 0:
            szamok += 1
        x += 1
    print("3-mal osztható számok: ", szamok)


def feladat3():
    x = float(input("Szám: "))
    while x % 10 != 0:
        x = float(input("Szám: "))

    print("Helyes!")


def feladat4():
    x = int(input("Szám: "))
    x = abs(x)
    while not (x % 2 == 0 and 10 <= x <= 98):
        x = int(input("Szám: "))
        x = abs(x)
    print("Helyes")


def feladat5():
    x = int(input("Szám: "))
    while not (x > 0 and x % 2 == 1):
        x = int(input("Szám: "))
    print("Helyes")


def feladat6():
    x = int(input("Szám: "))

    while not (x % 3 == 0 or (x ** 0.5) % 1 == 0):
        x = int(input("Szám: "))
    print("Helyes")


def feladat7():
    x = float(input("1. Szám: "))
    y = float(input("2. Szám: "))
    z = float(input("3. Szám: "))
    while not (x + y > z and x + z > y and y + z > x):
        x = float(input("1. Szám: "))
        y = float(input("2. Szám: "))
        z = float(input("3. Szám: "))
    print("Szerkeszthető háromszög")


def feladat8():
    szo = str(input("Szó: "))
    while not (len(szo) >= 3):
        szo = str(input("Szó: "))
    print(szo.upper())


def feladat9():
    szo = str(input("Szó: "))
    while not (len(szo) >= 4 and szo.islower()):
        szo = str(input("Szó: "))
    print("Helyes szó - - >", szo)


def feladat10():
    szam = 0
    x = int(input("Szám ( Leállításhoz írj be 0-át ): "))
    szam += x
    i = 0
    while not (x == 0):
        x = int(input("Szám: "))
        szam += x
        i += 1
    atlag = szam / i
    print("A számok átlaga", "{:.3}".format(atlag))


def feladat11():
    szam = 0
    x = int(input("Szám ( Leállításhoz írj be 0-át ): "))
    i = 0
    while not (x == 0):
        while not (x > 0):
            x = int(input("Szám: "))

        szam += x
        i += 1
        x = int(input("Szám: "))

    atlag = szam / i
    print("A számok átlaga", "{:.3}".format(atlag))


def feladat12():
    n = int(input("Létszám: "))
    i = 0
    serult = 0
    eredmenyek = 0
    while not i == n:
        ido = int(input("Másodperc: "))
        if ido == 0:
            serult += 1
        elif ido > 0:
            eredmenyek = eredmenyek + ido
        elif ido < 0:
            print("Helytelen adat")
            ido = int(input("Másodperc: "))
            eredmenyek = eredmenyek + ido
        i += 1
    befutott = n - serult
    print("Teljesítette: ", befutott, "versenyző", (befutott / n) * 100, "%")
    print("Átlag futott idő: ", eredmenyek / befutott)


def feladat12b():
    n = int(input("Létszám: "))
    i = 0
    serult = 0
    eredmenyek = 0
    elozo = 0
    monoton = True
    while not i == n:
        ido = int(input("Másodperc: "))

        if ido == 0:
            serult += 1
        elif ido > 0:
            eredmenyek = eredmenyek + ido
            if ido > elozo:
                print("Ez az érték nagyobb mint az előző")
            else:
                print("Ez az érték nagyobb mint az előző")
                monoton = False
            elozo = ido
        elif ido < 0:
            print("Helytelen adat")
            ido = int(input("Másodperc: "))
            eredmenyek = eredmenyek + ido
            if ido > elozo:
                print("Ez az érték nagyobb mint az előző")
            else:
                print("Ez az érték nagyobb mint az előző")
                monoton = False
            elozo = ido

        i += 1
    befutott = n - serult
    print("Teljesítette: ", befutott, "versenyző", (befutott / n) * 100, "%")
    print("Átlag futott idő: ", eredmenyek / befutott)
    if monoton is True:
        print("Szigorúan monoton nővekvő")
    if monoton is False:
        print("Nem szigorúan monoton")
