def mediana(diccionario):
    valores=list(diccionario.values())
    valores_ordenados=sorted(valores)
    n=len(valores_ordenados)
    if n%2==0:
        mediana=(valores_ordenados[n//2-1]+valores_ordenados[n//2])/2
    else:
        mediana=valores_ordenados[n//2]

    return mediana

diccionario={'valor0':5,'valor1':3,'valor2':8,'valor3':1,'valor4':6}
#print(mediana(diccionario))

import csv

def procesar(archivo_csv, curso):
    estudiantes = []
    with open(archivo_csv, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[2]==curso:
                estudiantes.append(row[0])
    if not estudiantes:
        raise ValueError("No hay estudiantes en el curso")
    return estudiantes

print(procesar("estudiantes.csv",3))