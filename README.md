# Titulo del proyecto

Desafío sentencias condicionales e iterativas

## Descripción del proyecto

Realizar 2 ejercicios aplicando los conceptos aprendidos en clase:
Actividad 1 - IMC
Se solicita crear el programa imc.py que permita calcular el IMC de una persona.

1. Al programa se debe ingresar el peso en Kg y la talla (altura) en centímetros.
   (1 Puntos)
2. Calcular el IMC ajustando los valores de entrada a las unidades requeridas por la
   fórmula. El resultado se debe informar con 2 decimales.
   (2 Puntos)
3. Entregar al usuario una salida acorde que permita conocer el valor de su IMC
   además de la clasificación dada por la OMS.
   (2 Puntos)

Actividad 2 - Cachipún

1. Se pide crear el programa cachipun.py, donde el usuario entregará como
   argumento: piedra, papel o tijera. Para que el computador pueda jugar escogerá un
   valor al azar. Para eso se solicita investigar random.choice() de la librería random.
   (1 Puntos)
1. Considerar las opciones de ganar, perder o empatar con la computadora.
   (2 Puntos)
1. En caso que el argumento sea distinto a piedra, papel o tijera, el programa debe
   mostrar las opciones que se pueden jugar.
   (2 Puntos)

# Inicio cachipun es un juego

import random

# Lista de opciones disponibles

cachipun = ["tijera", "papel", "piedra"]

# Selección aleatoria de la opción de la computadora

computador = random.choice(cachipun)

# Solicitar la jugada del usuario

usuario = input("Ingresa tu jugada: ")

# Mostrar las jugadas realizadas

print(f"Tu jugaste {usuario}")
print(f"Computador jugó {computador}")

# Validación y determinación del resultado

if usuario not in cachipun:
print("Argumento inválido: Debe ser piedra, papel o tijera.")
elif usuario == computador:
print("¡Empate!")
elif (usuario == "piedra" and computador == "tijera") or \
 (usuario == "papel" and computador == "piedra") or \
 (usuario == "tijera" and computador == "papel"):
print("¡Tú ganaste!")
else:
print("¡Perdiste!")

#fin

# desafio.juego

## Prerrequisitos o Dependencias

Lista de software y herramientas, incluyendo versiones, que necesitas para instalar y ejecutar este proyecto:

- Sistema Operativo Window, Linux, MacOS
- Lenguaje de programación python 3.12

## Instalación del Proyecto

Clona el repositorio

```bash
git clone git@github.com:KarenLimari/desafiosentencias_cond_iter.git
```

Ingresa a la carpeta del proyecto

```bash
cd desafiosentencias_cond_iter
```

## Instrucciones para Ejecutar el Proyecto

Ejecutar el siguiente comando

```bash
python imc.py
```

## Autor

[Karen Limari](https://github.com/KarenLimari)
[Ambar Zambrano](https://github.com/ambrazv)

## Licencia

Este proyecto está bajo la Licencia MIT - ve el archivo [LICENSE.md](LICENSE) para detalles
