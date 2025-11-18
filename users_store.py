import uuid


class UsersStore:
"""Simple in-memory user store using a dict.
Methods: all(), get(id), create(data), update(id, data), delete(id)
"""
def __init__(self):
self._users = {}


# seed with one user
uid = self._new_id()
self._users[uid] = {"id": uid, "name": "Alice", "email": "alice@example.com"}


def _new_id(self):
return str(uuid.uuid4())


def all(self):
return self._users


def get(self, user_id):
return self._users.get(user_id)


def create(self, data):
uid = self._new_id()
user = {"id": uid, **data}
self._users[uid] = user
return user


def update(self, user_id, data):
user = self._users.get(user_id)
if not user:
return None
# only overwrite allowed keys
allowed = ['name', 'email', 'meta']
for k in allowed:
if k in data:
user[k] = data[k]
self._users[user_id] = user
return user


def delete(self, user_id):
  return self._users.pop(user_id, None)
