import requests
import pytest

@pytest.mark.rest_api
def test_dueckduckgo_api():

    # Arrange
    url = 'https://api.duckduckgo.com/?q=dark+souls&format=json'

    # Act
    response = requests.get(url)
    body = response.json()

    # Assert
    assert response.status_code == 200

    print(body['AbstractText'])
    assert 'Dark Souls' in body['AbstractText']