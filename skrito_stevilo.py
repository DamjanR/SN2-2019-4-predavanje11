import random
import json

skrito_stevilo = random.randint(1, 10)

# prazen seznam []
# seznam_stevcev = []

with open("tocke.txt") as datoteka:
    tocke = json.loads(datoteka.read())

print("Točke do sedaj:")
for tocka in tocke:
    print("   " + str(tocka))

stevec = 0
while True:
    stevilo = int(input("Vpisi število: "))
# še drug način zapisa za števec glej predhodne naloge (+=stevec) !!!
    stevec = stevec + 1

    if stevilo == skrito_stevilo:
        print("Čestitke")
        break
    elif stevilo > skrito_stevilo:
        print("Število je manjše")
    else:
        print("Število je večje")

print("Število poskusov je bilo:" + str(stevec))

tocke.append(stevec)

with open("tocke.txt", "w") as datoteka:
# za pretvorbo int v str je json.dumps !
    datoteka.write(json.loads(tocke))