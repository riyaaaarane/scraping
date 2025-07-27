# Earth911 - scarping

We first scraped all 20 listing pages from the Earth911 website by iterating through the pagination using URL parameters (e.g., page=1, page=2, etc.). Each page was saved locally to avoid repeated server requests and ensure responsible scraping.
From these listing pages, we extracted individual business detail page URLs using BeautifulSoup, specifically targeting the <h2 class="title"> anchor tags. We then fetched each business detail page one by one and saved them locally.
From the saved detail pages, we extracted the required data:
- Business_Name
- last_update_date
- street_address
- materials_accepted

For data cleaning, we loaded the data into a Pandas DataFrame and applied the following steps:
- Converted all values to UTF-8 and removed invalid characters.
- Removed all non-ASCII characters using regex.
- Normalized extra whitespace and stripped leading/trailing spaces.
- Dropped records where Business_Name was missing or empty.

For error handling, we implemented try-except blocks while fetching web pages to handle network errors or broken links. We also used random sleep() delays between requests to avoid overloading the server and prevent potential blocking.
