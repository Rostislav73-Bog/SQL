from fastapi import APIRouter, Depends
from pydantic import BaseModel
from UserPostgresService import UserPostgresService
from di_container import Container
from dependency_injector.wiring import inject, Provide

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
@inject
async def create_user(
    db: UserModel,
    user_client: UserPostgresService = Depends(Provide[Container.user_client])
):
    await user_client.create_user(db.username, db.surname, db.age)


@router.get("/get_users")  # ALL
@inject
async def get_users(user_client: UserPostgresService = Depends(Provide[Container.user_client])):
    response = await user_client.get_users()
    print(response)
    return response


@router.get("/get_user/{id}")
@inject
async def get_user_by_id(user_id, user_client: UserPostgresService = Depends(Provide[Container.user_client])):
    user = await user_client.get_user_by_id(user_id)
    return user


@router.put("/update")
@inject
async def update_user(db: UserModelUpdate, user_client: UserPostgresService = Depends(Provide[Container.user_client])):
    await user_client.update_user_by_id(db)


@router.delete("/delete")
@inject
async def delete_user_id(db: UserModelId, user_client: UserPostgresService = Depends(Provide[Container.user_client])):
    await user_client.delete_user(db)
