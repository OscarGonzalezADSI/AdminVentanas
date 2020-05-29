from tkinter import *

def AdminVentanas(orden):

    def SubVentana1():
        root = Tk()
        root.title("Sub Ventana 1")
        root.resizable(False, False)
        root.geometry("400x400")
        # Poner contenido
        root.mainloop()

    def SubVentana2():
        root = Tk()
        root.title("Sub Ventana 2")
        root.resizable(False, False)
        root.geometry("400x400")
        # Poner contenido
        root.mainloop()

    def SubVentana3():
        root = Tk()
        root.title("Sub Ventana 3")
        root.resizable(False, False)
        root.geometry("400x400")
        # Poner contenido
        root.mainloop()
        
    def Datos():
        confBtn = {} # "texto",    funcion,  ancho, x, y
        confBtn[0] = ("ventana 1", SubVentana1, 25, 0, 0)
        confBtn[1] = ("ventana 2", SubVentana2, 25, 0, 25)
        confBtn[2] = ("ventana 3", SubVentana3, 25, 0, 50)
        
        return confBtn    

    def InterfaceUsuario(root):

        confMenu = Datos()

        btnConfiguracion = Button(root, text=confMenu[0][0], width=confMenu[0][2], command=confMenu[0][1])
        btnConfiguracion.place(x=confMenu[0][3], y=confMenu[0][4])
        
        btnConfiguracion = Button(root, text=confMenu[1][0], width=confMenu[0][2], command=confMenu[1][1])
        btnConfiguracion.place(x=confMenu[1][3], y=confMenu[1][4])
        
        btnConfiguracion = Button(root, text=confMenu[2][0], width=confMenu[0][2], command=confMenu[2][1])
        btnConfiguracion.place(x=confMenu[2][3], y=confMenu[2][4])

    def Desplegar():
        root = Tk()
        root.title("Titulo ventana")
        root.resizable(False, False)
        root.geometry("400x400")
        InterfaceUsuario(root)
        root.mainloop()

    def Controlador(orden):
        if(orden == "desplegar"):
            Desplegar()
            
    Controlador(orden)

AdminVentanas("desplegar")   
    
    
    
    
    