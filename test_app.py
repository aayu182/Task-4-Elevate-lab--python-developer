```python
import json
from app import app




def test_home():
client = app.test_client()
res = client.get('/')
assert res.status_code == 200
assert 'Flask User API' in res.get_json().get('message')

def test_create_get_delete_user():
client = app.test_client()


# create
payload = {"name": "TestUser", "email": "test@example.com"}
r = client.post('/users', json=payload)
assert r.status_code == 201
user = r.get_json()
uid = user['id']


# get
r2 = client.get(f'/users/{uid}')
assert r2.status_code == 200
assert r2.get_json()['email'] == payload['email']


# delete
r3 = client.delete(f'/users/{uid}')
assert r3.status_code == 200


# now not found
r4 = client.get(f'/users/{uid}')
assert r4.status_code == 404
