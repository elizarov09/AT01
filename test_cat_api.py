# test_cat_api.py
import pytest
from unittest.mock import patch
import requests
from cat_api import get_random_cat_image


def test_get_random_cat_image_success():
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [{"url": "https://cdn2.thecatapi.com/images/abc.jpg"}]

        result = get_random_cat_image()
        assert result == "https://cdn2.thecatapi.com/images/abc.jpg"


def test_get_random_cat_image_failure():
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 404
        mock_get.return_value.json.return_value = []
        mock_get.return_value.raise_for_status.side_effect = requests.exceptions.HTTPError

        result = get_random_cat_image()
        assert result is None


if __name__ == "__main__":
    pytest.main()
