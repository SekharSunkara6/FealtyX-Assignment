# Student CRUD API with FastAPI

This project is a simple REST API built with **FastAPI** for managing student records.  
It supports basic CRUD (Create, Read, Update, Delete) operations and uses in-memory storage.

## Features

- Create, read, update, and delete student records
- Input validation using Pydantic
- Thread-safe in-memory storage
- Interactive API documentation (Swagger UI)
- Easy local setup

## Requirements

- Python 3.8+
- pip (Python package manager)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/SekharSunkara6/FealtyX-Assignment.git
cd your-repo-name
```

### 2. (Optional) Create and Activate a Virtual Environment

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Server

```bash
uvicorn main:app --reload
```

The server will start at:  
[http://127.0.0.1:8000](http://127.0.0.1:8000)

## API Documentation

Once the server is running, open your browser and go to:

- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

You can use these pages to interact with and test all API endpoints.

## API Endpoints

| Method | Endpoint                     | Description              |
|--------|------------------------------|--------------------------|
| POST   | `/students`                  | Create a new student     |
| GET    | `/students`                  | Get all students         |
| GET    | `/students/{id}`             | Get a student by ID      |
| PUT    | `/students/{id}`             | Update a student by ID   |
| DELETE | `/students/{id}`             | Delete a student by ID   |
| GET    | `/students/{id}/summary`     | Get AI summary (if implemented) |

## Example Requests

**Create a student (POST /students):**
```json
{
  "id": 1,
  "name": "Alice",
  "age": 21,
  "email": "alice@example.com"
}
```

**Update a student (PUT /students/1):**
```json
{
  "id": 1,
  "name": "Alice Smith",
  "age": 22,
  "email": "alice.smith@example.com"
}
```

## Notes

- All data is stored in memory and will be lost when the server stops.
- Use `/docs` for interactive testing.
- If you see a message like `{ "message": "Student API is running!" }` at the root URL, your API is running correctly.

## Project Structure

```
your-repo-name/
│
├── main.py
├── requirements.txt
└── README.md
```

## License

This project is for educational purposes.

**Replace `https://github.com/SekharSunkara6/FealtyX-Assignment.git` with your actual GitHub username and repository name if needed.**
