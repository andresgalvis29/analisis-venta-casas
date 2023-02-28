from organize_data import dataOrganize
import time
import matplotlib.pyplot as plt

def seeData(file):
    dictData=dataOrganize(file)
    count = 0
    location = list(dictData.keys())
    prom = list(dictData.values())

    #Graficamos nuestro diccionario
    fig,ax = plt.subplots()
    bars = ax.barh(location,prom,height=0.5)
    ax.set(ylim=(0,10))
    ax.bar_label(bars,labels=[f'${x:,.1f}' for x in bars.datavalues])
    plt.show()
    

if __name__ == '__main__':
    seeData('casas_pereira.csv')