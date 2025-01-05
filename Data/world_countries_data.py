import http.client
import json
import csv
import time

# URL de l'API REST Countries
host = "restcountries.com"
endpoint = "/v3.1/all"

# Fonction pour récupérer les données avec plusieurs tentatives
def fetch_data_with_retry(host, endpoint, retries=3, delay=2):
    for attempt in range(retries):
        try:
            conn = http.client.HTTPSConnection(host, timeout=10)
            conn.request("GET", endpoint)
            response = conn.getresponse()

            if response.status != 200:
                raise Exception(f"Erreur HTTP: {response.status} {response.reason}")

            # Lire les données en morceaux
            chunks = []
            while True:
                chunk = response.read(4096)  # Lire par blocs de 4 Ko
                if not chunk:
                    break
                chunks.append(chunk)

            conn.close()
            # Décoder les données avec gestion des erreurs
            return b"".join(chunks).decode("utf-8", errors="replace")
        except Exception as e:
            print(f"Tentative {attempt + 1}/{retries} échouée : {e}")
            time.sleep(delay)  # Attendre avant une nouvelle tentative

    raise Exception("Échec de la récupération des données après plusieurs tentatives.")

# Récupérer les données des pays
try:
    data = fetch_data_with_retry(host, endpoint)
    # Sauvegarder les données brutes dans un fichier pour vérification
    with open('raw_data.json', 'w', encoding='utf-8') as raw_file:
        raw_file.write(data)
    # Charger les données JSON
    countries_data = json.loads(data)
except json.JSONDecodeError as e:
    print(f"Erreur lors de l'analyse JSON : {e}")
    print("Les données brutes ont été sauvegardées dans 'raw_data.json' pour diagnostic.")
    exit()
except Exception as e:
    print(f"Erreur irrécupérable : {e}")
    exit()

# Créer un fichier CSV pour écrire les données
with open('World_Countries.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    # Ajouter les en-têtes de colonnes
    headers = [
        "Pays", "Continent", "Capitale", "Superficie (km²)", "Nombres de villes", 
        "Monnaie", "Code téléphonique", "Climat", "Langues officielles", 
        "Date d'indépendance ou fête nationale", "Drapeau (URL)"
    ]
    writer.writerow(headers)

    # Remplir les données des pays
    for country in countries_data:
        # Récupérer les informations nécessaires
        name = country.get("name", {}).get("common", "N/A")
        continent = ", ".join(country.get("continents", [])) if country.get("continents") else "N/A"
        capital = ", ".join(country.get("capital", [])) if country.get("capital") else "N/A"
        area = country.get("area", "N/A")
        number_of_cities = "N/A"  # Note : Non disponible dans l'API REST Countries
        currencies = ", ".join([currency.get("name", "N/A") for currency in country.get("currencies", {}).values()]) if country.get("currencies") else "N/A"
        calling_code = country.get("idd", {}).get("root", "") + (country.get("idd", {}).get("suffixes", [""])[0]) if country.get("idd") else "N/A"
        climate = "N/A"  # Climat non disponible dans cette API
        languages = ", ".join(country.get("languages", {}).values()) if country.get("languages") else "N/A"
        independence_day = country.get("independence", "N/A") or country.get("startOfWeek", "N/A")
        flag = country.get("flags", {}).get("png", "N/A")

        # Écrire les données dans le fichier CSV
        writer.writerow([
            name, continent, capital, area, number_of_cities, 
            currencies, calling_code, climate, languages, 
            independence_day, flag
        ])

print("Fichier CSV 'World_Countries.csv' généré avec succès.")
