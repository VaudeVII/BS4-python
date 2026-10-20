import requests
from bs4 import BeautifulSoup
import csv

#-----setup
url = "https://realpython.github.io/fake-jobs/"
keywords = [k.strip().lower() for k in input("enter keywords separated by commas (example: python, developer): ").split(",") if k.strip()]
jobs = []
response = requests.get(url, timeout=10)
response.raise_for_status()
soup = BeautifulSoup(response.content, "html.parser")

for card in soup.select("#ResultsContainer div.card"):
    title = card.select_one("h2.title").text.strip()

    if keywords and not any(word in title.lower() for word in keywords):
        continue

    footer_links = card.select("footer a")
    jobs.append({
        "title": title,
        "company": card.select_one("h3.company").text.strip(),
        "location": card.select_one("p.location").text.strip(),
        "date_posted": card.select_one("time").text.strip(),
        "apply_link": footer_links[-1]["href"] if footer_links else "",
    })

print(f"Found {len(jobs)} matching jobs")

#-----save results
with open("jobs.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["title", "company", "location", "date_posted", "apply_link"])
    writer.writeheader()
    writer.writerows(jobs)

print("Saved jobs.csv")