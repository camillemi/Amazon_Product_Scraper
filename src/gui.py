"""
Nom: gui.py
Rôle: Ce script fournit l'interface graphique de l'application de scraping Amazon. Il permet aux utilisateurs de saisir l'URL du produit Amazon, 
d'initier le processus de scraping via un bouton, et d'afficher le résultat ou les erreurs éventuelles. L'interface inclut également un bouton pour 
ouvrir le fichier de sortie contenant les données extraites.
Auteur: LIN Mi
Licence: Réalisé pour le projet de scraping Amazon. 
Usage: make run_gui
"""

import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess

class ScraperApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Amazon Scraper")
        self.geometry("600x500")

        self.url_label = tk.Label(self, text="URL Amazon:")
        self.url_label.pack(pady=10)

        self.url_entry = tk.Entry(self, width=50)
        self.url_entry.pack(pady=10)

        self.scrape_button = tk.Button(self, text="Scrape", command=self.scrape)
        self.scrape_button.pack(pady=10)

        self.output_label = tk.Label(self, text="")
        self.output_label.pack(pady=10)

        self.output_button = tk.Button(self, text="Voir fichier de sortie", command=self.open_file)
        self.output_button.pack(pady=10)

    def scrape(self):
        url = self.url_entry.get()
        if url:
            result = subprocess.run(['python3', 'rechercher_resultats.py', url], capture_output=True, text=True, cwd='src')
            if result.returncode == 0:
                self.output_label.config(text="Scraping terminé. Résultat sauvegardé.")
            else:
                self.output_label.config(text=f"Erreur lors du scraping: {result.stderr}")

    def open_file(self):
        file_path = 'src/resultats_des_sorties.csv'
        try:
            subprocess.run(['xdg-open', file_path], check=True)
        except Exception as e:
            self.output_label.config(text=f"Erreur: {e}")

if __name__ == "__main__":
    app = ScraperApp()
    app.mainloop()

