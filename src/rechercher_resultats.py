"""
Nom: rechercher_resultats.py
Rôle: Extrait des données de produits à partir des pages de résultats de recherche d'Amazon et les enregistre dans un fichier CSV.
Auteur: LIN Mi
Licence: Réalisé pour le projet de scraping Amazon
"""
from selectorlib import Extractor
import requests
import pandas as pd
import sys

# Création d'un Extractor en lisant à partir du fichier YAML
e = Extractor.from_yaml_file('rechercher_resultats.yml')

def scrape(url):
    headers = {
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://www.amazon.com/',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

    # Téléchargement de la page en utilisant requests
    print("Téléchargement de %s" % url)
    r = requests.get(url, headers=headers)

    # Vérification simple pour détecter si la page a été bloquée (généralement 503)
    if r.status_code > 500:
        if "To discuss automated access to Amazon data please contact" in r.text:
            print("La page %s a été bloquée par Amazon. Veuillez essayer avec de meilleurs proxies\n" % url)
        else:
            print("La page %s a probablement été bloquée par Amazon car le code de statut était %d" % (url, r.status_code))
        return None
    
    # Extraction des données à l'aide de l'Extractor de selectorlib
    return e.extract(r.text)

# Vérifiez si un argument URL a été fourni
if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    print("Veuillez fournir une URL Amazon")
    sys.exit(1)

# Scraper l'URL fournie et sauvegarder les résultats dans une liste
data = scrape(url)
if data:
    product_data = []
    for product in data['products']:
        product['Rehercher_url'] = url
        print("Enregistrement du produit : %s" % product['Titre'])
        product_data.append(product)

    # Création d'un DataFrame à partir des données de produit
    df = pd.DataFrame(product_data)

    # Définition du chemin du fichier CSV de sortie
    output_file = 'resultats_des_sorties.csv'

    # Sauvegarde du DataFrame au format CSV
    df.to_csv(output_file, index=False)

    print(f'Le fichier CSV "{output_file}" a été créé avec succès.')
else:
    print("Aucune donnée n'a été extraite.")

