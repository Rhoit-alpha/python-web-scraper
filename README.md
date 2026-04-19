# 📚 Web Scraper — Books Data Extractor

A Python automation script that scrapes book listings from [books.toscrape.com](https://books.toscrape.com) and exports the data into a clean CSV file.

---

## 🚀 What It Does

- Scrapes multiple pages of book listings automatically
- Extracts: **Title**, **Price**, **Star Rating**, **Availability**
- Saves all data into a `books_data.csv` file
- Displays a sample preview in the terminal

---

## 🛠️ Installation

Make sure you have Python 3 installed, then run:

```bash
pip install requests beautifulsoup4
```

---

## ▶️ How to Run

```bash
python web_scraper.py
```

---

## 📁 Output

A file called `books_data.csv` will be created with columns:

| Title | Price (£) | Rating (/5) | Availability |
|-------|-----------|-------------|--------------|
| A Light in the Attic | £51.77 | 3 | In stock |
| ... | ... | ... | ... |

---

## ⚙️ Configuration

You can change these settings at the top of `web_scraper.py`:

| Setting | Default | Description |
|---------|---------|-------------|
| `MAX_PAGES` | 5 | Number of pages to scrape |
| `OUTPUT_FILE` | `books_data.csv` | Output filename |

---

## 💡 Skills Demonstrated

- Web scraping with `requests` and `BeautifulSoup`
- HTML parsing and data extraction
- CSV file generation with Python
- Error handling and clean terminal output

---

## 📬 Hire Me

Looking for a Python automation script for your business?  
Connect with me on [LinkedIn](#) or reach out directly!
