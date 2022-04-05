import asyncpg


class UserPostgresService:

    def __init__(self, url, table_name):
        self.url = url
        self.connection = None
        self.table_name = table_name

    async def __crate_table_users(self):
        await self.connection.execute(f'''
            CREATE TABLE IF NOT EXISTS {self.table_name} (
            user_id serial PRIMARY KEY,
            username VARCHAR( 255 ) NOT NULL,
            surname VARCHAR( 255 ) NOT NULL,
            age serial
            )
        ''')

    async def connect(self):
        self.connection = await asyncpg.connect(self.url)
        await self.__crate_table_users()

    async def disconnect(self):
        await self.connection.close()

    async def create_user(self, username: str, surname: str, age: int):
        await self.connection.execute(f'''
                INSERT INTO {self.table_name} (username, surname, age)
                VALUES ($1, $2, $3);
            ''', username, surname, age)

    async def get_users(self):
        users = await self.connection.fetch(
                f'select * from {self.table_name}'
        )
        return users

    async def get_user_by_id(self, user_id: int):
        user = await self.connection.fetchrow(
                f'select * from {self.table_name} where user_id={user_id};'
        )
        return user

    async def update_user_by_id(self, username: str):
        await self.connection.execute(
            f'''UPDATE {self.table_name} SET {username} ;'''
        )

    async def delete_user(self, user_id: int):
        await self.connection.execute(f'''
            DELETE FROM {self.table_name}
            WHERE {user_id};
        ''')


connection_url = "postgresql://postgres:postgres@127.0.0.1:5432/postgres"
user_service = UserPostgresService(connection_url, table_name='users')
