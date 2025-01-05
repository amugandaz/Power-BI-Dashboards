import csv

# Données complètes pour les 30 équipes de la MLB
mlb_teams_data = [
    {"name": "Atlanta Braves", "city": "Atlanta", "state": "Georgia", "foundation_year": 1871, "world_series_titles": 4, "logo": "https://upload.wikimedia.org/wikipedia/en/f/f2/Atlanta_Braves.svg"},
    {"name": "Baltimore Orioles", "city": "Baltimore", "state": "Maryland", "foundation_year": 1901, "world_series_titles": 3, "logo": "https://upload.wikimedia.org/wikipedia/en/b/bc/Baltimore_Orioles_cap.svg"},
    {"name": "Boston Red Sox", "city": "Boston", "state": "Massachusetts", "foundation_year": 1901, "world_series_titles": 9, "logo": "https://upload.wikimedia.org/wikipedia/en/6/6d/Boston_Red_Sox_cap_logo.svg"},
    {"name": "Chicago Cubs", "city": "Chicago", "state": "Illinois", "foundation_year": 1870, "world_series_titles": 3, "logo": "https://upload.wikimedia.org/wikipedia/commons/8/80/Chicago_Cubs_logo.svg"},
    {"name": "Chicago White Sox", "city": "Chicago", "state": "Illinois", "foundation_year": 1900, "world_series_titles": 3, "logo": "https://upload.wikimedia.org/wikipedia/commons/c/c1/Chicago_White_Sox.svg"},
    {"name": "Cincinnati Reds", "city": "Cincinnati", "state": "Ohio", "foundation_year": 1881, "world_series_titles": 5, "logo": "https://upload.wikimedia.org/wikipedia/en/0/01/Cincinnati_Reds_Logo.svg"},
    {"name": "Cleveland Guardians", "city": "Cleveland", "state": "Ohio", "foundation_year": 1894, "world_series_titles": 2, "logo": "https://upload.wikimedia.org/wikipedia/en/0/0b/Cleveland_Guardians_logo.svg"},
    {"name": "Colorado Rockies", "city": "Denver", "state": "Colorado", "foundation_year": 1993, "world_series_titles": 0, "logo": "https://upload.wikimedia.org/wikipedia/en/6/67/Colorado_Rockies_logo.svg"},
    {"name": "Detroit Tigers", "city": "Detroit", "state": "Michigan", "foundation_year": 1894, "world_series_titles": 4, "logo": "https://upload.wikimedia.org/wikipedia/en/9/9b/Detroit_Tigers_logo.svg"},
    {"name": "Houston Astros", "city": "Houston", "state": "Texas", "foundation_year": 1962, "world_series_titles": 2, "logo": "https://upload.wikimedia.org/wikipedia/en/6/6b/Houston_Astros.svg"},
    {"name": "Kansas City Royals", "city": "Kansas City", "state": "Missouri", "foundation_year": 1969, "world_series_titles": 2, "logo": "https://upload.wikimedia.org/wikipedia/en/1/1b/Kansas_City_Royals.svg"},
    {"name": "Los Angeles Angels", "city": "Anaheim", "state": "California", "foundation_year": 1961, "world_series_titles": 1, "logo": "https://upload.wikimedia.org/wikipedia/en/c/c1/Los_Angeles_Angels_logo.svg"},
    {"name": "Los Angeles Dodgers", "city": "Los Angeles", "state": "California", "foundation_year": 1883, "world_series_titles": 7, "logo": "https://upload.wikimedia.org/wikipedia/en/5/55/Los_Angeles_Dodgers_Logo.svg"},
    {"name": "Miami Marlins", "city": "Miami", "state": "Florida", "foundation_year": 1993, "world_series_titles": 2, "logo": "https://upload.wikimedia.org/wikipedia/en/f/fd/Miami_Marlins_logo.svg"},
    {"name": "Milwaukee Brewers", "city": "Milwaukee", "state": "Wisconsin", "foundation_year": 1969, "world_series_titles": 0, "logo": "https://upload.wikimedia.org/wikipedia/en/b/b8/Milwaukee_Brewers_logo.svg"},
    {"name": "Minnesota Twins", "city": "Minneapolis", "state": "Minnesota", "foundation_year": 1901, "world_series_titles": 3, "logo": "https://upload.wikimedia.org/wikipedia/en/b/b4/Minnesota_Twins_logo.svg"},
    {"name": "New York Mets", "city": "New York City", "state": "New York", "foundation_year": 1962, "world_series_titles": 2, "logo": "https://upload.wikimedia.org/wikipedia/en/7/7b/New_York_Mets.svg"},
    {"name": "New York Yankees", "city": "New York City", "state": "New York", "foundation_year": 1901, "world_series_titles": 27, "logo": "https://upload.wikimedia.org/wikipedia/en/2/25/New_York_Yankees_logo.svg"},
    {"name": "Oakland Athletics", "city": "Oakland", "state": "California", "foundation_year": 1901, "world_series_titles": 9, "logo": "https://upload.wikimedia.org/wikipedia/en/6/63/Oakland_A%27s_logo.svg"},
    {"name": "Philadelphia Phillies", "city": "Philadelphia", "state": "Pennsylvania", "foundation_year": 1883, "world_series_titles": 2, "logo": "https://upload.wikimedia.org/wikipedia/en/f/f0/Philadelphia_Phillies_logo.svg"},
    {"name": "Pittsburgh Pirates", "city": "Pittsburgh", "state": "Pennsylvania", "foundation_year": 1882, "world_series_titles": 5, "logo": "https://upload.wikimedia.org/wikipedia/en/1/19/Pittsburgh_Pirates_logo_2014.svg"},
    {"name": "San Diego Padres", "city": "San Diego", "state": "California", "foundation_year": 1969, "world_series_titles": 0, "logo": "https://upload.wikimedia.org/wikipedia/en/8/8d/San_Diego_Padres_logo.svg"},
    {"name": "San Francisco Giants", "city": "San Francisco", "state": "California", "foundation_year": 1883, "world_series_titles": 8, "logo": "https://upload.wikimedia.org/wikipedia/en/5/58/San_Francisco_Giants_Logo.svg"},
    {"name": "Seattle Mariners", "city": "Seattle", "state": "Washington", "foundation_year": 1977, "world_series_titles": 0, "logo": "https://upload.wikimedia.org/wikipedia/en/0/0f/Seattle_Mariners_Insignia.svg"},
    {"name": "St. Louis Cardinals", "city": "St. Louis", "state": "Missouri", "foundation_year": 1882, "world_series_titles": 11, "logo": "https://upload.wikimedia.org/wikipedia/en/6/6d/St._Louis_Cardinals_logo.svg"},
    {"name": "Tampa Bay Rays", "city": "St. Petersburg", "state": "Florida", "foundation_year": 1998, "world_series_titles": 0, "logo": "https://upload.wikimedia.org/wikipedia/en/0/0c/Tampa_Bay_Rays.svg"},
    {"name": "Texas Rangers", "city": "Arlington", "state": "Texas", "foundation_year": 1961, "world_series_titles": 0, "logo": "https://upload.wikimedia.org/wikipedia/en/4/41/Texas_Rangers_logo.svg"},
    {"name": "Toronto Blue Jays", "city": "Toronto", "state": "Ontario", "foundation_year": 1977, "world_series_titles": 2, "logo": "https://upload.wikimedia.org/wikipedia/en/b/ba/Toronto_Blue_Jays_logo.svg"},
    {"name": "Washington Nationals", "city": "Washington, D.C.", "state": "District of Columbia", "foundation_year": 1969, "world_series_titles": 1, "logo": "https://upload.wikimedia.org/wikipedia/en/e/e3/Washington_Nationals_logo.svg"}
]

# Écrire les données dans un fichier CSV
with open('MLB_Teams.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    headers = ["Nom de l'équipe", "Ville", "État", "Année de création", "Titres World Series", "Logo (URL)"]
    writer.writerow(headers)
    for team in mlb_teams_data:
        writer.writerow([team["name"], team["city"], team["state"], team["foundation_year"], team["world_series_titles"], team["logo"]])

print("Fichier CSV 'MLB_Teams.csv' généré avec succès.")
