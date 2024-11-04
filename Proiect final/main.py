import requests
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
        departament = utilizator['departament']
        if departament not in utilizatori_dupa_departament:
            utilizatori_dupa_departament[departament] = []
        utilizatori_dupa_departament[departament].append(utilizator)
    return utilizatori_dupa_departament

# Exemplu de utilizare
fisier_csv = 'utilizatori.csv'  # Asigura-te ca ai un fisier CSV cu coloanele: id, nume, prenume, email, departament
lista_utilizatori = citeste_utilizatori_din_csv(fisier_csv)
utilizatori_grupati = grupeaza_utilizatori_dupa_departament(lista_utilizatori)

# Afisarea rezultatelor
for departament, utilizatori in utilizatori_grupati.items():
    print(f"Departamentul {departament}:")
    for utilizator in utilizatori:
        print(f"  - {utilizator['nume']} {utilizator['prenume']}, {utilizator['email']}")
def get_flight_data(icao24):
    """Obține informații despre un zbor bazat pe numărul său ICAO 24.

    Args:
        icao24 (str): Numărul ICAO 24-bit al avionului.

    Returns:
        dict: Un dicționar cu informații despre zbor, sau None dacă nu s-au găsit date.
    """

    url = "https://opensky-network.org/api/states/all"
    params = {
        "icao24": icao24
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Verifică dacă a fost o eroare la request
        data = response.json()

        if data["states"]:
            state = data["states"][0]
            return {
                "callsign": state["callsign"],
                "origin_country": state["origin_country"],
                "time_position": state["time_position"],
                "onground": state["onground"],
                # ... alte informații pe care le poți extrage din date
            }
        else:
            print("Nu s-au găsit date pentru acest zbor.")
    except requests.exceptions.RequestException as e:
        print(f"A apărut o eroare la solicitarea API-ului: {e}")
        return None

if __name__ == "__main__":
    icao24 = input("Introdu numărul ICAO 24 al avionului: ")
    flight_data = get_flight_data(icao24)

    if flight_data:
        print("Callsign:", flight_data["callsign"])
        print("Țara de origine:", flight_data["origin_country"])
        # ... afișează alte informații relevante
    else:
        print("Nu s-au putut obține date despre zbor.")