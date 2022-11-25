import cerberus
import pytest
import requests

from jsonschema import validate


def test_check_header(service3_jsonplaceholder_url):
    """Check the value of 'Server' parameter in headers"""
    response = requests.get(service3_jsonplaceholder_url + "posts")
    assert response.headers["Server"] == "cloudflare"


@pytest.mark.parametrize("number", ["1", "2", "3", "4", "5"])
def test_validate_json_posts(service3_jsonplaceholder_url, number):
    """Validate json in response with jsonschema"""
    response = requests.get(service3_jsonplaceholder_url + "posts/" + number)
    response_json = response.json()

    schema = {
        "type": "object",
        "properties": {
        "userId": {"type": "number"},
        "id": {"type": "number"},
        "title": {"type": "string"},
        "body": {"type": "string"}
        },
        "required": ["userId", "id", "title", "body"]
    }

    validate(instance=response_json, schema=schema)


@pytest.mark.parametrize("number", ["1", "2", "3", "4", "5"])
def test_validate_json_comments(service3_jsonplaceholder_url, number):
    """Validate json in response with Cerberus"""
    response = requests.get(service3_jsonplaceholder_url + "comments/" + number)
    response_json = response.json()

    schema = {
        "postId": {"type": "number"},
        "id": {"type": "number"},
        "name": {"type": "string"},
        "email": {"type": "string"},
        "body": {"type": "string"},
    }

    validator = cerberus.Validator()
    assert validator.validate(response_json, schema)


@pytest.mark.xfail(reason="server will not be really update posts number")
def test_delete_post(service3_jsonplaceholder_url):
    """Check the opportunity to delete a post"""
    response = requests.delete(service3_jsonplaceholder_url + "posts/1")
    all = requests.get(service3_jsonplaceholder_url + "posts")
    assert response.status_code == 200
    assert len(all.json()) == 99


def test_check_photos_number(service3_jsonplaceholder_url):
    """Check the length of elements in json response"""
    response = requests.get(service3_jsonplaceholder_url + "photos")
    assert len(response.json()) == 5000
