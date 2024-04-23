# Definir la lista principal de candidatos
candidatos = []

# Función para registrar candidatos
def registrar_candidato():
    # Solicitar información al usuario
    nombre = input("Nombre y apellidos: ")
    identificacion = input("Identificación: ")
    correo = input("Correo electrónico: ")
    contacto = input("Contacto: ")
    edad = int(input("Edad: "))
    experiencia = int(input("Años de experiencia: "))
    profesion = input("Profesión: ")
    ciudad = input("Ciudad: ")
    sexo = input("Sexo: ")

    # Verificar condiciones
    if 25 <= edad <= 32 and (profesion == "Ing. sistemas" or profesion == "ing. informatico") and 2 <= experiencia <= 4:
        # Crear diccionario con la información del candidato
        candidato = {
            "Nombre": nombre,
            "Identificación": identificacion,
            "Correo electrónico": correo,
            "Contacto": contacto,
            "Edad": edad,
            "Años de experiencia": experiencia,
            "Profesión": profesion,
            "Ciudad": ciudad,
            "Sexo": sexo
        }

        # Agregar el candidato a la lista principal de candidatos
        candidatos.append(candidato)
        print("Candidato registrado exitosamente.")
    else:
        print("El candidato no cumple con las condiciones.")

# Función para consultar candidatos
def consultar_candidatos():
    # Mostrar todos los candidatos registrados
    for candidato in candidatos:
        print(candidato)

# Ejecutar el programa
while True:
    print("1. Registrar candidato")
    print("2. Consultar candidatos")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_candidato()
    elif opcion == "2":
        consultar_candidatos()
    elif opcion == "3":
        break
    else:
        print("Opción inválida. Intente nuevamente.")
