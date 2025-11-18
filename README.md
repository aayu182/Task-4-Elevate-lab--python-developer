# Flask User API


Simple REST API built with Flask for managing users (in-memory store).


## Endpoints


- `GET /` — health check
- `GET /users` — list all users
- `GET /users/<id>` — get a single user
- `POST /users` — create a user (JSON: {"name": "..", "email": ".."})
- `PUT /users/<id>` — update user (JSON with any of name/email/meta)
- `DELETE /users/<id>` — delete user


## Run locally


```bash
python3 -m venv venv
source venv/bin/activate # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python app.py
CURL EXAMPLE
Create user:

curl -X POST http://127.0.0.1:5000/users \
  -H 'Content-Type: application/json' \
  -d '{"name": "Bob", "email": "bob@example.com"}'

Get all users:

curl http://127.0.0.1:5000/users
