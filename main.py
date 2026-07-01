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
    if len(turnos) == 0:
        print("No hay turnos registrados:")
    else:
        print("n\-- Turnos registrados")
        for turno in turnos:
            print("----------------")
            print("Cliente:", turno["nombre"])
            print("Servicio:", turno["servicio"])
            print("Horario:", turno["horario"])

def buscar_cliente():
    nombre_buscar = input("Ingrese nombre del cliente:")
    encontrado = False
    for turno in turnos:
        if turno["nombre"] == nombre_buscar:
            print("\nCliente encontrado:")
            print("Servicio:", turno["servicio"])
            print("Horario:", turno["horario"])
            encontrado = True
        if encontrado == False:
            print("No se encontró el cliente")

opcion = 0
while opcion != 4:
    print("\n--- Sistema de Turnos Salón v2 ---")
    print("1 - Agregar turno")
    print("2 - Ver turnos")
    print("3 - Buscar cliente")
    print("4 - Salir")
    opcion = int(input("Elegí una opción:"))
    if opcion == 1:
        agregar_turno()
    else:
        if opcion == 2:
            mostrar_turnos()
        else:
            if opcion ==3:
                buscar_cliente()
            else:
                if opcion == 4:
                    print("Programa finalizado")
                else:
                    print("Opción incorrecta")
