#!/usr/bin/python
import mraa
import time

# Definimos las variables correspondientes a cada pin que queremos usar
LED_PIN = 12 # Pin correspondiente al LED rojo del Rock Pi 4 (GPIO1_B6)
BUTTON_PIN = 11 # Pin correspondiente al botón SW2 del Rock Pi 4 (GPIO1_B7)

# Creamos objetos "Gpio" para cada uno de los pines definidos anteriormente.
led_gpio = mraa.Gpio(LED_PIN)
button_gpio = mraa.Gpio(BUTTON_PIN)

# Configuramos el pin del LED como salida y lo apagamos inicialmente.
led_gpio.dir(mraa.DIR_OUT)
led_gpio.write(0)

# Configuramos el pin del botón como entrada y habilitamos su resistencia pull-up interna.
button_gpio.dir(mraa.DIR_IN)
button_gpio.mode(mraa.MODE_PULLUP)

try:
    while True:
        # Leemos el estado actual del botón. Si está presionado se enciende el LED, sino se apaga.
        if button_gpio.read() == 0:
            led_gpio.write(1) 
            print("Boton pulsado")
        else:
            led_gpio.write(0) 
            print("Boton no pulsado")
        
        time.sleep(0.1)

except KeyboardInterrupt: # Manejador de excepciones por si se interrumpe manualmente la ejecución del script.
    pass

finally:
    # Liberamos los recursos utilizados por los pines antes de salir del programa.
    led_gpio.write(0)
    del led_gpio, button_gpio