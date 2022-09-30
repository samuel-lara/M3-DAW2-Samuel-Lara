'''Programa per a validar notes'''

#Es crea la classe per a l'Error personalitzat
class ErrorPersonalitzat(Exception):
    pass

class ValueError(Exception):
    pass

#Es crea la clase nota
class Nota:
    def __init__(self, nota): #constructor
        self.nota = nota
        
        '''Solo me acepta los ERRORES que yo he creado'''
        #Creamos una función para ejecutar el tryExcept
    def notesAlumne(self):
        nota = int(self.nota)
        try:
            if nota > 10:
                raise ErrorPersonalitzat("ERROR - No es permet una nota major que 10") #error personalitzat
            elif nota < 0:
                raise ErrorPersonalitzat("ERROR - No es permet una nota menor que 0") #error personalitzat
        except ErrorPersonalitzat as e: #imprimim l'error personalitzat - Funciona
            print(e)
        except ValueError as e:  # Detecta si ha un error al tipus de dada-No funciona
            print("ERROR - S'ha d'introduïr un tipus de dada vàlid ", e)
        except KeyboardInterrupt as e:  # Detecta si s'ha desconectat el teclat o si l'usuari ha fet CTRL + C - No funciona
            print("ERROR - S'ha tallat la connexió amb el teclat: ", e)
        finally:
            print("Aquesta línia sempre s'imprimeix")

if __name__ == "__main__":
    #creem l'objecte nota
    notaIntroduida = int(input("Afegir una nota: "))
    Nota1 = Nota(notaIntroduida)
    print(Nota1.nota)
    Nota1.notesAlumne()