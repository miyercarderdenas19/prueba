from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image 
import pyodbc
import pandas as pd




class Producto:
    def __init__(self, ventana_producto):
        self.window = ventana_producto
        self.window.title("STEAMCONTROL")
        self.window.geometry("1200x700")
        self.window.resizable(2, 2)
        self.window.config(bd=10)
 
        server = 'SAP'

        bd ='SG-STEAMCONTROL'
        user = 'SAP/AuxSistemas'
        password ='Sg-St34m&C0ntr0l'
    

        try:


            conexion = pyodbc.connect(
                'DRIVER={ODBC Driver 17 for SQL  server};SERVER='+server+';DATABASE='+bd+';PWD='+password)
            
            print('Conexion exitosa')
        except:
            print('Error')    
            


        "--------------- Titulo --------------------"
        titulo = Label(ventana_producto, text="REGISTRO DE EQUIPOS", fg="black", font=("Comic Sans", 17, "bold"),
                       pady=10)
        titulo.pack()

        "--------------- Logos productos --------------------"
        frame_logo_productos = LabelFrame(ventana_producto)
        frame_logo_productos.config(bd=0)
        frame_logo_productos.pack()

        # Logo SAMSONLOGO
        imagen_samson = Image.open("imagenes/SAMSONLOGO.png")
        nueva_imagen_samson = imagen_samson.resize((60, 60))
        render_samson = ImageTk.PhotoImage(nueva_imagen_samson)
        label_samson = Label(frame_logo_productos, image=render_samson)
        label_samson.image = render_samson
        label_samson.grid(row=0, column=0, padx=15, pady=5)

        # Logo PrismaLOGO
        imagen_prisma = Image.open("imagenes/PrismaLOGO.png")
        nueva_imagen_prisma = imagen_prisma.resize((60, 60))
        render_prisma = ImageTk.PhotoImage(nueva_imagen_prisma)
        label_prisma = Label(frame_logo_productos, image=render_prisma)
        label_prisma.image = render_prisma
        label_prisma.grid(row=0, column=1, padx=15, pady=5)

        # Logo WilkersonVLOGO
        imagen_wilkerson = Image.open("imagenes/wilkersonLOGO.png")
        nueva_imagen_wilkerson = imagen_wilkerson.resize((60, 60))
        render_wilkerson = ImageTk.PhotoImage(nueva_imagen_wilkerson)
        label_wilkerson = Label(frame_logo_productos, image=render_wilkerson)
        label_wilkerson.image = render_wilkerson
        label_wilkerson.grid(row=0, column=2, padx=15, pady=5)

        # logo BurkertLOGO
        imagen_burkert = Image.open("imagenes/burkertLOGO.png")
        nueva_imagen_burkert = imagen_burkert.resize((60, 60))
        render_burkert = ImageTk.PhotoImage(nueva_imagen_burkert)
        label_burkert = Label(frame_logo_productos, image=render_burkert)
        label_burkert.image = render_burkert
        label_burkert.grid(row=0, column=3, padx=15, pady=5)

        # logo gastLOGO
        imagen_gast = Image.open("imagenes/gastLOGO.png")
        nueva_imagen_gast = imagen_gast.resize((60, 60))
        render_gast = ImageTk.PhotoImage(nueva_imagen_gast)
        label_gast = Label(frame_logo_productos, image=render_gast)
        label_gast.image = render_gast
        label_gast.grid(row=0, column=4, padx=15, pady=5)

        # logo rcmLOGO 
        imagen_rcm = Image.open("imagenes/rcmLOGO.png")
        nueva_imagen_rcm = imagen_rcm.resize((60, 60))
        render_rcm = ImageTk.PhotoImage(nueva_imagen_rcm)
        label_rcm = Label(frame_logo_productos, image=render_rcm)
        label_rcm.image = render_rcm
        label_rcm.grid(row=0, column=5, padx=15, pady=5)

        # logo tlvLOGO
        imagen_tlv = Image.open("imagenes/tlvLOGO.png")
        nueva_imagen_tlv = imagen_tlv.resize((60, 60))
        render_tlv = ImageTk.PhotoImage(nueva_imagen_tlv)
        label_tlv = Label(frame_logo_productos, image=render_tlv)
        label_tlv.image = render_tlv
        label_tlv.grid(row=0, column=8, padx=15, pady=5)

        "--------------- Frame marco --------------------"
        marco = LabelFrame(ventana_producto, text="Informacion del producto", font=("Comic Sans", 10, "bold"), pady=50)

        marco.pack()

        "--------------- Formulario --------------------"
        label_tipodemantenimiento = Label(marco, text="Tipo de mantenimiento: ", font=("Comic Sans", 10, "bold"))
        label_tipodemantenimiento.grid(row=0, column=0, sticky='w', padx=5, pady=8)
        self.combo_tipodemantenimiento = ttk.Combobox(marco,
                                        values=["-Selecione-", "Configuracion", "Correctivo", "Estudio", "Preventivo", "N/A", "No Reparable", "ICPV"],
                                        width=22, state="readonly")
        self.combo_tipodemantenimiento.current(0)
        self.combo_tipodemantenimiento.grid(row=0, column=1, padx=5, pady=8)

        "--------------------------------------------------------------------------------"
        label_lugar = Label(marco, text="Lugar: ", font=("Comic Sans", 10, "bold"))
        label_lugar.grid(row=1, column=0, sticky='e', padx=5, pady=8)
        self.combo_lugar = ttk.Combobox(marco,
                                              values=["-Selecione-", "Steamcontrol", "Planta del Cliente"], 
                                              width=22, state="readonly")
        self.combo_lugar.current(0)
        self.combo_lugar.grid(row=1, column=1, padx=5, pady=8)

        "--------------------------------------------------------------------------------"
        label_Responsable = Label(marco, text="Responsable: ", font=("Comic Sans", 10, "bold"))
        label_Responsable.grid(row=1, column=2, sticky='w', padx=5, pady=9)
        self.combo_Responsable = ttk.Combobox(marco,
                                        values=["-Selecione-", "Juan Araque", "Pedro Cofles", "Heldert Blanco", "Robinson Martinez", "Esteban Meza", "Juan Araque / Pedro Cofles"],
                                        width=22, state="readonly")
        self.combo_Responsable.current(0)
        self.combo_Responsable.grid(row=1, column=3, padx=5, pady=0)

        "--------------------------------------------------------------------------------"
        label_Torcometro = Label(marco, text="Torcometro: ", font=("Comic Sans", 10, "bold"))
        label_Torcometro.grid(row=0, column=2, sticky='s', padx=5, pady=8)
        self.combo_Torcometro = ttk.Combobox(marco,
                                               values=["-Selecione-", "10-411111", "14-175037", "G-9/NI-002BP", "N/A"],  
                                               width=22, state="readonly")
        self.combo_Torcometro.current(0)
        self.combo_Torcometro.grid(row=0, column=3, padx=5, pady=8)

        "--------------------------------------------------------------------------------"
        label_conocimiento = Label(marco, text="Torcometro: ", font=("Comic Sans", 10, "bold"))
        label_conocimiento.grid(row=2, column=2, sticky='w', padx=5, pady=8)
        self.combo_conocimiento = ttk.Combobox(marco,
                                               values=["-Selecione-", "10-411111", "14-175037", "G-9/NI-002BP", "N/A"],  
                                               width=22, state="readonly")
        self.combo_conocimiento.current(0)
        self.combo_conocimiento.grid(row=2, column=3, padx=5, pady=8)

        "--------------------------------------------------------------------------------"
        
        label_descripcion = Label(marco, text="Descripcion: ", font=("Comic Sans", 10, "bold"))
        label_descripcion.grid(row=2, column=0, sticky='e', padx=8, pady=4)
        self.descripcion = Text(marco, width=50, height=5)  
        self.descripcion.grid(row=2, column=1, padx=8, pady=8)

        "--------------- Frame botones --------------------"
        frame_botones = Frame(ventana_producto)
        frame_botones.pack()

        "--------------- Botones --------------------"
        boton_registrar = Button(frame_botones, text="REGISTRAR", command=self.Agregar_producto, height=2, width=10,
                                 bg="green", fg="white", font=("Comic Sans", 10, "bold"))
        boton_registrar.grid(row=0, column=1, padx=10, pady=15)

        "--------------- Tabla --------------------"
        self.tree = ttk.Treeview(height=10, columns=("columna1", "columna2"))

      

        self.tree.pack()

        "--------------- CRUD --------------------"

    def Agregar_producto(self):
        if self.Validar_formulario_completo():
            messagebox.showerror("showerror", "Error")("REGISTRO EXITOSO", f'Producto registrado: {self.combo_marca.get()}')
            print('REGISTRADO')
        self.Limpiar_formulario()

 
    
    

if __name__ == '__main__':
    # Crear la ventana principal
    root = Tk()

    root.title("steamcontrol")
    root.iconbitmap("imagenes/steamcontrol.ico")
    root.config(cursor="hand2")

    ventana_producto = Producto(root)


    #
    root.mainloop()
