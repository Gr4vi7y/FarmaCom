from pyexcel_ods import get_data
from time import time
import json

tiempo_inicial = time()
data = get_data("Medicamentos.ods")
f = data['Hoja1']

lista_original = {}
for i in range(1,len(f)):
    lista_original[f[i][0]] = {"Nombre": f[i][1], "Laboratorio": f[i][2], "Principios Activos": f[i][7],"Comercializado?": f[i][9], "Observaciones": f[i][11],"Afecta a la conduccion?": f[i][13],"Problemas de Suministro?": f[i][14]}
 

lista_limpia = {}
for key,value in lista_original.items():
    if value not in lista_limpia.values():
        lista_limpia[key] = value
print(lista_limpia)
print(" ")

with open('Medicamentos.json', 'w') as file:
    json.dump(lista_limpia, file, indent=4)

tiempo_final = time() 
tiempo_ejecucion = tiempo_final - tiempo_inicial
print('El tiempo de ejecucion fue: ',tiempo_ejecucion) #En segundos
