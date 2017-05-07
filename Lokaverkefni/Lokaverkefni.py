#Elís Orri

import random

tolur = []
stokkur1 = []
stokkur2 = []
for i in range(15):
    loop = "j"
    while loop == "j":
        tala = random.randint(0, 29)
        if tala not in tolur:
            stokkur1.append(tala)
            tolur.append(tala)
            loop = "n"
for x in range(15):
    loop = "j"
    while loop == "j":
        tala = random.randint(0, 29)
        if tala not in tolur:
            stokkur2.append(tala)
            tolur.append(tala)
            loop = "n"
loop = "j"
spilalisti = []
spil = open("spil.txt", "r", encoding='iso-8859-1')
for line in spil:
    spilalisti.append(eval(line))
spil.close()
pottur = []
flokkar = ["Nafn", "Þyngd í kílóum", "Mjólkurlagni dætra", "Einkunn ullar", "Fjöldi afkvæma", "Einkunn læris", "Frjósemi", "Gerð/þykkt bakvöðva", "Einkunn fyrir malir"]
hverGerir = 0
while loop == "j":
    spil1 = spilalisti[stokkur1[0]]
    spil2 = spilalisti[stokkur2[0]]
    if hverGerir == 0:
        print("Nafn:", spil1[0])
        print("1: Þyngd í kílóum:", spil1[1])
        print("2: Mjókurlagni dætra:", spil1[2])
        print("3: Einkunn ullar:", spil1[3])
        print("4: Fjöldi afkvæma:", spil1[4])
        print("5: Einkunn læris:", spil1[5])
        print("6: Frjósemi:", spil1[6])
        print("7: Gerð/þykkt bakvöðva:", spil1[7])
        print("8: Einkunn fyrir malir:", spil1[8])
        val = int(input("Hvaða eiginleika villtu nota? "))
        if spil1[val] > spil2[val]:
            print("Þú vannst!")
            spiltemp1 = stokkur1[0]
            spiltemp2 = stokkur2[0]
            stokkur1.remove(spiltemp1)
            stokkur2.remove(spiltemp2)
            stokkur1.append(spiltemp1)
            stokkur1.append(spiltemp2)
            while len(pottur) >= 1:
                stokkur1.append(pottur[0])
                potturtemp = pottur[0]
                pottur.remove(potturtemp)
            hverGerir = 1
        if spil1[val] < spil2[val]:
            print("Þú tapaðir!")
            spiltemp2 = stokkur2[0]
            spiltemp1 = stokkur1[0]
            stokkur2.remove(spiltemp2)
            stokkur1.remove(spiltemp1)
            stokkur2.append(spiltemp2)
            stokkur2.append(spiltemp1)
            while len(pottur) >= 1:
                stokkur1.append(pottur[0])
                potturtemp = pottur[0]
                pottur.remove(potturtemp)
            hverGerir = 1
        if spil1[val] == spil2[val]:
            print("Jafntefli! Spilin fara í pottin")
            pottur.append(stokkur1[0])
            pottur.append(stokkur2[0])
            spiltemp1 = stokkur1[0]
            spiltemp2 = stokkur2[0]
            stokkur1.remove(spiltemp1)
            stokkur2.remove(spiltemp2)
            hverGerir = 1
    elif hverGerir == 1:
        val = random.randint(1, 8)
        print("Tölvan valdi eiginleikan", flokkar[val], "og er með", spil2[val], "stig í honum")
        print("Þú ert með", spil1[val], "í honum")
        if spil1[val] > spil2[val]:
            print("Þú vannst!")
            spiltemp1 = stokkur1[0]
            spiltemp2 = stokkur2[0]
            stokkur1.remove(spiltemp1)
            stokkur2.remove(spiltemp2)
            stokkur1.append(spiltemp1)
            stokkur1.append(spiltemp2)
            while len(pottur) >= 1:
                stokkur1.append(pottur[0])
                potturtemp = pottur[0]
                pottur.remove(potturtemp)
            hverGerir = 0
        if spil1[val] < spil2[val]:
            print("Þú tapaðir!")
            spiltemp2 = stokkur2[0]
            spiltemp1 = stokkur1[0]
            stokkur2.remove(spiltemp2)
            stokkur1.remove(spiltemp1)
            stokkur2.append(spiltemp2)
            stokkur2.append(spiltemp1)
            while len(pottur) >= 1:
                stokkur1.append(pottur[0])
                potturtemp = pottur[0]
                pottur.remove(potturtemp)
            hverGerir = 0
        if spil1[val] == spil2[val]:
            print("Jafntefli! Spilin fara í pottin")
            pottur.append(stokkur1[0])
            pottur.append(stokkur2[0])
            spiltemp1 = stokkur1[0]
            spiltemp2 = stokkur2[0]
            stokkur1.remove(spiltemp1)
            stokkur2.remove(spiltemp2)
            hverGerir = 0
    print(stokkur1)
    if len(stokkur1) == 0:
        print("Þú tapaðir leiknum!")
        loop = "n"
    if len(stokkur2) == 0:
        print("Þú vannst leikinn!")
        loop = "n"