import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urljoin

# Basis-URL for nettsiden
base_url = "http://books.toscrape.com/"
current_url = base_url

# Liste for å lagre data om bøker
books_data = []

while True:
    response = requests.get(current_url)
    if response.status_code != 200:
        print(f"Klarte ikke å hente nettsiden. Statuskode: {response.status_code}")
        break

    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Hent alle bokelementene på siden
    books = soup.find_all('article', class_='product_pod')
    for book in books:
        # Tittel
        a_tag = book.find('h3').find('a')
        title = a_tag.get('title', 'Ukjent tittel')
        
        # Pris
        price = book.find('p', class_='price_color').text
        
        # Rating: Finn <p> med klassen "star-rating" og hent ut den andre klassen
        rating_tag = book.find('p', class_='star-rating')
        rating_classes = rating_tag.get('class', [])
        # Fjern den generelle "star-rating"-klassen for å få ratingen
        rating = next((cls for cls in rating_classes if cls != 'star-rating'), 'Ingen rating')
        
        # Tilgjengelighet: Finn teksten i elementet med klassen "instock availability"
        availability = book.find('p', class_='instock availability').get_text(strip=True)
        
        # Detaljside URL: Hent ut href-attributtet fra <a>-taggen og bygg en absolutt URL
        relative_url = a_tag.get('href')
        detail_url = urljoin(base_url, relative_url)
        
        books_data.append({
            'title': title,
            'price': price,
            'rating': rating,
            'availability': availability,
            'detail_url': detail_url
        })
    
    # Sjekk om det finnes en "Neste" side ved å lete etter et <li> med klassen "next"
    next_button = soup.find('li', class_='next')
    if next_button:
        next_link = next_button.find('a')['href']
        current_url = urljoin(current_url, next_link)
    else:
        # Ingen "Neste" side, så vi er ferdig med scraping
        break

# Skriv dataene til en CSV-fil
csv_fil = 'BtoS_extended.csv'
with open(csv_fil, 'w', newline='', encoding='utf-8') as f:
    fieldnames = ['title', 'price', 'rating', 'availability', 'detail_url']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(books_data)

print(f"Scraping ferdig! Data lagret i '{csv_fil}'")