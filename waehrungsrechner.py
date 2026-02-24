import requests

def waehrungsrechner():
    print("--- Willkommen beim Echtzeit-Währungsrechner ---")
    
    # Basis-Währung 
    von_waehrung = input("Von (z.B. USD, EUR, AZN): ").upper()
    zu_waehrung = input("Nach (z.B. TRY, AZN, EUR): ").upper()
    betrag = float(input(f"Betrag in {von_waehrung}: "))

    # API-URL für Echtzeit-Kurse 
    url = f"https://api.exchangerate-api.com/v4/latest/{von_waehrung}"

    try:
        response = requests.get(url)
        data = response.json()
        
        # Wechselkurs extrahieren 
        kurs = data['rates'][zu_waehrung]
        ergebnis = betrag * kurs

        print(f"\nAktueller Kurs: 1 {von_waehrung} = {kurs:.2f} {zu_waehrung}")
        print(f"{betrag} {von_waehrung} sind {ergebnis:.2f} {zu_waehrung}")

    except Exception as e:
        print("Fehler: Währung nicht gefunden oder keine Internetverbindung.")

if __name__ == "__main__":
    waehrungsrechner()