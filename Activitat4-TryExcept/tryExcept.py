def notasAlumno():
    try:
        x = int(input("Afegir una nota: "))
        if x > 10:
            raise OverflowError("ERROR - No es permet una nota major que 10") #error personalitzat
        elif x < 0:
            raise OverflowError("ERROR - No es permet una nota menor que 0") #error personalitzat
        
    except ValueError as e:  # Detecta si ha un error al tipus de dada
        print("ERROR - S'ha d'introduïr un tipus de dada vàlid ", e)
    except KeyboardInterrupt as e:  # Detecta si s'ha desconectat el teclat o si l'usuari ha fet CTRL + C
        print("ERROR - S'ha tallat la connexió amb el teclat: ", e)
    except OverflowError as e: #imprimim l'error personalitzat
        print(e)
    finally:
        print("Aquesta línia sempre s'imprimeix")

notasAlumno()
