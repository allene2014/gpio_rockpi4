from periphery import GPIO
pins = []

# Definir una lista con los números de pin que deseas utilizar
pin_numbers = [7,12,15,16,18,22,29,31,32,33,35,36,37,38,40] # 15 GPIO: disponibles segun documentacion oficial radxa.com 

#verificar si los pines estan en uso
for pn in pin_numbers:
    try:
        gpio_pin = periphery.GPIO(pn)
        used_pins.append(pn)
        gpio_pin.close()
    except: #periphery.GPIOError as e:
        print(f"El pin {pn} está siendo utilizado por otro recurso")#: {e}")
    try:
        gpio_pin = periphery.GPIO(pn)
        gpio_pin.close()
        print(f"El pin {pn} ha sido liberado exitosamente.")
    except: #periphery.GPIOError as e:
        print(f"No se pudo liberar el pin {pn}:") #{e}")
 

# Crear una función para manejar el evento cuando se detecte un cambio en el pin
def event_handler(pin):
    if pin.read():
        print(f"Pin {pin.number} ha sido activado")
        # Realizar alguna acción cuando el pin esté activado (on)
    else:
        print(f"Pin {pin.number} ha sido desactivado")
        # Realizar alguna acción cuando el pin esté desactivado (off)

try:
    # Crear objetos GPIO para cada número de pin especificado y configurarloxs como entradas (inputs)
    pins = [GPIO(pin_number, "in") for pin_number in pin_numbers]

    # Configurar las funciones de callback para cada objeto GPIO creado anteriormente
    for i in range(len(pins)):
        pins[i].callback(event_handler)

    input("Presiona Enter para finalizar...")

finally:
    # Asegúrate de liberar los recursos al finalizar.
    for i in range(len(pins)):
        pins[i].close()