import copy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture(autouse=True)
def reset_activities_state():
    """Keep tests isolated by restoring in-memory activity data."""
    # Arrange
    original_state = copy.deepcopy(activities)

    yield

    # Assert cleanup
    activities.clear()
    activities.update(original_state)


@pytest.fixture
def client():
    return TestClient(app)
