agenda = {}
salir_1 = "N"
salir_2 = "N"
inicio = 1
salir_3 = 0
salir_4 = 0
salir_5 = 0

while inicio == 1:
    print("BIENVENIDO AL SISTEMA DE AGENDA")
    print("A continuación le presentamos las siguientes opciones:")
    print("1. Agregar un nuevo contacto")
    print("2. Modificar un contacto existente")
    print("3. Salir del sistema")
    opcion = (input("Por favor selecciones el número de la opción que desea utiliar: "))

    if int(opcion) == 1:

        while salir_1=="N":
            salir_3 = 0
            salir_5 = 0
            ident = input("Digite el ID de su contacto: ")
            while salir_5 == 0:
                if ident in agenda.keys():
                    print("Este ID ya se encuentra en la agenda, por favor ingrese un nuevo ID o escriba salir para volver al menú principal")
                    ident = input("Digite el ID de su contacto o salir si desea volver al menú principal: ")

                elif ident.lower() == "salir":
                    salir_5 = 1
                    salir_1 = "Y"
                else: 
                    salir_5 = 1


                    nombre = input("Digite el Nombre de su contacto: ")

                    apellido = input("Digite el apellido de su contacto: ")

                    tel = input("Digite el teléfono de su contacto: ")

                    corr = input("Digite el correo de su contacto: ")
        
                    agenda[ident] = {"Nombre": nombre,"Apellido": apellido,"Tel":tel,"Correo":corr}
                    salir = input("Contacto agendado corrextamente. ¿Desea añadir otro contact? [S/N]: ")

                    while salir_3 == 0:
                        if salir.upper() == "S":
                            salir_3 = 1

                        elif salir.upper() == "N":
                            salir_1 = "Y"
                            salir_3 = 1
                        else:
                            print("Por favor digite una opción valida")
                            salir = input("¿Desea añadir otro contact0? [S/N]: ")

    elif int(opcion) == 2:
        while salir_2 == "N":
            salir_4 = 0
            q = input("Qué ID quiere modificar? ")
            if q in agenda.keys():   
                print("¿Cual de los datos del ID desea modificar?")
                print("1. Nombre")
                print("2. Apellido")
                print("3. Telefono")
                print("4. Correo")
                x = (input("Por favor indique el númmero del dato a modificar: "))
                if int(x) == 1:   
                    p = input("Digite nuevo dato: ")
                    agenda[q]["Nombre"] = p
                elif int(x) == 2:
                    p = input("Digite nuevo dato: ")
                    agenda[q]["Apellido"] = p
                elif int(x) == 3:
                    p = input("Digite nuevo dato: ")
                    agenda[q]["Tel"] = p
                elif int(x) == 4:
                    agenda[q]["Correo"] = p
                else:
                    print("No ha seleccionado un dato valido a modificar, por favor escriba el número correspondiente al dato que quiere modificar")
                    x = input("Quiere modificar Nombre (1), Apellido (2), Tel(3) o Correo (4)?: ")

            elif q.lower() == "salir":
                salir_2 = "Y"
            else: 
                print("Lo sentimos. Este ID no se encuentra en la agenda")
                q = input("Por favor, digite un ID existente que quiera modificar o escriba salir para volver al menú principal: ")

            print("Contacto actualizado exitosamente")
            sld = input("¿Desea actualizar algún otro contacto? [S/N]: ")

            while salir_4 == 0:
                if sld.upper() == "S":
                    salir_4 = 1
                elif sld.upper() == "N":
                    salir_2 = "Y"
                    salir_4 = 1
                else: 
                    print("Opción no valida. Por favor presione S si desea agregar otro contacto o N de lo contrario.")
                    sld = input("¿Desea actualizar algún otro contacto? [S/N]: ")

    elif int(opcion) == 3:
        print("Sistema finalizado exitosamente")
        print("Muchas gracias")
        inicio = 0

    else: 
        print("No ha seleccionado ninguna de las opciones validas")
        print("Por favor colocar el número de la opción a realizar: 1, 2 o 3.")
        opcion = input("Por favor selecciones el número de la opción que desea utiliar: ")




