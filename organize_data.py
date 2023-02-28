import csv
import time
import re
from collections import defaultdict

def eliminateRent(location):
    words = location.split()
    word = 'ARRIENDO' in words or 'ARRIENDO,' in words
    return word

def dataOrganize(file):
    fhand = open(file,encoding='utf8')
    filecsv = csv.DictReader(fhand,delimiter=',')
    filterdata = defaultdict(list)
    for object in filecsv:
        location = object['location'].upper()
        if eliminateRent(location) is True : continue
        price = object['price']
        price = re.sub('[$.]','',price)
        #print(location,'||',price)
        filterdata[location].append(int(price))
    for getlist in filterdata:
        prom = int(sum(filterdata[getlist])/len(filterdata[getlist]))
        filterdata[getlist] = prom
    return dict(filterdata)



if __name__ == '__main__':
    x = dataOrganize('casas_pereira.csv')
    print(x)