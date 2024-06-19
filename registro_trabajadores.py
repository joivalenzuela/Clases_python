def main():
    registro = []
    while True:
        opcion = input("1)Registrar Trabajador\n2)Listar todos los trabajadores\n3)Imprimir en planilla de sueldos\n4)Salir del programa\n: ")
        match opcion:
            case "1":
                registro.append(registrar())
            case "2":
                listar(registro)
            case "3":
                imprimir(registro)
            case "4":
                break
            case _:
                print("Instruccion no valida")
    
def calcular_sueldo(dinero):
    dinero = dinero - 70_000 - 120_000
    return dinero

def registrar():
    nombre = input("Nombre y apellido: ")
    cargo = input("Cargo: ")
    try:
        sueldo_bruto = int(input("Sueldo Bruto: "))
    except ValueError:
        print("ERROR.\nValor invalido")
        return 0
    return {"nombre":nombre,"cargo":cargo,"sueldo_bruto":sueldo_bruto,"sueldo_final":calcular_sueldo(sueldo_bruto)}

def listar(registro):
    sep ="|||"
    print(f"Trabajador{sep}Cargo{sep}Sueldo Bruto{sep}Desc. Salud{sep}Desc. AFP{sep}Liquido a pagar")
    for i in range(len(registro)):
        if registro = "":
            print("no hay data")
            return
        print(registro[i]["nombre"],sep,registro[i]["cargo"],sep,registro[i]["sueldo_bruto"],sep,"70000",sep,"120000",sep,registro[i]["sueldo_final"])
        
def imprimir(registro):
    opcion = input("Como desea imprimir\n1)Imprimir Todo\n2)Imprimir cargo especifico\n3)Volver\n: ")
    sep ="|||"
    with open("datos.txt","w") as datos:
        match opcion:
            case "1":
                datos.write(f"Trabajador{sep}Cargo{sep}Sueldo Bruto{sep}Desc. Salud{sep}Desc. AFP{sep}Liquido a pagar\n")
                for i in range(len(registro)):
                    datos.write(f"{registro[i]["nombre"]}{sep}{registro[i]["cargo"]}{sep}{registro[i]["sueldo_bruto"]}{sep}{"70000"}{sep}{"120000"}{sep}{registro[i]["sueldo_final"]}\n")
            case "2":
                cargo_elegido = input("Ingrese un cargo: ")
                datos.write(f"Trabajador{sep}{registro[i]["cargo"]}{sep}Sueldo Bruto{sep}Desc. Salud{sep}Desc. AFP{sep}Liquido a pagar\n")
                for i in range(len(registro)):
                    if registro[i]["cargo"] == cargo_elegido:
                        datos.write(f"{registro[i]["nombre"]}{sep}{registro[i]["sueldo_bruto"]}{sep}{"70000"}{sep}{"120000"}{sep}{registro[i]["sueldo_final"]}\n")
            case _:
                print("Instruccion no valida")
        datos.close() 
if __name__ == "__main__":
    main()            
    