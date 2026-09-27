# Task Manager REST API

A simple REST API built with Flask, running over HTTPS.

## Endpoints
| Method | Endpoint         | Description       |
|--------|------------------|--------------------|
| GET    | /tasks           | List all tasks     |
| GET    | /tasks/<id>      | Get a single task  |
| POST   | /tasks           | Create a task      |
| PUT    | /tasks/<id>      | Update a task      |
| DELETE | /tasks/<id>      | Delete a task      |

## Run locally
\`\`\`bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python app.py
\`\`\`