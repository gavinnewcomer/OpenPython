import os
from typing import Tuple

import requests

class OpenSeaClient():

    def __init__(self):
        self.base_url = 'https://api.opensea.io/api/v1/'
        self.session = requests.Session()
        try:
            self.api_key = os.environ['OpenSeaClient']
        except:
            self.api_key = ''
        self.headers = ''
        if self.api_key is not None:
            self.headers = {'X-API-KEY': self.api_key}
    
    def build_url(self, params: dict, module: str) -> Tuple[bool, str]:
        owner = params.get("owner", None)
        if owner is None:
            return False, "Owner Cannot Be None"
        if module is None:
            return False, "Module Cannot Be None"
        order_by = params.get("order_by", "sale_date")
        order_direction = params.get("order_direction", "desc")
        offset = params.get("offset", 0)
        limit = abs(params.get("limit", 50))
        if limit > 50 or limit == 0:
            limit = 50
        url = f'{self.base_url}{module}/?owner={owner}&order_by={order_by}&order_direction={order_direction}&offset={str(offset)}&limit={str(limit)}'
        return True, url
    
    def get(self, url: str) -> Tuple[bool, dict]:
        response = self.session.get(url, self.headers)
        if response.status_code == 200:
            return True, response.json()
        else:
            return False, response.json()
    
    def get_address_assets(self, params: dict) -> Tuple[bool, str, list]:
        did_pass, url = self.build_url(params, "assets")
        if did_pass is False:
            return did_pass, str, {}
        request_did_succeed, response = self.get(url)
        response_parsed = response.get("assets")
        if request_did_succeed is False:
            return request_did_succeed, "request failed",response
        else:
            return request_did_succeed, "success", response
        

