import yaml
from utils.api_client import APIClient


class Helpers:

    def getHeaders(self):
        headers = {"Content-Type": "application/json", "x-api-key": "reqres-free-v1"}
        return headers

    def getEndPoint(self, endpoint_key):
        client = APIClient()
        endpoint_path = client.returnEndpoints().get(endpoint_key)
        return endpoint_path

    def getAddUserReqBody(self, name, age):
        data = {"name": name, "job": age}
        return data
