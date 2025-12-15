import requests
from bs4 import BeautifulSoup
import pandas as pd

base = "http://quotes.toscrape.com"

df = pd.read_csv("quotes.csv")

birth_dates = []
birth_locations = []

with requests.Session() as s:
    for rel_url in df["author_url"]:
        author_url = rel_url if rel_url.startswith("http") else base + rel_url
        r = s.get(author_url, timeout=15)
        soup = BeautifulSoup(r.text, "html.parser")

        bd_tag = soup.find("span", class_="author-born-date")
        bl_tag = soup.find("span", class_="author-born-location")

        birth_dates.append(bd_tag.get_text(strip=True) if bd_tag else "")
        birth_locations.append(bl_tag.get_text(strip=True) if bl_tag else "")

df["birth_date"] = birth_dates
df["birth_location"] = birth_locations

df["length"] = df["quote"].apply(len)

df.to_csv("quotes.csv", index=False)

shortest = df.loc[df["length"].idxmin()]
longest = df.loc[df["length"].idxmax()]
print("Shortest Quote:", shortest["quote"])
print("Longest Quote:", longest["quote"])
