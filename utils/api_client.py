import requests
import yaml
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class APIClient:
    
    def __init__(self):
        with open("config/config.yaml") as f:
            config = yaml.safe_load(f)
        self.base_url = config["base_url"]
        self.headers = {}
        self.endpoints = config["endpoints"]

    def set_headers(self, headers_dict):
        self.headers.update(headers_dict)

    def get(self, endpoint):
        logging.info(f"Sending request to: {self.base_url + endpoint}")
        return requests.get(self.base_url + endpoint, headers=self.headers)

