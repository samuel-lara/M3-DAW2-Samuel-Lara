import datetime


class Note:
    def __init__(self, memo, tags=""):
        self.memo = memo
        self.date = datetime.date.today()
        self.tags = tags

    def match(self, filter):
        # busca el parametre que li passem i mira si coincideix amb la nota
        return filter in self.memo

######################


class NoteBook:
    def __init__(self):
        self.notes = []

    def search(self, filter):
        # bucle que torna un array si la nota coincideix amb alguna nota que li passem
        resultatBuscar = [note for note in self.notes if note.match(filter)]
        
        if resultatBuscar != []:
            print("S'ha trobat la nota")
        else:
            print("NO s'ha trobat la nota")

    def new_note(self, memo, tags=""):
        self.notes.append(Note(memo, tags))
        
    def show_notes(self):
        for note in self.notes:
            print(note.memo + " (tag:" + note.tags +  ")")


#########################

# Creació de l'objecte llibreta
Llibreta = NoteBook()

#########################


# MENU
contador = True
while contador:

    # imprimir llista
    print(
        '\n', 'Escollir una opció: \n',
        '1. Mostrar notes \n',
        '2. Buscar \n',
        '3. Afegir nova nota\n',
        '4. Sortir \n'
    )

    # numero introduït per teclat per l'usuari
    contador = input('Introduir el número:')

    if contador == "1":  # 1.Mostrar notes-Funciona
        print('Mostrant notes...')
        Llibreta.show_notes()
    elif contador == "2":  # 2.Buscar-Funciona
        buscar = input('Introduïr nota a buscar:')
        print('Buscant...')
        print('--------------')
        Llibreta.search(buscar)
    elif contador == "3":  # 3. Afegir-Funciona
        afegir = input('Afegir nova nota:')
        tags = input('Afegir nou Tag:')
        print('Afegint nova nota...')
        print('--------------')
        Llibreta.new_note(afegir, tags)
    elif contador == "4":  # 4.Sortir-Funciona
        contador = False
        print('Sortint...')
        print('--------------')
    else:
        print("Introdueix un número vàlid")
        print('--------------')
