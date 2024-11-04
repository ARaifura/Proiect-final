import csv

def citeste_utilizatori_din_csv(fisier_csv):
    """Citeste utilizatori dintr-un fisier CSV si ii returneaza ca o lista de dictionare.

    Args:
        fisier_csv (str): Calea catre fisierul CSV.

    Returns:
        list: O lista de dictionare, fiecare dictionar reprezentand un utilizator.
    """
    utilizatori = []
    with open(fisier_csv, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            utilizatori.append(row)
    return utilizatori

def grupeaza_utilizatori_dupa_departament(lista_utilizatori):
    """Grupeaza utilizatorii intr-un dictionar dupa departament.

    Args:
        lista_utilizatori (list): Lista de utilizatori.

    Returns:
        dict: Un dictionar unde cheile sunt departamentele si valorile sunt liste de utilizatori.
    """
    utilizatori_dupa_departament = {}
    for utilizator in lista_utilizatori:
        departament = utilizator.get('departament')
        if departament not in utilizatori_dupa_departament:
            utilizatori_dupa_departament[departament] = []
        utilizatori_dupa_departament[departament].append(utilizator)
    return utilizatori_dupa_departament
