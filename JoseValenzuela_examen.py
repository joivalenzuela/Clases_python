import random,math
def main():
    trabajadores = ["Juan Perez","Maria Garcia","Carlos Lopez","Ana Martinez","Pedro Rodriguez","Laura Hernandez","Miguel Sanches","Isabel Gomez","Francisco Diaz","Elena Fernandez"]
    while True:
        opcion = input("1. Asignar sueldos aleatorios\n2.Clasificar sueldos\n3.Ver estadisticas\n4.Reporte de sueldos\n5.Salir del programa\n")
        match opcion:
            case "1":
                trabajadores_sueldo = sueldos_aleatorios(trabajadores)
                print("Ejecutado correctamente")
            case "2":
                try:
                    clasificado = clasificar_sueldos(trabajadores_sueldo)
                    imprimir_sueldos_clasificados(clasificado)
                except UnboundLocalError:
                    print("ERROR. Primero debe generar los sueldos de los trabajadores")
            case "3":
                try:
                    ver_estadisticas(trabajadores_sueldo)
                except UnboundLocalError:
                    print("ERROR. Primero debe generar los sueldos de los trabajadores")
            case "4":
                try:
                    crear_archivo(crear_registro(trabajadores_sueldo))
                except UnboundLocalError:
                    print("ERROR. Primero debe generar los sueldos de los trabajadores")
                    
                    
            case "5":
                print("Finalizando Prograna...")
                print("Desarrollado por Jose Valenzuela\n20.880.062-0")
                break
            case _:
                print("Comando no valido")




def sueldos_aleatorios(trabajadores):
    trabajadores_sueldo = {}
    for i in range(len(trabajadores)):
        sueldo = random.randint(300_000,2_500_000)
        trabajadores_sueldo[trabajadores[i]] = sueldo
    return trabajadores_sueldo

def clasificar_sueldos(t_sueldos):
    clasificacion = {}
    tier1 = []
    tier2 = []
    tier3 = []    
    for key,value in t_sueldos.items():
        if int(value) < 800_000:
            tier1.append([key,value])
        elif 800_000 <= int(value) < 2_000_000:
            tier2.append([key,value])
        elif int(value) >= 2_000_000:
            tier3.append([key,value])
    clasificacion["menos_8k"] = tier1
    clasificacion["entre_8k_2m"] = tier2
    clasificacion["mayor_2m"] = tier3
    return clasificacion

def imprimir_sueldos_clasificados(clasificados):
    sum = 0
    print("CLASIFICACION:\n")
    print(f"Sueldos menores a $800.000 TOTAL: {len(clasificados["menos_8k"])}")
    print("Nombre empleado\tSueldo")
    for i in range(len(clasificados["menos_8k"])):
        print(f"{clasificados["menos_8k"][i][0]}\t${clasificados["menos_8k"][i][1]}")
        sum += int(clasificados["menos_8k"][i][1])
    print("\n")
    print(f"Sueldos entre $800.000 y $2.000.000 TOTAL: {len(clasificados["entre_8k_2m"])}")
    print("Nombre empleado\tSueldo")
    for i in range(len(clasificados["entre_8k_2m"])):
        print(f"{clasificados["entre_8k_2m"][i][0]}\t${clasificados["entre_8k_2m"][i][1]}")
        sum += int(clasificados["entre_8k_2m"][i][1])
    print("\n")
    print(f"Sueldos Superiores a $2.000.000 TOTAL: {len(clasificados["mayor_2m"])}")
    print("Nombre empleado\tSueldo")
    for i in range(len(clasificados["mayor_2m"])):
        print(f"{clasificados["mayor_2m"][i][0]}\t${clasificados["mayor_2m"][i][1]}")
        sum += int(clasificados["mayor_2m"][i][1])
    print("\n")
    print(f"TOTAL SUELDOS: ${sum}")
    print("\n")
    
    
def ver_estadisticas(datos):
    mayor = ["nada",0]
    menor = ["nada",3_000_000]
    promedio_sueldos = 0
    media_geometrica = 0
    sum = 0
    mult = 1
    for key,value in datos.items():
        value = int(value)
        if value >= mayor[1]:
            mayor = [key,value]
        if value <= menor[1]:
            menor = [key,value]
        sum += value
        mult *= value
    promedio_sueldos = sum/len(datos)
    media_geometrica = round(mult**(1/10),2)
    print("ESTADISTICAS: \n")
    print("Mayor Sueldo: ")
    print("Trabajador\tSueldo")
    print(f"{mayor[0]}\t${mayor[1]}\n")
    print("Menor Sueldo: ")
    print("Trabajador\tSueldo")
    print(f"{menor[0]}\t${menor[1]}\n")
    print(f"Promedio Sueldos: {promedio_sueldos}\n")
    print(f"Media geometrica Sueldos: {media_geometrica}\n")
    
def crear_registro(datos):
    registrofinal =[]
    registro = {}
    for key,value in datos.items():
        registro["Nombre Empleado"] = key
        registro["Sueldo Base"] = value
        registro["Descuento Salud"] = math.floor((value * 0.07))
        registro["Descuento AFP"] = math.floor((value * 0.12))
        registro["Sueldo Liquido"] = math.floor((registro["Sueldo Base"] - registro["Descuento Salud"]) - registro["Descuento AFP"])
        a = registro.copy()
        registrofinal.append(a)
    return registrofinal
def crear_archivo(registro):
    with open("reporte.csv","w") as archivo:
        archivo.write("Nombre Empleado,Sueldo Base,Descuento Salud,Descuento AFP,Sueldo Liquido\n")
        for i in range(len(registro)):
            archivo.write(f"{registro[i]["Nombre Empleado"]},{registro[i]["Sueldo Base"]},{registro[i]["Descuento Salud"]},{registro[i]["Descuento AFP"]},{registro[i]["Sueldo Liquido"]}\n")
        
        
if __name__ == "__main__":
    main()