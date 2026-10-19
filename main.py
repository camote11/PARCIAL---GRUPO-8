from plataforma import Plataforma
from contenido import cargar_datos

NO_ENCONTRADO = "No se encontró un título único. Escribe el título completo."


def pedir_numero(mensaje):
    """Pide un número entero. Devuelve None si no es válido."""
    try:
        return int(input(mensaje))
    except ValueError:
        print("Ingresa un número válido.")
        return None


def mostrar_lista(lista):
    """Muestra una lista de contenidos (Mi lista, historial)."""
    if len(lista) == 0:
        print("(vacío)")
    for i, c in enumerate(lista, start=1):
        print(f"{i}. {c.mostrar_info()}")


def menu_usuario(plataforma, usuario):
    while True:
        print(f"\n--- Hola {usuario.get_nombre()} (Plan {usuario.get_plan()}) ---")
        print("1. Ver catálogo")
        print("2. Buscar por título")
        print("3. Filtrar por género")
        print("4. Reproducir")
        print("5. Agregar a Mi lista")
        print("6. Ver Mi lista")
        print("7. Eliminar de Mi lista")
        print("8. Calificar")
        print("9. Ver historial")
        print("10. Limpiar historial")
        print("11. Ver planes")
        print("12. Cambiar de plan")
        print("13. Calcular costo de mi plan")
        print("14. Ver mi perfil")
        print("15. Cambiar contraseña")
        print("16. Cerrar sesión")
        op = input("Opción: ").strip()

        if op == "1":
            plataforma.mostrar_catalogo()
        elif op == "2":
            plataforma.mostrar_catalogo(plataforma.buscar_por_titulo(input("Título: ")))
        elif op == "3":
            plataforma.mostrar_catalogo(plataforma.filtrar_por_genero(input("Género: ")))
        elif op == "4":
            print(plataforma.reproducir(usuario, input("Título a reproducir: ")))
        elif op == "5":
            c = plataforma.obtener_contenido(input("Título a agregar: "))
            if c is None:
                print(NO_ENCONTRADO)
            elif usuario.agregar_a_mi_lista(c):
                print("Agregado a Mi lista.")
            else:
                print("Ya estaba en tu lista.")
        elif op == "6":
            mostrar_lista(usuario.get_mi_lista())
        elif op == "7":
            c = plataforma.obtener_contenido(input("Título a eliminar: "))
            if c is None:
                print(NO_ENCONTRADO)
            elif usuario.eliminar_de_mi_lista(c):
                print("Eliminado de Mi lista.")
            else:
                print("Ese título no está en tu lista.")
        elif op == "8":
            c = plataforma.obtener_contenido(input("Título a calificar: "))
            if c is None:
                print(NO_ENCONTRADO)
            else:
                puntaje = pedir_numero("Puntaje (1-5): ")
                if puntaje is not None:
                    if c.calificar(puntaje):
                        print(f"Gracias. Promedio actual: {c.promedio():.1f}/5")
                    else:
                        print("El puntaje debe ser de 1 a 5.")
        elif op == "9":
            mostrar_lista(usuario.get_historial())
        elif op == "10":
            usuario.limpiar_historial()
            print("Historial borrado.")
        elif op == "11":
            plataforma.mostrar_planes()
        elif op == "12":
            print(plataforma.cambiar_plan(usuario, input("Nuevo plan (Basico/Premium): ")))
        elif op == "13":
            meses = pedir_numero("¿Cuántos meses quieres pagar?: ")
            if meses is not None and meses > 0:
                print(f"Total: ${plataforma.calcular_costo(usuario, meses):.2f}")
            elif meses is not None:
                print("Los meses deben ser mayores a 0.")
        elif op == "14":
            print(usuario.mostrar_perfil())
        elif op == "15":
            actual = input("Contraseña actual: ")
            nueva = input("Contraseña nueva: ")
            if usuario.cambiar_clave(actual, nueva):
                print("Contraseña cambiada.")
            else:
                print("Contraseña actual incorrecta.")
        elif op == "16":
            print("Sesión cerrada.")
            break
        else:
            print("Opción inválida.")


def main():
    plataforma = Plataforma("Disney+")
    cargar_datos(plataforma)
    # usuario de prueba
    plataforma.registrar_usuario("Demo", "demo@gmail.com", "1234", "Premium")
    plataforma.registrar_usuario("Melany", "melany@gmail.com", "4321", "Basico")

    while True:
        print("\n=== DISNEY+ ===")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Salir")
        op = input("Opción: ").strip()

        if op == "1":
            nombre = input("Nombre: ")
            correo = input("Correo: ")
            clave = input("Clave: ")
            plan = input("Plan (Basico/Premium): ")
            ok, mensaje = plataforma.registrar_usuario(nombre, correo, clave, plan)
            print(mensaje)
        elif op == "2":
            usuario = plataforma.iniciar_sesion(input("Correo: "), input("Clave: "))
            if usuario is not None:
                menu_usuario(plataforma, usuario)
            else:
                print("Correo o clave incorrectos.")
        elif op == "3":
            print("Hasta pronto.")
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
