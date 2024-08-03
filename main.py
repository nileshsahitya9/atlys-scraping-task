from fastapi import FastAPI, Depends
from scraper import Scraper
from storage import Storage
from cache import Cache
from notifications import Notifier
from auth import authenticate

app = FastAPI()

@app.post("/scrape/")
def scrape(limit: int = 5, proxy: str = None, token: str = Depends(authenticate)):
    scraper = Scraper(base_url="https://dentalstall.com/shop/", proxies={'http': proxy, 'https': proxy})
    storage = Storage(file_path="products.json")
    cache = Cache()
    
    products = scraper.scrape_pages(limit)
    print(products)
    
    for product in products:
        cached_product = cache.get_product(product.product_title)
        if not cached_product or cached_product['product_price'] != product.product_price:
            storage.save_products(products)
            cache.set_product(product.product_title, product.dict())
    
    Notifier.notify(f"Scraped {len(products)} products.")

    return {"status": "success", "products_scraped": len(products)}
