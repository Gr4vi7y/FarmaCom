#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk, font, filedialog

import numpy as np
from pyexcel_ods import get_data
from unidecode import unidecode
import json

import getpass

# La clase 'Aplicacion' ha crecido. En el ejemplo se incluyen
# nuevos widgets en el método constructor __init__(): Uno de
# ellos es el botón 'Info'  que cuando sea presionado llamará 
# al método 'verinfo' para mostrar información en el otro 
# widget, una caja de texto: un evento ejecuta una acción: 

class Farmacia():
    def __init__(self):

        # En el ejemplo se utiliza el prefijo 'self' para
        # declarar algunas variables asociadas al objeto 
        # ('mi_app')  de la clase 'Aplicacion'. Su uso es 
        # imprescindible para que se pueda acceder a sus
        # valores desde otros métodos:
        
        self.raiz = Tk()
        self.raiz.title('Farmacia')
        self.raiz.geometry('500x300')
        self.raiz.resizable(width=True,height=True)
        
        fuente = font.Font(weight='bold')
        self.etiq1 = ttk.Label(self.raiz, text="Buscar por referencia:", 
                               font=fuente)
        
        self.referencia = StringVar()
        self.referencia.set("Introduce la referencia")
        


    
        progress= ttk.Progressbar(self.raiz, orient = 'horizontal', length=120, mode = 'determinate')

        progress.pack()
        progress.config(mode='determinate', maximum=100, value=0)

        progress.start()



        
        self.ctext1 = ttk.Entry(self.raiz, 
                        textvariable=self.referencia, 
                        width=30)
        
        self.separ1 = ttk.Separator(self.raiz, orient=HORIZONTAL)
        
        self.boton1 = ttk.Button(self.raiz, text="Buscar", 
                         command=self.buscar)
        
        self.etiq1.pack(side=TOP, fill=BOTH, expand=True, 
                padx=5, pady=5)
        self.ctext1.pack(side=TOP, fill=X, expand=True, 
                         padx=100)
        
        
        self.boton1.pack(side=LEFT, fill=BOTH, expand=True, 
                 padx=5, pady=5)
        
        # Define el widget Text 'self.tinfo ' en el que se
        # pueden introducir varias líneas de texto:
        
        self.tinfo = Text(self.raiz, width=50, height=10)
        
        # Sitúa la caja de texto 'self.tinfo' en la parte
        # superior de la ventana 'self.raiz':
        
        self.tinfo.pack(side=TOP)
        
        # Define el widget Button 'self.binfo' que llamará 
        # al metodo 'self.verinfo' cuando sea presionado
        
        self.binfo = ttk.Button(self.raiz, text='Cargar Archivo', 
                                command=self.cargar_archivo)
        
        # Coloca el botón 'self.binfo' debajo y a la izquierda
        # del widget anterior
                                
        self.binfo.pack(side=LEFT)
        
        # Define el botón 'self.bsalir'. En este caso
        # cuando sea presionado, el método destruirá o
        # terminará la aplicación-ventana 'self.raíz' con 
        # 'self.raiz.destroy'
        
        self.bsalir = ttk.Button(self.raiz, text='Salir', 
                                 command=self.raiz.destroy)
                                 
        # Coloca el botón 'self.bsalir' a la derecha del 
        # objeto anterior.
                                 
        self.bsalir.pack(side=RIGHT)
        
        # El foco de la aplicación se sitúa en el botón
        # 'self.binfo' resaltando su borde. Si se presiona
        # la barra espaciadora el botón que tiene el foco
        # será pulsado. El foco puede cambiar de un widget
        # a otro con la tecla tabulador [tab]
        
        self.binfo.focus_set()
        self.raiz.mainloop()
        

        
    def buscar(self):
        referencia = self.referencia.get()
        self.verinfo(referencia)
    
    def verinfo(self, referencia):
        
        # Borra el contenido que tenga en un momento dado
        # la caja de texto
        
        self.tinfo.delete("1.0", END)
        
        # Obtiene información de la ventana 'self.raiz':
        
        info1 = inventario[referencia].nombre
        info2 = inventario[referencia].laboratorio
        info3 = inventario[referencia].principios
        info4 = str(inventario[referencia].comercializado)
        info5 = str(inventario[referencia].observaciones)
        info6 = str(inventario[referencia].conduccion)
        info7 = str(inventario[referencia].suministro)
        info8 = str(inventario[referencia].stock)
        info9 = str(inventario[referencia].sustitutos)
        
        # Construye una cadena de texto con toda la
        # información obtenida:
        
        texto_info = "Nombre: " + info1 + "\n"
        texto_info += "Laboratorio: " + info2 + "\n"
        texto_info += "Principios Activos: " + info3 + "\n"
        texto_info += "¿Comercializado?: " + info4 + "\n"
        texto_info += "¿Necesita receta?: " + info5 + "\n"
        texto_info += "¿Afecta a la conduccion?: " + info6 + "\n"
        texto_info += "¿Problemas de suministro?: " + info7 + "\n"
        texto_info += "Stock: " + info8 + "\n" 
        texto_info += "Medicamentos sustitutos: " + info9 + "\n"
        
        # Inserta la información en la caja de texto:
        
        self.tinfo.insert("1.0", texto_info)
        
    def cargar_archivo(self):
        
        global inventario
        self.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("ods files","*.ods"),("all files","*.*")))
        direccion_archivo = self.filename
        data = get_data(direccion_archivo)
        f = data['Hoja1']

        for i in range(1,len(f)):
            f[i][11]=unidecode(f[i][11])
            f[i][11]=f[i][11].lower()
        
        lista_original = {}
        for i in range(1,len(f)):
            if 'medicamento sujeto a prescripcion medica' in f[i][11]:
                lista_original[f[i][0]] = [f[i][1], f[i][2], f[i][7], f[i][9], True, f[i][13], f[i][14]]
            else:
                lista_original[f[i][0]] = [f[i][1], f[i][2], f[i][7], f[i][9], False, f[i][13], f[i][14]]


        lista_limpia = {}
        for key,value in lista_original.items():
            if value not in lista_limpia.values():
                lista_limpia[key] = value
                
        key = list(lista_limpia.keys())
        values = list(lista_limpia.values())        
        
        inventario = {}
        for j in range(0, len(key)):
            if values[j][6] == 'SI':
                stock=np.random.poisson(2)
            else:
                stock=np.random.poisson(5)
            inventario[key[j]] = {"Nombre": values[j][0],"Laboratorio": values[j][1],"Principios Activos": values[j][2],"Comercializado?": values[j][3],"Prescripcion Medica": values[j][4],"Afecta a la conduccion?": values[j][5],"Problemas de Suministro?": values[j][6], "Stock": stock, "Sustitutos": []}       
        
        with open('prueba_con_stock.json', 'w') as file:
            json.dump(inventario, file)
            
        with open('prueba_con_stock.json', 'r') as file:
            inventario_cargado = json.load(file)
            
        claves = list(inventario_cargado.keys())
        valores = list(inventario_cargado.values())
        
        inventario_final = {}
        for i in range (0, len(claves)):
            inventario_final[claves[i]] = Medicamento(valores[i]["Nombre"], valores[i]["Laboratorio"], valores[i]["Principios Activos"], valores[i]["Comercializado?"], valores[i]["Prescripcion Medica"], valores[i]["Afecta a la conduccion?"], valores[i]["Problemas de Suministro?"], 0 , valores[i]["Stock"])
        
        lista_equivalentes = {}    
        for i in range(0, len(inventario_final)):
            principios1=inventario_final[claves[i]].principios
            prescripcion1=inventario_final[claves[i]].observaciones
            principios_separados_i=principios1.split(",")
            lista_equivalentes[claves[i]] = []
            
            for j in range(0, len(inventario_cargado)):
                principios2=inventario_final[claves[j]].principios
                prescripcion2=inventario_final[claves[j]].observaciones
                principios_separados_j=principios2.split(",")
                if prescripcion1==prescripcion2 or prescripcion1==True:
                    if principios_separados_i == principios_separados_j and i != j:
                        lista_equivalentes[claves[i]].append(claves[j])
                        
              
        lf = list(inventario_final.values())
        key = list(inventario_final.keys())
        le = lista_equivalentes   
        inventario = {}

        for j in range(0,len(lf)):
            inventario[key[j]] = Medicamento(lf[j].nombre, lf[j].laboratorio, lf[j].principios, lf[j].comercializado, lf[j].observaciones, lf[j].conduccion, lf[j].suministro, le[key[j]], lf[j].stock)                        
        print(key)

        
class Medicamento(object):
    """ Clase Medicamento. Representa un Medicamento.
    Atributos
    ---------
    nombre = string
    laboratorio = string
    principios = string
    comercializado = boolean
    observaciones = boolean
    conduccion = boolean
    suministro = int
    existencias = int
    
    
    """
    def __init__(self, nombre_med, lab_med, p_act, comer, obs, afect_cond, prob_sum, sust, stock):
        self.nombre = nombre_med
        self.laboratorio = lab_med 
        self.principios = p_act 
        self.comercializado = comer 
        self.observaciones = obs
        self.conduccion = afect_cond
        self.suministro = prob_sum
        self.stock = stock
        self.sustitutos = sust

    def __str__(self):
        datos = "Nombre: " + self.nombre + "\nLaboratorio: " + self.laboratorio + "\nPrincipios Activos: " + self.principios + "\nComercializado: " + str(self.comercializado) + "\nPrescripcion: " + str(self.observaciones) + "\nAfecta a conduccion: " + str(self.conduccion) + "\nProblemas de suministro: " + str(self.suministro) + "\nStock: " + str(self.stock) + "\nSustitutos: " + str(self.sustitutos)
        return datos
    
    def sustituto(self):
        sust = "Las referencias de los medicamentos sustitutos son: " + str(self.sustitutos)
        return sust
    
    def reponer_auto(self):
        if self.suministro == 'SI':
            self.stock= self.stock + np.random.poisson(2)
        else:
            self.stock= self.stock + np.random.poisson(5)
        return self.stock
    
    def reponer_manual(self, cantidad):
        self.stock = self.stock + cantidad
        return self.stock

def main():
    mi_app = Farmacia()
    return 0

if __name__ == '__main__':
    main()
