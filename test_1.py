import requests
import yaml

with open("config.yaml") as f:
    data = yaml.safe_load(f)


def test_post_presence(get_token_auth):
    header = {
        "X-Auth-Token": get_token_auth
    }
    body = {
        "owner": "notMe"
    }
    r = requests.get(data["url_api"], params=body, headers=header).json()["data"]
    name = [i["title"] for i in r]
    assert data["owner_title_name"] in name, "not found"


def test_create_new_post(get_token_auth):
    header = {
        "X-Auth-Token": get_token_auth
    }
    body = {
        "title": data["title"],
        "description": data["description"],
        "content": data["content"]
    }
    r = requests.post(data["url_api"], data=body, headers=header)
    con = requests.get(data["url_api"], data=body, headers=header).json()["data"]
    description = [i["description"] for i in con]
    assert data["description"] in description, "not created"
