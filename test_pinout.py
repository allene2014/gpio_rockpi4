import periphery
import os
gpio_direction = "/sys/class/gpio/gpio23/direction"

#input("Que pin desea manipular")

#with open(gpio_direction, "w") as f:
#       f.write("in")

gpio_direction = "/sys/class/gpio/gpio23/direction"

# Verifica si el archivo existe y es accesible
if os.path.isfile(gpio_direction) and os.access(gpio_direction, os.R_OK):
    # Abre el archivo en modo lectura y lee su contenido
    with open(gpio_direction, "r") as f:
        content = f.read().strip()

    # Comprueba si el contenido es "out"
    if content == "out":
        print("El pin GPIO 23 está exportado y configurado como salida.")
    else:
        print("El pin GPIO 23 está exportado pero no se encuentra configurado como salida.")
else:
    print("El pin GPIO 23 no está exportado o no se tiene acceso al archivo de dirección.")
print("---------------------------------------------------------------------------------------------")
print("------------------------------R-O-C-K--P I--4------------------------------------------------")
print("---------------------------------------------------------------------------------------------")
hquestions=input("Desea enviar comandos a los pines? \n 'Y / N' \n")

if hquestions == "Y":
    salida =input("escriba el comando para la salida 'out / on' \n")
    with open(gpio_direction, "w") as f:
        f.write(salida)
#elif hquestions != "Y" or hquestions != "N":
#    print("Por favor ingrese una respuesta Valida, 'Y/N'... \n")
else:
    print ("saliendo..")







