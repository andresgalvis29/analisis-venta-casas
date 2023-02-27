from organize_data import dataOrganize
import time
import matplotlib.pyplot as plt
#import pandas as pd

def run():
    dictData=dataOrganize('casas_pereira.csv')
    count = 0
    location = list(dictData.keys())
    prom = list(dictData.values())
    #print(dictData)
    #pandasserie = pd.Series(dictData)
    #print(pandasserie)
    #pandasserie.plot(kind='barh', sort_columns=True, legend=True)

    #plot 
    fig,ax = plt.subplots()
    bars = ax.barh(location,prom,height=0.5)
    ax.set(ylim=(0,10))
    ax.bar_label(bars,labels=[f'${x:,.1f}' for x in bars.datavalues])
    plt.show()
    

if __name__ == '__main__':
    run()