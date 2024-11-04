import requests

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
        response.raise_for_status()
        data = response.json()

        if data["states"]:
            state = data["states"][0]
            return {
                "callsign": state[1],
                "origin_country": state[2],
                "time_position": state[3],
                "onground": state[8],
                # Alte informații extrase pot fi adăugate aici
            }
        else:
            print("Nu s-au găsit date pentru acest zbor.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"A apărut o eroare la solicitarea API-ului: {e}")
        return None
