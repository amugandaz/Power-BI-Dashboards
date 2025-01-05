import csv

# Données complètes pour les 32 équipes de la NFL
nfl_teams_data = [
    {"name": "Arizona Cardinals", "city": "Glendale", "state": "Arizona", "foundation_year": 1898, "super_bowl_titles": 0, "logo": "https://upload.wikimedia.org/wikipedia/en/7/72/Arizona_Cardinals_logo.svg"},
    {"name": "Atlanta Falcons", "city": "Atlanta", "state": "Georgia", "foundation_year": 1965, "super_bowl_titles": 0, "logo": "https://upload.wikimedia.org/wikipedia/en/c/c5/Atlanta_Falcons_logo.svg"},
    {"name": "Baltimore Ravens", "city": "Baltimore", "state": "Maryland", "foundation_year": 1996, "super_bowl_titles": 2, "logo": "https://upload.wikimedia.org/wikipedia/en/1/16/Baltimore_Ravens_logo.svg"},
    {"name": "Buffalo Bills", "city": "Buffalo", "state": "New York", "foundation_year": 1960, "super_bowl_titles": 0, "logo": "https://upload.wikimedia.org/wikipedia/en/7/77/Buffalo_Bills_logo.svg"},
    {"name": "Carolina Panthers", "city": "Charlotte", "state": "North Carolina", "foundation_year": 1993, "super_bowl_titles": 0, "logo": "https://upload.wikimedia.org/wikipedia/en/1/1c/Carolina_Panthers_logo.svg"},
    {"name": "Chicago Bears", "city": "Chicago", "state": "Illinois", "foundation_year": 1919, "super_bowl_titles": 1, "logo": "https://upload.wikimedia.org/wikipedia/commons/5/5c/Chicago_Bears_logo.svg"},
    {"name": "Cincinnati Bengals", "city": "Cincinnati", "state": "Ohio", "foundation_year": 1968, "super_bowl_titles": 0, "logo": "https://upload.wikimedia.org/wikipedia/en/8/81/Cincinnati_Bengals_logo.svg"},
    {"name": "Cleveland Browns", "city": "Cleveland", "state": "Ohio", "foundation_year": 1946, "super_bowl_titles": 0, "logo": "https://upload.wikimedia.org/wikipedia/en/d/d8/Cleveland_Browns_logo.svg"},
    {"name": "Dallas Cowboys", "city": "Arlington", "state": "Texas", "foundation_year": 1960, "super_bowl_titles": 5, "logo": "https://upload.wikimedia.org/wikipedia/commons/1/15/Dallas_Cowboys.svg"},
    {"name": "Denver Broncos", "city": "Denver", "state": "Colorado", "foundation_year": 1960, "super_bowl_titles": 3, "logo": "https://upload.wikimedia.org/wikipedia/en/4/44/Denver_Broncos_logo.svg"},
    {"name": "Detroit Lions", "city": "Detroit", "state": "Michigan", "foundation_year": 1930, "super_bowl_titles": 0, "logo": "https://upload.wikimedia.org/wikipedia/en/7/71/Detroit_Lions_logo.svg"},
    {"name": "Green Bay Packers", "city": "Green Bay", "state": "Wisconsin", "foundation_year": 1919, "super_bowl_titles": 4, "logo": "https://upload.wikimedia.org/wikipedia/commons/5/50/Green_Bay_Packers_logo.svg"},
    {"name": "Houston Texans", "city": "Houston", "state": "Texas", "foundation_year": 2002, "super_bowl_titles": 0, "logo": "https://upload.wikimedia.org/wikipedia/en/2/28/Houston_Texans_logo.svg"},
    {"name": "Indianapolis Colts", "city": "Indianapolis", "state": "Indiana", "foundation_year": 1953, "super_bowl_titles": 2, "logo": "https://upload.wikimedia.org/wikipedia/en/0/00/Indianapolis_Colts_logo.svg"},
    {"name": "Jacksonville Jaguars", "city": "Jacksonville", "state": "Florida", "foundation_year": 1993, "super_bowl_titles": 0, "logo": "https://upload.wikimedia.org/wikipedia/en/7/74/Jacksonville_Jaguars_logo.svg"},
    {"name": "Kansas City Chiefs", "city": "Kansas City", "state": "Missouri", "foundation_year": 1960, "super_bowl_titles": 3, "logo": "https://upload.wikimedia.org/wikipedia/en/e/e1/Kansas_City_Chiefs_logo.svg"},
    {"name": "Las Vegas Raiders", "city": "Las Vegas", "state": "Nevada", "foundation_year": 1960, "super_bowl_titles": 3, "logo": "https://upload.wikimedia.org/wikipedia/en/6/6a/Las_Vegas_Raiders_logo.svg"},
    {"name": "Los Angeles Chargers", "city": "Los Angeles", "state": "California", "foundation_year": 1960, "super_bowl_titles": 0, "logo": "https://upload.wikimedia.org/wikipedia/en/7/72/Los_Angeles_Chargers_logo.svg"},
    {"name": "Los Angeles Rams", "city": "Los Angeles", "state": "California", "foundation_year": 1936, "super_bowl_titles": 2, "logo": "https://upload.wikimedia.org/wikipedia/en/8/8e/Los_Angeles_Rams_logo.svg"},
    {"name": "Miami Dolphins", "city": "Miami Gardens", "state": "Florida", "foundation_year": 1966, "super_bowl_titles": 2, "logo": "https://upload.wikimedia.org/wikipedia/en/3/37/Miami_Dolphins_logo.svg"},
    {"name": "Minnesota Vikings", "city": "Minneapolis", "state": "Minnesota", "foundation_year": 1960, "super_bowl_titles": 0, "logo": "https://upload.wikimedia.org/wikipedia/en/4/48/Minnesota_Vikings_logo.svg"},
    {"name": "New England Patriots", "city": "Foxborough", "state": "Massachusetts", "foundation_year": 1960, "super_bowl_titles": 6, "logo": "https://upload.wikimedia.org/wikipedia/en/b/b9/New_England_Patriots_logo.svg"},
    {"name": "New Orleans Saints", "city": "New Orleans", "state": "Louisiana", "foundation_year": 1967, "super_bowl_titles": 1, "logo": "https://upload.wikimedia.org/wikipedia/commons/5/50/New_Orleans_Saints_logo.svg"},
    {"name": "New York Giants", "city": "East Rutherford", "state": "New Jersey", "foundation_year": 1925, "super_bowl_titles": 4, "logo": "https://upload.wikimedia.org/wikipedia/commons/6/60/New_York_Giants_logo.svg"},
    {"name": "New York Jets", "city": "East Rutherford", "state": "New Jersey", "foundation_year": 1960, "super_bowl_titles": 1, "logo": "https://upload.wikimedia.org/wikipedia/en/6/6d/New_York_Jets_logo.svg"},
    {"name": "Philadelphia Eagles", "city": "Philadelphia", "state": "Pennsylvania", "foundation_year": 1933, "super_bowl_titles": 1, "logo": "https://upload.wikimedia.org/wikipedia/en/8/8e/Philadelphia_Eagles_logo.svg"},
    {"name": "Pittsburgh Steelers", "city": "Pittsburgh", "state": "Pennsylvania", "foundation_year": 1933, "super_bowl_titles": 6, "logo": "https://upload.wikimedia.org/wikipedia/commons/d/de/Pittsburgh_Steelers_logo.svg"},
    {"name": "San Francisco 49ers", "city": "San Francisco", "state": "California", "foundation_year": 1946, "super_bowl_titles": 5, "logo": "https://upload.wikimedia.org/wikipedia/en/4/49/San_Francisco_49ers_logo.svg"},
    {"name": "Seattle Seahawks", "city": "Seattle", "state": "Washington", "foundation_year": 1976, "super_bowl_titles": 1, "logo": "https://upload.wikimedia.org/wikipedia/en/8/8e/Seattle_Seahawks_logo.svg"},
    {"name": "Tampa Bay Buccaneers", "city": "Tampa", "state": "Florida", "foundation_year": 1976, "super_bowl_titles": 2, "logo": "https://upload.wikimedia.org/wikipedia/en/a/a2/Tampa_Bay_Buccaneers_logo.svg"},
    {"name": "Tennessee Titans", "city": "Nashville", "state": "Tennessee", "foundation_year": 1960, "super_bowl_titles": 0, "logo": "https://upload.wikimedia.org/wikipedia/en/c/c1/Tennessee_Titans_logo.svg"},
    {"name": "Washington Commanders", "city": "Landover", "state": "Maryland", "foundation_year": 1932, "super_bowl_titles": 3, "logo": "https://upload.wikimedia.org/wikipedia/en/1/14/Washington_Commanders_logo.svg"}
]

# Écrire les données dans un fichier CSV
with open('NFL_Teams.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    headers = ["Nom de l'équipe", "Ville", "État", "Année de création", "Titres Super Bowl", "Logo (URL)"]
    writer.writerow(headers)
    for team in nfl_teams_data:
        writer.writerow([team["name"], team["city"], team["state"], team["foundation_year"], team["super_bowl_titles"], team["logo"]])

print("Fichier CSV 'NFL_Teams.csv' généré avec succès.")
