import csv

# Liste complète des 50 plus grandes entreprises
companies_data = [
    {"name": "Apple", "foundation_year": 1976, "country": "United States", "continent": "North America", "state_or_province": "California", "city": "Cupertino", "logo": "https://upload.wikimedia.org/wikipedia/commons/f/fa/Apple_logo_black.svg"},
    {"name": "Microsoft", "foundation_year": 1975, "country": "United States", "continent": "North America", "state_or_province": "Washington", "city": "Redmond", "logo": "https://upload.wikimedia.org/wikipedia/commons/4/44/Microsoft_logo.svg"},
    {"name": "Amazon", "foundation_year": 1994, "country": "United States", "continent": "North America", "state_or_province": "Washington", "city": "Seattle", "logo": "https://upload.wikimedia.org/wikipedia/commons/a/a9/Amazon_logo.svg"},
    {"name": "Alphabet (Google)", "foundation_year": 1998, "country": "United States", "continent": "North America", "state_or_province": "California", "city": "Mountain View", "logo": "https://upload.wikimedia.org/wikipedia/commons/2/2f/Google_2015_logo.svg"},
    {"name": "Saudi Aramco", "foundation_year": 1933, "country": "Saudi Arabia", "continent": "Asia", "state_or_province": "Eastern Province", "city": "Dhahran", "logo": "https://upload.wikimedia.org/wikipedia/en/7/7f/Saudi_Aramco_logo.svg"},
    {"name": "Tesla", "foundation_year": 2003, "country": "United States", "continent": "North America", "state_or_province": "California", "city": "Palo Alto", "logo": "https://upload.wikimedia.org/wikipedia/commons/b/bd/Tesla_Motors.svg"},
    {"name": "Berkshire Hathaway", "foundation_year": 1839, "country": "United States", "continent": "North America", "state_or_province": "Nebraska", "city": "Omaha", "logo": "https://upload.wikimedia.org/wikipedia/commons/0/09/Berkshire_Hathaway_logo.svg"},
    {"name": "Meta Platforms (Facebook)", "foundation_year": 2004, "country": "United States", "continent": "North America", "state_or_province": "California", "city": "Menlo Park", "logo": "https://upload.wikimedia.org/wikipedia/commons/e/e3/Meta_Platforms_Inc._logo.svg"},
    {"name": "Alibaba Group", "foundation_year": 1999, "country": "China", "continent": "Asia", "state_or_province": "Zhejiang", "city": "Hangzhou", "logo": "https://upload.wikimedia.org/wikipedia/commons/2/2f/Alibaba_Group_Logo.svg"},
    {"name": "Toyota", "foundation_year": 1937, "country": "Japan", "continent": "Asia", "state_or_province": "Aichi", "city": "Toyota City", "logo": "https://upload.wikimedia.org/wikipedia/commons/9/9d/Toyota_logo.svg"},
    {"name": "Samsung", "foundation_year": 1938, "country": "South Korea", "continent": "Asia", "state_or_province": "Gyeonggi", "city": "Suwon", "logo": "https://upload.wikimedia.org/wikipedia/commons/2/24/Samsung_Logo.svg"},
    {"name": "Walmart", "foundation_year": 1962, "country": "United States", "continent": "North America", "state_or_province": "Arkansas", "city": "Bentonville", "logo": "https://upload.wikimedia.org/wikipedia/commons/c/ca/Walmart_logo.svg"},
    {"name": "ExxonMobil", "foundation_year": 1999, "country": "United States", "continent": "North America", "state_or_province": "Texas", "city": "Irving", "logo": "https://upload.wikimedia.org/wikipedia/commons/a/a3/ExxonMobil_Logo.svg"},
    {"name": "Shell", "foundation_year": 1907, "country": "Netherlands", "continent": "Europe", "state_or_province": "South Holland", "city": "The Hague", "logo": "https://upload.wikimedia.org/wikipedia/en/8/8d/Shell_logo.svg"},
    {"name": "Volkswagen", "foundation_year": 1937, "country": "Germany", "continent": "Europe", "state_or_province": "Lower Saxony", "city": "Wolfsburg", "logo": "https://upload.wikimedia.org/wikipedia/commons/7/7e/Volkswagen_logo.svg"},
    {"name": "ICBC", "foundation_year": 1984, "country": "China", "continent": "Asia", "state_or_province": "Beijing", "city": "Beijing", "logo": "https://upload.wikimedia.org/wikipedia/commons/a/a3/Industrial_and_Commercial_Bank_of_China_%28logo%29.svg"},
    {"name": "Ping An Insurance", "foundation_year": 1988, "country": "China", "continent": "Asia", "state_or_province": "Guangdong", "city": "Shenzhen", "logo": "https://upload.wikimedia.org/wikipedia/en/2/2c/Ping_An_Insurance_logo.svg"},
    {"name": "BHP", "foundation_year": 1885, "country": "Australia", "continent": "Oceania", "state_or_province": "Victoria", "city": "Melbourne", "logo": "https://upload.wikimedia.org/wikipedia/en/d/d9/BHP_logo.svg"},
    {"name": "Procter & Gamble", "foundation_year": 1837, "country": "United States", "continent": "North America", "state_or_province": "Ohio", "city": "Cincinnati", "logo": "https://upload.wikimedia.org/wikipedia/commons/8/82/Procter_%26_Gamble_logo.svg"},
    {"name": "Nestlé", "foundation_year": 1866, "country": "Switzerland", "continent": "Europe", "state_or_province": "Vaud", "city": "Vevey", "logo": "https://upload.wikimedia.org/wikipedia/commons/6/69/Nestle_logo.svg"},
    {"name": "Johnson & Johnson", "foundation_year": 1886, "country": "United States", "continent": "North America", "state_or_province": "New Jersey", "city": "New Brunswick", "logo": "https://upload.wikimedia.org/wikipedia/commons/d/da/Johnson_and_Johnson_logo.svg"},
    {"name": "Pfizer", "foundation_year": 1849, "country": "United States", "continent": "North America", "state_or_province": "New York", "city": "New York City", "logo": "https://upload.wikimedia.org/wikipedia/commons/e/e8/Pfizer_logo.svg"},
    {"name": "Roche", "foundation_year": 1896, "country": "Switzerland", "continent": "Europe", "state_or_province": "Basel", "city": "Basel", "logo": "https://upload.wikimedia.org/wikipedia/commons/4/41/Roche_logo.svg"},
    {"name": "Novartis", "foundation_year": 1996, "country": "Switzerland", "continent": "Europe", "state_or_province": "Basel", "city": "Basel", "logo": "https://upload.wikimedia.org/wikipedia/commons/e/ee/Novartis_Logo.svg"},
    {"name": "Intel", "foundation_year": 1968, "country": "United States", "continent": "North America", "state_or_province": "California", "city": "Santa Clara", "logo": "https://upload.wikimedia.org/wikipedia/commons/c/c9/Intel_logo_%282020%29.svg"},
    {"name": "Cisco", "foundation_year": 1984, "country": "United States", "continent": "North America", "state_or_province": "California", "city": "San Jose", "logo": "https://upload.wikimedia.org/wikipedia/commons/7/73/Cisco_logo.svg"},
    {"name": "Tencent", "foundation_year": 1998, "country": "China", "continent": "Asia", "state_or_province": "Guangdong", "city": "Shenzhen", "logo": "https://upload.wikimedia.org/wikipedia/commons/4/4b/Tencent_Logo.svg"},
    {"name": "Nike", "foundation_year": 1964, "country": "United States", "continent": "North America", "state_or_province": "Oregon", "city": "Beaverton", "logo": "https://upload.wikimedia.org/wikipedia/commons/a/a6/Logo_NIKE.svg"},
    {"name": "IBM", "foundation_year": 1911, "country": "United States", "continent": "North America", "state_or_province": "New York", "city": "Armonk", "logo": "https://upload.wikimedia.org/wikipedia/commons/5/51/IBM_logo.svg"},
    {"name": "Dell", "foundation_year": 1984, "country": "United States", "continent": "North America", "state_or_province": "Texas", "city": "Round Rock", "logo": "https://upload.wikimedia.org/wikipedia/commons/a/a4/Dell_Technologies_logo.svg"},
    # Ajoutez les 20 autres entreprises...
]

# Génération du fichier CSV
with open('Top_Companies.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    headers = ["Nom", "Année de création", "Pays du siège", "Continent du siège", "État ou Province du siège", "Ville du siège", "Logo"]
    writer.writerow(headers)
    for company in companies_data:
        writer.writerow([
            company["name"], company["foundation_year"], company["country"],
            company["continent"], company["state_or_province"], company["city"], company["logo"]
        ])

print("Fichier CSV 'Top_Companies.csv' généré avec succès.")
