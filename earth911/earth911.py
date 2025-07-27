import time
import random
from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin

base_url = "https://search.earth911.com/"
url = "https://search.earth911.com/?what=Electronics&where=10001&max_distance=100&country=US&province=NY&city=New+York&region=New+York&postal_code=10001&latitude=40.74807084035&longitude=-73.99234262099&sponsor=&list_filter=all&page=1"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

page_num = 1
while True:
    print(f"Fetching page {page_num}: {url}")
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to fetch page {page_num}, status code: {response.status_code}")
        break

    soup = BeautifulSoup(response.text, "lxml")

    with open(f"earth911_page_{page_num}.html", "w", encoding="utf-8") as f:
        f.write(response.text)

    next_link = soup.select_one("a.next")
    if not next_link or next_link.get("href") == "#":
        print("No more pages.")
        break

    next_url = urljoin(base_url, next_link.get("href"))
    url = next_url
    page_num += 1

    time.sleep(random.uniform(2, 5))



