import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_table(url, table_selector="table"):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the first table
    table = soup.select_one(table_selector)
    rows = []
    if table:
        for row in table.find_all("tr"):
            cols = [col.get_text(strip=True) for col in row.find_all(["td", "th"])]
            if cols:
                rows.append(cols)

    # Convert to DataFrame
    df = pd.DataFrame(rows[1:], columns=rows[0])  # first row as header
    return df

if __name__ == "__main__":
    url = "https://www.contextures.com/xlSampleData01.html"  # sample site with table
    df = scrape_table(url)
    print(df.head())

    # Save to CSV
    df.to_csv("scraped_table.csv", index=False)
    print("Data saved to scraped_table.csv")