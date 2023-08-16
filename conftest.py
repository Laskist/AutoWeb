import pytest
import requests
import yaml

with open("config.yaml") as f:
    data = yaml.safe_load(f)


@pytest.fixture()
def get_token_auth():
    params = {
        "username": data["username"],
        "password": data["password"]
    }
    r = requests.post(url=data["url"], data=params)
    return r.json()["token"]
