class Contenido:
"""Clase base que representa un contenido en el catálogo.
    Atributos:
        titulo (str): Título de la obra.
        año (int): Año de estreno.
        genero (str): Género cinematográfico o televisivo.
        clasificacion (str): Clasificación por edad (ej. ATP, +13).
        tipo (str): Tipo de contenido ('Película' o 'Serie').
        puntaje(List[int]): Lista de puntaje que otorgan los usuarios (entre 1 y 5)"""

    def __init__(self, titulo, año, genero, clasificacion, tipo):
        """Inicializa los atributos principales de un contenido."""
        self.__titulo: str = titulo
        self.__año: int = año
        self.__genero: str = genero
        self.__clasificacion: str = clasificacion  
        self.__tipo: str = tipo
        self.__puntajes: List[int] = []  

    def get_titulo(self):
        """Obtiene el título del contenido."""
        return self.__titulo

    def get_año(self):
        """Obtiene el año de estreno del contenido."""
        return self.__año

    def get_genero(self):
        """Obtiene el género del contenido."""
        return self.__genero

    def get_clasificacion(self):
        """Obtiene la clasificación por edad del contenido."""
        return self.__clasificacion

    def get_tipo(self):
        """Obtiene el tipo de contenido"""
        return self.__tipo

    def get_puntajes(self) -> List[int]:
        """Obtiene una copia de la lista de puntajes recibidos."""
        return list(self.__puntajes)
        
    def mostrar_info(self):
        """Devuelve un string con los datos generales del contenido."""
        return (f"{self.__titulo} ({self.__año}) - "
            f"{self.__tipo} - {self.__genero} - "
            f"Clasificación: {self.__clasificacion}")
        
    def brinda_puntaje(self, puntaje):
        """Guarda un puntaje de 1 a 5. Devuelve False si es inválido."""
        if 1 <= puntaje <= 5:
            self.__calificaciones.append(puntaje)
            return True
        return False

    def promedio(self):
        """Promedio de las calificaciones (0 si aún no tiene)."""
        if len(self.__calificaciones) == 0:
            return 0
        return sum(self.__calificaciones) / len(self.__calificaciones)

class Pelicula(Contenido):
    """Película: agrega la duración."""

    def __init__(self, titulo, genero, año, duracion, clasificacion="ATP", tipo="Película"):
        super().__init__(titulo, año, genero, clasificacion, tipo)
        self.__duracion = duracion
        
    def get_duracion(self):
        """Obtiene la duración en minutos de la película."""
        return self.__duracion

    def mostrar_info(self):
        """Modifica mostrar_info para que también imprima la duración."""
        return "PELÍCULA: " + super().mostrar_info() + f" - {self.__duracion} min"

class Serie(Contenido):
    """Serie: agrega la cantidad de temporadas."""

    def __init__(self, titulo, genero, año, temporadas, clasificacion="ATP", tipo="Serie"):
        super().__init__(titulo, año, genero, clasificacion, tipo)
        self.__temporadas = temporadas

    def get_temporadas(self):
        """Obtiene la cantidad de temporadas de la serie."""
        return self.__temporadas

    def mostrar_info(self):
        """Modifica mostrar_info para incluir las temporadas."""
        return "SERIE: " + super().mostrar_info() + f" - {self.__temporadas} temporadas"

def cargar_datos(plataforma):
    """Precarga el catálogo inicial de películas y series en la plataforma."""
  
    plataforma.agregar_contenido(Pelicula("El Rey León", "Animación", 1994, 88))
    plataforma.agregar_contenido(Pelicula("Frozen", "Animación", 2013, 102))
    plataforma.agregar_contenido(Pelicula("Coco", "Animación", 2017, 105))
    plataforma.agregar_contenido(Pelicula("Avengers: Endgame", "Acción", 2019, 181))
    plataforma.agregar_contenido(Pelicula("Black Panther", "Acción", 2018, 134))
    plataforma.agregar_contenido(Serie("The Mandalorian", "Ciencia ficción", 2019, 3))
    plataforma.agregar_contenido(Serie("Loki", "Fantasía", 2021, 2))
    plataforma.agregar_contenido(Serie("Bluey", "Animación", 2018, 3))
