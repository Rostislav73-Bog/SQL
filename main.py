from fastapi import FastAPI
import asyncpg
from create import router

DATABASE_URL = "postgresql://postgres:postgres@127.0.0.1:5432/postgres"

app = FastAPI()
app.include_router(router)


async def create_user():
    conn = await asyncpg.connect(DATABASE_URL)
    # Cоздаю таблицу
    await conn.execute('''              
        CREATE TABLE  conn.execute (  
	    user_id serial PRIMARY KEY,
	    username VARCHAR( 255 ) UNIQUE NOT NULL
        );
    ''')                    # Не создается, таблица. Использую Dbever
    await conn.execute('''
            INSERT INTO conn.execute (username)
            VALUES ("something_1");
        ''')
    # Добавлю информациб в созданную таблицу
    await conn.execute('''
                INSERT INTO count_name (username)
                VALUES ("something_1");
            ''')

    await conn.close()
