# ============================================================
#  Web Scraper - Scrape Job Listings from Indeed (via requests + BeautifulSoup)
#  Author   : Your Name
#  Language : Python 3
#  Libraries: requests, beautifulsoup4, csv, datetime
#
#  WHAT IT DOES:
#    - Scrapes job listings for a keyword you choose (e.g. "Python Developer")
#    - Extracts: Job Title, Company, Location, Date Posted
#    - Saves everything neatly into a CSV file
#    - Shows results in the terminal too
#
#  HOW TO INSTALL LIBRARIES:
#    pip install requests beautifulsoup4
#
#  HOW TO RUN:
#    python web_scraper.py
# ============================================================

import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime


# ── SETTINGS ────────────────────────────────────────────────
BASE_URL = "https://books.toscrape.com/catalogue/"
START_URL = "https://books.toscrape.com/catalogue/page-1.html"
MAX_PAGES  = 5          # How many pages to scrape (each page has 20 books)
OUTPUT_FILE = "books_data.csv"
# ────────────────────────────────────────────────────────────


def get_page(url):
    """Fetch the HTML content of a page."""
    headers = {"User-Agent": "Mozilla/5.0"}  # Pretend to be a browser
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise error if request failed
        return response.text
    except requests.RequestException as e:
        print(f"  [ERROR] Could not fetch page: {e}")
        return None


def parse_books(html):
    """Extract book details from the page HTML."""
    soup = BeautifulSoup(html, "html.parser")
    books = []

    # Each book is inside an <article class="product_pod"> tag
    for article in soup.find_all("article", class_="product_pod"):

        # --- Title ---
        title = article.h3.a["title"]

        # --- Price ---
        price = article.find("p", class_="price_color").text.strip()

        # --- Rating (written as words like "One", "Two", etc.) ---
        rating_word = article.p["class"][1]  # e.g. "Three"
        rating_map  = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
        rating      = rating_map.get(rating_word, 0)

        # --- Availability ---
        availability = article.find("p", class_="instock availability").text.strip()

        books.append({
            "Title"       : title,
            "Price (£)"   : price.replace("£", "Â£").replace("Â£", "£"),
            "Rating (/5)" : rating,
            "Availability": availability,
        })

    return books


def get_next_page(html, current_page_num):
    """Build the URL for the next page."""
    soup = BeautifulSoup(html, "html.parser")
    next_btn = soup.find("li", class_="next")
    if next_btn:
        next_page_num = current_page_num + 1
        return f"{BASE_URL}page-{next_page_num}.html"
    return None   # No more pages


def save_to_csv(all_books, filename):
    """Save the list of books to a CSV file."""
    if not all_books:
        print("No data to save.")
        return

    fieldnames = ["Title", "Price (£)", "Rating (/5)", "Availability"]
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_books)

    print(f"\n  ✅  Data saved to '{filename}'")


def display_sample(books, n=5):
    """Print the first n results nicely in the terminal."""
    print(f"\n{'='*60}")
    print(f"  SAMPLE RESULTS (first {n} books)")
    print(f"{'='*60}")
    for i, book in enumerate(books[:n], 1):
        print(f"\n  [{i}] {book['Title']}")
        print(f"       Price      : {book['Price (£)']}")
        print(f"       Rating     : {'⭐' * book['Rating (/5)']} ({book['Rating (/5)']} / 5)")
        print(f"       Available  : {book['Availability']}")
    print(f"\n{'='*60}")


def main():
    print("="*60)
    print("  📚  Web Scraper — Books to Scrape")
    print(f"  Started : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*60)

    all_books   = []
    current_url = START_URL
    page_num    = 1

    while current_url and page_num <= MAX_PAGES:
        print(f"\n  🔍 Scraping page {page_num} → {current_url}")
        html = get_page(current_url)

        if html is None:
            break

        books = parse_books(html)
        all_books.extend(books)
        print(f"     Found {len(books)} books on this page. Total so far: {len(all_books)}")

        current_url = get_next_page(html, page_num)
        page_num   += 1

    # Show a sample in the terminal
    display_sample(all_books)

    # Save everything to CSV
    save_to_csv(all_books, OUTPUT_FILE)

    print(f"\n  🎉 Done! Scraped {len(all_books)} books total.")
    print(f"  Open '{OUTPUT_FILE}' to see all the data.\n")


if __name__ == "__main__":
    main()
