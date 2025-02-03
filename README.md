# web-scraper

Dette prosjektet er et Python-basert web scraper som henter informasjon om bøker fra nettsiden [Books to Scrape](http://books.toscrape.com/). Programmet laster ned bokdata – inkludert tittel, pris, rating, tilgjengelighet og detaljside-URL – og lagrer informasjonen i en CSV-fil.

## Funksjonalitet

- **Scraping fra flere sider:** Henter data ved hjelp av paginering.
- **Dataekstraksjon:** Henter ut informasjon som tittel, pris, rating og tilgjengelighet.
- **CSV-utdata:** Skriver den innsamlede informasjonen til en CSV-fil for videre bruk eller analyse.

## Teknologier

- **Python 3.x**
- **Requests:** For å gjøre HTTP-forespørsler.
- **BeautifulSoup:** For parsing og datauttrekking fra HTML.
- **csv:** For å lagre data i CSV-format.
- **urllib.parse (urljoin):** For å håndtere URL-konstruksjoner.

## Installasjon

1. **Klone repository:**

   ```bash
   git clone https://github.com/<ditt-brukernavn>/web-scraper.git