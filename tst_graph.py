import RPi.GPIO as GPIO
import tkinter as tk

# Configuración inicial de los pines GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT) # Pin 17 configurado como salida


class App:
    def __init__(self, master):
        self.master = master
        master.title("Controlador de Puertos GPIO")
        
        # Botón para abrir el puerto gpio 17
        self.btn_on = tk.Button(master, text="Abrir", command=self.open_port)
        self.btn_on.pack()
        
        # Botón para cerrar el puerto gpio 17
        self.btn_off = tk.Button(master, text="Cerrar", command=self.close_port)
        self.btn_off.pack()
        
    def open_port(self):
        	GPIO.output(17, True)

    def close_port(self):
        	GPIO.output(17,False)


root = tk.Tk()
app = App(root)
root.mainloop()

# Limpiamos y liberamos los recursos utilizados por los pines gpio antes de salir del programa.
GPIO.cleanup()