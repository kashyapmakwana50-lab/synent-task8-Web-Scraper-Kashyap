import requests
from bs4 import BeautifulSoup
import csv
import json
import os

url = "https://quotes.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

data = []

for quote in soup.find_all("div", class_="quote"):
    text = quote.find("span", class_="text").text
    author = quote.find("small", class_="author").text

    tags = []
    for tag in quote.find_all("a", class_="tag"):
        tags.append(tag.text)

    data.append({
        "quote": text,
        "author": author,
        "tags": tags
    })

folder = os.path.dirname(os.path.abspath(__file__))

csv_file = os.path.join(folder, "quotes.csv")
json_file = os.path.join(folder, "quotes.json")

with open(csv_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["quote", "author", "tags"]
    )

    writer.writeheader()

    for item in data:
        writer.writerow({
            "quote": item["quote"],
            "author": item["author"],
            "tags": ", ".join(item["tags"])
        })

with open(json_file, "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

print("Scraping completed!")
print("CSV saved:", csv_file)
print("JSON saved:", json_file)
