Ye updated professional README.md hai — isko pura copy karke apni `README.md` file me paste kar do.

# Team Project Planner API

## About the Project

This is a backend project built using Django for managing a simple team project planning system.

The application allows management of users, teams, boards, and tasks through REST APIs.

Instead of using a database, local JSON files are used for persistence. This keeps the application lightweight and focuses mainly on backend logic, modular architecture, validation, and API implementation.

The project is designed with clean code structure, proper error handling, and scalable architecture.

---

## Features

* User Management

  * Create user
  * Get users
  * Delete user

* Team Management

  * Create team
  * Add users to teams
  * Get teams

* Board Management

  * Create boards under teams
  * Get boards

* Task Management

  * Create tasks
  * Assign tasks to users
  * Update task status
  * Get tasks

* File-based persistence using JSON files

* Proper validation and exception handling

* Modular project structure

---

## Tech Stack

* Python
* Django
* JSON File Storage
* REST APIs

---

## Project Architecture

The project follows a modular layered architecture:

views → services → storage layer

* views.py → Handles API requests and responses
* services → Contains business logic
* storage layer → Handles JSON file read/write operations

---

## Project Structure

project/
│── api/
│   │── views.py
│   │── urls.py
│   │── services/
│   │── storage/
│
│── db/
│   │── users.json
│   │── teams.json
│   │── boards.json
│   │── tasks.json
│
│── manage.py
│── requirements.txt
│── README.md

---

## Modules

### User Module

* Create user
* Get all users
* Delete user

### Team Module

* Create team
* Add users to team
* Get teams

### Board Module

* Create board linked to a team
* Get boards

### Task Module

* Create task linked to board and user
* Get tasks
* Update task status

---

## Data Storage

All application data is stored locally inside the `db/` folder using JSON files.

Files used:

* users.json
* teams.json
* boards.json
* tasks.json

No external database is used.

---

## Sample APIs

### Create User

POST /api/users/create/

### Create Team

POST /api/teams/create/

### Create Board

POST /api/boards/create/

### Create Task

POST /api/tasks/create/

### Update Task Status

PUT /api/tasks/update-status/

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

* Missing required fields
* Invalid IDs
* Duplicate entries
* Invalid task status
* Non-existing resources

All errors are returned in JSON format with proper messages.

---

## Design Choice

I used JSON file storage instead of a database because the assignment mainly focused on backend logic and local persistence.

This approach keeps the project lightweight, easy to test, and independent from database configuration while still maintaining structured data handling.

---

## How to Run

### 1. Install Dependencies

pip install -r requirements.txt

### 2. Run Server

python manage.py runserver

### 3. Open APIs

[http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/)

Use Postman or browser to test the APIs.

---

## Assumptions

* IDs are auto-generated
* Each team can contain multiple users
* Each task belongs to one board
* Each task is assigned to one user
* Data is persisted locally using JSON files

---

## Future Improvements

* Authentication & Authorization
* Task priority and deadlines
* Pagination and filtering
* Unit testing
* Docker support
* Database integration (PostgreSQL/MySQL)

---

## Conclusion

This project helped me understand backend API development, modular architecture, validation handling, file-based persistence, and clean code organization using Django.

The focus was on building scalable and maintainable APIs while keeping the implementation simple and efficient.
