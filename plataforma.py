from usuario import Usuario
from plan import BASICO, PREMIUM


class Plataforma:
    """Plataforma de streaming: administra el catálogo, los usuarios y los planes."""

    def __init__(self, nombre):
        self.__nombre = nombre
        self.__catalogo = []          # objetos Contenido (Pelicula / Serie)
        self.__usuarios = []          # objetos Usuario registrados
        self.__planes = [BASICO, PREMIUM]

    def get_nombre(self):
        return self.__nombre

    def get_catalogo(self):
        return self.__catalogo

    # ------------------------------------------------------------------
    # Utilidades internas
    # ------------------------------------------------------------------
    @staticmethod
    def _normalizar(texto):
        """Minúsculas y sin tildes, para comparar textos sin problemas."""
        return texto.strip().lower().translate(str.maketrans("áéíóú", "aeiou"))

    def _buscar_usuario(self, correo):
        for usuario in self.__usuarios:
            if usuario.get_correo().lower() == correo.strip().lower():
                return usuario
        return None

    # ------------------------------------------------------------------
    # Catálogo
    # ------------------------------------------------------------------
    def agregar_contenido(self, contenido):
        """Lo usa cargar_datos() de contenido.py."""
        self.__catalogo.append(contenido)

    def mostrar_catalogo(self, lista=None):
        """Muestra el catálogo completo o una lista de contenidos ya filtrada."""
        lista = self.__catalogo if lista is None else lista
        if not lista:
            print("No se encontraron contenidos.")
            return
        print(f"\n--- Catálogo de {self.__nombre} ---")
        for i, contenido in enumerate(lista, start=1):
            print(f"{i}. {contenido.mostrar_info()}")

    def buscar_por_titulo(self, texto):
        texto = self._normalizar(texto)
        return [c for c in self.__catalogo
                if texto in self._normalizar(c.get_titulo())]

    def filtrar_por_genero(self, genero):
        genero = self._normalizar(genero)
        return [c for c in self.__catalogo
                if self._normalizar(c.get_genero()) == genero]

    # ------------------------------------------------------------------
    # Planes
    # ------------------------------------------------------------------
    def obtener_plan(self, nombre_plan):
        """Devuelve el objeto Plan con ese nombre, o None si no existe."""
        nombre_plan = self._normalizar(nombre_plan)
        for plan in self.__planes:
            if self._normalizar(plan.get_nombre()) == nombre_plan:
                return plan
        return None

    def mostrar_planes(self):
        print(f"\n--- Planes de {self.__nombre} ---")
        for plan in self.__planes:
            print(plan.mostrar_info())

    def cambiar_plan(self, usuario, nombre_plan):
        plan = self.obtener_plan(nombre_plan)
        if plan is None:
            return "El plan no existe. Elige Basico o Premium."
        if plan.get_nombre() == usuario.get_plan():
            return f"Ya tienes el plan {plan.get_nombre()}."
        usuario.cambiar_plan(plan.get_nombre())
        return f"Plan cambiado a {plan.get_nombre()}."

    def calcular_costo(self, usuario, meses):
        """Costo total del plan actual del usuario por varios meses."""
        plan = self.obtener_plan(usuario.get_plan())
        return plan.calcular_total(meses)

    # ------------------------------------------------------------------
    # Usuarios
    # ------------------------------------------------------------------
    def registrar_usuario(self, nombre, correo, clave, nombre_plan):
        """Devuelve (True/False, mensaje)."""
        nombre = nombre.strip()
        correo = correo.strip()
        if not nombre or not clave:
            return False, "El nombre y la clave no pueden estar vacíos."
        if not Usuario.validar_correo(correo):
            return False, "Correo inválido (usa gmail, hotmail, outlook, yahoo o icloud .com)."
        if self._buscar_usuario(correo) is not None:
            return False, "Ese correo ya está registrado."
        plan = self.obtener_plan(nombre_plan)
        if plan is None:
            return False, "El plan no existe. Elige Basico o Premium."

        self.__usuarios.append(Usuario(nombre, correo, clave, plan.get_nombre()))
        return True, f"Usuario {nombre} registrado con el plan {plan.get_nombre()}."

    def iniciar_sesion(self, correo, clave):
        """Devuelve el Usuario si los datos son correctos; si no, None."""
        usuario = self._buscar_usuario(correo)
        if usuario is not None and usuario.verificar_clave(clave):
            return usuario
        return None

    # ------------------------------------------------------------------
    # Reproducción
    # ------------------------------------------------------------------
    def reproducir(self, usuario, titulo):
        """Busca el contenido y lo guarda en el historial del usuario."""
        coincidencias = self.buscar_por_titulo(titulo)
        if not coincidencias:
            return "No se encontró ese título en el catálogo."
        if len(coincidencias) > 1:
            return "Hay varios resultados, escribe el título completo."

        contenido = coincidencias[0]
        usuario.reproducir(contenido)

        plan = self.obtener_plan(usuario.get_plan())
        aviso = " (con anuncios)" if plan.tiene_anuncios() else ""
        return f"Reproduciendo: {contenido.get_titulo()}{aviso}"