from logging.config import fileConfig
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from alembic import context
from models.employee import Base  # Import your Base from models.py
from db.connection import DATABASE_URL  # Import the correct DATABASE_URL

# This is the Alembic Config object, which provides access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
fileConfig(config.config_file_name)

# Set the target metadata to the metadata from your models
target_metadata = Base.metadata  # Assuming 'Base' is defined in your models.py

# Alembic's migration functions
def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    context.configure(
        url=DATABASE_URL,  # Use the DATABASE_URL defined in your database.py
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = create_engine(DATABASE_URL)

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
