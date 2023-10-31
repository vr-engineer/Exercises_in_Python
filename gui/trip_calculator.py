#Uso de variables de control
# Ejemplo del tren
# Algunas funciones no están terminadas.
# tkinter para python 3.

import tkinter as tk
from tkinter import ttk #widgets

# ===== Funciones

def calculo(): 

    if billete_ida_vuelta.get() == True:
        coste.set(2*distancia.get()*precio.get()*viajeros.get())
    else:
        coste.set(distancia.get()*precio.get()*viajeros.get())
    

# ================= GUI ======
ventana=tk.Tk()
ventana.title("Viaje selección") #Sería lo mismo que hacer -> ventana=tk.Tk(className='Viaje')


# --- Imagen ---
imagen=tk.PhotoImage(file='INDRA_AIR_AUTOMATION_marco.png')
ttk.Label(ventana, image=imagen).pack()

# --- icono de la ventana ----
ventana.iconphoto(False, imagen)

# ---- Viajejos ------
t_viajeros=ttk.Label(ventana, text='Viajeros:') #Linea de texto
t_viajeros.pack() #hay que gestionar la posicioin del widget
viajeros=tk.IntVar() #variable de control
f_viajeros=ttk.Spinbox(ventana, textvariable=viajeros, from_=0, to=200)
#f_viajeros=ttk.Entry(ventana, textvariable=viajeros) #asociamos variable de control con widget
f_viajeros.pack() #hay que gestionar la posicioin del widget

# ---- Tipo de billete ----
billete_ida_vuelta=tk.BooleanVar(value=True) #variable de control
f_billete=ttk.Checkbutton(ventana, text='Ida y vuelta', variable=billete_ida_vuelta, onvalue=True, offvalue=False)
f_billete.pack()

# ----- Clase ------
t_clase=ttk.Label(ventana, text='Clase:')
t_clase.pack()
clase1=tk.BooleanVar(value=False) #variable de control
clase2=tk.BooleanVar(value=False) #variable de control
clase3=tk.BooleanVar(value=False) #variable de control
f_clase1=ttk.Checkbutton(ventana, text='Turista', variable=clase1, onvalue=True, offvalue=False)
f_clase1.pack()
f_clase2=ttk.Checkbutton(ventana, text='Primera', variable=clase2, onvalue=True, offvalue=False)
f_clase2.pack()
f_clase3=ttk.Checkbutton(ventana, text='Lujo', variable=clase3, onvalue=True, offvalue=False)
f_clase3.pack()


# ---- Distancia -----
t_distancia=ttk.Label(ventana, text='Distancia (Km)')
t_distancia.pack()
distancia=tk.DoubleVar() #variable de control
f_distancia=ttk.Entry(ventana, textvariable=distancia) #Asociamos el campo de texto a la variable float
f_distancia.pack()


# --- Precio -----
t_precio=ttk.Label(ventana, text='Precio:')
t_precio.pack()
precio=tk.DoubleVar() #Variable de control
f_precio=ttk.Entry(ventana, textvariable=precio) 
f_precio.pack()

# --- A pagar -----
t_coste=ttk.Label(ventana, text='A pagar:')
t_coste.pack()
coste=tk.DoubleVar(value=0)
f_coste=ttk.Label(ventana, textvariable=f'{coste}')      #Muestra el valor de la varibale. Asociamos la variable de control con el widget
f_coste.pack()                                      #Siempre es necesario un gestor para que la ventana muestre el widget

# --- Calcular Botón -----
ttk.Button(ventana, text='Calcular', command=calculo).pack(side='left') #Widget al que le asociamos un comando

# --- Salir Botón -----
ttk.Button(ventana, text='Salir', command=ventana.destroy).pack(side='right')

ventana.mainloop()

# ========== 

