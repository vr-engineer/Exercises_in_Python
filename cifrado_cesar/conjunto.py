#Script para cifrado y descifrado César

import filtro2   #Este módulo incluye la función que ajusta el diccionario de palabras para la IA. 

#Este programa permite realizar el cifrado césar de un texto.
#Nos permite elegir la clave de cifrado (desplazamiento).
#Lee caracteres de Ñ, espacios, mayúsculas, minúsculas, tildes y diéresis.


print('-- Script to César encrypt and decrypt text --')
print('Choose an option:\n 1)Encrypt\n 2)Decrypt\n 3)Exit\n')
op=0

while op not in [1,2,3]:
    op=int(input('_'))
else:
    if op==1:
        print('-- César encryption --\n')
        ruta=input('Ruta o nombre del fichero: ') #Pide al usuario determinar el fichero a leer posteriormente.
        f=open(ruta,'r',encoding='utf-8')         #Abre el fichero con texto a cifrar en modo lectura.
        lectura=f.read(1).upper()                 #Lee el primer carácter y lo asigna a la variable "lectura" (sólo contiene un carácter). 
        cadena=''                                 #La variable "cadena" es una cadena de caracteres vacía.

        while lectura!='':                        #El bucle no finaliza hasta que se lean todos los caracteres del fichero.
            if lectura==' ':                      #Carácter espacio.
                pass                              #Los espacios son ignorados. (Así se quitan los espacios)
            elif lectura=='Ñ':                    #El carácter Ñ se cambia por NN.
                cadena+='NN'
            elif lectura=='Á':
                cadena+='A'
            elif lectura=='É':
                cadena+='E'
            elif lectura=='Í':
                cadena+='I'
            elif lectura=='Ó':
                cadena+='O'
            elif lectura=='Ú' or lectura=='Ü':
                cadena+='U'
            else:
                cadena+=lectura                 #Para el resto caracteres, no hay cambios. Se van cocatenendo en la cadena de caracteres de la varibale "cadena".
            lectura=f.read(1).upper()           #Se lee el siguiente carácter.
        f.close()                               #Se cierra el fichero.


        clave=int(input('Elija una clave (0-26): '))   #Se selcciona la clave de cifrado.  0 y 26 darán el mismo resultado.

        cadena_cif=''                                  #Proceso inverso al descifrado. 
        for caracter in cadena:
            posicion=((ord(caracter)-65)+clave)%26
            letra=chr(posicion+65)
            cadena_cif+=letra                          #La cadena de caracteres con el texto cifrado se asigna a la variable "cadena_cif".
    
        #print('{:3}|{}'.format(clave,cadena_cif))  <- para comprobar (desactivado)

        #-- Se van a agrupar los caracteres de 5 en 5. 
        cadena_cif_separada=''                                              
        contador=0                          #Contador de caracteres.
        for i in cadena_cif:
            if contador<5:                  #Hasta 5 (0,1,2,3 y 4).
                cadena_cif_separada+=i      #Concatenación
                contador+=1
            else:
                cadena_cif_separada+=' '+i  #Concatenación. La cadena de caracteres con el texto cifrado separado de 5 en 5 se asigna a la variable "cadena_cif_separada".
                contador=1                  #Volvemos a iniciar a 1 porque escribimos ' '+i


        print('{:3}|{}'.format(clave,cadena_cif_separada))     #Imprime en pantalla el texto cifrado. 
        cesar=open('mensaje_cifrado.txt','w',encoding='utf-8') #Crea un fichero .txt
        cesar.write(cadena_cif_separada)                       #Escribe el texto cifrado en un fichero .txt
        cesar.close()

    if op==2:
        
        filtro2.IA()                                           #Crea el Diccionario_sin.txt
        print('-- César decryption --\n')
        #--
        ruta2=input('Ruta o nombre del fichero: ')             #Pide al usuario determinar el fichero a leer posteriormente.
        f=open(ruta2,'r',encoding='utf-8')                     #Abre el fichero con texto cifrado, en modo lectura y codificación utf-8. Crea el objeto "f".
        cadena=''                                              #Asignamos a la variable "cadena" una cadena de caracteres vacía.

        #-- Eliminar espacios intermedios.
        lectura=f.read(1)                                      #Lee 1 carácter del fichero abierto. (El primer carácter de la primera línea). El carácter se asigna a la varibale "lectura".
        while lectura!='':                                     #Mientras haya caracteres para leer, el bucle while no finalizará.
            if lectura!=' ':                                   #Si el carácter leído es el espacio en blanco, éste no se concatena a la cadena de caracteres de la variable "cadena". 
                cadena+=lectura                                #De esta forma, se eliminan los espacios entre cada 5 caracteres. 
            lectura=f.read(1)                                  #Lee un nuevo carácter del fichero y lo vuelve a asiganr a la variable "lectura".
        f.close()                                              #Finalizado el bucle while, el fichero se cierra.

        #-- 

        f=open("fichero_plano.txt",'w',encoding='utf-8')       #Con esta línea y la siguiente, se crea un fichero con el nombre "fichero_plano.txt" vacío.
        f.close()                                              #El fichero queda cerrado.

        #--
        print('Bucle de crackeo\n')                            #Imprime el mensaje, según indica el ejecicio.

        for clave in range(0,27):                              #La variable "clave" tomará los valores del 0 al 26, uno por cada iteración del bucle. Así comprobamos todas las claves posibles. 
    
            cadena_des=''                                      #La variable "cadena_des" se inicializa como cadena de caracteres vacía.  
            for caracter in cadena:                            #La variable "caracter" tomará un elemento de la cadena de caracteres de la variable "cadena" en cada iteración del bucle for.
                posicion=((ord(caracter)-65)-clave)%26         #Se hace un cambio de escala al restar 65. Se pasa de la escala A(65) - Z(90) a A(0) - Z(25).
                                                               #Cuando al restar el valor de "clave" da un número negativo; al hacer el módulo, la operación matemática que hace python es:
                                                               # -a%b = (-a+b)%b
                letra=chr(posicion+65)                         #Al sumar 65 se vuelve a la escala A(65) - Z(90) y se hace la conversión del valor ascii a carácter.
                cadena_des+=letra                              #La cadena de caracteres, a la que se irán concatenando caracteres nuevos descifrados, se asigna a la variable "cadena_des"".    
        #--
            Diccionario=open('Diccionario_sin.txt','r')        #Se abre el fichero "Diccionario_sin.txt" que contiene el registro de palabras posibles creado por el programa filtro.py. Se crea el objeto "Diccionario".
            contador=0                                         #Se inicializa la variable "contador" a 0. Definiéndola aquí se garantiza que con cada nueva clave se reinicia a cero.
            for palabra in Diccionario:                        #Se recorren todas las filas del fichero "Diccionario". La cadena que corresponde a cada fila del fichero se asigna a la variable "palabra". 
                if palabra.rstrip('\n') in cadena_des:         #De la cadena habrá que eliminar el carácter salto de línea. Al mismo tiempo, se comprueba si esa cadena es una subcadena de la cadena "cadena_des".
                    contador+=1                                #Si es una subcadena, se suma 1 al contador. 
                    # print(palabra,end='') -- para comprobar que palabras coinciden (desactivado). 
            Diccionario.close()                                #Una vez se llega a la última fila del fichero, el bucle for finaliza y el fichero se cierra. 
        #--
            f=open("fichero_plano.txt",'a',encoding='utf-8')   #Se abre el fichero que se había creado antes, de nombre "fichero_plano.txt" en modo añadir. 
            print('Clave {:2}|Certeza {:3}|{}'.format(clave,contador,cadena_des))     #Imprime en la pantalla de la consola el texto descifrado, la clave usada y el grado de certeza sobre si la clave es la correcta o no. 
            f.write('Clave {:2}|Certeza {:3}|{}\n'.format(clave,contador,cadena_des)) #Lo mismo que antes, pero lo escribe en el fichero abierto. (Se le añade el salto de línea a mayores).  
            f.close()                                          #Se cierra el fichero. 
    
    else:
        print('Fin del programa')
