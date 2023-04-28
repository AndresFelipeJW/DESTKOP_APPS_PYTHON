#---------------------------------
# Desktop app No. 1
#---------------------------------

# se importa la libreria tkinter con todas sus funciones 
from tkinter import *

#----------------------------
# funciones de la app
#----------------------------

#-----------------------------
# ventana principal de la app
#-----------------------------

# se declara una variable llamada ventana_principal, que adquiere las caracteristicas de un objeto Tk()
ventana_principal = Tk()

# TAMAÑO DE LA VENTANA 
ventana_principal.geometry("800x600")

# TITULO DE VENTANA
ventana_principal.title("ESPECIALIDAD EN SISTEMAS - GUANENTA")

# DESHABILITAR BOTON DE MAXIMIZAR
ventana_principal.resizable(False, False)

# COLOR DE FONDO DE LA VENTANA 
ventana_principal.config(bg="white")

#-------------------------
# FRAMA ROJO
#-------------------------
frame_verde = Frame(ventana_principal)
frame_verde.config(bg="red3", width=1000, height=150)
frame_verde.place(x=0, y=0)     #ANCHO     #ALTURA


#------------------------
# FRAMA AMARILLO
#------------------------
frame_rojo = Frame(ventana_principal)
frame_rojo.config(bg="yellow", width=1000, height=600)
frame_rojo.place(x=0, y=150)     


#-------------------------
# FRAMA ROJO
#-------------------------
frame_blanco = Frame(ventana_principal)
frame_blanco.config(bg="red3", width=1000, height=150)
frame_blanco.place(x=0, y=450)


#-------------------------
# FRAMA ROJO
#-------------------------
frame_blanco = Frame(ventana_principal)
frame_blanco.config(bg="red3", width=100, height=100)
frame_blanco.place(x=120, y=250)



# run 
# SE EJECUTA EL METODO MAINLOOP() DE LA CLASE TK() A TRAVES DE LA INSTANCIA DE LA INTANCIA ventana_principal. Este metodo despliega la ventana en pantalla y queda a la espera de le que el usuario haga (click en un boton, escribir, etc). Cada accion del usuario se conoce como unn evento. El método mainloop() es un bucle infinito.
ventana_principal.mainloop()

