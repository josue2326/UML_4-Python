import tkinter as tk
from tkinter import ttk, messagebox, font
import datetime
import random
import os
from PIL import Image, ImageTk

# Colores personalizados
COLOR_BARRA_SUPERIOR = "#333333"
COLOR_MENU_LATERAL = "#444444"
COLOR_CUERPO_PRINCIPAL = "#555555"
COLOR_MENU_CURSOR_ENCIMA = "#666666"

class Autor:
    def __init__(self, equipo, entrenador):
        self.equipo = equipo
        self.entrenador = entrenador
        self.categorias = []

    def agregar_categoria(self, categoria):
        self.categorias.append(categoria)

    def mostrar_info(self):
        return f"Equipo: {self.equipo}, Entrenador: {self.entrenador}"

class Categoria:
    def __init__(self, nombre, edad, posicion):
        self.nombre = nombre
        self.edad = edad
        self.posicion = posicion

    def mostrar_info(self):
        return f"Jugador: {self.nombre}, Edad: {self.edad}, Posición: {self.posicion}"

class Libro:
    def __init__(self, equipo_local, equipo_visitante, estadio):
        self.equipo_local = equipo_local
        self.equipo_visitante = equipo_visitante
        self.estadio = estadio
        self.resultado = None

    def mostrar_partido(self):
        return f"Partido: {self.equipo_local} vs {self.equipo_visitante} en {self.estadio}."

    def jugar_partido(self):
        resultados_posibles = ["Victoria", "Empate", "Derrota"]
        self.resultado = random.choice(resultados_posibles)

    def mostrar_resultado(self):
        if self.resultado:
            return f"Resultado: {self.resultado}"
        else:
            return "El partido no ha sido jugado aún"

class Usuario:
    def __init__(self, nombre, pais=None, anio_fundacion=None):
        self.nombre = nombre
        self.pais = pais
        self.anio_fundacion = anio_fundacion
        self.equipos = []  # Lista para almacenar equipos

    def agregar_equipo(self, equipo):
        self.equipos.append(equipo)

    def mostrar_info(self):
        return f"Equipo: {self.nombre}, País: {self.pais}, Año de fundación: {self.anio_fundacion}"

class Prestamo:
    def __init__(self, libro, usuario, fecha_prestamo, fecha_devolucion=None):
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion

    def mostrar_info(self):
        return (f"Préstamo - Libro: {self.libro.titulo}, Usuario: {self.usuario.nombre}, "
                f"Fecha de préstamo: {self.fecha_prestamo}, Fecha de devolución: {self.fecha_devolucion}")

class Biblioteca:
    def __init__(self):
        self.usuarios = []
        self.prestamos = []
        self.autores = []
        self.categorias = []
        self.libros = []
        
    def registrar_equipo(self, equipo):
        self.usuarios.append(equipo)


    def registrar_libro(self, libro):
        self.libros.append(libro)

    def registrar_grupo(self, grupo):
        self.prestamos.append(grupo)

    def realizar_prestamo(self, libro, usuario, fecha_prestamo):
        prestamo = Prestamo(libro, usuario, fecha_prestamo)
        self.prestamos.append(prestamo)

    def generar_fixture(self):
        if not self.libros:
            return "No hay partidos programados."
        
        fixture = []
        for libro in self.libros:
            partido = libro.mostrar_partido()
            resultado = libro.mostrar_resultado()
            fixture.append(f"{partido} - {resultado}")
        return "\n".join(fixture)

    def mostrar_jugadores(self):
        if not self.autores:
            return "No hay jugadores registrados."
        return "\n".join(autor.mostrar_info() for autor in self.autores)
    
    def registrar_equipo(self, equipo):
        self.usuarios.append(equipo)

    def registrar_categoria(self, categoria):
        self.categorias.append(categoria)
        
    def mostrar_categorias(self):
        if not self.categorias:
            return "No hay categorías registradas."
        return "\n".join(categoria.mostrar_info() for categoria in self.categorias)

    def mostrar_equipos(self):
        if not self.usuarios:
            return "No hay equipos registrados."
        return "\n".join(usuario.mostrar_info() for usuario in self.usuarios)

class FormularioMaestroDesign(tk.Tk):
    def __init__(self):
        super().__init__()
        self.biblioteca = Biblioteca()
        self.init_data()
        self.logo = ImageTk.PhotoImage(Image.open("imagenes/logo.png").resize((360, 460)))
        self.perfil = ImageTk.PhotoImage(Image.open("imagenes/Perfil.png").resize((100, 100)))
        self.config_window()
        self.paneles()
        self.controles_barra_superior()        
        self.controles_menu_lateral()
        self.controles_cuerpo()
        

    
    def init_data(self):
        autores = [
            Autor("Barcelona", "Guardiola"),
            Autor("Real Madrid", "Zidane"),
            Autor("Manchester United", "Ferguson"),
            Autor("Liverpool", "Klopp"),
            Autor("Juventus", "Allegri"),
            Autor("Paris Saint-Germain", "Tuchel"),
            Autor("Bayern Munich", "Flick"),
            Autor("Chelsea", "Mourinho"),
            Autor("Atletico Madrid", "Simeone"),
            Autor("AC Milan", "Ancelotti")
        ]

        categorias = [
            Categoria("Lionel Messi", "35", "Delantero"),
            Categoria("Cristiano Ronaldo", "38", "Delantero"),
            Categoria("Neymar Jr.", "32", "Delantero"),
            Categoria("Kylian Mbappe", "25", "Delantero"),
            Categoria("Luka Modric", "38", "Centrocampista"),
            Categoria("Mohamed Salah", "31", "Delantero"),
            Categoria("Kevin De Bruyne", "32", "Centrocampista"),
            Categoria("Robert Lewandowski", "35", "Delantero"),
            Categoria("Sergio Ramos", "37", "Defensa"),
            Categoria("Virgil van Dijk", "32", "Defensa"),
            Categoria("Eden Hazard", "33", "Delantero"),
            Categoria("Karim Benzema", "36", "Delantero"),
            Categoria("Paul Pogba", "31", "Centrocampista"),
            Categoria("Antoine Griezmann", "33", "Delantero"),
            Categoria("Harry Kane", "30", "Delantero"),
            Categoria("Erling Haaland", "23", "Delantero"),
            Categoria("Raheem Sterling", "29", "Delantero"),
            Categoria("Sadio Mane", "32", "Delantero"),
            Categoria("Bruno Fernandes", "29", "Centrocampista"),
            Categoria("Zlatan Ibrahimovic", "42", "Delantero")
        ]

        libros = [
            Libro("Real Madrid", "Barcelona", "Bernabéu"),
            Libro("Manchester United", "Liverpool", "Old Trafford"),
            Libro("Bayern Munich", "Juventus", "Allianz Arena"),
            Libro("Paris Saint-Germain", "Chelsea", "Parc des Princes"),
            Libro("Manchester City", "Atlético de Madrid", "Etihad Stadium"),
            Libro("Barcelona", "Real Madrid", "Camp Nou"),
            Libro("Liverpool", "Manchester United", "Anfield"),
            Libro("Juventus", "Bayern Munich", "Juventus Stadium"),
            Libro("Chelsea", "Paris Saint-Germain", "Stamford Bridge"),
            Libro("Atlético de Madrid", "Manchester City", "Wanda Metropolitano")
        ]

        for autor in autores:
            for categoria in categorias:
                autor.agregar_categoria(categoria)

        for autor in autores:
            self.biblioteca.autores.append(autor)
            
        for libro in libros:
            self.biblioteca.registrar_libro(libro)
        
        usuarios = [
            Usuario("Barcelona", "España", "1899"),
            Usuario("Real Madrid", "España", "1902"),
            Usuario("Manchester United", "Inglaterra", "1878"),
            Usuario("Liverpool", "Inglaterra", "1892"),
            Usuario("Juventus", "Italia", "1897"),
            Usuario("Paris Saint-Germain", "Francia", "1970"),
            Usuario("Bayern Munich", "Alemania", "1900"),
            Usuario("Chelsea", "Inglaterra", "1905"),
            Usuario("Atletico Madrid", "España", "1903"),
            Usuario("AC Milan", "Italia", "1899")
        ]

        for categoria in categorias:
            self.biblioteca.registrar_categoria(categoria)
        
        for usuario in usuarios:
            self.biblioteca.registrar_equipo(usuario)

    def config_window(self):
        self.title("Football Analytics")
        self.geometry("950x600")
        self.configure(bg="#333333")
        # Corregir el método iconbitmap y usar la ruta absoluta del archivo .ico
        icon_path = os.path.abspath("imagenes/logo.ico")
        self.iconbitmap(icon_path)
        self.resizable(False, False)

    def paneles(self):
        self.barra_superior = tk.Frame(self, bg=COLOR_BARRA_SUPERIOR)
        self.barra_superior.pack(fill=tk.X)

        self.menu_lateral = tk.Frame(self, bg=COLOR_MENU_LATERAL)
        self.menu_lateral.pack(fill=tk.Y, side=tk.LEFT)

        self.cuerpo_principal = tk.Frame(self, bg=COLOR_CUERPO_PRINCIPAL)
        self.cuerpo_principal.pack(fill=tk.BOTH, expand=True)

    def controles_barra_superior(self):
        lbl_titulo = tk.Label(self.barra_superior, text="Football Analytics", font=("Roboto", 18), bg=COLOR_BARRA_SUPERIOR, fg="white")
        lbl_titulo.pack(pady=10)

    def controles_menu_lateral(self):
        btn_inicio = tk.Button(self.menu_lateral, text="Inicio", font=("Roboto", 12), bg=COLOR_MENU_LATERAL, fg="white", bd=0, command=self.mostrar_inicio)
        btn_inicio.pack(pady=10, padx=20, anchor='w')

        btn_jugadores = tk.Button(self.menu_lateral, text="Jugadores", font=("Roboto", 12), bg=COLOR_MENU_LATERAL, fg="white", bd=0, command=self.mostrar_jugadores)
        btn_jugadores.pack(pady=10, padx=20, anchor='w')

        btn_categorias = tk.Button(self.menu_lateral, text="Categorías", font=("Roboto", 12), bg=COLOR_MENU_LATERAL, fg="white", bd=0, command=self.mostrar_categorias)
        btn_categorias.pack(pady=10, padx=20, anchor='w')

        btn_equipos = tk.Button(self.menu_lateral, text="Equipos", font=("Roboto", 12), bg=COLOR_MENU_LATERAL, fg="white", bd=0, command=self.mostrar_equipos)
        btn_equipos.pack(pady=10, padx=20, anchor='w')

        btn_fixture = tk.Button(self.menu_lateral, text="Fixture", font=("Roboto", 12), bg=COLOR_MENU_LATERAL, fg="white", bd=0, command=self.mostrar_fixture)
        btn_fixture.pack(pady=10, padx=20, anchor='w')

        # Nuevas pestañas
        btn_ingresar_jugadores = tk.Button(self.menu_lateral, text="Ingresar Jugadores", font=("Roboto", 12), bg=COLOR_MENU_LATERAL, fg="white", bd=0, command=self.ingresar_jugadores)
        btn_ingresar_jugadores.pack(pady=10, padx=20, anchor='w')

        btn_ingresar_equipos = tk.Button(self.menu_lateral, text="Ingresar Equipos", font=("Roboto", 12), bg=COLOR_MENU_LATERAL, fg="white", bd=0, command=self.ingresar_equipos)
        btn_ingresar_equipos.pack(pady=10, padx=20, anchor='w')

    def controles_cuerpo(self):
        # Controles del cuerpo principal
        self.cuerpo_label = tk.Label(self.cuerpo_principal, image=self.logo, bg=COLOR_CUERPO_PRINCIPAL)
        self.cuerpo_label.place(relx=0.5, rely=0.5, anchor='center')

        # Añadir reloj debajo de la imagen principal
        self.clock_label = Clock(self.cuerpo_principal, font=("Roboto", 16), bg=COLOR_CUERPO_PRINCIPAL, fg="white")
        self.clock_label.pack(pady=(20, 10))

    def mostrar_inicio(self):
        self.limpiar_cuerpo()
        self.controles_cuerpo()

    def mostrar_jugadores(self):
        self.limpiar_cuerpo()
        texto_jugadores = self.biblioteca.mostrar_jugadores()
        lbl_jugadores = tk.Label(self.cuerpo_principal, text=texto_jugadores, font=("Roboto", 12), bg=COLOR_CUERPO_PRINCIPAL, fg="white", justify=tk.LEFT)
        lbl_jugadores.pack(pady=20, padx=20)

    def mostrar_categorias(self):
        self.limpiar_cuerpo()
        texto_categorias = self.biblioteca.mostrar_categorias()
        lbl_categorias = tk.Label(self.cuerpo_principal, text=texto_categorias, font=("Roboto", 12), bg=COLOR_CUERPO_PRINCIPAL, fg="white", justify=tk.LEFT)
        lbl_categorias.pack(pady=20, padx=20)

    def mostrar_equipos(self):
        self.limpiar_cuerpo()
        texto_equipos = self.biblioteca.mostrar_equipos()
        lbl_equipos = tk.Label(self.cuerpo_principal, text=texto_equipos, font=("Roboto", 12), bg=COLOR_CUERPO_PRINCIPAL, fg="white", justify=tk.LEFT)
        lbl_equipos.pack(pady=10, padx=20)

    def mostrar_fixture(self):
        self.limpiar_cuerpo()
        texto_fixture = self.biblioteca.generar_fixture()
        lbl_fixture = tk.Label(self.cuerpo_principal, text=texto_fixture, font=("Roboto", 12), bg=COLOR_CUERPO_PRINCIPAL, fg="white", justify=tk.LEFT)
        lbl_fixture.pack(pady=20, padx=20)

    def ingresar_jugadores(self):
        self.limpiar_cuerpo()

        lbl_titulo = tk.Label(self.cuerpo_principal, text="Ingresar Jugadores", font=("Roboto", 16), bg=COLOR_CUERPO_PRINCIPAL, fg="white")
        lbl_titulo.pack(pady=20)

        # Campos para ingresar nombre, edad y posición del jugador
        self.nombre_var = tk.StringVar()
        self.edad_var = tk.IntVar()
        self.posicion_var = tk.StringVar()

        lbl_nombre = tk.Label(self.cuerpo_principal, text="Nombre:", font=("Roboto", 12), bg=COLOR_CUERPO_PRINCIPAL, fg="white")
        lbl_nombre.pack(pady=(10, 5))
        entry_nombre = tk.Entry(self.cuerpo_principal, textvariable=self.nombre_var, font=("Roboto", 12))
        entry_nombre.pack(ipadx=10, ipady=5)

        lbl_edad = tk.Label(self.cuerpo_principal, text="Edad:", font=("Roboto", 12), bg=COLOR_CUERPO_PRINCIPAL, fg="white")
        lbl_edad.pack(pady=(10, 5))
        entry_edad = tk.Entry(self.cuerpo_principal, textvariable=self.edad_var, font=("Roboto", 12))
        entry_edad.pack(ipadx=10, ipady=5)

        lbl_posicion = tk.Label(self.cuerpo_principal, text="Posición:", font=("Roboto", 12), bg=COLOR_CUERPO_PRINCIPAL, fg="white")
        lbl_posicion.pack(pady=(10, 5))
        entry_posicion = tk.Entry(self.cuerpo_principal, textvariable=self.posicion_var, font=("Roboto", 12))
        entry_posicion.pack(ipadx=10, ipady=5)

        # Botón para registrar jugador
        btn_registrar = tk.Button(self.cuerpo_principal, text="Registrar", font=("Roboto", 12), bg="#777777", fg="white", bd=0, command=self.registrar_jugador)
        btn_registrar.pack(pady=20)

    def registrar_jugador(self):
        # Obtener los valores de los campos de entrada
        nombre = self.nombre_var.get().strip()
        edad = self.edad_var.get()
        posicion = self.posicion_var.get().strip()

        # Validar que todos los campos estén llenos
        if nombre == "" or posicion == "":
            messagebox.showerror("Error", "Por favor complete todos los campos.")
            return

        # Crear una nueva instancia de Categoria
        jugador_nuevo = Categoria(nombre, edad, posicion)

        # Agregar el jugador a la biblioteca
        self.biblioteca.registrar_categoria(jugador_nuevo)

        # Limpiar los campos después de registrar
        self.nombre_var.set("")
        self.edad_var.set("")
        self.posicion_var.set("")

        # Mostrar de nuevo la lista actualizada de jugadores
        self.mostrar_categorias()
        
    def ingresar_equipos(self):
        self.limpiar_cuerpo()
        lbl_titulo = tk.Label(self.cuerpo_principal, text="Ingresar Equipos", font=("Roboto", 16), bg=COLOR_CUERPO_PRINCIPAL, fg="white")
        lbl_titulo.pack(pady=20)

        # Campos para ingresar nombre, país y año de fundación del equipo
        self.nombre_equipo_var = tk.StringVar()
        self.pais_var = tk.StringVar()
        self.anio_fundacion_var = tk.StringVar()

        lbl_nombre_equipo = tk.Label(self.cuerpo_principal, text="Nombre del Equipo:", font=("Roboto", 12), bg=COLOR_CUERPO_PRINCIPAL, fg="white")
        lbl_nombre_equipo.pack(pady=(10, 5))
        entry_nombre_equipo = tk.Entry(self.cuerpo_principal, textvariable=self.nombre_equipo_var, font=("Roboto", 12))
        entry_nombre_equipo.pack(ipadx=10, ipady=5)

        lbl_pais = tk.Label(self.cuerpo_principal, text="País:", font=("Roboto", 12), bg=COLOR_CUERPO_PRINCIPAL, fg="white")
        lbl_pais.pack(pady=(10, 5))
        entry_pais = tk.Entry(self.cuerpo_principal, textvariable=self.pais_var, font=("Roboto", 12))
        entry_pais.pack(ipadx=10, ipady=5)

        lbl_anio_fundacion = tk.Label(self.cuerpo_principal, text="Año de Fundación:", font=("Roboto", 12), bg=COLOR_CUERPO_PRINCIPAL, fg="white")
        lbl_anio_fundacion.pack(pady=(10, 5))
        entry_anio_fundacion = tk.Entry(self.cuerpo_principal, textvariable=self.anio_fundacion_var, font=("Roboto", 12))
        entry_anio_fundacion.pack(ipadx=10, ipady=5)

        # Botón para registrar equipo
        btn_registrar = tk.Button(self.cuerpo_principal, text="Registrar Equipo", font=("Roboto", 12), bg="#777777", fg="white", bd=0, command=self.registrar_equipo)
        btn_registrar.pack(pady=20)

    def registrar_equipo(self):
        # Obtener los valores de los campos de entrada
        nombre_equipo = self.nombre_equipo_var.get().strip()
        pais = self.pais_var.get().strip()
        anio_fundacion = self.anio_fundacion_var.get().strip()

        # Validar que todos los campos estén llenos
        if nombre_equipo == "" or pais == "" or anio_fundacion == "":
            messagebox.showerror("Error", "Por favor complete todos los campos.")
            return

        # Crear una nueva instancia de Equipo
        equipo_nuevo = Usuario(nombre_equipo, pais, anio_fundacion)


        # Agregar el equipo a la biblioteca
        self.biblioteca.registrar_equipo(equipo_nuevo)

        # Limpiar los campos después de registrar
        self.nombre_equipo_var.set("")
        self.pais_var.set("")
        self.anio_fundacion_var.set("")

        # Mostrar de nuevo la lista actualizada de equipos
        self.mostrar_equipos()
        
    def mostrar_equipos(self):
        self.limpiar_cuerpo()  # Ensure this function is correctly clearing the body

    # Fetch the list of equipos from the biblioteca
        texto_equipos = self.biblioteca.mostrar_equipos()

    # Create a label to display the list
        lbl_equipos = tk.Label(self.cuerpo_principal, text=texto_equipos, font=("Roboto", 12), bg=COLOR_CUERPO_PRINCIPAL, fg="white", justify=tk.LEFT)
        lbl_equipos.pack(pady=20, padx=20)


    def limpiar_cuerpo(self):
        for widget in self.cuerpo_principal.winfo_children():
            widget.destroy()

class Clock(tk.Label):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.update_time()

    def update_time(self):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.config(text=current_time)
        self.after(1000, self.update_time)  

if __name__ == "__main__":
    app = FormularioMaestroDesign()
    app.mainloop()
