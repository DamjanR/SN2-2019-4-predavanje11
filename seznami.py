stevila = [5, 2, 8, 3]

# izpis vseh števil
print(stevila)

#Urejanje seznama
stevila.sort()
print("Števila smo uredili")

# izpis urejenih števl
print(stevila)

# izpis števila na mestu 1
print(stevila[1])

# izpis števila vseh elementov
print("Število vseh elementov je " + str(len(stevila)))

# doda število ampak vedno na konc seznama
stevila.append(7)
# zbriše vrednost tri ne na mestu tri!
stevila.remove(3)
# zbriše PRAV element na MESTU 0 (nič) TO JE 2!!!
del stevila[0]

print("spremenjen seznam:")
print(stevila)

print("Vsi elementi prek for zanke")
for stevilo in stevila:
    print("Sedaj je število enako " + str(stevilo))