import pandas as pd

df = pd.read_csv("business_full_details.csv", encoding="utf-8", on_bad_lines='skip')

for col in df.columns:
    df[col] = df[col].astype(str).str.encode('utf-8', 'ignore').str.decode('utf-8', 'ignore')
    df[col] = df[col].str.replace(r'[^\x00-\x7F]+', ' ', regex=True)  # remove non-ASCII chars
    df[col] = df[col].str.replace(r'\s+', ' ', regex=True).str.strip()  # normalize whitespace
df = df[df['Business_Name'].notna() & df['Business_Name'].str.strip().ne('')]

# Save cleaned file
df.to_csv("cleaned_business_details.csv", index=False, encoding='utf-8-sig')
print("Cleaned and re-saved.")
