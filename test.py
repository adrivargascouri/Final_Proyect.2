import tkinter as tk 

window = tk.Tk()
window.title ("Ventana de prueba")

button = tk.Button (window, text="Hola", command=window.quit)
button.pack()

window.mainloop()