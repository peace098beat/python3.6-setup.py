import json
import pytest

from fiblockchain.application import application

@pytest.fixture
def client():
    return application.test_client()

def test_response(client):
    result = client.get("/test")
    response_body = json.loads(result.get_data())
    assert result.status_code == 200
    assert result.headers['Content-Type'] == 'application/json'
    assert response_body['Output'] == 'Hello Test'

import sys
def test_version():
    assert sys.version_info.major == 3
