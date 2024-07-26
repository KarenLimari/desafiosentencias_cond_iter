#Actividad 1 - IMC
# El IMC, conocido también como el Índice de masa corporal, es una medida que asocia el peso de una persona con su talla (su altura). Este valor es utilizado normalmente como un indicador nutricional y constituye un índice fácil y sencillo de calcular para determinar el estado de obesidad y sobrepeso de una persona. El IMC se calcula de la siguiente manera:

#IMC = W / H^2

#W : corresponde al peso de la persona en Kg.
#H: corresponde a la altura en metros.
#IMC: EL valor del IMC, en [Kg/m2]
#Para ello, la Organización Mundial de la Salud (OMS) ha determinado una clasificación así para distintos rangos de valores.

#IMC Clasificación OMS
#< 18.5 Bajo Peso
#[ 18.5, 25 [ Adecuado
#[ 25, 30 [ Sobrepeso
#[ 30, 35[ Obesidad Grado I
#[ 35, 40 [ Obesidad Grado II
#> 40 Obesidad Grado III

#En busca de mejorar la salud nutricional de los pacientes, se le solicita a usted como programador el hecho de diseñar una herramienta que permita determinar el estado nutricional de una persona.

#Paso 1 
#Determinar variables
import math
peso = int(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros: "))

#Paso 2 
#Determinar las variables para la fórmula de imc
imc = peso / altura **2
imc = math.ceil(imc)
print(f"Tu índice de masa corporal es: {imc} kg/m2")

#Paso 3
#condiciones
if imc < 18.5:
    print("La clasificación OMS es: Bajo peso")

#Output