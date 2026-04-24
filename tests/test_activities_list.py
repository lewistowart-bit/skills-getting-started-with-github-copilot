from tests.conftest import *


def test_get_activities_returns_200(client):
    # Arrange
    url = "/activities"

    # Act
    response = client.get(url)

    # Assert
    assert response.status_code == 200


def test_get_activities_returns_all_activities(client):
    # Arrange
    url = "/activities"

    # Act
    response = client.get(url)

    # Assert
    data = response.json()
    assert len(data) == 9


def test_get_activities_each_has_required_fields(client):
    # Arrange
    url = "/activities"
    required_fields = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get(url)

    # Assert
    data = response.json()
    for activity in data.values():
        assert required_fields.issubset(activity.keys())


def test_get_activities_participants_are_lists(client):
    # Arrange
    url = "/activities"

    # Act
    response = client.get(url)

    # Assert
    data = response.json()
    for activity in data.values():
        assert isinstance(activity["participants"], list)
