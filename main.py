
#Python

from typing import Optional
from fastapi.datastructures import Default
from fastapi.param_functions import Path, Query

#Pydantic
from pydantic import BaseModel

#FastAPI
from fastapi import FastAPI
from fastapi import Body, Query, Path

app = FastAPI()


#Models
class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    hair_color: Optional[str] = None
    is_married: Optional[bool] = None

    #Ejemplo por defecto en el body
    class Config:
        schema_extra = {
            "example":{
                "first_name":"sergio",
                "last_name": "Rubiano",
                "age":17,
                "hair_color":"black",
                "is_married":True
            }
        }

@app.get("/")
def home():
    return {
        "Hello":"world"
    }


@app.post("/person/new")
def create_person(person: Person = Body(...)):
    return person


#Query Parameters

@app.get("/person/detail")
def show_person(
    name: Optional[str] = Query(
        None, 
        min_length=1, 
        max_length=50,
        title="Person Name",
        description="This is the person name. It's between 1 and 50 characters"
        ),
    age: str = Query(
        ...,
        title="Person Age",
        description="This is the person age. It's required"
    )
):
    return {name : age}


# Validaciones: Path parameters
@app.get("/person/detail/{person_id}")
def show_person(
    person_id: int = Path(
        ...,
        gt=0
        ),
):
    return {person_id: "It exists!"}

