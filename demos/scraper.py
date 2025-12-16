import requests
from bs4 import BeautifulSoup
import pandas as pd

# Target site (replace with your own)
url = "https://quotes.toscrape.com/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Extract quotes and authors
quotes = []
for quote_block in soup.find_all("div", class_="quote"):
    text = quote_block.find("span", class_="text").get_text()
    author = quote_block.find("small", class_="author").get_text()
    quotes.append({"quote": text, "author": author})

# Convert to DataFrame
df = pd.DataFrame(quotes)
print(df.head())

# Save to CSV
df.to_csv("quotes_scraped.csv", index=False)