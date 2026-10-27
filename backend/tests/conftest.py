import os
from pathlib import Path

os.environ["FRIEND_TEST_DB"] = str(Path(__file__).parent / "test.db")

import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def client():
    with TestClient(app) as test_client:
        yield test_client
