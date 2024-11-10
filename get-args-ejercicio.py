#Respuesta de ChatGPT
import sys

#En values tendremos una lista con los valores (como strings)
values = sys.argv[1:] #lee los argumentos desde la línea de comandos 

#Su código debajo de aquí
#Convertir los valores de strings a números (int o float)
numbers = [float(value) for value in values]

#Calcular la media
average = sum(numbers) / len(numbers)

#Mostrar la media con dos decimales
print(f'{average:.2f}')