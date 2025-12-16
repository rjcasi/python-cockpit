import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def crawl_site(start_url, max_pages=5):
    visited = set()
    to_visit = [start_url]

    while to_visit and len(visited) < max_pages:
        url = to_visit.pop(0)
        if url in visited:
            continue

        print(f"Crawling: {url}")
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")

            # Extract all links
            for link in soup.find_all("a", href=True):
                full_url = urljoin(url, link['href'])
                if full_url not in visited:
                    to_visit.append(full_url)

            visited.add(url)
        except Exception as e:
            print(f"Error crawling {url}: {e}")

    return visited

if __name__ == "__main__":
    start = "https://quotes.toscrape.com/"
    crawled = crawl_site(start, max_pages=10)
    print("\nVisited pages:")
    for page in crawled:
        print(page)S