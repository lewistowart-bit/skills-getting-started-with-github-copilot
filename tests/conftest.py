import copy
import pytest
from fastapi.testclient import TestClient
import src.app as app_module
from src.app import app

ORIGINAL_ACTIVITIES = copy.deepcopy(app_module.activities)


@pytest.fixture
def client():
    app_module.activities = copy.deepcopy(ORIGINAL_ACTIVITIES)
    return TestClient(app, follow_redirects=False)
