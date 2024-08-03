import redis
import json

class Cache:
    def __init__(self, host='localhost', port=7000, db=0):
        self.client = redis.Redis(host=host, port=port, db=db)

    def get_product(self, product_title: str):
        return self.client.get(product_title)

    def set_product(self, product_title: str, product: dict):
        self.client.set(product_title, json.dumps(product))
