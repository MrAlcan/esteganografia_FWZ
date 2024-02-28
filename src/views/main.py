import tkinter as tk
from tkinter import ttk
import os




class MainWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.configure(background='black')  # Color de fondo para el opaco
        '''
        self.help_window = HelpWindow(self)
        self.encode_window = EncodeWindow(self)
        self.decode_window = DecodeWindow(self)
        self.information_window = InformationWindow(self)'''
        
        # Obtener la ruta absoluta de la imagen
        image_path = os.path.join(os.path.dirname(__file__), "resources/img", "background.png")
        icon_help_path = os.path.join(os.path.dirname(__file__), "resources/img", "icon_help.png")
        icon_info_path = os.path.join(os.path.dirname(__file__), "resources/img", "icon_info.png")
        icon_encode_path = os.path.join(os.path.dirname(__file__), "resources/img", "icon_encoder.png")
        icon_decode_path = os.path.join(os.path.dirname(__file__), "resources/img", "icon_decoder.png")

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

        # Etiqueta en el centro superior
        titleWindow = tk.Label(self, text="Menú del Programa", font=("Arial", 13), fg="white", bg="black")
        titleWindow.grid(row=1, column=0, pady=10)

        # Párrafo de información
        description = """
        Programa de Esteganografia utilizando la combinación de la Transformada de Fourier, Wavelet y Z.
        El proceso puede llevarse a cabo en señales de audio para ocultar informacion como texto plano, audios, e imagenes.
        """
        description_text = tk.Label(self, text=description, font=("Arial", 10), fg="white", bg="black", justify="left")
        description_text.grid(row=2, column=0, columnspan=2, padx=10, pady=10)


        btn1 = ttk.Button(self, text="Codificar", compound=tk.TOP, command=self.change_encode_view)
        #btn.grid(row=3 + i//2, column=i%2, padx=10, pady=10, rowspan=2, sticky="nesw")
        btn1.grid(row=4 + 0//2, column=0%2, padx=10, pady=10)

        # Cargar el icono y asignarlo al botón
        icon_image1 = tk.PhotoImage(file=icon_encode_path)
        icon_image_reduced1 = icon_image1.subsample(5, 5)
        btn1.config(image=icon_image_reduced1)
        btn1.image = icon_image_reduced1





        btn2 = ttk.Button(self, text="Decodificar", compound=tk.TOP, command=self.change_decode_view)
        #btn.grid(row=3 + i//2, column=i%2, padx=10, pady=10, rowspan=2, sticky="nesw")
        btn2.grid(row=4 + 1//2, column=1%2, padx=10, pady=10)

        # Cargar el icono y asignarlo al botón
        icon_image2 = tk.PhotoImage(file=icon_decode_path)
        icon_image_reduced2 = icon_image2.subsample(5, 5)
        btn2.config(image=icon_image_reduced2)
        btn2.image = icon_image_reduced2




        btn3 = ttk.Button(self, text="Informacion", compound=tk.TOP, command=self.change_info_view)
        #btn.grid(row=3 + i//2, column=i%2, padx=10, pady=10, rowspan=2, sticky="nesw")
        btn3.grid(row=4 + 2//2, column=2%2, padx=10, pady=10)

        # Cargar el icono y asignarlo al botón
        icon_image3 = tk.PhotoImage(file=icon_info_path)
        icon_image_reduced3 = icon_image3.subsample(5, 5)
        btn3.config(image=icon_image_reduced3)
        btn3.image = icon_image_reduced3



        btn4 = ttk.Button(self, text="Ayuda", compound=tk.TOP, command=self.change_help_view)
        #btn.grid(row=3 + i//2, column=i%2, padx=10, pady=10, rowspan=2, sticky="nesw")
        btn4.grid(row=4 + 3//2, column=3%2, padx=10, pady=10)

        # Cargar el icono y asignarlo al botón
        icon_image4 = tk.PhotoImage(file=icon_help_path)
        icon_image_reduced4 = icon_image4.subsample(5, 5)
        btn4.config(image=icon_image_reduced4)
        btn4.image = icon_image_reduced4

        '''
        # Botones con iconos y etiquetas en una grilla de 2x2
        buttons = [
            (icon_encode_path, "Codificar", self.encode_window),
            (icon_decode_path, "Decodificar", self.decode_window),
            (icon_info_path, "Información", self.information_window),
            (icon_help_path, "Ayuda", self.help_window)
        ]

    

        for i, (icon_button, text_button, next_view) in enumerate(buttons):
            btn = ttk.Button(self, text=text_button, compound=tk.TOP, command=lambda new_view=next_view: self.change_view(new_view))
            #btn.grid(row=3 + i//2, column=i%2, padx=10, pady=10, rowspan=2, sticky="nesw")
            btn.grid(row=4 + i//2, column=i%2, padx=10, pady=10)

            # Cargar el icono y asignarlo al botón
            icon_image = tk.PhotoImage(file=icon_button)
            icon_image_reduced = icon_image.subsample(5, 5)
            btn.config(image=icon_image_reduced)
            btn.image = icon_image_reduced

            # Etiqueta arriba del botón
            #label_button = tk.Label(self, text=text_button, font=("Arial", 10), fg="white", bg="black")
            #label_button.grid(row=4 + i//2 - 1, column=i%2, padx=10, sticky="n")'''

    def change_info_view(self):
        

        from information import InformationWindow
        print("entro pero no se que pasa")
        # Ocultar la vista actual
        #self.grid_forget()
        self.information_window = InformationWindow(self)

        # Mostrar la vista destino
        self.information_window.place(x=0, y=0, relwidth=1, relheight=1)
    
    def change_help_view(self):
        from help import HelpWindow
        print("entro pero no se que pasa")
        # Ocultar la vista actual
        #self.grid_forget()
        self.help_window = HelpWindow(self)

        # Mostrar la vista destino
        self.help_window.place(x=0, y=0, relwidth=1, relheight=1)
    
    def change_encode_view(self):
        
        from encode import EncodeWindow
        print("entro pero no se que pasa")
        # Ocultar la vista actual
        #self.grid_forget()
        self.encode_window = EncodeWindow(self)

        # Mostrar la vista destino
        self.encode_window.place(x=0, y=0, relwidth=1, relheight=1)
    
    def change_decode_view(self):
        from decode import DecodeWindow
        print("entro pero no se que pasa")
        # Ocultar la vista actual
        #self.grid_forget()
        self.decode_window = DecodeWindow(self)

        # Mostrar la vista destino
        self.decode_window.place(x=0, y=0, relwidth=1, relheight=1)

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()