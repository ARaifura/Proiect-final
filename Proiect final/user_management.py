from csv_utils import citeste_utilizatori_din_csv, scrie_utilizatori_in_csv


def adauga_utilizator_in_csv(fisier_csv, id, nume, prenume, email, icao24, departure_country, destination_country,
                             duration_minutes):
    """Adauga un utilizator nou in fisierul CSV."""
    utilizatori = citeste_utilizatori_din_csv(fisier_csv)

    utilizator_nou = {
        "id": id,
        "nume": nume,
        "prenume": prenume,
        "email": email,
        "icao24": icao24,
        "departure_country": departure_country,
        "destination_country": destination_country,
        "duration_minutes": duration_minutes
    }

    utilizatori.append(utilizator_nou)

    scrie_utilizatori_in_csv(fisier_csv, utilizatori)


def modifica_utilizator(fisier_csv):
    """Modifica un utilizator existent."""
    utilizatori = citeste_utilizatori_din_csv(fisier_csv)
    id_de_modificat = input("Introdu ID-ul utilizatorului de modificat: ")
    utilizator_de_modificat = None

    for utilizator in utilizatori:
        if utilizator['id'] == id_de_modificat:
            utilizator_de_modificat = utilizator
            break

    if utilizator_de_modificat:
        print(f"Utilizator gasit: {utilizator_de_modificat}")
        nume = input(f"Nume (lăsat gol pentru {utilizator_de_modificat['nume']}): ") or utilizator_de_modificat['nume']
        prenume = input(f"Prenume (lăsat gol pentru {utilizator_de_modificat['prenume']}): ") or \
                  utilizator_de_modificat['prenume']
        email = input(f"Email (lăsat gol pentru {utilizator_de_modificat['email']}): ") or utilizator_de_modificat[
            'email']
        departure_country = input(
            f"Țara de plecare (lăsat gol pentru {utilizator_de_modificat['departure_country']}): ") or \
                            utilizator_de_modificat['departure_country']
        destination_country = input(
            f"Țara de destinație (lăsat gol pentru {utilizator_de_modificat['destination_country']}): ") or \
                              utilizator_de_modificat['destination_country']
        duration_minutes = input(
            f"Durata zborului (lăsat gol pentru {utilizator_de_modificat['duration_minutes']}): ") or \
                           utilizator_de_modificat['duration_minutes']

        utilizator_de_modificat.update({
            "nume": nume,
            "prenume": prenume,
            "email": email,
            "departure_country": departure_country,
            "destination_country": destination_country,
            "duration_minutes": duration_minutes
        })

        scrie_utilizatori_in_csv(fisier_csv, utilizatori)

        print("Utilizatorul a fost modificat cu succes!")
    else:
        print("Nu s-a găsit utilizatorul cu acest ID.")