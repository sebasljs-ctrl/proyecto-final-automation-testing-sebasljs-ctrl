import pytest
import requests

from utils.config import API_BASE_URL
from utils.data_reader import read_json
from utils.logger import get_logger


logger = get_logger(__name__)


@pytest.mark.api
def test_api_get():
    logger.info("Requesting existing and non existing posts")
    response = requests.get(f"{API_BASE_URL}/posts/1", timeout=10)
    body = response.json()

    assert response.status_code == 200
    assert body["id"] == 1
    assert "title" in body
    assert "body" in body

    error_response = requests.get(f"{API_BASE_URL}/posts/999999", timeout=10)
    assert error_response.status_code == 404


@pytest.mark.api
def test_api_post():
    payload = read_json("api_payloads.json")["new_post"]
    logger.info("Creating post with API")
    response = requests.post(f"{API_BASE_URL}/posts", json=payload, timeout=10)
    body = response.json()

    assert response.status_code == 201
    assert body["title"] == payload["title"]
    assert body["body"] == payload["body"]
    assert body["userId"] == payload["userId"]
    assert "id" in body


@pytest.mark.api
def test_api_delete():
    logger.info("Deleting post with API")
    response = requests.delete(f"{API_BASE_URL}/posts/1", timeout=10)

    assert response.status_code == 200
