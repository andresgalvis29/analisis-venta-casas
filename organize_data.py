import csv
import time
import re
from collections import defaultdict

#Esta Funcion nos permite eliminar todo lo relacionado con los arriendo de nuestro .csv
def eliminateRent(location):
    words = location.split()
    word = 'ARRIENDO' in words or 'ARRIENDO,' in words
    return word

# Funcion para organizar los datos del programa
def dataOrganize(file):
    fhand = open(file,encoding='utf8')
    filecsv = csv.DictReader(fhand,delimiter=',')
    filterdata = defaultdict(list) # Pasamos a defaultdict para poder insertar una lista como valor a nuestro diccionario
    for object in filecsv:
        location = object['location'].upper() # Ponemos todo en mayuscula para encontrar las locaciones que son iguales
        if eliminateRent(location) is True : continue
        price = object['price']
        price = re.sub('[$.]','',price) # Eliminamos el $ y . para poder pasar a entero el precio de cada casa
        filterdata[location].append(int(price))
    for getlist in filterdata:
        prom = int(sum(filterdata[getlist])/len(filterdata[getlist])) # Realizamos el promedio con las listas anexas en cada locacion
        filterdata[getlist] = prom
    return dict(filterdata)



if __name__ == '__main__':
    x = dataOrganize('casas_pereira.csv')
    print(x)