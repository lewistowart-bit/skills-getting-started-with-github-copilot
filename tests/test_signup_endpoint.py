from tests.conftest import *


def test_signup_adds_participant_successfully(client):
    # Arrange
    activity = "Chess Club"
    email = "newstudent@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == f"Signed up {email} for {activity}"


def test_signup_participant_appears_in_activity(client):
    # Arrange
    activity = "Chess Club"
    email = "newstudent@mergington.edu"

    # Act
    client.post(f"/activities/{activity}/signup?email={email}")

    # Assert
    activities_response = client.get("/activities")
    participants = activities_response.json()[activity]["participants"]
    assert email in participants


def test_signup_rejects_unknown_activity(client):
    # Arrange
    activity = "Nonexistent Club"
    email = "student@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_signup_rejects_duplicate_email(client):
    # Arrange
    activity = "Chess Club"
    email = "duplicate@mergington.edu"
    client.post(f"/activities/{activity}/signup?email={email}")

    # Act
    response = client.post(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert response.status_code == 400
    assert response.json()["detail"] == "Student already signed up for this activity"
