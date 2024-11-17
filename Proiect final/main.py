import tkinter as tk
from tkinter import messagebox
from csv_utils import citeste_utilizatori_din_csv, adauga_utilizator_in_csv, afiseaza_toti_pasagerii, modifica_utilizator_in_csv, sterge_utilizator_din_csv
from flight_data import get_flight_data

class Application:
    def __init__(self, root, fisier_csv):
        self.root = root
        self.fisier_csv = fisier_csv
        self.root.title("Aplicație Zboruri")
        self.show_main_menu()

    def show_main_menu(self):
        """Afisează meniul principal."""
        self.clear_frame()

        tk.Button(self.root, text="Adaugă utilizator", command=self.add_user).pack(pady=10)
        tk.Button(self.root, text="Afisează toți pasagerii", command=self.show_all_passengers).pack(pady=10)
        tk.Button(self.root, text="Modifică utilizator", command=self.modify_user).pack(pady=10)
        tk.Button(self.root, text="Șterge utilizator", command=self.delete_user).pack(pady=10)
        tk.Button(self.root, text="Obține date de zbor", command=self.get_flight_info).pack(pady=10)
        tk.Button(self.root, text="Ieșire", command=self.root.quit).pack(pady=10)

    def clear_frame(self):
        """Curăță frame-ul curent."""
        for widget in self.root.winfo_children():
            widget.destroy()

    def add_user(self):
        """Interfața pentru adăugarea unui utilizator."""
        self.clear_frame()

        tk.Label(self.root, text="ID:").pack()
        id_entry = tk.Entry(self.root)
        id_entry.pack()

        tk.Label(self.root, text="Nume:").pack()
        nume_entry = tk.Entry(self.root)
        nume_entry.pack()

        tk.Label(self.root, text="Prenume:").pack()
        prenume_entry = tk.Entry(self.root)
        prenume_entry.pack()

        tk.Label(self.root, text="Email:").pack()
        email_entry = tk.Entry(self.root)
        email_entry.pack()

        tk.Label(self.root, text="ICAO24:").pack()
        icao24_entry = tk.Entry(self.root)
        icao24_entry.pack()

        tk.Label(self.root, text="Țara de plecare:").pack()
        departure_country_entry = tk.Entry(self.root)
        departure_country_entry.pack()

        tk.Label(self.root, text="Țara deasupra căreia zboară:").pack()
        over_country_entry = tk.Entry(self.root)
        over_country_entry.pack()

        tk.Label(self.root, text="Durata zborului:").pack()
        duration_entry = tk.Entry(self.root)
        duration_entry.pack()

        def submit_user():
            id = id_entry.get()
            nume = nume_entry.get()
            prenume = prenume_entry.get()
            email = email_entry.get()
            icao24 = icao24_entry.get()
            departure_country = departure_country_entry.get()
            over_country = over_country_entry.get()
            duration = duration_entry.get()

            adauga_utilizator_in_csv(self.fisier_csv, id, nume, prenume, email, icao24, departure_country, over_country, duration)
            messagebox.showinfo("Succes", "Utilizator adăugat cu succes!")
            self.show_main_menu()

        tk.Button(self.root, text="Adaugă Utilizator", command=submit_user).pack(pady=10)
        tk.Button(self.root, text="Înapoi", command=self.show_main_menu).pack(pady=10)

    def show_all_passengers(self):
        """Afisează toți pasagerii înregistrati."""
        self.clear_frame()
        utilizatori = citeste_utilizatori_din_csv(self.fisier_csv)

        if utilizatori:
            for i, utilizator in enumerate(utilizatori):
                over_country = utilizator.get('over_country', 'Informație indisponibilă')
                tk.Label(self.root, text=f"ID: {utilizator['id']}, {utilizator['nume']} {utilizator['prenume']}, Zboară deasupra: {over_country}").pack()
        else:
            messagebox.showinfo("Info", "Nu există utilizatori înregistrați.")

        tk.Button(self.root, text="Înapoi", command=self.show_main_menu).pack()

    def modify_user(self):
        """Modifică un utilizator existent."""
        self.clear_frame()

        tk.Label(self.root, text="Introduceți ID-ul utilizatorului de modificat:").pack()
        id_entry = tk.Entry(self.root)
        id_entry.pack()

        def submit_modify_user():
            id_de_modificat = id_entry.get()

            # Cerem utilizatorului să introducă noile date
            tk.Label(self.root, text="Nume:").pack()
            nume_entry = tk.Entry(self.root)
            nume_entry.pack()

            tk.Label(self.root, text="Prenume:").pack()
            prenume_entry = tk.Entry(self.root)
            prenume_entry.pack()

            tk.Label(self.root, text="Email:").pack()
            email_entry = tk.Entry(self.root)
            email_entry.pack()

            tk.Label(self.root, text="ICAO24:").pack()
            icao24_entry = tk.Entry(self.root)
            icao24_entry.pack()

            tk.Label(self.root, text="Țara de plecare:").pack()
            departure_country_entry = tk.Entry(self.root)
            departure_country_entry.pack()

            tk.Label(self.root, text="Țara deasupra căreia zboară:").pack()
            over_country_entry = tk.Entry(self.root)
            over_country_entry.pack()

            tk.Label(self.root, text="Durata zborului:").pack()
            duration_entry = tk.Entry(self.root)
            duration_entry.pack()

            def submit():
                nume = nume_entry.get()
                prenume = prenume_entry.get()
                email = email_entry.get()
                icao24 = icao24_entry.get()
                departure_country = departure_country_entry.get()
                over_country = over_country_entry.get()
                duration = duration_entry.get()

                if modifica_utilizator_in_csv(self.fisier_csv, id_de_modificat, nume, prenume, email, icao24, departure_country, over_country, duration):
                    messagebox.showinfo("Succes", "Utilizator modificat cu succes!")
                else:
                    messagebox.showinfo("Eroare", "ID-ul utilizatorului nu a fost găsit.")
                self.show_main_menu()

            tk.Button(self.root, text="Modifică Utilizator", command=submit).pack(pady=10)
            tk.Button(self.root, text="Înapoi", command=self.show_main_menu).pack(pady=10)

    def delete_user(self):
        """Șterge un utilizator."""
        self.clear_frame()

        tk.Label(self.root, text="Introduceți ID-ul utilizatorului de șters:").pack()
        id_entry = tk.Entry(self.root)
        id_entry.pack()

        def submit_delete_user():
            id_de_sters = id_entry.get()

            if sterge_utilizator_din_csv(self.fisier_csv, id_de_sters):
                messagebox.showinfo("Succes", "Utilizator șters cu succes!")
            else:
                messagebox.showinfo("Eroare", "ID-ul utilizatorului nu a fost găsit.")
            self.show_main_menu()

        tk.Button(self.root, text="Șterge Utilizator", command=submit_delete_user).pack(pady=10)
        tk.Button(self.root, text="Înapoi", command=self.show_main_menu).pack(pady=10)

    def get_flight_info(self):
        """Obține informații despre zbor pe baza ICAO24."""
        self.clear_frame()

        tk.Label(self.root, text="Introduceți ICAO24:").pack()
        icao24_entry = tk.Entry(self.root)
        icao24_entry.pack()

        def submit_flight():
            icao24 = icao24_entry.get()
            flight_data = get_flight_data(icao24)
            if flight_data:
                messagebox.showinfo("Informații Zbor", f"Apel avion: {flight_data['callsign']}\n"
                                                      f"Țara de plecare: {flight_data['origin_country']}\n"
                                                      f"Viteza: {flight_data['velocity']} km/h\n"
                                                      f"Altitudine: {flight_data['altitude']} metri\n"
                                                      f"Țara deasupra căreia zboară: {flight_data['over_country']}")
            else:
                messagebox.showinfo("Eroare", "Nu s-au găsit date pentru acest zbor.")

            self.show_main_menu()

        tk.Button(self.root, text="Obține informații Zbor", command=submit_flight).pack(pady=10)
        tk.Button(self.root, text="Înapoi", command=self.show_main_menu).pack(pady=10)

# Crearea aplicației
if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root, "utilizatori.csv")
    root.mainloop()
