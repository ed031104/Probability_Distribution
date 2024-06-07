import service.StudentService as StudentService
from tabulate import tabulate



Ns = float(input("Ingresa el Nivel de Significancia = "))
muestra =int(input("Ingresa el tamaño de la muestra = "))
mediaM = float(input("Ingresa la Media Muestral = "))
desvE = float(input("Ingresa la Desviacion Estandar = "))
mediaH = float(input("Ingresa la Media Hipotética = ")) 

data = [
    ["Nivel de Significancia", "Tamaño de la muestra", "Media Muestral", "Desviacion Estandar", "Media Hipotética"],
    [Ns, muestra, mediaM, desvE, mediaH]
    ]

StudentService.DistribucionTStudent(Ns, muestra, mediaM, desvE, mediaH)

print(tabulate(data, headers=[''], tablefmt='grid'))

