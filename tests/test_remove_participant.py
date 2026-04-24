from tests.conftest import *


def test_remove_participant_successfully(client):
    # Arrange
    activity = "Chess Club"
    email = "michael@mergington.edu"  # pre-seeded participant

    # Act
    response = client.delete(f"/activities/{activity}/participants?email={email}")

    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == f"Unregistered {email} from {activity}"


def test_remove_participant_no_longer_in_activity(client):
    # Arrange
    activity = "Chess Club"
    email = "michael@mergington.edu"  # pre-seeded participant

    # Act
    client.delete(f"/activities/{activity}/participants?email={email}")

    # Assert
    activities_response = client.get("/activities")
    participants = activities_response.json()[activity]["participants"]
    assert email not in participants


def test_remove_participant_rejects_unknown_activity(client):
    # Arrange
    activity = "Nonexistent Club"
    email = "student@mergington.edu"

    # Act
    response = client.delete(f"/activities/{activity}/participants?email={email}")

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_remove_participant_rejects_non_member(client):
    # Arrange
    activity = "Chess Club"
    email = "notamember@mergington.edu"

    # Act
    response = client.delete(f"/activities/{activity}/participants?email={email}")

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Student is not signed up for this activity"
