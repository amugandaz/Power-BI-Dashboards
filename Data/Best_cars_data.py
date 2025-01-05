import csv

# Liste complète des 50 plus grands constructeurs automobiles
automobile_manufacturers_data = [
    {"name": "Toyota", "foundation_year": 1937, "country": "Japan", "continent": "Asia", "state_or_province": "Aichi", "city": "Toyota City", "logo": "https://upload.wikimedia.org/wikipedia/commons/9/9d/Toyota_logo.svg"},
    {"name": "Volkswagen Group", "foundation_year": 1937, "country": "Germany", "continent": "Europe", "state_or_province": "Lower Saxony", "city": "Wolfsburg", "logo": "https://upload.wikimedia.org/wikipedia/commons/7/7e/Volkswagen_logo.svg"},
    {"name": "General Motors", "foundation_year": 1908, "country": "United States", "continent": "North America", "state_or_province": "Michigan", "city": "Detroit", "logo": "https://upload.wikimedia.org/wikipedia/commons/8/8e/General_Motors_logo.svg"},
    {"name": "Ford Motor Company", "foundation_year": 1903, "country": "United States", "continent": "North America", "state_or_province": "Michigan", "city": "Dearborn", "logo": "https://upload.wikimedia.org/wikipedia/commons/3/3e/Ford_logo_flat.svg"},
    {"name": "Honda Motor Co.", "foundation_year": 1948, "country": "Japan", "continent": "Asia", "state_or_province": "Tokyo", "city": "Tokyo", "logo": "https://upload.wikimedia.org/wikipedia/commons/3/36/Honda_logo.svg"},
    {"name": "Hyundai Motor Company", "foundation_year": 1967, "country": "South Korea", "continent": "Asia", "state_or_province": "Seoul", "city": "Seoul", "logo": "https://upload.wikimedia.org/wikipedia/commons/4/4e/Hyundai_Motor_Company_logo.svg"},
    {"name": "Nissan", "foundation_year": 1933, "country": "Japan", "continent": "Asia", "state_or_province": "Kanagawa", "city": "Yokohama", "logo": "https://upload.wikimedia.org/wikipedia/commons/0/0b/Nissan_logo.svg"},
    {"name": "BMW Group", "foundation_year": 1916, "country": "Germany", "continent": "Europe", "state_or_province": "Bavaria", "city": "Munich", "logo": "https://upload.wikimedia.org/wikipedia/commons/4/44/BMW.svg"},
    {"name": "Mercedes-Benz Group AG", "foundation_year": 1926, "country": "Germany", "continent": "Europe", "state_or_province": "Baden-Württemberg", "city": "Stuttgart", "logo": "https://upload.wikimedia.org/wikipedia/commons/e/ed/Mercedes-Benz_star_2022.svg"},
    {"name": "Stellantis", "foundation_year": 2021, "country": "Netherlands", "continent": "Europe", "state_or_province": "North Holland", "city": "Amsterdam", "logo": "https://upload.wikimedia.org/wikipedia/commons/e/e4/Stellantis_logo.svg"},
    {"name": "Tesla, Inc.", "foundation_year": 2003, "country": "United States", "continent": "North America", "state_or_province": "California", "city": "Palo Alto", "logo": "https://upload.wikimedia.org/wikipedia/commons/b/bd/Tesla_Motors.svg"},
    {"name": "Renault", "foundation_year": 1899, "country": "France", "continent": "Europe", "state_or_province": "Île-de-France", "city": "Boulogne-Billancourt", "logo": "https://upload.wikimedia.org/wikipedia/commons/e/e2/Renault_2021_logo.svg"},
    {"name": "Peugeot", "foundation_year": 1810, "country": "France", "continent": "Europe", "state_or_province": "Île-de-France", "city": "Paris", "logo": "https://upload.wikimedia.org/wikipedia/commons/d/d3/Peugeot_logo_2021.svg"},
    {"name": "Ferrari", "foundation_year": 1939, "country": "Italy", "continent": "Europe", "state_or_province": "Emilia-Romagna", "city": "Maranello", "logo": "https://upload.wikimedia.org/wikipedia/en/d/d9/Ferrari_Logo.svg"},
    {"name": "Lamborghini", "foundation_year": 1963, "country": "Italy", "continent": "Europe", "state_or_province": "Emilia-Romagna", "city": "Sant'Agata Bolognese", "logo": "https://upload.wikimedia.org/wikipedia/en/4/4d/Lamborghini_logo.svg"},
    {"name": "Audi", "foundation_year": 1909, "country": "Germany", "continent": "Europe", "state_or_province": "Bavaria", "city": "Ingolstadt", "logo": "https://upload.wikimedia.org/wikipedia/commons/6/63/Audi_logo_2023.svg"},
    {"name": "Porsche", "foundation_year": 1931, "country": "Germany", "continent": "Europe", "state_or_province": "Baden-Württemberg", "city": "Stuttgart", "logo": "https://upload.wikimedia.org/wikipedia/en/3/32/Porsche_logo.svg"},
    {"name": "Kia Corporation", "foundation_year": 1944, "country": "South Korea", "continent": "Asia", "state_or_province": "Seoul", "city": "Seoul", "logo": "https://upload.wikimedia.org/wikipedia/commons/3/39/Kia_logo.svg"},
    {"name": "Mazda", "foundation_year": 1920, "country": "Japan", "continent": "Asia", "state_or_province": "Hiroshima", "city": "Hiroshima", "logo": "https://upload.wikimedia.org/wikipedia/en/0/0d/Mazda_logo_2023.svg"},
    {"name": "Suzuki", "foundation_year": 1909, "country": "Japan", "continent": "Asia", "state_or_province": "Shizuoka", "city": "Hamamatsu", "logo": "https://upload.wikimedia.org/wikipedia/commons/7/7e/Suzuki_logo.svg"},
    {"name": "Volvo Cars", "foundation_year": 1927, "country": "Sweden", "continent": "Europe", "state_or_province": "Västra Götaland", "city": "Gothenburg", "logo": "https://upload.wikimedia.org/wikipedia/commons/5/5f/Volvo_Cars_logo_2020.svg"},
    {"name": "Subaru", "foundation_year": 1953, "country": "Japan", "continent": "Asia", "state_or_province": "Gunma", "city": "Ota", "logo": "https://upload.wikimedia.org/wikipedia/commons/4/42/Subaru_logo.svg"},
    {"name": "Mitsubishi Motors", "foundation_year": 1870, "country": "Japan", "continent": "Asia", "state_or_province": "Tokyo", "city": "Tokyo", "logo": "https://upload.wikimedia.org/wikipedia/commons/1/1e/Mitsubishi_Motors_logo.svg"},
    {"name": "Chevrolet", "foundation_year": 1911, "country": "United States", "continent": "North America", "state_or_province": "Michigan", "city": "Detroit", "logo": "https://upload.wikimedia.org/wikipedia/commons/0/06/Chevrolet_logo.svg"},
    {"name": "Jaguar Land Rover", "foundation_year": 1922, "country": "United Kingdom", "continent": "Europe", "state_or_province": "England", "city": "Coventry", "logo": "https://upload.wikimedia.org/wikipedia/commons/2/26/Jaguar_Land_Rover_logo.svg"},
    {"name": "Tata Motors", "foundation_year": 1945, "country": "India", "continent": "Asia", "state_or_province": "Maharashtra", "city": "Mumbai", "logo": "https://upload.wikimedia.org/wikipedia/commons/f/f7/Tata_Motors_Logo.svg"},
    {"name": "Geely", "foundation_year": 1986, "country": "China", "continent": "Asia", "state_or_province": "Zhejiang", "city": "Hangzhou", "logo": "https://upload.wikimedia.org/wikipedia/en/d/d0/Geely_logo.svg"},
    {"name": "Changan", "foundation_year": 1862, "country": "China", "continent": "Asia", "state_or_province": "Chongqing", "city": "Chongqing", "logo": "https://upload.wikimedia.org/wikipedia/en/3/35/Changan_Auto_logo.svg"},
    {"name": "Daimler Trucks", "foundation_year": 2019, "country": "Germany", "continent": "Europe", "state_or_province": "Baden-Württemberg", "city": "Stuttgart", "logo": "https://upload.wikimedia.org/wikipedia/en/7/72/Daimler_Trucks_Logo.svg"},
]

# Génération du fichier CSV
with open('Top_Automobile_Manufacturers.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    headers = ["Nom", "Année de création", "Pays", "Continent", "État ou Province", "Ville", "Logo"]
    writer.writerow(headers)
    for manufacturer in automobile_manufacturers_data:
        writer.writerow([
            manufacturer["name"], manufacturer["foundation_year"], manufacturer["country"],
            manufacturer["continent"], manufacturer["state_or_province"], manufacturer["city"],
            manufacturer["logo"]
        ])

print("Fichier CSV 'Top_Automobile_Manufacturers.csv' généré avec succès.")
