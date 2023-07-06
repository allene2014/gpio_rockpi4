import periphery
import sys

argumentos = sys.argv[1:]

pi = argumentos[0]
st = argumentos[1]

rock_pins = [75,149,154,157,74,73,112,76,158]
def controlar_dispositivo(pi, st):

    pin = pi.strip(',')  # Eliminar comas y otros caracteres no deseados
    pin_int = int(pin)

    # Verificar si el PIN es correcto
    if pin_int in rock_pins:
        action = st
        if action == "encender":
            try:
                gpio_output = periphery.GPIO(pin_int, "out") 
                gpio_output.write(True)  # Enciende el dispositivo estableciendo la salida a True
                print("El dispositivo ha sido encendido.")
            except Exception as e:
                print(f"No se pudo encender el dispositivo: {e}")
        elif action == "apagar":
            try:
                gpio_output = periphery.GPIO(pin_int, "out")  
                gpio_output.write(False)  # Apaga el dispositivo estableciendo la salida a False
                print("El dispositivo ha sido apagado.")
            except Exception as e:
                print(f"No se pudo apagar el dispositivo: {e}")

controlar_dispositivo(pi, st)