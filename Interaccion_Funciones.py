#
#TODO: Juego, elige el palito menor. pierdes si eliges el palíto más corto.

from random import shuffle

#*Lista inicial
palitos = ['-', '--', '---', '----']

#*Función que mezcle palitos
def mezclar(lista):
    shuffle(lista)
    return lista

#*Función que pida pedir uno de los 4 números
def probar_suerte():
    intento = ''
    while intento not in ['1', '2', '3', '4']:
        intento = input('Elige un número del 1 al 4: ')
    return int(intento)

#*Función comprobar el intento
def comprobar_intento(lista, intento):
    if lista[intento-1] == '-':
        print("A lavar los platos XD")
    else: print('Esta vez te has salvado 7u7 !!!')
    print(f'Te ha tocado {lista[intento-1]}')

palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
comprobar_intento(palitos_mezclados, seleccion)