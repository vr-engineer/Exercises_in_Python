#117
cantidad=int(input('Determine la cantidad en €: '))
desglose=0
for d in [500,200,100,50,20,10,5,2,1]:
    if cantidad>=d:
        desglose=cantidad//d
        cantidad-=(desglose*d)
        if desglose!=0 and d>2:
            if desglose>1:
                print('{0} billetes de {1}'.format(desglose,d))
            else:
                print('{0} billete de {1}'.format(desglose,d))
        elif desglose!=0 and d<=2:
            if desglose>1:
                print('{0} monedas de {1}'.format(desglose,d))
            else:
                print('{0} moneda de {1}'.format(desglose,d))
    else:
        continue
    
