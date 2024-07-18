# Guide de l'utilisateur pour Amazon Product Scraper

## Introduction
Amazon Product Scraper est un outil convivial qui vous permet de scraper des informations sur les produits d'Amazon. Ce guide vous explique comment installer, configurer et utiliser l'application.

## Installation
Prérequis
Python 3.6 ou supérieur

Étapes
Cloner le dépôt :

git clone https://github.com/camillemi/Amazo_Product_Scraper.git
cd Amazo_Product_Scraper

Installer les dépendances :

make install

## Utilisation de l'application

Exécution de l'interface graphique
Démarrer l'interface graphique :

make run_gui

Entrer l'URL du produit Amazon dans le champ de saisie.

Cliquer sur le bouton "Scraper".

Voir le résultat : Une fois le scraping terminé, les résultats seront sauvegardés dans resultats_des_sorties.csv.

## Exécution en ligne de commande

Exécuter le script avec l'URL du produit Amazon en argument :

python3 src/rechercher_resultats.py <amazon_product_url>
Voir le résultat : Les résultats seront sauvegardés dans resultats_des_sorties.csv.2. **Voir la sortie** : Les résultats seront sauvegardés dans `src/resultats_des_sorties.csv`.
Pour tester le scraper, vous pouvez utiliser les exemples d'URL fournis dans le fichier `src/Exemples_urls.txt`.

## Dépannage

Assurez-vous d'avoir une connexion Internet stable.
Vérifiez que l'URL du produit Amazon est correcte.
Vérifiez que les dépendances requises sont installées en exécutant à nouveau make install.

##Contact
Pour toute question ou problème, veuillez contacter [linmi2018@gmail.com].







