

```python
from flask import Flask, request, jsonify, abort
from users_store import UsersStore
from config import DEFAULT_HOST, DEFAULT_PORT

app = Flask(__name__)
store = UsersStore()

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Flask User API is running"}), 200

@app.route('/users', methods=['GET'])
def get_users():
    """Return list of all users"""
    return jsonify(list(store.all().values())), 200

@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = store.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user), 200

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json(force=True, silent=True)
    if not data:
        return jsonify({"error": "Invalid or missing JSON"}), 400

    # basic validation
    name = data.get('name')
    email = data.get('email')
    if not name or not email:
        return jsonify({"error": "'name' and 'email' are required"}), 400

    user = store.create({"name": name, "email": email, "meta": data.get('meta', {})})
    return jsonify(user), 201

@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json(force=True, silent=True)
    if not data:
        return jsonify({"error": "Invalid or missing JSON"}), 400

    user = store.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    updated = store.update(user_id, data)
    return jsonify(updated), 200

@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    deleted = store.delete(user_id)
    if not deleted:
        return jsonify({"error": "User not found"}), 404
    return jsonify({"message": "User deleted"}), 200

if __name__ == '__main__':
    app.run(host=DEFAULT_HOST, port=DEFAULT_PORT, debug=True)
```



