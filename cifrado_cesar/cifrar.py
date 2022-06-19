#Nombre: Víctor Rivero Díez
#Ejercicio: Propuesta 2 - Hackeando, a lo bruto, a Julio César

#Este programa permite realizar el cifrado césar de un texto.
#Nos permite elegir la clave de cifrado (desplazamiento).
#Lee caracteres de Ñ, espacios, mayúsculas, minúsculas, tildes y diéresis.


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
