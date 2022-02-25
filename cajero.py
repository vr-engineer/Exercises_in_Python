#Algoritmo de un cajero automático ATM para sacar dinero.
#El usuario introduce la cantidad a sustraer y la ATM se la devolverá en billetes de 50€, 20€ y 10€ según la disponibilidad de los mismos.
#Devolverá la menor cantidad de billetes posible. 

def entrega(billetes):
    global CAJA_50,CAJA_20,CAJA_10  #Determinamos que las varibales son las globales y se pueden modificar dentro de la función
    n_50=0
    n_20=0
    n_10=0
    
    if (CAJA_50*50)+(CAJA_20*20)+(CAJA_10*10)< billetes:
        print('El cajero no dispone de billetes')
        return
    else:
        while billetes>=50 and CAJA_50>0:
            billetes-=50
            n_50+=1
            CAJA_50-=1
        while billetes>=20 and CAJA_20>0:
            billetes-=20
            n_20+=1
            CAJA_20-=1
        while billetes>=10 and CAJA_10>0:
            billetes-=10
            n_10+=1
            CAJA_10-=1


    print(f'{n_50} billetes de 50€ y quedan en cajero {CAJA_50} billetes')
    print(f'{n_20} billetes de 20€ y quedan en cajero {CAJA_20} billetes')
    print(f'{n_10} billetes de 10€ y quedan en cajero {CAJA_10} billetes')
        

CAJA_50=50 #Variable global
CAJA_20=50 #Variable global
CAJA_10=50 #Variable global


cantidad=int(input('¿Cuánto quiere sacar?'))
while cantidad%10!=0:          #Si no introducimos la cantidad divisible por 10, nos vuelve a pedir introducir el valor
    print('No es posible esa cantidad')
    cantidad=int(input('¿Cuánto quiere sacar?'))
else:
    entrega(cantidad)           #Si la cantidad es múltiplo de 10, ejecuta la función
             
