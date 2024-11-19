import requests

import requests
import time  # Pentru pauză între încercări

def get_country_from_coordinates(latitude, longitude, retries=3, delay=10):
    """
    Obține țara folosind coordonatele geografice prin Nominatim API.
    Încearcă de până la `retries` ori în caz de eroare, cu o pauză de `delay` secunde între încercări.
    """
    url = f"https://nominatim.openstreetmap.org/reverse"
    params = {
        "lat": latitude,
        "lon": longitude,
        "format": "json",
        "zoom": 5,  # Detalii despre țară
    }

    for attempt in range(retries):
        try:
            print(f"Încercare {attempt + 1}/{retries} pentru coordonatele: {latitude}, {longitude}")
            response = requests.get(url, params=params)
            response.raise_for_status()  # Ridică excepție dacă statusul nu e 200
            try:
                data = response.json()
            except ValueError as ve:
                print(f"Eroare la parsarea răspunsului JSON: {ve}")
                return "Eroare la parsarea datelor"

            # Verificăm dacă informația despre țară este disponibilă
            if "address" in data and "country" in data["address"]:
                return data["address"]["country"]
            else:
                print(f"Nu s-a găsit informația despre țară pentru coordonatele: {latitude}, {longitude}")
                return "Informație indisponibilă"

        except requests.exceptions.RequestException as e:
            print(f"Încercarea {attempt + 1} a eșuat: {e}")
            if attempt < retries - 1:
                print(f"Aștept {delay} secunde înainte de următoarea încercare...")
                time.sleep(delay)  # Pauză fixă de 3 secunde
            else:
                print("Eroare: Nu s-a reușit conectarea la API-ul Nominatim după toate încercările.")
                return "Eroare la obținerea țării"


def get_flight_data(icao24):
    """Obține informații despre un zbor bazat pe numărul său ICAO 24."""
    url = "https://opensky-network.org/api/states/all"
    params = {"icao24": icao24}

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        if data["states"]:
            state = data["states"][0]
            # Extragem informațiile disponibile
            latitude = state[6]
            longitude = state[5]

            # Verificăm coordonatele înainte de a solicita țara
            if latitude is not None and longitude is not None:
                over_country = get_country_from_coordinates(latitude, longitude)
            else:
                over_country = "Informație indisponibilă"

            flight_data = {
                "callsign": state[1],  # Apelul avionului
                "origin_country": state[2],  # Țara de plecare
                "velocity": round(state[9] * 1.852, 2) if state[9] else None,  # Viteza (knots -> km/h)
                "altitude": state[7] if state[7] is not None else "Informație indisponibilă",  # Altitudinea
                "latitude": latitude if latitude is not None else "Informație indisponibilă",  # Latitudinea
                "longitude": longitude if longitude is not None else "Informație indisponibilă",  # Longitudinea
                "over_country": over_country,
            }
            return flight_data
        else:
            print("Nu s-au găsit date pentru acest zbor.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"A apărut o eroare la solicitarea API-ului OpenSky: {e}")
        return None
