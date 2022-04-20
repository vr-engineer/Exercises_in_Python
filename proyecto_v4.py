#//////////////////////////////////////////////////////////
#   Programa para el estudio de inglés.

#   El programa cuenta con menú de opciones:
#   Primera opción: Añadir nuevas palabras inglés-español a la base de datos
#   Segunda opción: Escribir la palabra en español dada una palabra aleatoria en inglés + sonido en inglés
#   Tercera opción: Escribir la palabra en inglés dada una palabra aleatoria en español + sonido en inglés
#   Cuarta opción: Diccionario
#   Quinta opción: Salir del programa 


#//////////////////////////////////////////////////////////

#--- Importación de módulos y funciones -------------------
from gtts import gTTS             #Para pasar el texto a audio. Hay que instalar la librería previamente. 
from playsound import playsound   #Para poder reproducir el audio. Hay que instalar la librería previamente. Hay que hacer una modificación https://www.codestudyblog.com/cs2201py/40113095112.html
import random                     #Para generar números de forma aleatoria. Módulo incluido en la librería estándar. En este caso he importado el módulo entero.
from sys import exit              #Del módulo sys de la librería estándar sólo nos interesa la función exit. 


#--- Definición de clases ----------------------------------
class Palabra:
    def __init__(self,español,inglés,categoría):
        self.español=español
        self.inglés=inglés
        self.categoría=categoría

    def __str__(self):   
        registro='{0} = {1}'.format(self.inglés,self.español)
        return registro

    def audio(self):
        voz=gTTS(self.inglés, lang='en',slow=False)
        voz.save('audio.mp3')
        playsound('audio.mp3')

#--- Definición de funciones -------------------------------------
def menu():                                                 #Función del menú
    print("  --------- Menú --------")
    print("1) Añadir palabras nuevas")
    print("2) Traducir a español")
    print("3) Traducir a inglés")
    print("4) Diccionario")
    print("5) Salir")
    opcion=int(input("__"))                                 #Lee la opción elegida por el usuario.
    while opcion not in (1,2,3,4,5):                      #Garantiza que la opción es una de las posibles.
        opcion=int(input("__Opción incorrecta\n__"))        #Si no es una de las posibles, vuelve a solicitarla al usuario.
    else:
        return opcion                                       #Si la opción es correcta, la función devuelve el entero introducido por teclado.

def añadir(demo=False,n_cadena=''):                                     #Función para añadir nuevas palabras al fichero (bbdd). Cuenta con un parámetro de entrada por defecto False.
    
    if demo==False:
        español=input("Escriba el término en español: ")        #español será una variable de tipo cadena que representará un término en español. 
        while español=='':                                      #Garantiza que no se introduzca un término en blanco (cadena vacía). 
            español=input("Escriba el término en español: ")    #Ante una cadena vacía, pide al usuario volver a escribir el término. 
        español=español.lower()                                 #Garantiza que todas las letras estén en minúsculas, aunque las escribamos en mayúsculas.

        inglés=input("Escriba el término en inglés: ")          #inglés será una variable de tipo cadena que representará un término en inglés.
        while inglés=='':
            inglés=input("Escriba el término en inglés: ")
        inglés=inglés.lower()

        categoría=input("Escriba la categoría (sus,ver,adj,adv): ") #categoría será una variable de tipo cadena que representará la catagoría a la que pertenece el término en inglés.
        while categoría=='':
            categoría=input("Escriba la categoría (sus,ver,adj,adv): ") 
        categoría=categoría.lower()
        
        n_cadena=español+','+inglés+','+categoría+'\n'          #Concatenación de cadenas, añadiendo ',' para posteriormente usarlo como separador de los términos.   

        f=open(ruta,'r',encoding='utf-8')                       #Se abre el fichero en modo lectura. Vamos a comprobar si la cadena n_cadena ya existe en el fichero. 
        for linea in f:                                         #Lee línea a línea el fichero.
            if n_cadena==linea:                                 #Si la cadena de n_cadena es igual a la cadena de linea, se cierra el fichero, se informa al usuario y finaliza la función añadir() sin escribir nada al fichero.
                f.close()
                print('Esta palabra ya existe en la bbdd')
                return                                          #finaliza la función
        f.close()                                               #Si la condición n_cadena==linea no se cumplió en ningún caso, finaliza el bucle for y se cierra el fichero.
        f=open(ruta,'a',encoding='utf-8')                       #Se abre el fichero de nuevo, pero esta vez en modo añadir.
        f.write(n_cadena)                                       #Se escribe la cadena de n_cadena en el fichero.
        f.close()                                               #Se cierra el fichero
        print("Término añadido")                                #Se informa al usuario de que el nuevo término ya fue añadido.

    else:                                                                    
        f=open(ruta,'a',encoding='utf-8')                       
        f.write(n_cadena) #habria que usar la variable global                                       
        f.close()

def elegir_categoria():                                     
#La función creará a partir de las palabras guardadas en el fichero, todos los objetos de tipo clase Palabra que pertenezcan a la categoría elegida por el usuario.

    f=open(ruta,'r',encoding='utf-8')  #Abrimos el fichero en modo lectura.
    sustantivos=[]                     
    verbos=[]
    adjetivos=[]
    adverbios=[]
    
    print("Elija una categoría:\n\t1 - Sustantivo\n\t2 - Adjetivo\n\
\t3 - Adverbio\n\t4 - Verbo\n")
    categoría=int(input('Opción- '))
    while categoría not in (1,2,3,4):                             #Garantiza que la opción es una de las posibles.
        categoría=int(input('Opción incorrecta\n '))

    fila = f.readline()
    while fila!='':
        esp,eng,cat = fila.split(',')
        cat=cat.rstrip('\n')
        if categoría==1 and cat=='sus':
            sustantivos.append(Palabra(esp,eng,cat))                  
        elif categoría==2 and cat=='adj':
            adjetivos.append(Palabra(esp,eng,cat))
        elif categoría==3 and cat=='adv':
            advervios.append(Palabra(esp,eng,cat))
        elif categoría==4 and cat=='ver':
            verbos.append(Palabra(esp,eng,cat))
        fila = f.readline()
    f.close()

    if categoría==1 :
        return sustantivos[:]
    elif categoría==2:
        return adjetivos[:]
    elif categoría==3:
        return advervios[:]
    elif categoría==4:
        return verbos[:]
    

def generar_aleatorio(l):                                   #Garantizamos que cada palabra aleatoria sea distinta a la anterior hasta que sale el último elemento.
    orden=list(range(len(l)))                               #range solo admite enteros.
    desorden=random.sample(orden,len(orden))                #Genera una de lista de enteros no repetidos.
    return desorden[:]                                      #Devolvemos una copia de la lista desorden.

def buscar():
    print("Diccionario_________________")
    buscar=input("Escriba la palabra a buscar: ")
    buscar=buscar.lower()   
    f=open(ruta,'r',encoding='utf-8')                       
    for linea in f:                                         
        esp,eng,cat = linea.split(',')
        if buscar==esp or buscar==eng:                                
            f.close()
            Palabra(esp,eng,cat).audio()
            return Palabra(esp,eng,cat)
    f.close()
    return "El término no está incluido o no existe"



#--- Programa principal ---------------------------------

print(" -- Programa para entrenar inglés --\n")

#El programa necesita trabajar con un fichero por lo que al iniciar el programa nos pide uno.

existe_bbdd=int(input('¿Ya tiene una bbdd creada [1] o quiere crear una nueva [2]? '))
while existe_bbdd not in (1,2):
    existe_bbdd=int(input('¿Ya tiene una bbdd creada [1] o quiere crear una nueva [2]? '))

if existe_bbdd==1:
    ruta=input('Ruta o nombre del fichero .txt: ')
    print('Base de datos añadida\n')
else:
    f=open('bbdd.txt','w',encoding='utf-8')
    f.close()
    ruta='bbdd.txt'                                      #El nombre por defecto que el programa le da al fichero lo guardamos en la variable ruta.
    demo=bool(input("¿Desea cargar una demo? (x)Sí (ENTER)No  "))
    demo_lista=['chico,lad,sus\n','misericordia,mercy,sus\n','sentimiento,feeling,sus\n',\
                'impresionante,awesome,adj\n','sorprendente,stunning,adj\n','loco,crazy,adj\n'\
                'por casualidad,by chance,adv\n','apenas,hardly,adv\n','para siempre,forever,adv\n'\
                'creer,reckon,ver\n','gritar,shout,ver\n','comenzar,take up,ver\n']   #demo_lista es varibel global
    for n_cadena in demo_lista:
        añadir(demo,n_cadena)                                                                   #le pasamos el valor de demo, True o False.
    
     
    print('Base de datos creada\n')                      


mostrar_menu=True                                                            #True para que inicialmente se ejecute el bucle while.
while mostrar_menu:

    om=menu()                                                                #LLamada a la función menu().

    if om==1:    
        op1=True                                                             #True para que inicialmente se ejecute el bucle while 
        while op1:
            añadir()                                                         #LLamada a la función añadir()
            op1=bool(input("¿Desea añadir más términos? (x)Sí (ENTER)No  ")) #Si opl es True, se volverá a llamar a la función añadir(). 
        else:
            continue                                                         #Si op1 es False, se vuleve a mostrar el menú. (Se vuelve a ejecutar el bucle while mostrar_menu). 
        
        
    elif om==2:

        print("\nDebe escribir el significado de la palabara en español.")
        lista_Palabras=elegir_categoria()                       #Llamada a la función elegir_categoria()
        sorteo=generar_aleatorio(lista_Palabras)
        op3=True
        while op3:
            
            for d in sorteo:
                print('| {} |'.format(lista_Palabras[d].inglés))       #Palabra elegida al azar.
                esp=input('\t\t\t-> ')                                 #Pedimos que se escriba la palabra en español.
                esp=esp.lower()                                        #Garantizamos que todas las letras introducidas sean minúsculas.
                while esp!=lista_Palabras[d].español:                  #Comprueba que la palabra en español esté bien escrita.
                    esp=input('\t\t\tMal escrito\n\t\t\t-> ')
                    esp=esp.lower()                         
                print('| {} | {} |'.format(lista_Palabras[d].inglés,esp))
                lista_Palabras[d].audio()
                op3=bool(input("\nOtra palabra? x)Sí  ENTER)No\n"))
                if op3==False:
                    break                                               #Finaliza el bucle for
        else:
            continue                                                               

    elif om==3:
        
        print("\nDebe escribir el significado de la palabara en inglés")
        lista_Palabras=elegir_categoria()  
        sorteo=generar_aleatorio(lista_Palabras)
        op4=True
        while op4:

            for d in sorteo:
                print('| {} |'.format(lista_Palabras[d].español))
                eng=input('\t\t\t-> ')
                eng=eng.lower()
                while eng!=lista_Palabras[d].inglés:
                    eng=input('\t\t\tMal escrito\n\t\t\t-> ')
                    eng=eng.lower()   
                print('| {} | {} |'.format(lista_Palabras[d].español,eng))
                lista_Palabras[d].audio()
                op4=bool(input("\nOtra palabra? x)Sí  ENTER)No\n"))
                if op4==False:
                    break 
        else:
            continue

    
    elif om==4:

        print(buscar(),'\n')
        
                            

    elif om==5:
        mostrar_menu=False
        
else:
    exit("Salió del programa")
    

        
