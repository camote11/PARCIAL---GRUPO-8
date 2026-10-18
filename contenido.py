class Contenido:

    def __init__(self, titulo, año, genero, clasificacion, tipo):
        self.__titulo = titulo
        self.__año = año
        self.__genero = genero
        self.__clasificacion = clasificacion
        self.__tipo = tipo

    def get_titulo(self):
        return self.__titulo

    def get_año(self):
        return self.__año

    def get_genero(self):
        return self.__genero

    def get_clasificacion(self):
        return self.__clasificacion

    def get_tipo(self):
        return self.__tipo
    def mostrar_info(self):
        return (f"{self.__titulo} ({self.__año}) - "
            f"{self.__tipo} - {self.__genero} - "
            f"Clasificación: {self.__clasificacion}")

class Pelicula(Contenido):
    """Película: agrega la duración."""

    def __init__(self, titulo, genero, año, duracion, clasificacion="ATP", tipo="Película"):
        super().__init__(titulo, año, genero, clasificacion, tipo)
        self.__duracion = duracion

    def mostrar_info(self):
        return "PELÍCULA: " + super().mostrar_info() + f" - {self.__duracion} min"

class Serie(Contenido):
    """Serie: agrega la cantidad de temporadas."""

    def __init__(self, titulo, genero, año, temporadas, clasificacion="ATP", tipo="Serie"):
        super().__init__(titulo, año, genero, clasificacion, tipo)
        self.__temporadas = temporadas

    def mostrar_info(self):
        return "SERIE: " + super().mostrar_info() + f" - {self.__temporadas} temporadas"

def cargar_datos(plataforma):
  
    plataforma.agregar_contenido(Pelicula("El Rey León", "Animación", 1994, 88))
    plataforma.agregar_contenido(Pelicula("Frozen", "Animación", 2013, 102))
    plataforma.agregar_contenido(Pelicula("Coco", "Animación", 2017, 105))
    plataforma.agregar_contenido(Pelicula("Avengers: Endgame", "Acción", 2019, 181))
    plataforma.agregar_contenido(Pelicula("Black Panther", "Acción", 2018, 134))
    plataforma.agregar_contenido(Serie("The Mandalorian", "Ciencia ficción", 2019, 3))
    plataforma.agregar_contenido(Serie("Loki", "Fantasía", 2021, 2))
    plataforma.agregar_contenido(Serie("Bluey", "Animación", 2018, 3))
