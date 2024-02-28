import tkinter as tk
from tkinter import ttk
import os


class DecodeWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.configure(background='black')  # Color de fondo para el opaco
        
        # Obtener la ruta absoluta de la imagen
        image_path = os.path.join(os.path.dirname(__file__), "resources/img", "background.png")
        icon_retry_path = os.path.join(os.path.dirname(__file__), "resources/img", "icon_retry.png")


        # Cargar la imagen de fondo
        self.image_background = tk.PhotoImage(file=image_path)
        self.label_background = tk.Label(self, image=self.image_background)
        self.label_background.place(x=0, y=0, relwidth=1, relheight=1)

        # Opacar la imagen de fondo
        self.label_background.configure(bg="black")
        self.label_background.place(relwidth=1, relheight=1)

        # Título del programa en una esquina superior
        title = tk.Label(self, text="Esteganografia en señales de audio con Fourier Wavelet y Z", font=("Arial", 14), fg="white", bg="black")
        title.grid(row=0, column=0, columnspan=2, sticky="nw", padx=10, pady=10)

        btn = ttk.Button(self, text="Volver", compound=tk.TOP, command=self.change_main_view)
        #btn.grid(row=3 + i//2, column=i%2, padx=10, pady=10, rowspan=2, sticky="nesw")
        btn.grid(row=1, column=0, padx=0, pady=0, sticky="nw")

        # Cargar el icono y asignarlo al botón
        icon_image = tk.PhotoImage(file=icon_retry_path)
        icon_image_reduced = icon_image.subsample(30, 30)
        btn.config(image=icon_image_reduced)
        btn.image = icon_image_reduced

        # Etiqueta en el centro superior
        titleWindow = tk.Label(self, text="Ventana de decodificación del Programa", font=("Arial", 13), fg="white", bg="black")
        titleWindow.grid(row=2, column=0, pady=10)

        # Párrafo de información
        description = """
        Programa de Esteganografia utilizando la combinación de la Transformada de Fourier, Wavelet y Z.
        El proceso puede llevarse a cabo en señales de audio para ocultar informacion como texto plano, audios, e imagenes.
        """
        description_text = tk.Label(self, text=description, font=("Arial", 10), fg="white", bg="black", justify="left")
        description_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def change_main_view(self):
        from main import MainWindow
        self.main_window = MainWindow(self)
        self.main_window.place(x=0, y=0, relwidth=1, relheight=1)



if __name__ == "__main__":
    app = DecodeWindow()
    app.mainloop()