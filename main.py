from fastapi import FastAPI
import asyncpg
from create import router

DATABASE_URL = "postgresql://postgres:postgres@127.0.0.1:5432/postgres"

app = FastAPI()
app.include_router(router)


async def create_user():
    conn = await asyncpg.connect(DATABASE_URL)
    await conn('''
        CREATE TABLE postgres(                  
            id serial PRIMARY KEY,
            name text
        )
    ''')                                            #Не создается, табличка. Использую Dbever. Почему?
    await conn.execute('''
            INSERT INTO users(name) VALUES($1)
        ''', 'Bob')

    await conn.close()
