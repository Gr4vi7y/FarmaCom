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

lista_original = {}
for i in range(1,len(f)):
    lista_original[f[i][0]] = [f[i][1], f[i][2], f[i][7], f[i][9], f[i][11], f[i][13], f[i][14]]
print(lista_original)
print(" ")   

lista_limpia = {}
for key,value in lista_original.items():
    if value not in lista_limpia.values():
        lista_limpia[key] = value
print(lista_limpia)
print(" ")

print(lista_limpia.keys())
print(" ")

medicamentos = {}
lf = list(lista_limpia.values())
key = list(lista_limpia.keys())
print(lf)
print(" ")

for j in range(0,len(lf)):
    medicamentos[key[j]] = Medicamento(lf[j][0], lf[j][1], lf[j][2], lf[j][3], lf[j][4], lf[j][5], lf[j][6])                        

print(medicamentos.keys())
print(" ")
print(medicamentos["40537"])
print(" ")
print(medicamentos["7235"])
print(" ")
print(medicamentos["18329"])
