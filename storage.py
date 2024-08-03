import json
from typing import List
from models import Product

class Storage:
    def __init__(self, file_path: str):
        self.file_path = file_path
    
    def save_products(self, products: List[Product]):
        with open(self.file_path, 'w') as f:
            json.dump([product.dict() for product in products], f)
    
    def load_products(self) -> List[Product]:
        with open(self.file_path, 'r') as f:
            return [Product(**prod) for prod in json.load(f)]