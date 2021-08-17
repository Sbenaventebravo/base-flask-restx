import pytest
from app import app 


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_entity_list(client):
    response = client.get("/v1/entity")
    data = response.json
    assert data == {"items": [], "count": 0}

def test_get_entity(client):
    entity_id = "id"
    response = client.get(f"/v1/entity/{entity_id}")
    data = response.json
    assert data == {
        'message': 'The requested URL was not found on the server.'
        ' If you entered the URL manually please check your spelling and try again.'
        ' You have requested this URI [/v1/entity/id] but did you mean'
        ' /v1/entity/<string:id> or /v1/entity ?'
        }

def test_put_entity(client):
    entity_id = "id"
    response = client.put(f"/v1/entity/{entity_id}")
    data = response.json
    assert data == {
        'message': 'The requested URL was not found on the server.'
        ' If you entered the URL manually please check your spelling and try again.'
        ' You have requested this URI [/v1/entity/id] but did you mean'
        ' /v1/entity/<string:id> or /v1/entity ?'
    }

def test_delete_entity(client):
    entity_id = "id"
    response = client.delete(f"/v1/entity/{entity_id}")
    data = response.json
    assert data == {
        'message': 'The requested URL was not found on the server.'
        ' If you entered the URL manually please check your spelling and try again.'
        ' You have requested this URI [/v1/entity/id] but did you mean'
        ' /v1/entity/<string:id> or /v1/entity ?'
    }