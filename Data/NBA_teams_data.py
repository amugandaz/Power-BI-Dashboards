import csv

# Données complètes pour les 30 équipes de la NBA
nba_teams_data = [
    {
        "name": "Atlanta Hawks",
        "city": "Atlanta",
        "state": "Georgia",
        "foundation_year": 1946,
        "nba_titles": 1,
        "logo": "https://upload.wikimedia.org/wikipedia/en/2/24/Atlanta_Hawks_logo.svg"
    },
    {
        "name": "Boston Celtics",
        "city": "Boston",
        "state": "Massachusetts",
        "foundation_year": 1946,
        "nba_titles": 17,
        "logo": "https://upload.wikimedia.org/wikipedia/en/8/8f/Boston_Celtics.svg"
    },
    {
        "name": "Brooklyn Nets",
        "city": "Brooklyn",
        "state": "New York",
        "foundation_year": 1967,
        "nba_titles": 0,
        "logo": "https://upload.wikimedia.org/wikipedia/en/4/44/Brooklyn_Nets_newlogo.svg"
    },
    {
        "name": "Charlotte Hornets",
        "city": "Charlotte",
        "state": "North Carolina",
        "foundation_year": 1988,
        "nba_titles": 0,
        "logo": "https://upload.wikimedia.org/wikipedia/en/c/c4/Charlotte_Hornets_%282014%29.svg"
    },
    {
        "name": "Chicago Bulls",
        "city": "Chicago",
        "state": "Illinois",
        "foundation_year": 1966,
        "nba_titles": 6,
        "logo": "https://upload.wikimedia.org/wikipedia/en/6/67/Chicago_Bulls_logo.svg"
    },
    {
        "name": "Cleveland Cavaliers",
        "city": "Cleveland",
        "state": "Ohio",
        "foundation_year": 1970,
        "nba_titles": 1,
        "logo": "https://upload.wikimedia.org/wikipedia/en/f/f7/Cleveland_Cavaliers_logo.svg"
    },
    {
        "name": "Dallas Mavericks",
        "city": "Dallas",
        "state": "Texas",
        "foundation_year": 1980,
        "nba_titles": 1,
        "logo": "https://upload.wikimedia.org/wikipedia/en/9/97/Dallas_Mavericks_logo.svg"
    },
    {
        "name": "Denver Nuggets",
        "city": "Denver",
        "state": "Colorado",
        "foundation_year": 1967,
        "nba_titles": 1,
        "logo": "https://upload.wikimedia.org/wikipedia/en/7/76/Denver_Nuggets.svg"
    },
    {
        "name": "Detroit Pistons",
        "city": "Detroit",
        "state": "Michigan",
        "foundation_year": 1941,
        "nba_titles": 3,
        "logo": "https://upload.wikimedia.org/wikipedia/en/1/1e/Detroit_Pistons_logo.svg"
    },
    {
        "name": "Golden State Warriors",
        "city": "San Francisco",
        "state": "California",
        "foundation_year": 1946,
        "nba_titles": 7,
        "logo": "https://upload.wikimedia.org/wikipedia/en/0/01/Golden_State_Warriors_logo.svg"
    },
    {
        "name": "Houston Rockets",
        "city": "Houston",
        "state": "Texas",
        "foundation_year": 1967,
        "nba_titles": 2,
        "logo": "https://upload.wikimedia.org/wikipedia/en/2/28/Houston_Rockets.svg"
    },
    {
        "name": "Indiana Pacers",
        "city": "Indianapolis",
        "state": "Indiana",
        "foundation_year": 1967,
        "nba_titles": 0,
        "logo": "https://upload.wikimedia.org/wikipedia/en/1/1b/Indiana_Pacers.svg"
    },
    {
        "name": "Los Angeles Clippers",
        "city": "Los Angeles",
        "state": "California",
        "foundation_year": 1970,
        "nba_titles": 0,
        "logo": "https://upload.wikimedia.org/wikipedia/en/b/bb/Los_Angeles_Clippers_%282015%29.svg"
    },
    {
        "name": "Los Angeles Lakers",
        "city": "Los Angeles",
        "state": "California",
        "foundation_year": 1947,
        "nba_titles": 17,
        "logo": "https://upload.wikimedia.org/wikipedia/commons/3/3c/Los_Angeles_Lakers_logo.svg"
    },
    {
        "name": "Memphis Grizzlies",
        "city": "Memphis",
        "state": "Tennessee",
        "foundation_year": 1995,
        "nba_titles": 0,
        "logo": "https://upload.wikimedia.org/wikipedia/en/f/f1/Memphis_Grizzlies.svg"
    },
    {
        "name": "Miami Heat",
        "city": "Miami",
        "state": "Florida",
        "foundation_year": 1988,
        "nba_titles": 3,
        "logo": "https://upload.wikimedia.org/wikipedia/en/f/fb/Miami_Heat_logo.svg"
    },
    {
        "name": "Milwaukee Bucks",
        "city": "Milwaukee",
        "state": "Wisconsin",
        "foundation_year": 1968,
        "nba_titles": 2,
        "logo": "https://upload.wikimedia.org/wikipedia/en/4/4a/Milwaukee_Bucks_logo.svg"
    },
    {
        "name": "Minnesota Timberwolves",
        "city": "Minneapolis",
        "state": "Minnesota",
        "foundation_year": 1989,
        "nba_titles": 0,
        "logo": "https://upload.wikimedia.org/wikipedia/en/c/c2/Minnesota_Timberwolves_logo.svg"
    },
    {
        "name": "New Orleans Pelicans",
        "city": "New Orleans",
        "state": "Louisiana",
        "foundation_year": 2002,
        "nba_titles": 0,
        "logo": "https://upload.wikimedia.org/wikipedia/en/0/0d/New_Orleans_Pelicans_logo.svg"
    },
    {
        "name": "New York Knicks",
        "city": "New York City",
        "state": "New York",
        "foundation_year": 1946,
        "nba_titles": 2,
        "logo": "https://upload.wikimedia.org/wikipedia/en/2/25/New_York_Knicks_logo.svg"
    },
    {
        "name": "Oklahoma City Thunder",
        "city": "Oklahoma City",
        "state": "Oklahoma",
        "foundation_year": 1967,
        "nba_titles": 1,
        "logo": "https://upload.wikimedia.org/wikipedia/en/5/5d/Oklahoma_City_Thunder.svg"
    },
    {
        "name": "Orlando Magic",
        "city": "Orlando",
        "state": "Florida",
        "foundation_year": 1989,
        "nba_titles": 0,
        "logo": "https://upload.wikimedia.org/wikipedia/en/1/10/Orlando_Magic_logo.svg"
    },
    {
        "name": "Philadelphia 76ers",
        "city": "Philadelphia",
        "state": "Pennsylvania",
        "foundation_year": 1946,
        "nba_titles": 3,
        "logo": "https://upload.wikimedia.org/wikipedia/en/0/0e/Philadelphia_76ers_logo.svg"
    },
    {
        "name": "Phoenix Suns",
        "city": "Phoenix",
        "state": "Arizona",
        "foundation_year": 1968,
        "nba_titles": 0,
        "logo": "https://upload.wikimedia.org/wikipedia/en/d/dc/Phoenix_Suns_logo.svg"
    },
    {
        "name": "Portland Trail Blazers",
        "city": "Portland",
        "state": "Oregon",
        "foundation_year": 1970,
        "nba_titles": 1,
        "logo": "https://upload.wikimedia.org/wikipedia/en/2/21/Portland_Trail_Blazers_logo.svg"
    },
    {
        "name": "Sacramento Kings",
        "city": "Sacramento",
        "state": "California",
        "foundation_year": 1948,
        "nba_titles": 1,
        "logo": "https://upload.wikimedia.org/wikipedia/en/c/c7/SacramentoKings.svg"
    },
    {
        "name": "San Antonio Spurs",
        "city": "San Antonio",
        "state": "Texas",
        "foundation_year": 1967,
        "nba_titles": 5,
        "logo": "https://upload.wikimedia.org/wikipedia/en/a/a2/San_Antonio_Spurs.svg"
    },
    {
        "name": "Toronto Raptors",
        "city": "Toronto",
        "state": "Ontario",
        "foundation_year": 1995,
        "nba_titles": 1,
        "logo": "https://upload.wikimedia.org/wikipedia/en/3/36/Toronto_Raptors_logo.svg"
    },
    {
        "name": "Utah Jazz",
        "city": "Salt Lake City",
        "state": "Utah",
        "foundation_year": 1974,
        "nba_titles": 0,
        "logo": "https://upload.wikimedia.org/wikipedia/en/0/04/Utah_Jazz_logo_%282016%29.svg"
    },
    {
        "name": "Washington Wizards",
        "city": "Washington, D.C.",
        "state": "District of Columbia",
        "foundation_year": 1961,
        "nba_titles": 1,
        "logo": "https://upload.wikimedia.org/wikipedia/en/0/02/Washington_Wizards_logo.svg"
    }
]

# Écrire les données dans un fichier CSV
with open('NBA_Teams.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    # En-têtes
    headers = [
        "Nom de l'équipe", "Ville", "État", "Année de création", "Titres NBA", "Logo (URL)"
    ]
    writer.writerow(headers)

    # Données des équipes
    for team in nba_teams_data:
        writer.writerow([
            team["name"],
            team["city"],
            team["state"],
            team["foundation_year"],
            team["nba_titles"],
            team["logo"]
        ])

print("Fichier CSV 'NBA_Teams.csv' généré avec succès.")
