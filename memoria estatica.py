import array

calificaciones = array.array('i', [0] * 5)  

for i in range(5):
    calificaciones[i] = int(input(f"Captura la calificación {i + 1}: "))

print("Calificaciones capturadas:", calificaciones.tolist())

