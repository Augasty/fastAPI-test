from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def index():
    return students


# endpoint parameters => used to return data relating to and input in the endpoint
students = {
    1: {'name': 'John', 'age': 17, 'year': 'XII'},
    2: {'name': 'Sayak', 'age': 22, 'year': 'BTech'},
}

# Path Parameterspo


@app.get("/get-student/{student_id}")
def get_student(student_id: int):
    return students[student_id]

# using Path to give description, max and min value


@app.get("/get-student-2/{student_id}")
def get_student(student_id: int = Path(..., description="give the ID of the student", gt=0, lt=3)):
    return students[student_id]

# Query Parameters
# here we don't pass the query parameter in the endpoint here
@app.get("/get-by-name")
def get_student(name: str):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not found"}


# to make any input parameter optional, give a default None value
@app.get("/get-by-name-with-default")
def get_student(name: str = None):
    if not name:
        return students
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]

# non-default argument can't follow default argument
# def get_student(name: str = None, test: int):
# will throw error...
# to write non-default argument after default argument


@app.get("/get-by-name-with-default2")
def get_student(*, name: str = None, id: int):
    if not name and not id:
        return students
    for student_id in students:
        if not name:
            if student_id == id:
                return students[student_id]
        else:
            if student_id == id and students[student_id]["name"] == name:
                return students[student_id]

    return {"Data": "Not found"}

# combining path and query parameters
@app.get("/get-by-name-path-and-query/{student_id}")
def get_student(*, student_id:int, name: str = None):
    if not name and not student_id:
        return students
    for id in students:
        if not name:
            if student_id == id:
                return students[id]
        else:
            if student_id == id and students[id]["name"] == name:
                return students[id]

    return {"Data": "Not found"}


# post methods
class Student_class(BaseModel):
    name: Optional[str] 
    age: Optional[int] 
    year: Optional[str]


@app.post('/create-student/{student_id}')
def create_student(student_id: int, student_class: Student_class):
    if student_id in students:
        return {"error":"student exists"}
    students[student_id] = student_class
    return students[student_id]


# put request
# to make put request work, create data with post request, and then UPDATE THAT CREATED DATA
@app.put('/update-student/{student_id}')
def update_student(student_id: int, student_class: Student_class):
    if student_id not in students:
        return {"error":"student doesn't exist"}
    if student_class.name != None:
        students[student_id].name = student_class.name
    if student_class.age != None:
        students[student_id].age = student_class.age
    if student_class.year != None:
        students[student_id].year = student_class.year
    return students[student_id]    


#  delete request
@app.delete('/delete-student/{student_id}')
def delete_student(student_id: int):
    if student_id not in students:
        return {"error":"student doesn't exists"}
    del students[student_id]
    return {"Message": "Student deleted successfully"}