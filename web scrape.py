import requests
from bs4 import BeautifulSoup
import csv

url = "https://example.com"

try:
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.title.text
    print("Page Title:", title)

    headings = soup.find_all("h1")
    print("\nHeadings:")
    for h in headings:
        print("-", h.text)

    with open("scraped_data.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Type", "Content"])
        writer.writerow(["Title", title])

        for h in headings:
            writer.writerow(["Heading", h.text])

    print("\nData saved successfully!")

except Exception as e:
    print("Error:", e)
