#Nombre: Víctor Rivero Díez
#Ejercicio: Propuesta 2 - Hackeando, a lo bruto, a Julio César

#El objetivo de este programa es quitar tildes y diéresis, pasar a mayúsculas y convertir Ñ en NN.
def IA():
    Diccionario=open('Diccionario.txt','r')          #Abre el fichero en modo lectura. Al objeto fichero se le da el nombre de Diccionario.
    Diccionario_sin=open('Diccionario_sin.txt','w')  #Abre y crea el fichero. Al objeto fichero se le da el nombre de Diccionario_sin. En este se guardará el resultado.

    for linea in Diccionario:                        #Se recorre línea a línea Diccionario. "linea" será una cadena de caracteres acabada en \n.
        linea=linea.rstrip('\n').upper()             #Quitamos '\n' de la cadena y ponemos en mayúscula todos sus caracteres.
        letras=list(linea)                           #La cadena de caracteres la convertimos en una lista, llamada "letras", para poder modificar algunos de ellos. La cadena de caracteres es inmutable.
        for i in range(len(letras)):                 #Recorre los elementos de "letras".
            if letras[i]=='Á':                       #Medinate indexacción, se accede a cada carácter de la lista, se comprueba y, si procede, se cambia.
                letras[i]='A'
            if letras[i]=='É':
                letras[i]='E'
            if letras[i]=='Í':
                letras[i]='I'
            if letras[i]=='Ó':
                letras[i]='O'
            if letras[i]=='Ú' or letras[i]=='Ü':
                letras[i]='U'
            if letras[i]=='Ñ':
                letras[i]='NN'
        linea=''.join(letras)                       #La función join() permite convertir la lista de caracteres en una cadena de caracteres nuevamente. Ésta última se guarda en la variable "linea".
        if len(linea)>4:                            #Si la cadena, es decir, la palabra del diccionario, tiene una longitud mayor que 4, es decir, más de 4 letras, la escribimos en el fichero Diccionario_sin.
            Diccionario_sin.write(linea+'\n')       #Se añade el salto de línea o de carro para mantener el formato. 
        
    Diccionario.close()                             #Se cierran los dos ficheros. 
    Diccionario_sin.close()
