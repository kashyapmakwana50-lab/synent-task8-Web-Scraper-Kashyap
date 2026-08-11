# Quotes Web Scraper 🕷️

A simple Python web scraper that collects quotes, authors, and tags from Quotes to Scrape and saves the data as CSV and JSON files.

## Features

* Scrapes quotes from a website
* Collects quote text and author names
* Collects quote tags
* Saves data to CSV
* Saves data to JSON
* Automatically saves files in the project folder

## How to Run

Install the required libraries:

```bash
pip install requests beautifulsoup4
```

Then run:

```bash
python task8.py
```

## Output

The scraper creates two files:

```text
quotes.csv
quotes.json
```

### Example

```text
Scraping completed!
CSV saved: .../quotes.csv
JSON saved: .../quotes.json
```

## Requirements

* Python 3.x
* `requests`
* `beautifulsoup4`

## License

This project is open source and free to use.
