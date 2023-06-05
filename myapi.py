from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/")
def index():
    return {"name": "first data"}


# endpoint parameters => used to return data relating to and input in the endpoint
students = {
    1: {'name': 'John', 'age': 17, 'class': 'XII'},
    2: {'name': 'Sayak', 'age': 22, 'class': 'BTech'},
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
# 37:38
