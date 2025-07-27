from bs4 import BeautifulSoup
import os
import pandas as pd

results = []

for filename in os.listdir("details"):
    if not filename.endswith(".html"):
        continue

    path = os.path.join("details", filename)
    with open(path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "lxml")

    h1 = soup.find("h1", class_="back-to")
    if not h1:
        continue

    # Business Name
    business_name = h1.contents[0].strip()

    # Last Updated Date
    last_verified_span = h1.find("span", class_="last-verified")
    last_updated = last_verified_span.get_text(strip=True).replace("Updated ", "") if last_verified_span else ""

    # Street Address
    address_tags = soup.select("div.contact p.addr")
    street_address = ", ".join(tag.get_text(strip=True) for tag in address_tags if tag.get_text(strip=True))

    # Materials Accepted
    material_spans = soup.select("table.materials-accepted td.material-name span.material")
    materials_accepted = [span.get_text(strip=True).replace("﻿", " ") for span in material_spans]
    materials_accepted_str = ", ".join(materials_accepted)

    results.append({
        "Business_Name": business_name,
        "Last_Updated": last_updated,
        "Street_Address": street_address,
        "Materials_Accepted": materials_accepted_str,
    })

df = pd.DataFrame(results)
df.to_csv("business_full_details.csv", index=False, encoding="utf-8-sig")
print(" Extracted Business Name, Last Updated, Address, and Materials Accepted.")
