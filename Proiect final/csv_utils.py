import csv


def citeste_utilizatori_din_csv(fisier_csv):
    """Citeste utilizatori dintr-un fisier CSV si ii returneaza ca o lista de dictionare."""
    utilizatori = []
    with open(fisier_csv, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            utilizatori.append(row)
    return utilizatori


def adauga_utilizator_in_csv(fisier_csv, utilizator_nou):
    """Adauga un utilizator in fisierul CSV."""
    utilizatori = citeste_utilizatori_din_csv(fisier_csv)

    # Adauga utilizatorul nou
    utilizatori.append(utilizator_nou)

    with open(fisier_csv, 'w', newline='') as csvfile:
        fieldnames = ['id', 'nume', 'prenume', 'email', 'icao24', 'departure_country', 'destination_country',
                      'duration_minutes']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(utilizatori)


def afiseaza_toti_pasagerii(fisier_csv):
    """Afiseaza toti pasagerii din fisierul CSV."""
    utilizatori = citeste_utilizatori_din_csv(fisier_csv)

    if utilizatori:
        for utilizator in utilizatori:
            print(f"ID: {utilizator['id']}")
            print(f"Nume: {utilizator['nume']}")
            print(f"Prenume: {utilizator['prenume']}")
            print(f"Email: {utilizator['email']}")
            print(f"ICAO24: {utilizator['icao24']}")
            print(f"Țara de plecare: {utilizator['departure_country']}")
            print(f"Țara de destinație: {utilizator['destination_country']}")
            print(f"Durata zborului: {utilizator['duration_minutes']} minute\n")
    else:
        print("Nu sunt utilizatori in fisier.")
