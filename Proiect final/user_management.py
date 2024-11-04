def adauga_utilizator(lista_utilizatori, id, nume, prenume, email, parola, departament):
    """Adauga un utilizator nou in lista.

    Args:
        lista_utilizatori (list): Lista existenta de utilizatori.
        id (str): ID-ul utilizatorului.
        nume (str): Numele utilizatorului.
        prenume (str): Prenumele utilizatorului.
        email (str): Email-ul utilizatorului.
        parola (str): Parola utilizatorului.
        departament (str): Departamentul utilizatorului.
    """
    nou_utilizator = {
        "id": id,
        "nume": nume,
        "prenume": prenume,
        "email": email,
        "parola": parola,
        "departament": departament
    }
    lista_utilizatori.append(nou_utilizator)
