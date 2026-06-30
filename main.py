turnos = []
def agregar_turno():
    nombre = input("Nombre de cliente:")
    servicio = input("Servico:")
    horario = input("Horario:")

    turno = {
        "nombre": nombre,
        "servicio": servicio,
        "horario": horario
    }
    turnos.append(turno)
    print("Turno agregado correctamente")

def mostrar_turnos():
    print("\nTurnos registrados:")
    for turno in turnos:
        print(turno)

opcion = 0
while opcion != 3:
    print("\n--- Sistema de Turnos Salón ---")
    print("1 - Agregar turno")
    print("2 - Ver turnos")
    print("3 - Salir")

    opcion = int(input("Elegí una opción"))
    if opcion == 1:
        agregar_turno()
    else:
        if opcion == 2:
            mostrar_turnos()
        else:
            if opcion ==3:
                print("Programa finalizado")
            else:
                print("Opción incorrecta")
