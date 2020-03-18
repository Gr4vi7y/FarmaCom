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
    
    """
    def __init__(self, nombre_med, lab_med, p_act, comer, obs, afect_cond, prob_sum):
        self.nombre = nombre_med
        self.laboratorio = lab_med 
        self.principios = p_act 
        self.comercializado = comer 
        self.observaciones = obs
        self.conduccion = afect_cond
        self.suministro = prob_sum
        self.stock = 2
    def __str__(self):
        datos = "Nombre: " + self.nombre + "\nLaboratorio: " + self.laboratorio + "\nPrincipios Activos: " + self.principios + "\nComercializado: " + str(self.comercializado) + "\nPrescripcion: " + str(self.observaciones) + "\nAfecta a conduccion: " + str(self.conduccion) + "\nProblemas de suministro: " + str(self.suministro) + "\nStock: " + str(self.stock)
        return datos


    
from pyexcel_ods import get_data

data = get_data("Medicamentos.ods")
f = data['Hoja1']



from unidecode import unidecode


for i in range(1,len(f)):

    f[i][11]=unidecode(f[i][11])
    f[i][11]=f[i][11].lower()


print(" ")


        
lista_original = {}
for i in range(1,len(f)):
    if 'medicamento sujeto a prescripcion medica' in f[i][11]:
        lista_original[f[i][0]] = [f[i][1], f[i][2], f[i][7], f[i][9], 'True', f[i][13], f[i][14]]
    else:
        lista_original[f[i][0]] = [f[i][1], f[i][2], f[i][7], f[i][9], 'False', f[i][13], f[i][14]]

lista_limpia = {}
for key,value in lista_original.items():
    if value not in lista_limpia.values():
        lista_limpia[key] = value
        

key = list(lista_limpia.keys())
values = list(lista_limpia.values())


inventario = {}
for i in range(0, len(key)):
    inventario[key[i]] = {"Nombre": values[i][0],"Laboratorio": values[i][1],"Principios Activos": values[i][2],"Comercializado?": values[i][3],"Prescripcion Medica": values[i][4],"Afecta a la conduccion?": values[i][5],"Problemas de Suministro?": values[i][6]}

import json
with open('Medicamentos.json', 'w') as file:
    json.dump(inventario, file)

with open('MedicamentosVisible.json', 'w') as file:
    json.dump(inventario, file, indent=4)
