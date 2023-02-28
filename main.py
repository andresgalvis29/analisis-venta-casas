from see_data import seeData

def run():
    entry = ''
    while len(entry) < 1:
        entry = input('Ingrese el nombre del archivo :')
    try:
        seeData(entry)
    except FileNotFoundError:
        print('El archivo no se ha encontrado, por favor corra otra vez el programa')


if __name__ == '__main__':
    run()