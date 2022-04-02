from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/CRUD",
    tags=["CRUD"]
)


class BD_Name(BaseModel):
    name: str
    surname: str
    age: int


@router.post("/create")
async def add_name(db: BD_Name):            #Использую Postman для тестирование API
    return {
        'name': db.name,
        'surname': db.surname,
        'age': db.age,
    }
