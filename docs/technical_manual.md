# Manuel Technique pour Amazon Product Scraper

Ce manuel technique fournit des détails approfondis sur la mise en œuvre, la configuration et la maintenance de l'application Amazon Product Scraper. Ce document est destiné aux développeurs et aux administrateurs systèmes qui souhaitent comprendre le fonctionnement interne de l'application.

## Structure du Projet
Le projet est organisé comme suit :

my_scraper_project/

├── src/

│   ├── rechercher_resultats.py

│   ├── rechercher_resultats.yml

│   ├── gui.py

│   ├── requirements.txt

│   └── Exemples_urls.txt

├── docs/

│   ├── user_guide.md

│   └── technical_manual.md

├── debian/

│   ├── control

│   ├── postinst

│   └── postrm

├── README.md

├── setup.py

├── MANIFEST.in

├── LICENSE

└── Makefile

## Composants

1. rechercher_resultats.py
Ce script principal utilise les bibliothèques requests et selectorlib pour télécharger et extraire les données des pages de produits Amazon. Il enregistre les résultats dans un fichier CSV.

Fonctionnement :
Télécharge la page à partir de l'URL fournie.
Utilise selectorlib pour extraire les informations du produit basées sur le fichier de modèle YAML (rechercher_resultats.yml).
Enregistre les données extraites dans resultats_des_sorties.csv.

2. rechercher_resultats.yml
Ce fichier contient les sélecteurs CSS utilisés par selectorlib pour extraire les informations nécessaires des pages de produits Amazon.

3. gui.py
Ce script contient l'interface graphique (GUI) construite avec tkinter. Il permet à l'utilisateur d'entrer une URL de produit Amazon, de lancer le processus de scraping et de voir les résultats.

Fonctionnement :
Affiche une fenêtre avec un champ de saisie pour l'URL et un bouton pour démarrer le scraping.
Exécute rechercher_resultats.py lorsque l'utilisateur clique sur le bouton "Scrape".
Affiche un message de confirmation ou d'erreur selon le résultat du processus de scraping.

4. requirements.txt
Ce fichier liste toutes les dépendances Python nécessaires au projet.


5. Exemples_urls.txt
Ce fichier contient des exemples d'URL de produits Amazon à utiliser pour tester le scraper.

6. debian/control
Ce fichier contient les informations de contrôle pour créer un paquet Debian pour l'application.

 
7. debian/postinst
Ce script est exécuté après l'installation du paquet Debian.


8. debian/postrm
Ce script est exécuté après la suppression du paquet Debian.


9. Makefile
Ce fichier contient des tâches pour automatiser l'installation des dépendances, l'exécution de l'application GUI et le nettoyage des fichiers générés.

	
10. README.md
Ce fichier fournit une vue d'ensemble de l'application, des instructions d'installation et des exemples d'utilisation.

11. setup.py
Ce script est utilisé pour créer un paquet installable de l'application.


12. MANIFEST.in
Ce fichier inclut des fichiers supplémentaires dans le paquet.

13. Licence
Ce projet est sous licence GNU GPL v3.

## Configuration

### Variables d'Environnement

L'application ne nécessite pas de variables d'environnement spécifiques pour fonctionner. Cependant, assurez-vous que votre environnement Python est correctement configuré avec toutes les dépendances installées.

### Dépendances

Liste des principales dépendances Python :
requests
selectorlib
pandas
tkinter

## Déploiement

Créer un Paquet Debian
Naviguer vers le répertoire du projet :

cd my_scraper_project
Construire le paquet Debian :
dpkg-deb --build debian
Installer le Paquet Debian

Installer le paquet :
sudo dpkg -i amazon-product-scraper.deb

## Maintenance
Mise à Jour des Dépendances
Pour mettre à jour les dépendances, modifiez requirements.txt et exécutez :
make install

## Dépannage

Problèmes de scraping :

Vérifiez que l'URL du produit Amazon est correcte.
Vérifiez que le fichier rechercher_resultats.yml contient les bons sélecteurs CSS.
Problèmes de dépendances :

Assurez-vous que toutes les dépendances listées dans requirements.txt sont installées.
Exécutez à nouveau make install pour installer les dépendances manquantes
.
## Conclusion

Ce manuel technique vous a fourni une vue d'ensemble détaillée de l'application Amazon Product Scraper. Pour toute question supplémentaire ou pour des contributions, veuillez consulter le fichier README.md et les guides d'utilisation fournis dans le répertoire docs.
