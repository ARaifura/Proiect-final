# import csv
# import requests

def citeste_utilizatori_din_csv(fisier_csv):
    utilizatori = []
    try:
        with open(fisier_csv, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            utilizatori = [row for row in reader]
    except FileNotFoundError:
        print(f"Fișierul {fisier_csv} nu a fost găsit.")
    return utilizatori

import csv
def scrie_utilizatori_in_csv(fisier_csv, utilizatori):
    # Include 'over_country' în lista de fieldnames
    fieldnames = ["id", "nume", "prenume", "email", "icao24", "departure_country", "destination_country",
                  "duration_minutes", "over_country"]

    with open(fisier_csv, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()  # Scrie antetul
        writer.writerows(utilizatori)  # Scrie toate liniile

    # Extragem automat toate cheile din primul utilizator ca fieldnames
    fieldnames = utilizatori[0].keys()



def adauga_utilizator_in_csv(fisier_csv, id, nume, prenume, email, icao24, departure_country, destination_country, duration_minutes, over_country=''):
    utilizatori = citeste_utilizatori_din_csv(fisier_csv)

    utilizator_nou = {
        "id": id,
        "nume": nume,
        "prenume": prenume,
        "email": email,
        "icao24": icao24,
        "departure_country": departure_country,
        "destination_country": destination_country,
        "duration_minutes": duration_minutes,
        "over_country": over_country  # Asigură-te că acest câmp există
    }

    utilizatori.append(utilizator_nou)
    scrie_utilizatori_in_csv(fisier_csv, utilizatori)


def afiseaza_toti_pasagerii(fisier_csv):
    """Afisează toți pasagerii din fișierul CSV."""
    utilizatori = citeste_utilizatori_din_csv(fisier_csv)

    if utilizatori:
        for utilizator in utilizatori:
            print(f"ID: {utilizator['id']}")
            print(f"Nume: {utilizator['nume']}")
            print(f"Prenume: {utilizator['prenume']}")
            print(f"Email: {utilizator['email']}")
            print(f"ICAO24: {utilizator['icao24']}")
            print(f"Țara de plecare: {utilizator['departure_country']}")
            print(f"Avionul zboară deasupra: {utilizator['over_country']}")  # Modificat pentru 'over_country'
            print(f"Durata zborului: {utilizator['duration_minutes']} minute\n")
    else:
        print("Nu sunt utilizatori in fisier.")

def modifica_utilizator_in_csv(fisier_csv, id_de_modificat, nume, prenume, email, icao24, departure_country, destination_country, duration_minutes, over_country=''):
    utilizatori = citeste_utilizatori_din_csv(fisier_csv)
    utilizator_de_modificat = None

    for utilizator in utilizatori:
        if utilizator['id'] == id_de_modificat:
            utilizator_de_modificat = utilizator
            break

    if utilizator_de_modificat:
        utilizator_de_modificat.update({
            "nume": nume,
            "prenume": prenume,
            "email": email,
            "icao24": icao24,
            "departure_country": departure_country,
            "destination_country": destination_country,
            "duration_minutes": duration_minutes,
            "over_country": over_country  # Actualizează și acest câmp
        })

        scrie_utilizatori_in_csv(fisier_csv, utilizatori)
        return True
    else:
        return False


def sterge_utilizator_din_csv(fisier_csv, id_de_sters):
    # Logica de ștergere a utilizatorului
    utilizatori = citeste_utilizatori_din_csv(fisier_csv)
    utilizatori_noi = [utilizator for utilizator in utilizatori if utilizator['id'] != id_de_sters]

    if len(utilizatori) == len(utilizatori_noi):
        return False  # Nu a fost găsit niciun utilizator cu ID-ul respectiv

    scrie_utilizatori_in_csv(fisier_csv, utilizatori_noi)
    return True  # Utilizatorul a fost șters cu succes

