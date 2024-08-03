import requests
from bs4 import BeautifulSoup
from typing import List
from models import Product

class Scraper:
    def __init__(self, base_url: str, proxies: dict = None):
        self.base_url = base_url
        self.proxies = proxies
    
    def scrape_page(self, page_num: int) -> List[Product]:
        url = f"{self.base_url}?page={page_num}"
        response = requests.get(url, proxies=self.proxies)
        soup = BeautifulSoup(response.text, 'html.parser')

        
        products = []
        for item in soup.find_all('li', class_='product'):
            title = item.find('h2', class_='woo-loop-product__title').text.strip()
            price = float(item.find('span', class_='woocommerce-Price-amount amount').text.strip().replace('₹', '').replace(',', ''))
            img_url = item.find('img')['src']
            
            products.append(Product(product_title=title, product_price=price, path_to_image=img_url))
        
        return products

    def scrape_pages(self, limit: int) -> List[Product]:
        print("limit", limit)
        all_products = []
        for i in range(1, limit + 1):
            all_products.extend(self.scrape_page(i))
        return all_products