from fastapi import APIRouter
from pydantic import BaseModel
from UserPostgresService import user_service

router = APIRouter(
    prefix="/CRUD",
    tags=["CRUD"]
)


class UserModel(BaseModel):
    username: str
    surname: str
    age: int


class UserModelId(BaseModel):
    user_id: int


class UserModelUpdate(BaseModel):
    username: str


# Использую Postman для тестирование API

@router.post("/create")
async def create_user(db: UserModel):
    await user_service.create_user(db.username, db.surname, db.age)


@router.get("/get_users")  # ALL
async def get_users():
    response = await user_service.get_users()
    print(response)
    return response


@router.get("/get_user/{id}")
async def get_user_by_id(user_id):
    user = await user_service.get_user_by_id(user_id)
    return user


@router.put("/update")
async def update_user(db: UserModelUpdate):
    await user_service.update_user_by_id(db)


@router.delete("/delete")
async def delete_user_id(db: UserModelId):
    await user_service.delete_user(db)
