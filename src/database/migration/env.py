from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool, create_engine
from sqlalchemy.orm import sessionmaker
import configparser
from src.models.users import User
from alembic import context

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
from src.models.base import Base
target_metadata = Base.metadata
# target_metadata = None

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


# tạo 1 tài khoản mặc định
def seeder_user():
    config = configparser.ConfigParser()
    config.read("alembic.ini")
    db_url = config.get("alembic", "sqlalchemy.url")
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    connection = None
    session = None
    try:
        # tạo 1 tài khoản mặc định
        connection = engine.connect()
        session = Session()
        session.add(User(username='0912229762', name='admin', password='1'))
        session.commit()

    except Exception as E:

        print("Không thể kết nối được database")

    finally:
        connection.close()
        session.close()

if context.is_offline_mode():
    run_migrations_offline()
    seeder_user()
else:
    run_migrations_online()
    seeder_user()