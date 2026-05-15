import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

class GDScraper:
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        self.results = []

    def fetch_data(self, url, tag, class_name=None):
        try:
            print(f"\n[SYSTEM] Rufe Daten von {url} ab...")
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Suche nach Elementen (optional mit Klasse)
            if class_name:
                elements = soup.find_all(tag, class_=class_name)
            else:
                elements = soup.find_all(tag)
            
            self.results = [el.get_text().strip() for el in elements]
            return self.results

        except Exception as e:
            print(f"[ERROR] Fehler beim Scrapen: {e}")
            return []

    def save_to_file(self, filename="export.csv"):
        if not self.results:
            print("[WARN] Keine Daten zum Speichern vorhanden.")
            return

        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Index", "Inhalt", "Zeitstempel"])
            for i, content in enumerate(self.results, 1):
                writer.writerow([i, content, datetime.now().strftime("%Y-%m-%d %H:%M")])
        
        print(f"[SUCCESS] Daten erfolgreich in {filename} gespeichert!")

def main():
    scraper = GDScraper()
    print("--- GreenData Scraper v1.0 ---")
    
    target_url = input("Ziel-URL: ")
    target_tag = input("HTML-Tag (z.B. h2, p, li): ")
    target_class = input("Klasse (optional, Enter zum Überspringen): ")
    
    data = scraper.fetch_data(target_url, target_tag, target_class if target_class else None)
    
    if data:
        print(f"\nGefundene Einträge ({len(data)}):")
        for i, text in enumerate(data[:10], 1): # Zeige nur die ersten 10
            print(f"{i}. {text[:75]}...")
            
        save_choice = input("\nSoll ich die Ergebnisse in einer CSV speichern? (j/n): ")
        if save_choice.lower() == 'j':
            scraper.save_to_file("gd_export.csv")

if __name__ == "__main__":
    main()