import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os
import shutil


class EncodeWindow(tk.Frame):
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
        btn.grid(row=1, column=0, padx=0, pady=0, sticky="nw")

        # Cargar el icono y asignarlo al botón
        icon_image = tk.PhotoImage(file=icon_retry_path)
        icon_image_reduced = icon_image.subsample(30, 30)
        btn.config(image=icon_image_reduced)
        btn.image = icon_image_reduced

        # Etiqueta en el centro superior
        titleWindow = tk.Label(self, text="Ventana de Codificación", font=("Arial", 13), fg="white", bg="black")
        titleWindow.grid(row=2, column=0, pady=10)

        # Párrafo de información
        description = """
        Programa de Esteganografia utilizando la combinación de la Transformada de Fourier, Wavelet y Z.
        El proceso puede llevarse a cabo en señales de audio para ocultar informacion como texto plano, audios, e imagenes.
        """
        description_text = tk.Label(self, text=description, font=("Arial", 10), fg="white", bg="black", justify="left")
        description_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        # Etiqueta archivo a esconder
        label_secret_message = tk.Label(self, text="Archivo a escoder", font=("Arial", 12), fg="white", bg="black")
        label_secret_message.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        # Botón desplegable para seleccionar formato
        self.format_var = tk.StringVar()
        self.format_combobox = ttk.Combobox(self, textvariable=self.format_var, values=["texto", "audio", "imagen"], state="readonly", font=("Arial", 12))
        self.format_combobox.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        # Botón para seleccionar archivo
        self.select_btn = ttk.Button(self, text="Seleccionar archivo", command=self.select_file)
        self.select_btn.grid(row=4, column=1, columnspan=2, padx=10, pady=10)

        # Label para mostrar el nombre del archivo cargado
        self.label_name_file = ttk.Label(self, text="", background='black', foreground='white')
        self.label_name_file.grid(row=5, column=1, columnspan=2, padx=10, pady=10)

        # Label para mostrar el tipo de archivo
        self.label_type_file = ttk.Label(self, text="", background='black', foreground='white')
        self.label_type_file.grid(row=6, column=1, columnspan=2, padx=10, pady=10)

        # Etiqueta de la contrasena
        label_password = tk.Label(self, text="Contraseña", font=("Arial", 12), fg="white", bg="black")
        label_password.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

        # Espacio para escribir la contraseña
        self.password_entry = ttk.Entry(self, width=40)
        self.password_entry.grid(row=7, column=1, columnspan=2, padx=10, pady=10)

        # Etiqueta del archivo receptor
        label_file_receiver = tk.Label(self, text="Archivo a receptor", font=("Arial", 12), fg="white", bg="black")
        label_file_receiver.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

        # Botón para seleccionar archivo receptor
        self.select_audio_btn = ttk.Button(self, text="Seleccionar archivo de audio", command=self.select_audio_file)
        self.select_audio_btn.grid(row=9, column=0, columnspan=2, padx=10, pady=10)

        # Label para mostrar el nombre del archivo receptor cargado
        self.label_audio_receiver_file = ttk.Label(self, text="", background='black', foreground='white')
        self.label_audio_receiver_file.grid(row=8, column=1, columnspan=2, padx=10, pady=10)

        # Label para mostrar el tipo de archivo receptor
        self.label_audio_receiver_format = ttk.Label(self, text="", background='black', foreground='white')
        self.label_audio_receiver_format.grid(row=9, column=1, columnspan=2, padx=10, pady=10)

        

        # Botón para codificar
        self.btn_encoder = ttk.Button(self, text="Codificar", command=self.encoder_audio)
        self.btn_encoder.grid(row=10, column=0, columnspan=2, padx=10, pady=10)

    def select_file(self):
        format_file = self.format_var.get()
        if format_file == "texto":
            types = [("Archivos de texto", "*.txt")]
        elif format_file == "audio":
            types = [("Archivos de audio", "*.mp3;*.wav")]
        elif format_file == "imagen":
            types = [("Archivos de imagen", "*.jpg;*.jpeg;*.png")]
        else:
            types = []
        file_selected = filedialog.askopenfilename(filetypes=types)
        if file_selected:
            print(f"Archivo seleccionado: {file_selected}")
            self.label_name_file.config(text=f"Archivo: {file_selected}")
            type_file = file_selected.split(".")[-1]
            self.label_type_file.config(text=f"Tipo: {format_file}")
            # Guardar archivo en la carpeta temporal
            try:
                name_new_file_hide = "object_hide"+"."+type_file
                shutil.copy(file_selected, os.path.join(os.path.dirname(__file__),"../temp/message", name_new_file_hide))
                print(f"Archivo copiado a la carpeta temporal")
            except Exception as e:
                print(f"Error al copiar el archivo: {e}")

    def select_audio_file(self):
        types = [("Archivos de audio", "*.mp3;*.wav")]
        file_selected = filedialog.askopenfilename(filetypes=types)
        if file_selected:
            print(f"Archivo seleccionado: {file_selected}")
            self.label_audio_receiver_file.config(text=f"Archivo: {file_selected}")
            type_file = file_selected.split(".")[-1]
            self.label_audio_receiver_format.config(text=f"Tipo: {type_file}")
            try:
                name_new_file_receiver = "object_hide"+"."+type_file
                shutil.copy(file_selected, os.path.join(os.path.dirname(__file__),"../temp/receiver", name_new_file_receiver))
                print(f"Archivo receptor copiado a la carpeta temporal")
            except Exception as e:
                print(f"Error al copiar el archivo: {e}")

    def encoder_audio(self):
        formato = self.format_var.get()
        password_encoder = self.password_entry.get()
        print(f"Formato seleccionado: {formato}, Texto: {password_encoder}")
        # Guardar texto en un archivo de texto
        try:
            with open(os.path.join(os.path.dirname(__file__), "../temp", "password_text.txt"), "w") as file:
                file.write(password_encoder)
            print("Texto guardado en el archivo password_text.txt")
        except Exception as e:
            print(f"Error al guardar el texto en el archivo: {e}")
        

    def change_main_view(self):
        from main import MainWindow
        self.main_window = MainWindow(self)
        self.main_window.place(x=0, y=0, relwidth=1, relheight=1)



if __name__ == "__main__":
    app = EncodeWindow()
    app.mainloop()