# To-Do List API

## Objective
Create a basic To-Do list API using Django and Django Rest Framework (DRF) that supports basic CRUD operations (Create, Read, Update, Delete) for tasks.

## Features
- Create Task
- Retrieve Task List
- Retrieve Single Task
- Update Task
- Delete Task
- Filter tasks due today

### Endpoints
- **Create Task**: `POST /api/tasks/`
- **Retrieve Task List**: `GET /api/tasks/`
- **Retrieve Single Task**: `GET /api/tasks/<id>/`
- **Update Task**: `PUT/PATCH /api/tasks/<id>/`
- **Delete Task**: `DELETE /api/tasks/<id>/`
- **Tasks Due Today**: `GET /api/tasks/due-today/`

### Validations
1. Ensure the title is not empty.
2. If provided, `due_date` should be a future date.

## Setup Instructions

1. Clone the repository:
    ```sh
    git clone git@github.com:ankit-royal/django-todo-api.git
    cd django-todo-api
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv .venv
    ```
    ```sh
    .venv\Scripts\activate  # On Windows
    source venv/bin/activate  # On Linux and Mac
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Run the server:
    ```sh
    python manage.py runserver
    ```
