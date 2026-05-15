# GDScraper v1.0

Ein modularer Webscraper, entwickelt mit Python. Das Tool ermöglicht es, gezielt Daten von Webseiten zu extrahieren und diese strukturiert für die Weiterverarbeitung zu speichern.

## 🚀 Features
- **OOP-Struktur:** Das Projekt ist in Klassen organisiert, was eine einfache Erweiterung und Wartung ermöglicht.
- **Flexibles Scraping:** Suche nach spezifischen HTML-Tags und CSS-Klassen über Benutzereingaben.
- **CSV-Export:** Automatisches Speichern der Ergebnisse inklusive Zeitstempel für die Datenanalyse.
- **Robustes Handling:** Implementierung von Custom Headers (User-Agent) zur Vermeidung von Zugriffssperren.

## 🛠️ Tech-Stack
- **Sprache:** Python 3.12
- **Libraries:** - `BeautifulSoup4` (Parsing)
  - `Requests` (HTTP-Anfragen)
  - `CSV` (Datenexport)

## 🔧 Nutzung
1. Abhängigkeiten installieren:
   ```bash
   pip install requests beautifulsoup4