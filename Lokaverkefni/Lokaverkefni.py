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
while loop == "j":
    