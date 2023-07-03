
from periphery import GPIO

# Definimos una función para obtener el estado del pin.
def get_pin_status(pin):
    gpio = GPIO(int(pin), "in")
    status = gpio.read()
    gpio.close()
    
    return status

# Definimos una función para configurar varios pines con sus respectivos estados.
def set_pins(pins):
  for pin in pins:
      try:
          # Intentamos crear un objeto utilizando la biblioteca periphery y configurarlo según corresponda.
          gpio_object = GPIO(int(pin['number']), "out")
          
          if bool(pin['status']):
              gpio_object.write(True)
              print(f"PIN {pin['number']} Encendido.")
              
          else:
              gpio_object.write(False)
              print(f"PIN {pin['number']} Apagado.")

          # Liberamos recursos utilizados por este objeto específico antes de continuar con otro PIN. 
          gpio_object.close()

      except ValueError:
        print(f"{pin} no es un número válido")

# Definimos una lista vacía donde almacenaremos los objetos correspondientes a cada pin.
pins_data = []

while True:
    # Obtenemos desde el usuario la entrada correspondiente al siguiente pin a agregar o "q" para salir.
    next_pin_input = input("Ingrese próximo PIN ('q' para salir): ")
    
    if next_pin_input.lower() == 'q':
        break
    
    try:
        # Intentamos crear un objeto utilizando la biblioteca periphery y lo agregamos a nuestra lista de datos.
        gpio_object = GPIO(int(next_pin_input), "out")
        
        pins_data.append({
            'number': int(next_pin_input),
            'status': get_pin_status(next_pin_input)
        })
        
        print(f"PIN {next_pin_input} agregado correctamente.")
        
        # Liberamos recursos utilizados por este objeto específico antes de continuar con otro PIN. 
        gpio_object.close()

    except ValueError:
      print(f"{next_pin_input} no es un número válido")

print("Datos finales:")
for data in pins_data:
  print(f"Pin: {data['number']} - Estado: {'Encendido' if data['status'] else 'Apagado'}")

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

