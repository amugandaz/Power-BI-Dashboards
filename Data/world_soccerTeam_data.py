import csv

# Données complètes pour 40 équipes de football européennes célèbres
teams_data = [
    {
        "name": "Manchester United",
        "country": "Angleterre",
        "city": "Manchester",
        "league": "Premier League",
        "foundation_year": 1878,
        "major_titles": 66,
        "logo": "https://upload.wikimedia.org/wikipedia/en/7/7a/Manchester_United_FC_crest.svg"
    },
    {
        "name": "Real Madrid",
        "country": "Espagne",
        "city": "Madrid",
        "league": "La Liga",
        "foundation_year": 1902,
        "major_titles": 97,
        "logo": "https://upload.wikimedia.org/wikipedia/en/5/56/Real_Madrid_CF.svg"
    },
    {
        "name": "Bayern Munich",
        "country": "Allemagne",
        "city": "Munich",
        "league": "Bundesliga",
        "foundation_year": 1900,
        "major_titles": 81,
        "logo": "https://upload.wikimedia.org/wikipedia/commons/1/1f/FC_Bayern_München_logo_(2021).svg"
    },
    {
        "name": "Paris Saint-Germain",
        "country": "France",
        "city": "Paris",
        "league": "Ligue 1",
        "foundation_year": 1970,
        "major_titles": 43,
        "logo": "https://upload.wikimedia.org/wikipedia/en/a/a7/Paris_Saint-Germain_F.C..svg"
    },
    {
        "name": "Juventus",
        "country": "Italie",
        "city": "Turin",
        "league": "Serie A",
        "foundation_year": 1897,
        "major_titles": 70,
        "logo": "https://upload.wikimedia.org/wikipedia/en/d/d2/Juventus_Turin.svg"
    },
    {
        "name": "Barcelona",
        "country": "Espagne",
        "city": "Barcelone",
        "league": "La Liga",
        "foundation_year": 1899,
        "major_titles": 95,
        "logo": "https://upload.wikimedia.org/wikipedia/en/4/47/FC_Barcelona_%28crest%29.svg"
    },
    {
        "name": "Chelsea",
        "country": "Angleterre",
        "city": "Londres",
        "league": "Premier League",
        "foundation_year": 1905,
        "major_titles": 32,
        "logo": "https://upload.wikimedia.org/wikipedia/en/c/cc/Chelsea_FC.svg"
    },
    {
        "name": "Liverpool",
        "country": "Angleterre",
        "city": "Liverpool",
        "league": "Premier League",
        "foundation_year": 1892,
        "major_titles": 68,
        "logo": "https://upload.wikimedia.org/wikipedia/en/0/0c/Liverpool_FC.svg"
    },
    {
        "name": "AC Milan",
        "country": "Italie",
        "city": "Milan",
        "league": "Serie A",
        "foundation_year": 1899,
        "major_titles": 58,
        "logo": "https://upload.wikimedia.org/wikipedia/commons/d/d0/Logo_of_AC_Milan.svg"
    },
    {
        "name": "Inter Milan",
        "country": "Italie",
        "city": "Milan",
        "league": "Serie A",
        "foundation_year": 1908,
        "major_titles": 40,
        "logo": "https://upload.wikimedia.org/wikipedia/en/3/3b/FC_Internazionale_Milano_2021.svg"
    },
    {
        "name": "Ajax Amsterdam",
        "country": "Pays-Bas",
        "city": "Amsterdam",
        "league": "Eredivisie",
        "foundation_year": 1900,
        "major_titles": 73,
        "logo": "https://upload.wikimedia.org/wikipedia/en/7/79/Ajax_Amsterdam.svg"
    },
    {
        "name": "Benfica",
        "country": "Portugal",
        "city": "Lisbonne",
        "league": "Primeira Liga",
        "foundation_year": 1904,
        "major_titles": 82,
        "logo": "https://upload.wikimedia.org/wikipedia/en/a/a2/SL_Benfica_logo.svg"
    },
    {
        "name": "Porto",
        "country": "Portugal",
        "city": "Porto",
        "league": "Primeira Liga",
        "foundation_year": 1893,
        "major_titles": 78,
        "logo": "https://upload.wikimedia.org/wikipedia/en/f/f1/FC_Porto.svg"
    },
    {
        "name": "Atletico Madrid",
        "country": "Espagne",
        "city": "Madrid",
        "league": "La Liga",
        "foundation_year": 1903,
        "major_titles": 32,
        "logo": "https://upload.wikimedia.org/wikipedia/en/c/c1/Atletico_Madrid_2017_logo.svg"
    },
    {
        "name": "Borussia Dortmund",
        "country": "Allemagne",
        "city": "Dortmund",
        "league": "Bundesliga",
        "foundation_year": 1909,
        "major_titles": 22,
        "logo": "https://upload.wikimedia.org/wikipedia/en/6/67/Borussia_Dortmund_logo.svg"
    },
    {
        "name": "Lyon",
        "country": "France",
        "city": "Lyon",
        "league": "Ligue 1",
        "foundation_year": 1950,
        "major_titles": 21,
        "logo": "https://upload.wikimedia.org/wikipedia/en/c/cd/Olympique_Lyonnais.svg"
    },
    {
        "name": "Marseille",
        "country": "France",
        "city": "Marseille",
        "league": "Ligue 1",
        "foundation_year": 1899,
        "major_titles": 25,
        "logo": "https://upload.wikimedia.org/wikipedia/en/8/86/Olympique_Marseille_logo.svg"
    },
    {
        "name": "Sevilla",
        "country": "Espagne",
        "city": "Séville",
        "league": "La Liga",
        "foundation_year": 1890,
        "major_titles": 25,
        "logo": "https://upload.wikimedia.org/wikipedia/en/3/3f/Sevilla_FC_logo.svg"
    },
    {
        "name": "Arsenal",
        "country": "Angleterre",
        "city": "Londres",
        "league": "Premier League",
        "foundation_year": 1886,
        "major_titles": 48,
        "logo": "https://upload.wikimedia.org/wikipedia/en/5/53/Arsenal_FC.svg"
    },
    {
        "name": "Tottenham Hotspur",
        "country": "Angleterre",
        "city": "Londres",
        "league": "Premier League",
        "foundation_year": 1882,
        "major_titles": 26,
        "logo": "https://upload.wikimedia.org/wikipedia/en/b/b4/Tottenham_Hotspur.svg"
    },
    {
        "name": "Napoli",
        "country": "Italie",
        "city": "Naples",
        "league": "Serie A",
        "foundation_year": 1926,
        "major_titles": 10,
        "logo": "https://upload.wikimedia.org/wikipedia/en/2/26/SSC_Napoli.svg"
    },
    {
        "name": "PSV Eindhoven",
        "country": "Pays-Bas",
        "city": "Eindhoven",
        "league": "Eredivisie",
        "foundation_year": 1913,
        "major_titles": 57,
        "logo": "https://upload.wikimedia.org/wikipedia/en/0/05/PSV_Eindhoven.svg"
    },
    {
        "name": "AS Roma",
        "country": "Italie",
        "city": "Rome",
        "league": "Serie A",
        "foundation_year": 1927,
        "major_titles": 15,
        "logo": "https://upload.wikimedia.org/wikipedia/en/f/f7/AS_Roma.svg"
    },
    {
        "name": "Lazio",
        "country": "Italie",
        "city": "Rome",
        "league": "Serie A",
        "foundation_year": 1900,
        "major_titles": 16,
        "logo": "https://upload.wikimedia.org/wikipedia/en/e/e3/SS_Lazio.svg"
    },
    {
        "name": "Feyenoord",
        "country": "Pays-Bas",
        "city": "Rotterdam",
        "league": "Eredivisie",
        "foundation_year": 1908,
        "major_titles": 39,
        "logo": "https://upload.wikimedia.org/wikipedia/en/2/20/Feyenoord_logo.svg"
    },
    {
        "name": "Sporting CP",
        "country": "Portugal",
        "city": "Lisbonne",
        "league": "Primeira Liga",
        "foundation_year": 1906,
        "major_titles": 52,
        "logo": "https://upload.wikimedia.org/wikipedia/en/3/3e/Sporting_CP_logo.svg"
    },
    {
        "name": "Rangers",
        "country": "Écosse",
        "city": "Glasgow",
        "league": "Scottish Premiership",
        "foundation_year": 1872,
        "major_titles": 120,
        "logo": "https://upload.wikimedia.org/wikipedia/en/a/a2/Rangers_FC.svg"
    },
    {
        "name": "Celtic",
        "country": "Écosse",
        "city": "Glasgow",
        "league": "Scottish Premiership",
        "foundation_year": 1887,
        "major_titles": 113,
        "logo": "https://upload.wikimedia.org/wikipedia/en/f/fd/Celtic_FC.svg"
    },
    {
        "name": "Shakhtar Donetsk",
        "country": "Ukraine",
        "city": "Donetsk",
        "league": "Premier League Ukrainienne",
        "foundation_year": 1936,
        "major_titles": 35,
        "logo": "https://upload.wikimedia.org/wikipedia/en/c/cb/Shakhtar_Donetsk.svg"
    },
    {
        "name": "Dynamo Kyiv",
        "country": "Ukraine",
        "city": "Kyiv",
        "league": "Premier League Ukrainienne",
        "foundation_year": 1927,
        "major_titles": 68,
        "logo": "https://upload.wikimedia.org/wikipedia/en/0/0a/FC_Dynamo_Kyiv.svg"
    },
    {
        "name": "Red Star Belgrade",
        "country": "Serbie",
        "city": "Belgrade",
        "league": "SuperLiga Serbe",
        "foundation_year": 1945,
        "major_titles": 56,
        "logo": "https://upload.wikimedia.org/wikipedia/en/6/6b/Red_Star_Belgrade.svg"
    },
    {
        "name": "Anderlecht",
        "country": "Belgique",
        "city": "Bruxelles",
        "league": "Pro League Belge",
        "foundation_year": 1908,
        "major_titles": 76,
        "logo": "https://upload.wikimedia.org/wikipedia/en/1/16/RSC_Anderlecht.svg"
    },
    {
        "name": "Club Brugge",
        "country": "Belgique",
        "city": "Bruges",
        "league": "Pro League Belge",
        "foundation_year": 1891,
        "major_titles": 60,
        "logo": "https://upload.wikimedia.org/wikipedia/en/1/12/Club_Brugge_KV_logo.svg"
    },
    {
        "name": "Olympiacos",
        "country": "Grèce",
        "city": "Le Pirée",
        "league": "Super League Grecque",
        "foundation_year": 1925,
        "major_titles": 79,
        "logo": "https://upload.wikimedia.org/wikipedia/en/7/7e/Olympiacos_FC_logo.svg"
    },
    {
        "name": "Galatasaray",
        "country": "Turquie",
        "city": "Istanbul",
        "league": "Super Lig Turque",
        "foundation_year": 1905,
        "major_titles": 61,
        "logo": "https://upload.wikimedia.org/wikipedia/en/2/2f/Galatasaray_Logo.svg"
    }
]

# Écrire les données dans un fichier CSV
with open('Football_Clubs_40.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    # En-têtes
    headers = [
        "Nom de l'équipe", "Pays", "Ville", "Championnat", 
        "Année de création", "Nombres de titres majeurs", "Logo (URL)"
    ]
    writer.writerow(headers)

    # Données des équipes
    for team in teams_data:
        writer.writerow([
            team["name"],
            team["country"],
            team["city"],
            team["league"],
            team["foundation_year"],
            team["major_titles"],
            team["logo"]
        ])

print("Fichier CSV 'Football_Clubs_40.csv' généré avec succès.")
