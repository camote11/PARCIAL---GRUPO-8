class Contenido:

  def __init__(self, titulo, año, genero, clasificacion, tipo):
        self.__titulo = titulo
        self.__año = año
        self.__genero = genero
        self.__clasificacion = clasificacion
        self.__tipo = tipo

    def get_titulo(self):
        return self.__titulo

    def get_anio(self):
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

    def __init__(self, titulo, genero, anio, duracion):
        super().__init__(titulo, genero, anio)
        self.__duracion = duracion

    def mostrar_info(self):
        return "PELÍCULA: " + super().mostrar_info() + f" - {self.__duracion} min"

class Serie(Contenido):
    """Serie: agrega la cantidad de temporadas."""

    def __init__(self, titulo, genero, anio, temporadas):
        super().__init__(titulo, genero, anio)
        self.__temporadas = temporadas

    def mostrar_info(self):
        return "SERIE: " + super().mostrar_info() + f" - {self.__temporadas} temporadas"
