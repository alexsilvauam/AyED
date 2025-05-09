# Agregar elementos  a la cola enqueue
cola = []

cola.append('Cliente 1')
cola.append('Cliente 2')
cola.append('Cliente 3')
cola.append('Cliente 4')
cola.append('Cliente 5')
cola.append('Cliente 6')
cola.append('Cliente 7')
cola.append('Cliente 8')
cola.append('Cliente 9')
cola.append('Cliente 10')

print(cola)
for cliente in cola:
    print(cliente)

#Eliminar al primero cliente de la cola dequeue
print('Eliminando al primer cliente de la cola')
cliente.atendido = cola.pop(0)
print(cliente.atendido)

print("Cola de clientes despues de atender al primero")
for cliente in cola:
    print(cliente)
    
