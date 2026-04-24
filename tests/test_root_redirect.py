from tests.conftest import *


def test_root_redirects_to_index(client):
    # Arrange
    url = "/"

    # Act
    response = client.get(url)

    # Assert
    assert response.status_code == 307
    assert response.headers["location"] == "/static/index.html"
