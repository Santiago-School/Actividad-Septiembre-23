print(" ")
print(" Santiago Carrasco Tarea2.5 En esta ocacion el usuario debe adivinar un numero del 1 al 7")
print(" ")
# numero paraa adivinar
numero = 7  # se puede cambiar este número

# pedir al usuario que adivine
adivinanza = int(input("adivina el numero (0-10): "))

# comprobar si adivinó
if adivinanza == numero:
    print("correcto! adivinaste el numero")
else:
    print("intenta de nuevo")
