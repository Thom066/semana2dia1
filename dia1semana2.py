warning = "\033[93m"
danger = "\033[91m"
success = "\033[92m"
reset = "\033[0m"

compras = []
contador_compras = 1

precios_base = {
    "nacional": 230000,
    "internacional": 4200000
}

while True:
    print("\n--- SISTEMA DE RESERVAS DE EQUIPAJE AÉREO ---")
    print("1. Registrar nueva compra")
    print("2. Menú administrador")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Nombre del pasajero: ")

        while True:
            tipo_viaje = input("Tipo de viaje (nacional/internacional): ").lower()
            if tipo_viaje in precios_base:
                break
            else:
                print(warning + "Tipo de viaje inválido." + reset)

        while True:
            try:
                peso_equipaje = float(input("Peso del equipaje principal (kg): "))
                break
            except:
                print(warning + "Ingrese un valor válido." + reset)

        lleva_mano = input("¿Lleva equipaje de mano? (si/no): ").lower()
        peso_mano = 0
        if lleva_mano == "si":
            while True:
                try:
                    peso_mano = float(input("Peso del equipaje de mano (kg): "))
                    break
                except:
                    print(warning + "Ingrese un valor válido." + reset)

        fecha = input("Fecha del viaje (YYYY-MM-DD): ")

        if peso_equipaje > 50:
            estado_equipaje = danger + "No admitido" + reset
            costo_equipaje = 0
        elif peso_equipaje <= 20:
            estado_equipaje = success + "Equipaje aceptado" + reset
            costo_equipaje = 50000
        elif peso_equipaje <= 30:
            estado_equipaje = success + "Equipaje aceptado" + reset
            costo_equipaje = 70000
        else:
            estado_equipaje = success + "Equipaje aceptado" + reset
            costo_equipaje = 110000

        if lleva_mano == "si":
            if peso_mano > 13:
                estado_mano = warning + "Rechazado" + reset
            else:
                estado_mano = success + "Aceptado" + reset
        else:
            estado_mano = warning + "No lleva equipaje de mano" + reset

        precio_base = precios_base[tipo_viaje]
        total = precio_base + (costo_equipaje if "aceptado" in estado_equipaje.lower() else 0)
        id_compra = f"COMP{contador_compras:04d}"
        contador_compras += 1

        compra = {
            "id": id_compra,
            "nombre": nombre,
            "tipo_viaje": tipo_viaje,
            "fecha": fecha,
            "estado_equipaje": estado_equipaje,
            "estado_mano": estado_mano,
            "total": total
        }
        compras.append(compra)

        print("\n--- RESUMEN DE COMPRA ---")
        print(success + f"ID de compra: {id_compra}" + reset)
        print(f"Nombre: {nombre}")
        print(f"Destino: {tipo_viaje.capitalize()}")
        print(f"Fecha: {fecha}")
        print(f"Estado del equipaje principal: {estado_equipaje}")
        print(f"Estado del equipaje de mano: {estado_mano}")
        print(success + f"Costo total del viaje: ${total:,}" + reset)

    elif opcion == "2":
        print("\n--- MENÚ ADMIN ---")
        print("1. Total recaudado en todas las compras")
        print("2. Total recaudado para una fecha específica")
        print("3. Número total de pasajeros procesados")
        print("4. Número de pasajeros nacionales/internacionales")
        print("5. Consultar compra por ID")
        opcion_admin = input("Seleccione una opción: ")

        if opcion_admin == "1":
            total = sum(compra['total'] for compra in compras)
            print(success + f"Total recaudado: ${total:,}" + reset)
        elif opcion_admin == "2":
            fecha = input("Ingrese la fecha (YYYY-MM-DD): ")
            total_fecha = sum(compra['total'] for compra in compras if compra['fecha'] == fecha)
            print(success + f"Total recaudado en {fecha}: ${total_fecha:,}" + reset)
        elif opcion_admin == "3":
            print(success + f"Total de pasajeros procesados: {len(compras)}" + reset)
        elif opcion_admin == "4":
            nacionales = sum(1 for compra in compras if compra['tipo_viaje'] == 'nacional')
            internacionales = sum(1 for compra in compras if compra['tipo_viaje'] == 'internacional')
            print(success + f"Pasajeros nacionales: {nacionales}" + reset)
            print(success + f"Pasajeros internacionales: {internacionales}" + reset)
        elif opcion_admin == "5":
            id_buscar = input("Ingrese el ID de compra: ")
            encontrado = False
            for compra in compras:
                if compra['id'] == id_buscar:
                    print("\n--- DETALLE DE COMPRA ---")
                    for k, v in compra.items():
                        print(f"{k.capitalize()}: {v}")
                    encontrado = True
                    break
            if not encontrado:
                print(danger + "Compra no encontrada." + reset)
        else:
            print(warning + "Opción inválida" + reset)

    elif opcion == "3":
        print(success + "Gracias por usar el sistema. ¡Hasta pronto!" + reset)
        break
    else:
        print(warning + "Opción inválida, intente de nuevo." + reset)
