import requests
from bs4 import BeautifulSoup

URL = "PRODUCT_URL"
TARGET = 299.99

html = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"}).text
soup = BeautifulSoup(html, "html.parser")

price = float(soup.select_one(".price").text.replace("$", ""))

if price <= TARGET:
    print(f"🔥 Price dropped to ${price}")
