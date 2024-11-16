from csv_utils import afiseaza_toti_pasagerii, adauga_utilizator_in_csv
from flight_data import get_flight_data

def meniu_principal(fisier_csv):
    while True:
        print("\nMeniu Principal:")
        print("1. Adauga utilizator")
        print("2. Afiseaza toti pasagerii")
        print("3. Obtine date zbor")
        print("4. Iesire")

        optiune = input("Alege o optiune: ")

        if optiune == "1":
            # Adaugă un utilizator nou
            id = input("ID: ")
            nume = input("Nume: ")
            prenume = input("Prenume: ")
            email = input("Email: ")
            icao24 = input("ICAO24: ")
            departure_country = input("Țara de plecare: ")
            destination_country = input("Țara de destinație: ")
            duration_minutes = input("Durata zborului (minute): ")

            utilizator_nou = {
                'id': id,
                'nume': nume,
                'prenume': prenume,
                'email': email,
                'icao24': icao24,
                'departure_country': departure_country,
                'destination_country': destination_country,
                'duration_minutes': duration_minutes
            }
            adauga_utilizator_in_csv(fisier_csv, utilizator_nou)

        elif optiune == "2":
            afiseaza_toti_pasagerii(fisier_csv)

        elif optiune == "3":
            icao24 = input("Introduceti ICAO24 pentru a obtine datele zborului: ")
            flight_data = get_flight_data(icao24)
            if flight_data:
                print(f"Tara de plecare: {flight_data['origin_country']}")
                print(f"Tara de destinatie: {flight_data['destination_country'] if flight_data['destination_country'] else 'Informatie indisponibila'}")
                print(f"Viteza avionului: {flight_data['velocity']} km/h")
                print(f"Altitudinea: {flight_data['altitude']} m")
                print(f"Latitudinea: {flight_data['latitude']}")
                print(f"Longitudinea: {flight_data['longitude']}")
        elif optiune == "4":
            print("Ieșire din aplicație.")
            break

if __name__ == "__main__":
    fisier_csv = 'utilizatori.csv'
    meniu_principal(fisier_csv)
