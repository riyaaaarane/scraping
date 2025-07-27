from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin
import requests
import time
import random

BASE_URL = "https://search.earth911.com"
detail_urls = set()

for i in range(1, 21):  
    filename = f"earth911_page_{i}.html"
    if not os.path.exists(filename):
        print(f"{filename} not found, skipping.")
        continue

    with open(filename, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "lxml")

    for h2 in soup.select("h2.title > a"):
        href = h2.get("href")
        if href:
            base_path = href.split("?")[0]
            full_url = urljoin(BASE_URL, base_path)
            detail_urls.add(full_url)

print(f"Extracted {len(detail_urls)} unique business detail URLs.")
print(detail_urls)


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

os.makedirs("details", exist_ok=True)

for i, url in enumerate(detail_urls):
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            with open(f"details/detail_{i+1}.html", "w", encoding="utf-8") as f:
                f.write(response.text)
            print(f"Saved detail page {i+1}")
        else:
            print(f"Failed ({response.status_code}): {url}")
    except Exception as e:
        print(f"Error fetching {url}: {e}")

    time.sleep(random.uniform(2, 5))

