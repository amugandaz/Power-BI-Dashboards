import csv

# Données complètes pour les 32 équipes de la NHL
nhl_teams_data = [
    {"name": "Anaheim Ducks", "city": "Anaheim", "state": "California", "foundation_year": 1993, "stanley_cup_titles": 1, "logo": "https://upload.wikimedia.org/wikipedia/en/1/15/Anaheim_Ducks_logo.svg"},
    {"name": "Arizona Coyotes", "city": "Glendale", "state": "Arizona", "foundation_year": 1972, "stanley_cup_titles": 0, "logo": "https://upload.wikimedia.org/wikipedia/en/2/27/Arizona_Coyotes_logo.svg"},
    {"name": "Boston Bruins", "city": "Boston", "state": "Massachusetts", "foundation_year": 1924, "stanley_cup_titles": 6, "logo": "https://upload.wikimedia.org/wikipedia/en/4/42/Boston_Bruins.svg"},
    {"name": "Buffalo Sabres", "city": "Buffalo", "state": "New York", "foundation_year": 1970, "stanley_cup_titles": 0, "logo": "https://upload.wikimedia.org/wikipedia/en/9/99/Buffalo_Sabres_Logo.svg"},
    {"name": "Calgary Flames", "city": "Calgary", "state": "Alberta", "foundation_year": 1972, "stanley_cup_titles": 1, "logo": "https://upload.wikimedia.org/wikipedia/en/6/60/Calgary_Flames_logo.svg"},
    {"name": "Carolina Hurricanes", "city": "Raleigh", "state": "North Carolina", "foundation_year": 1972, "stanley_cup_titles": 1, "logo": "https://upload.wikimedia.org/wikipedia/en/3/32/Carolina_Hurricanes_logo.svg"},
    {"name": "Chicago Blackhawks", "city": "Chicago", "state": "Illinois", "foundation_year": 1926, "stanley_cup_titles": 6, "logo": "https://upload.wikimedia.org/wikipedia/en/8/89/Chicago_Blackhawks_logo.svg"},
    {"name": "Colorado Avalanche", "city": "Denver", "state": "Colorado", "foundation_year": 1972, "stanley_cup_titles": 3, "logo": "https://upload.wikimedia.org/wikipedia/en/4/45/Colorado_Avalanche_logo.svg"},
    {"name": "Columbus Blue Jackets", "city": "Columbus", "state": "Ohio", "foundation_year": 2000, "stanley_cup_titles": 0, "logo": "https://upload.wikimedia.org/wikipedia/en/4/4f/Columbus_Blue_Jackets_logo.svg"},
    {"name": "Dallas Stars", "city": "Dallas", "state": "Texas", "foundation_year": 1967, "stanley_cup_titles": 1, "logo": "https://upload.wikimedia.org/wikipedia/en/a/a1/Dallas_Stars_logo.svg"},
    {"name": "Detroit Red Wings", "city": "Detroit", "state": "Michigan", "foundation_year": 1926, "stanley_cup_titles": 11, "logo": "https://upload.wikimedia.org/wikipedia/en/e/e0/Detroit_Red_Wings_logo.svg"},
    {"name": "Edmonton Oilers", "city": "Edmonton", "state": "Alberta", "foundation_year": 1972, "stanley_cup_titles": 5, "logo": "https://upload.wikimedia.org/wikipedia/en/4/4e/Edmonton_Oilers_logo.svg"},
    {"name": "Florida Panthers", "city": "Sunrise", "state": "Florida", "foundation_year": 1993, "stanley_cup_titles": 0, "logo": "https://upload.wikimedia.org/wikipedia/en/8/87/Florida_Panthers_2016_logo.svg"},
    {"name": "Los Angeles Kings", "city": "Los Angeles", "state": "California", "foundation_year": 1967, "stanley_cup_titles": 2, "logo": "https://upload.wikimedia.org/wikipedia/en/c/c1/Los_Angeles_Kings_logo.svg"},
    {"name": "Minnesota Wild", "city": "Saint Paul", "state": "Minnesota", "foundation_year": 2000, "stanley_cup_titles": 0, "logo": "https://upload.wikimedia.org/wikipedia/en/a/aa/Minnesota_Wild_logo.svg"},
    {"name": "Montreal Canadiens", "city": "Montreal", "state": "Quebec", "foundation_year": 1909, "stanley_cup_titles": 24, "logo": "https://upload.wikimedia.org/wikipedia/en/6/69/Montreal_Canadiens.svg"},
    {"name": "Nashville Predators", "city": "Nashville", "state": "Tennessee", "foundation_year": 1998, "stanley_cup_titles": 0, "logo": "https://upload.wikimedia.org/wikipedia/en/9/9e/Nashville_Predators_Logo_2011.svg"},
    {"name": "New Jersey Devils", "city": "Newark", "state": "New Jersey", "foundation_year": 1974, "stanley_cup_titles": 3, "logo": "https://upload.wikimedia.org/wikipedia/en/9/9f/New_Jersey_Devils_logo.svg"},
    {"name": "New York Islanders", "city": "Uniondale", "state": "New York", "foundation_year": 1972, "stanley_cup_titles": 4, "logo": "https://upload.wikimedia.org/wikipedia/en/4/42/New_York_Islanders_logo.svg"},
    {"name": "New York Rangers", "city": "New York City", "state": "New York", "foundation_year": 1926, "stanley_cup_titles": 4, "logo": "https://upload.wikimedia.org/wikipedia/en/3/3a/New_York_Rangers.svg"},
    {"name": "Ottawa Senators", "city": "Ottawa", "state": "Ontario", "foundation_year": 1992, "stanley_cup_titles": 0, "logo": "https://upload.wikimedia.org/wikipedia/en/d/d4/Ottawa_Senators.svg"},
    {"name": "Philadelphia Flyers", "city": "Philadelphia", "state": "Pennsylvania", "foundation_year": 1967, "stanley_cup_titles": 2, "logo": "https://upload.wikimedia.org/wikipedia/en/d/dc/Philadelphia_Flyers.svg"},
    {"name": "Pittsburgh Penguins", "city": "Pittsburgh", "state": "Pennsylvania", "foundation_year": 1967, "stanley_cup_titles": 5, "logo": "https://upload.wikimedia.org/wikipedia/en/3/3a/Pittsburgh_Penguins_logo.svg"},
    {"name": "San Jose Sharks", "city": "San Jose", "state": "California", "foundation_year": 1991, "stanley_cup_titles": 0, "logo": "https://upload.wikimedia.org/wikipedia/en/3/37/SanJoseSharksLogo.svg"},
    {"name": "Seattle Kraken", "city": "Seattle", "state": "Washington", "foundation_year": 2021, "stanley_cup_titles": 0, "logo": "https://upload.wikimedia.org/wikipedia/en/6/67/Seattle_Kraken_logo.svg"},
    {"name": "St. Louis Blues", "city": "St. Louis", "state": "Missouri", "foundation_year": 1967, "stanley_cup_titles": 1, "logo": "https://upload.wikimedia.org/wikipedia/en/e/e3/St_Louis_Blues_logo.svg"},
    {"name": "Tampa Bay Lightning", "city": "Tampa", "state": "Florida", "foundation_year": 1992, "stanley_cup_titles": 3, "logo": "https://upload.wikimedia.org/wikipedia/en/3/3d/Tampa_Bay_Lightning_logo.svg"},
    {"name": "Toronto Maple Leafs", "city": "Toronto", "state": "Ontario", "foundation_year": 1917, "stanley_cup_titles": 13, "logo": "https://upload.wikimedia.org/wikipedia/en/d/d1/Toronto_Maple_Leafs_logo.svg"},
    {"name": "Vancouver Canucks", "city": "Vancouver", "state": "British Columbia", "foundation_year": 1970, "stanley_cup_titles": 0, "logo": "https://upload.wikimedia.org/wikipedia/en/3/3a/Vancouver_Canucks_logo.svg"},
    {"name": "Vegas Golden Knights", "city": "Paradise", "state": "Nevada", "foundation_year": 2017, "stanley_cup_titles": 1, "logo": "https://upload.wikimedia.org/wikipedia/en/a/ac/Vegas_Golden_Knights_logo.svg"},
    {"name": "Washington Capitals", "city": "Washington, D.C.", "state": "District of Columbia", "foundation_year": 1974, "stanley_cup_titles": 1, "logo": "https://upload.wikimedia.org/wikipedia/en/5/5d/Washington_Capitals.svg"},
    {"name": "Winnipeg Jets", "city": "Winnipeg", "state": "Manitoba", "foundation_year": 1999, "stanley_cup_titles": 0, "logo": "https://upload.wikimedia.org/wikipedia/en/f/fb/Winnipeg_Jets_logo.svg"}
]

# Écrire les données dans un fichier CSV
with open('NHL_Teams.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    headers = ["Nom de l'équipe", "Ville", "État", "Année de création", "Titres Stanley Cup", "Logo (URL)"]
    writer.writerow(headers)
    for team in nhl_teams_data:
        writer.writerow([team["name"], team["city"], team["state"], team["foundation_year"], team["stanley_cup_titles"], team["logo"]])

print("Fichier CSV 'NHL_Teams.csv' généré avec succès.")
