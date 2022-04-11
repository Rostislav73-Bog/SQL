from dependency_injector import containers, providers
from UserPostgresService import UserPostgresService


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    user_client = providers.Singleton(
        UserPostgresService,
        url=config.postgres.host,
        table_name=config.postgres.table_name
    )

