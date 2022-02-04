#Algoritmo que calcula el desglose mínimo de billetes y monedas de una cantidad introducida exacta de euros 

cantidad=int(input('Introduzca una cantidad: '))

billetes_500=cantidad//500                                    #calculamos cuántos billetes de 500 hay.
if billetes_500!=0:                                           #Si no hay, no se hace nada.
    if billetes_500>1:                                        #Si hay y es más de 1, imprime la palabra billetes.
        print(billetes_500,' billetes de 500€\n')             #Impriminos el nº de billetes y el texto.
    else:                                                     #Si hay y es 1, imprime la palabra billete.
        print(billetes_500,' billete de 500€\n')
    resto500=cantidad%500                                     #Lo que queda, se guarda en la varibale resto500.
else:
    resto500=cantidad                                         #Si no hay billenes de 500, la cantidad introducida se guarda en resto500. 

billetes_200=resto500//200                                    #calculamos cuántos billetes de 200 hay. 
if billetes_200!=0:
    if billetes_200>1:
        print(billetes_200,' billetes de 200€\n')
    else:
        print(billetes_200,' billete de 200€\n')
    resto200=resto500%200
else:
    resto200=resto500

billetes_100=resto200//100                                    #calculamos cuántos billetes de 100 hay.
if billetes_100!=0:
    if billetes_100>1:
        print(billetes_100,' billetes de 100€\n')
    else:
        print(billetes_100,' billete de 100€\n')
    resto100=resto200%100
else:
    resto100=resto200

billetes_50=resto100//50                                    #calculamos cuántos billetes de 50 hay.
if billetes_50!=0:
    if billetes_50>1:
        print(billetes_50,' billetes de 50€\n')
    else:
        print(billetes_50,' billete de 50€\n')
    resto50=resto100%50
else:
    resto50=resto100

billetes_20=resto50//20                                     #calculamos cuántos billetes de 20 hay.
if billetes_20!=0:
    if billetes_20>1:
        print(billetes_20,' billetes de 20€\n')
    else:
        print(billetes_20,' billete de 20€\n')
    resto20=resto50%20
else:
    resto20=resto50

billetes_10=resto20//10                                     #calculamos cuántos billetes de 10 hay.
if billetes_10!=0:
    if billetes_10>1:
        print(billetes_10,' billetes de 10€\n')
    else:
        print(billetes_10,' billete de 10€\n')
    resto10=resto20%10
else:
    resto10=resto20

billetes_5=resto10//5                                       #calculamos cuántos billetes de 5 hay.
if billetes_5!=0:
    if billetes_5>1:
        print(billetes_5,' billetes de 5€\n')
    else:
        print(billetes_5,' billete de 5€\n')
    resto5=resto10%5
else:
    resto5=resto10

moneda2=resto5//2                                          #calculamos cuántas monedad de 2€ hay.
if moneda2!=0:  #Si hay                     
    if moneda2>1: #Si hay más de una, monedas.
        print(moneda2,' monedas de 2€\n')
    else:         #Si sólo hay una,moneda.
        print(moneda2,' moneda de 2€\n')
elif resto5>0:  #Si no hay monedas de 2€, entonces el resto5 es 0 o solo 1
    print(resto5,' moneda de 1€\n')
resto2=resto5%2

if resto2>0:  #Solo puede quedar una moneda que sea de 1
   print(resto2,' moneda de 1€\n')
