lista1 = []
lista2 = list()

lista1.append("Tanisha")
print(lista1)

lista1.append("Aleyka")
print(lista1)

lista1.insert(1, "Enya")
print(lista1)

lista1.insert(4, "Wendy")
print(lista1)

lista2 = lista1

print("Lista2 {lista2}")
print("Lista1 {lista1}")

lista1.append("Carasuperlocagimnasio")

print("Lista2 {lista2}")
print("Lista1 {lista1}")


lista1.pop()

print("Lista2 {lista2}")
print("Lista1 {lista1}")


del lista1[0]

