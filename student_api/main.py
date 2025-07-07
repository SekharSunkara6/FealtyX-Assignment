from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from threading import Lock
import requests

# In-memory storage and lock for thread safety
students = {}
students_lock = Lock()

# Student model
class Student(BaseModel):
    id: int
    name: str
    age: int
    email: EmailStr

app = FastAPI()

@app.post("/students")
def create_student(student: Student):
    with students_lock:
        if student.id in students:
            raise HTTPException(status_code=400, detail="Student ID already exists")
        students[student.id] = student
    return student

@app.get("/students")
def get_all_students():
    with students_lock:
        return list(students.values())

@app.get("/students/{student_id}")
def get_student(student_id: int):
    with students_lock:
        student = students.get(student_id)
        if not student:
            raise HTTPException(status_code=404, detail="Student not found")
        return student

@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: Student):
    with students_lock:
        if student_id not in students:
            raise HTTPException(status_code=404, detail="Student not found")
        if updated_student.id != student_id:
            raise HTTPException(status_code=400, detail="ID in path and body must match")
        students[student_id] = updated_student
    return updated_student

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    with students_lock:
        if student_id not in students:
            raise HTTPException(status_code=404, detail="Student not found")
        del students[student_id]
    return {"detail": "Student deleted"}

def get_student_summary(student):
    prompt = f"Summarize the following student profile:\nName: {student.name}\nAge: {student.age}\nEmail: {student.email}"
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt
        }
    )
    if response.status_code == 200:
        return response.json().get("response", "")
    else:
        return "Failed to generate summary."

@app.get("/students/{student_id}/summary")
def student_summary(student_id: int):
    with students_lock:
        student = students.get(student_id)
        if not student:
            raise HTTPException(status_code=404, detail="Student not found")
    summary = get_student_summary(student)
    return {"summary": summary}


@app.get("/")
def read_root():
    return {"message": "Student API is running!"}
