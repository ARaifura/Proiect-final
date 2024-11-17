import csv

def citeste_utilizatori_din_csv(fisier_csv):
    """Citeste utilizatori dintr-un fisier CSV si ii returneaza ca o lista de dictionare."""
    utilizatori = []
    with open(fisier_csv, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            utilizatori.append(row)
    return utilizatori

def scrie_utilizatori_in_csv(fisier_csv, utilizatori):
    """Scrie utilizatori în fișierul CSV."""
    with open(fisier_csv, 'w', newline='') as csvfile:
        # Actualizează fieldnames pentru a include 'over_country' în loc de 'destination_country'
        fieldnames = ['id', 'nume', 'prenume', 'email', 'icao24', 'departure_country', 'over_country', 'duration_minutes']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(utilizatori)

def adauga_utilizator_in_csv(fisier_csv, id, nume, prenume, email, icao24, departure_country, over_country, duration_minutes):
    """Adauga un utilizator nou în fișierul CSV."""
    utilizatori = citeste_utilizatori_din_csv(fisier_csv)

    utilizator_nou = {
        "id": id,
        "nume": nume,
        "prenume": prenume,
        "email": email,
        "icao24": icao24,
        "departure_country": departure_country,
        "over_country": over_country,  # Folosim 'over_country' în loc de 'destination_country'
        "duration_minutes": duration_minutes
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

def modifica_utilizator_in_csv(fisier_csv):
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
        prenume = input(f"Prenume (lăsat gol pentru {utilizator_de_modificat['prenume']}): ") or utilizator_de_modificat['prenume']
        email = input(f"Email (lăsat gol pentru {utilizator_de_modificat['email']}): ") or utilizator_de_modificat['email']
        departure_country = input(f"Țara de plecare (lăsat gol pentru {utilizator_de_modificat['departure_country']}): ") or utilizator_de_modificat['departure_country']
        over_country = input(f"Avionul zboară deasupra (lăsat gol pentru {utilizator_de_modificat['over_country']}): ") or utilizator_de_modificat['over_country']
        duration_minutes = input(f"Durata zborului (lăsat gol pentru {utilizator_de_modificat['duration_minutes']}): ") or utilizator_de_modificat['duration_minutes']

        utilizator_de_modificat.update({
            "nume": nume,
            "prenume": prenume,
            "email": email,
            "departure_country": departure_country,
            "over_country": over_country,  # Folosim 'over_country'
            "duration_minutes": duration_minutes
        })

        scrie_utilizatori_in_csv(fisier_csv, utilizatori)

        print("Utilizatorul a fost modificat cu succes!")
    else:
        print("Nu s-a găsit utilizatorul cu acest ID.")

def sterge_utilizator_din_csv(fisier_csv, id_de_sters):
    # Logica de ștergere a utilizatorului
    utilizatori = citeste_utilizatori_din_csv(fisier_csv)
    utilizatori_noi = [utilizator for utilizator in utilizatori if utilizator['id'] != id_de_sters]

    if len(utilizatori) == len(utilizatori_noi):
        return False  # Nu a fost găsit niciun utilizator cu ID-ul respectiv

    scrie_utilizatori_in_csv(fisier_csv, utilizatori_noi)
    return True  # Utilizatorul a fost șters cu succes

