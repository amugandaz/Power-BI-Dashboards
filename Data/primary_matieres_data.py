import csv

# Liste complète des 50 matières premières
raw_materials_data = [
    {"name": "Or", "chemical_formula": "Au", "main_producing_country": "China", "continent": "Asia", "image": "https://upload.wikimedia.org/wikipedia/commons/4/48/Gold_Nugget.jpg"},
    {"name": "Diamant", "chemical_formula": "C", "main_producing_country": "Botswana", "continent": "Africa", "image": "https://upload.wikimedia.org/wikipedia/commons/a/a9/Natural_Diamond.jpg"},
    {"name": "Étain", "chemical_formula": "Sn", "main_producing_country": "Indonesia", "continent": "Asia", "image": "https://upload.wikimedia.org/wikipedia/commons/3/35/Tin-2.jpg"},
    {"name": "Fer", "chemical_formula": "Fe", "main_producing_country": "Australia", "continent": "Oceania", "image": "https://upload.wikimedia.org/wikipedia/commons/a/a4/Iron_ore_hematite.jpg"},
    {"name": "Cuivre", "chemical_formula": "Cu", "main_producing_country": "Chile", "continent": "South America", "image": "https://upload.wikimedia.org/wikipedia/commons/5/55/NatCopper.jpg"},
    {"name": "Aluminium", "chemical_formula": "Al", "main_producing_country": "China", "continent": "Asia", "image": "https://upload.wikimedia.org/wikipedia/commons/8/8b/Aluminium-4.jpg"},
    {"name": "Platine", "chemical_formula": "Pt", "main_producing_country": "South Africa", "continent": "Africa", "image": "https://upload.wikimedia.org/wikipedia/commons/f/fe/Platinum_crystals.jpg"},
    {"name": "Argent", "chemical_formula": "Ag", "main_producing_country": "Mexico", "continent": "North America", "image": "https://upload.wikimedia.org/wikipedia/commons/a/a7/Silver_ore.jpg"},
    {"name": "Lithium", "chemical_formula": "Li", "main_producing_country": "Australia", "continent": "Oceania", "image": "https://upload.wikimedia.org/wikipedia/commons/d/d4/Spodumene_Lithium_Ore.jpg"},
    {"name": "Uranium", "chemical_formula": "U", "main_producing_country": "Kazakhstan", "continent": "Asia", "image": "https://upload.wikimedia.org/wikipedia/commons/f/fe/Uraninite.jpg"},
    {"name": "Nickel", "chemical_formula": "Ni", "main_producing_country": "Indonesia", "continent": "Asia", "image": "https://upload.wikimedia.org/wikipedia/commons/a/a6/Nickel_sulfide.jpg"},
    {"name": "Zinc", "chemical_formula": "Zn", "main_producing_country": "China", "continent": "Asia", "image": "https://upload.wikimedia.org/wikipedia/commons/6/67/Zinc_1.jpg"},
    {"name": "Cobalt", "chemical_formula": "Co", "main_producing_country": "Democratic Republic of Congo", "continent": "Africa", "image": "https://upload.wikimedia.org/wikipedia/commons/a/a2/Cobalt%28metallic_beads%29.jpg"},
    {"name": "Charbon", "chemical_formula": "C", "main_producing_country": "China", "continent": "Asia", "image": "https://upload.wikimedia.org/wikipedia/commons/2/20/Coal_anthracite.jpg"},
    {"name": "Pétrole", "chemical_formula": "N/A (Hydrocarbon mixture)", "main_producing_country": "United States", "continent": "North America", "image": "https://upload.wikimedia.org/wikipedia/commons/4/4a/Crude_oil_sample.jpg"},
    {"name": "Gaz naturel", "chemical_formula": "CH₄", "main_producing_country": "United States", "continent": "North America", "image": "https://upload.wikimedia.org/wikipedia/commons/6/69/Natural_gas_flare.jpg"},
    {"name": "Bauxite", "chemical_formula": "Al₂O₃", "main_producing_country": "Australia", "continent": "Oceania", "image": "https://upload.wikimedia.org/wikipedia/commons/8/87/Bauxite.jpg"},
    {"name": "Plomb", "chemical_formula": "Pb", "main_producing_country": "China", "continent": "Asia", "image": "https://upload.wikimedia.org/wikipedia/commons/9/99/Lead_piece.jpg"},
    {"name": "Manganèse", "chemical_formula": "Mn", "main_producing_country": "South Africa", "continent": "Africa", "image": "https://upload.wikimedia.org/wikipedia/commons/4/48/Manganese_electrolytic_and_1cm3_cube.jpg"},
    {"name": "Tungstène", "chemical_formula": "W", "main_producing_country": "China", "continent": "Asia", "image": "https://upload.wikimedia.org/wikipedia/commons/f/f0/Tungsten_single_crystal.jpg"},
    {"name": "Kaolin", "chemical_formula": "Al₂Si₂O₅(OH)₄", "main_producing_country": "United States", "continent": "North America", "image": "https://upload.wikimedia.org/wikipedia/commons/e/ed/Kaolinite.jpg"},
    {"name": "Rubis", "chemical_formula": "Al₂O₃", "main_producing_country": "Myanmar", "continent": "Asia", "image": "https://upload.wikimedia.org/wikipedia/commons/4/4e/Ruby.jpg"},
    {"name": "Saphir", "chemical_formula": "Al₂O₃", "main_producing_country": "Madagascar", "continent": "Africa", "image": "https://upload.wikimedia.org/wikipedia/commons/7/72/Sapphire_crystal.jpg"},
    {"name": "Émeraude", "chemical_formula": "Be₃Al₂Si₆O₁₈", "main_producing_country": "Colombia", "continent": "South America", "image": "https://upload.wikimedia.org/wikipedia/commons/1/17/Emerald_crystal.jpg"},
    {"name": "Quartz", "chemical_formula": "SiO₂", "main_producing_country": "Brazil", "continent": "South America", "image": "https://upload.wikimedia.org/wikipedia/commons/b/b0/Quartz%2C_Tibet.jpg"},
    {"name": "Granit", "chemical_formula": "N/A (Silicate minerals)", "main_producing_country": "India", "continent": "Asia", "image": "https://upload.wikimedia.org/wikipedia/commons/8/84/Granite.JPG"},
    {"name": "Graphite", "chemical_formula": "C", "main_producing_country": "China", "continent": "Asia", "image": "https://upload.wikimedia.org/wikipedia/commons/7/7e/Natural_graphite.jpg"},
    {"name": "Argile", "chemical_formula": "N/A (Mineral mixture)", "main_producing_country": "United States", "continent": "North America", "image": "https://upload.wikimedia.org/wikipedia/commons/f/f3/Clay.jpg"},
    {"name": "Sable", "chemical_formula": "SiO₂", "main_producing_country": "India", "continent": "Asia", "image": "https://upload.wikimedia.org/wikipedia/commons/1/1a/Sand.jpg"},
    {"name": "Sel", "chemical_formula": "NaCl", "main_producing_country": "United States", "continent": "North America", "image": "https://upload.wikimedia.org/wikipedia/commons/e/eb/Salt.jpg"},
]

# Génération du fichier CSV
with open('Raw_Materials.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    headers = ["Nom", "Formule chimique", "Principal pays producteur", "Continent", "Image"]
    writer.writerow(headers)
    for material in raw_materials_data:
        writer.writerow([
            material["name"], material["chemical_formula"], material["main_producing_country"],
            material["continent"], material["image"]
        ])

print("Fichier CSV 'Raw_Materials.csv' généré avec succès.")
