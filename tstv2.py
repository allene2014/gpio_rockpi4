from periphery import GPIO
#import paho.mqtt.client as mqtt #test mqtt 

pins_ps = \
    {'75':'7/75','149':'15/149','154':'16/154','157':'22/157','74':'29/74','73':'31/73','112':'32/112','76':'33/76','158':'37/158'}
rp = \
    {'75':'7','149':'15','154':'16','157':'22','74':'29','73':'31','112':'32','76':'33','158':'37'}

# Definimos una función para obtener el estado del pin.
def get_pin_status(pin):
    gpio = GPIO(int(pin), "in")
    status = gpio.read()
    gpio.close()
    
    return status

# Definimos una función para configurar varios pines con sus respectivos estados.
def set_pins(pins):
  for pin in pins:
    pnr = pin['number']
    try:
        # Intentamos crear un objeto utilizando la biblioteca periphery y configurarlo según corresponda.
        gpio_object = GPIO(int(pin['number']), "out")
        if bool(pin['status']):
            gpio_object.write(True)
            print(f"PIN {rp.get(str(pnr))} Encendido.") 
            
        else:
            gpio_object.write(False)
            print(f"PIN {rp.get(str(pnr))} Apagado.")
        # Liberamos recursos utilizados por este objeto específico antes de continuar con otro PIN. 
        gpio_object.close()
    except ValueError:
      print(f"{pin} no es un número válido")
def comunicationPy(rk1, rk2, rk3) #rk1 pines a encender "1,2,3" #k2 status bool "1,0" # Reset pines (s/n)
    # Definimos una lista vacía donde almacenaremos los objetos correspondientes a cada pin.
    pins_data = []
    #rock_pins = [75,131,149,154,156,157,74,73,112,76,133,132,158,134,135] #pines GPIO documentacion
    rock_pins = [75,149,154,157,74,73,112,76,158]
    
    for rpin in rock_pins:
        try:
            gpio_object = GPIO(int(rpin),"out")
            pins_data.append({
                'number': int(rpin),
                'status': get_pin_status(rpin)
            })
            gpio_object.close()
        except ValueError:
          print(f"{rpin} no es un número válido")
        print(f"PIN {rpin} agregado correctamente.")
    
    print("Datos finales:")
    # Recorremos el objeto para asignar al usuario una vista de los puertos y su status
    for data in pins_data:
        pnr = data['number']
        pns = data['status']
        print(f"Pin: {pins_ps.get(str(pnr))} - Estado: {'Encendido' if pins_ps.get(str(pns)) else 'Apagado'}")
    
    # Solicitamos al usuario los pines a encender y su estado.
    pins_to_set = input("Ingrese lista de pines a encender separados por coma (Ejemplo: 1,2,3): ")
    desired_state = input("Estado deseado (0 para apagado o 1 para encendido): ")
    
    # Creamos una lista de diccionarios donde cada uno representa un pin a configurar junto con su estado deseado.
    pins_to_set_list = [{'number': int(x), 'status': bool(int(desired_state))} for x in pins_to_set.split(',')]
    
    # Configuramos los pines según corresponda utilizando la función set_pins definida anteriormente.
    set_pins(pins_to_set_list)

# Agregamos una nueva función que resetea todos los pines activos a su estado por defecto (apagados).
def reset_pins():
    for pin in pins_data:
        try:
            gpio_object = GPIO(pin['number'], "out")
            
            if bool(pin['status']):
                gpio_object.write(False)
                print(f"PIN {pin['number']} Apagado.")
            # Liberamos recursos utilizados por este objeto específico antes de continuar con otro PIN. 
            gpio_object.close()

        except ValueError:
          print(f"{pin} no es un número válido")

# Solicitamos al usuario si desea resetear los pines activos.
reset_pins_input = input("¿Desea resetear los pines activos? (s/n): ")

if reset_pins_input.lower() == 's':
    reset_pins()
    print("Pines activos reiniciados correctamente.")
else:
    print("No se reiniciaron los pines activos.")
