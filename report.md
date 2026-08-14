# Web Scraping – Project Report

## 1. Objective

The objective of this project is to create a Python web scraper that collects quotes, authors, and associated tags from a website and saves the extracted information into CSV and JSON files.

## 2. Methodology

The program sends an HTTP request to the target website using the `requests` library. The returned HTML content is processed using `BeautifulSoup` to locate quote elements and extract their text, author, and tags.

The extracted information is stored in a Python list before being exported into two different file formats.

## 3. Implementation

The program uses:

* `requests` to retrieve the webpage.
* `BeautifulSoup` to parse and extract HTML data.
* `csv` to create the CSV output file.
* `json` to create the JSON output file.
* `os` to determine the script's directory and save the output files there.

The generated files are named `quotes.csv` and `quotes.json`.

## 4. Testing and Results

The scraper was executed successfully and extracted the available quotes from the target webpage along with their authors and tags.

The collected data was successfully saved in both CSV and JSON formats. The output files were checked to confirm that the extracted information was stored correctly.

## 5. Conclusion

The Web Scraping project successfully demonstrates how Python can retrieve, parse, and store data from a webpage. It provides structured output in both CSV and JSON formats and demonstrates practical use of HTTP requests, HTML parsing, and data storage.
