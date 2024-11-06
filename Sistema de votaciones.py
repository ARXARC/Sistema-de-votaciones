dpi = input("Ingresa tu dpi ")
rs1 = input("\nQuieres continuar con ese DPI/ {y/n} ")

if rs1 == "y":
    if len(dpi) == 13:
        edad = int(input("\nIngresa tu edad "))
        
        if edad >= 7 and edad <= 18:
            dep = input("\nIngresa en mayus tu departamento ")
            
            lista_dep = ["ALTA VERAPAZ", 
                          "BAJA VERAPAZ", 
                          "CHIMALTENANGO", 
                          "CHIQUIMULA", 
                          "EL PROGRESO", 
                          "ESCUINTLA", 
                          "GUATEMALA", 
                          "HUEHUETENANGO", 
                          "IZABAL", 
                          "JALAPA", 
                          "JUTIAPA", 
                          "PETÉN", 
                          "QUICHÉ", 
                          "QUETZALTENANGO",
                          "RETALHULEU",
                          "SACATEPÉQUEZ",
                          "SAN MARCOS", 
                          "SANTA ROSA", 
                          "SOLOLÁ", 
                          "SUCHITEPÉQUEZ", 
                          "TOTONICAPÁN", 
                          "ZACAPA"]
            
            if dep not in lista_dep:
                print("\nDepartamento invalido")
            else:
                nombre = input("\nIngresa tu nombre ")
                print("\n Hola ", nombre, "por quien quieres votar")
                voto_presidente = input("\nVotar por precidente ROJO (A) AZUL (B)"    )
                voto_alcalde = input("\nVotar por alcalde VERDE(C) NARANJA(D)"    )

                if voto_presidente == "A":
                    presidente="ROJO"
                elif voto_presidente == "B":
                    presidente="AZUL"
                else:
                    print("\nOperacion no valida")

                if voto_alcalde == "C":
                    alcalde= "VERDE"
                elif voto_alcalde == "D":
                    alcalde="NARANJA"
                else:
                    print("\nOperacion no valida")

                cf2=input("Quires confirmar tus vostos? y/n")
                if cf2=="y":

                    print("\n Tu ficha de votacion fue:","\n Tu: ",nombre,"\nA la dedad de: ",edad,"\n Con el dpi: ",dpi,"\n Del departamento de: ",dep ,"\n Votaste para el presidente: ",presidente,"\n Y para alcalde por: ", alcalde,"\n Gracias por votar")
                else:
                    print("Operacion no valida")
        else:
            print("\nNo cumples con la edad")
    else:
        print("\ningresa un dpi valido")
else: 
    print("Operacion cancelada")
