import re

class Usuario:
    """Usuario de la plataforma con validación de correo, plan, Mi lista e historial."""

    def __init__(self, nombre, correo, clave, plan):
        self.__nombre = nombre
        self.__correo = correo
        self.__clave = clave
        self.__plan = plan            # "Basico" o "Premium"
        self.__mi_lista = []
        self.__historial = []

    @staticmethod
    def validar_correo(correo):
        """Valida que el correo pertenezca a dominios comunes (gmail, hotmail, etc.)."""
        patron = r"^[a-zA-Z0-9_.+-]+@(gmail|hotmail|outlook|yahoo|icloud)\.com$"
        return bool(re.match(patron, correo, re.IGNORECASE))

    # Getters básicos
    def get_nombre(self): return self.__nombre
    def get_correo(self): return self.__correo
    def get_plan(self): return self.__plan
    def get_mi_lista(self): return self.__mi_lista
    def get_historial(self): return self.__historial

    def cambiar_plan(self, plan):
        self.__plan = plan

    def verificar_clave(self, clave):
        return self.__clave == clave

    def cambiar_clave(self, actual, nueva):
        if self.verificar_clave(actual) and nueva:
            self.__clave = nueva
            return True
        return False

    def agregar_a_mi_lista(self, contenido):
        if contenido in self.__mi_lista:
            return False
        self.__mi_lista.append(contenido)
        return True

    def eliminar_de_mi_lista(self, contenido):
        if contenido in self.__mi_lista:
            self.__mi_lista.remove(contenido)
            return True
        return False

    def reproducir(self, contenido):
        self.__historial.append(contenido)

    def limpiar_historial(self):
        self.__historial.clear()

    def mostrar_perfil(self):
        return (f"Usuario: {self.__nombre}\n"
                f"Correo: {self.__correo}\n"
                f"Plan: {self.__plan}\n"
                f"Mi lista: {len(self.__mi_lista)} elementos\n"
                f"Historial: {len(self.__historial)} títulos")