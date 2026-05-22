# Team Project Planner API

## About the Project
This is a backend project built using Django for managing a simple team project planning system.  
It allows creation and management of users, teams, boards, and tasks using REST APIs.

Instead of using a database, I have used local JSON files for data storage. This helps in keeping the system simple and easy to understand while focusing on backend logic and API design.

The main goal of this project is to build clean, modular, and scalable APIs with proper validation, error handling, and file-based persistence.

---

## Features

- User management (create, get, delete users)
- Team management (create teams, add users to teams)
- Board management (create boards under teams)
- Task management (create and manage tasks)
- Task status update (todo → in_progress → done)
- File-based data persistence using JSON files
- Proper validation and error handling in all APIs

---

## Tech Stack

- Python
- Django
- JSON file storage (no database)
- Django HTTP request handling

---

## Project Architecture

The project follows a modular structure:

views → API layer → file storage (db folder)

- views.py → Handles HTTP requests
- API layer → Contains business logic (user, team, board, task)
- storage layer → Handles JSON file read/write operations

---

## Modules

### User Module
- Create user
- Get all users
- Delete user

### Team Module
- Create team
- Get teams
- Add user to team

### Board Module
- Create board linked to team
- Get boards

### Task Module
- Create task linked to board and user
- Get tasks
- Update task status

---

## Data Storage

All data is stored in the `db/` folder as JSON files:

- users.json
- teams.json
- boards.json
- tasks.json

No external database is used in this project.

---

## API Flow

1. Create Users  
2. Create Teams  
3. Add Users to Teams  
4. Create Boards  
5. Create Tasks  
6. Update Task Status  

---

## Error Handling

The application handles:
- Missing required fields
- Invalid IDs
- Duplicate entries
- Non-existing resources

All errors are returned in JSON format.

---

## How to Run

1. Install dependencies:


pip install -r requirements.txt


2. Run server:

python manage.py runserver


3. Open APIs in browser or Postman:

http://127.0.0.1:8000/api/


---

## Assumptions

- IDs are auto-generated
- Each team can have multiple users
- Each task belongs to one board and one user
- Data is stored locally using JSON files

---

## Conclusion

This project helped me understand backend API development, modular architecture, and f
