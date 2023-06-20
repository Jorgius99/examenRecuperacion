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
        next(reader)
        for row in reader:
            if row[3]==str(curso):
                estudiantes.append(tuple(row))
    if not estudiantes:
        raise ValueError("No hay estudiantes en el curso")
    return estudiantes

print(procesar("estudiantes.csv",3))


def combinar(dic1,dic2, dic3):
    diccionario_final={}
    for nombre in dic1:
        edad=dic1.get(nombre)
        profesion=dic2.get(nombre)
        sueldo=dic3.get(nombre)
        diccionario_final[nombre]={'edad':edad, 'profesion':profesion, 'sueldo':sueldo}
    return diccionario_final

diccionario_nombres_edades = {'Ana': 25, 'Juan': 30, 'Maria': 28}
diccionario_nombres_profesiones = {'Ana': 'Ingeniera', 'Juan': 'Doctor', 'Maria':'Abogada'}
diccionario_nombres_sueldos = {'Ana': 5000, 'Juan': 7000, 'Maria': 6000}

#print(combinar(diccionario_nombres_edades, diccionario_nombres_profesiones, diccionario_nombres_sueldos))

def palabra_repetida(fichero):
    with open(fichero) as f:
        palabras=f.read().splitlines()
    contador={}
    for palabra in palabras:
        contador[palabra]=contador.get(palabra,0)+1
    palabra_mas_repetida=max(contador, key=contador.get)
    return palabra_mas_repetida

#print(palabra_repetida("palabras.txt"))