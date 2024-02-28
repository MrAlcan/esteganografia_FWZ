import tkinter as tk
from tkinter import ttk
import os
from main import MainWindow

class PresentationWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Esteganografia en audio")
        self.geometry("800x600")  # Tamaño específico
        self.configure(background='black')  # Color de fondo para el opaco

        # Obtener la ruta absoluta de la imagen
        image_path = os.path.join(os.path.dirname(__file__), "resources/img", "background.png")

        # Cargar la imagen de fondo
        self.image_background = tk.PhotoImage(file=image_path)
        self.label_background = tk.Label(self, image=self.image_background)
        self.label_background.place(x=0, y=0, relwidth=1, relheight=1)

        # Opacar la imagen de fondo
        self.label_background.configure(bg="black")
        self.label_background.place(relwidth=1, relheight=1)

        # Crear una barra de progreso
        self.progress_bar = ttk.Progressbar(self, orient='horizontal', length=400, mode='determinate')
        self.progress_bar.place(relx=0.5, rely=0.5, anchor='center')

        # Crear texto de carga
        self.loading_text = tk.Label(self, text="Cargando la aplicación...", font=("Arial", 16), fg="white", bg="black")
        self.loading_text.place(relx=0.5, rely=0.6, anchor='center')

        # Llenar la barra de progreso gradualmente
        self.porcentage = 0
        self.fill_progress_bar()

    def fill_progress_bar(self):
        if self.porcentage <= 100:
            self.progress_bar["value"] = self.porcentage
            self.porcentage += 1
            self.after(10, self.fill_progress_bar)
        else:
            #print("llego al else")
            self.change_view()

    def change_view(self):
        #print("estamos en el cambio de vista")
        self.main_window = MainWindow(self)
        self.main_window.place(x=0, y=0, relwidth=1, relheight=1)
        #self.main_window.place(relx=0.5, rely=0.5, anchor='center')
        #self.main_window.tkraise()
        #print("En teoria ya deberia cambiar de pantalla")


if __name__ == "__main__":
    app = PresentationWindow()
    app.mainloop()
