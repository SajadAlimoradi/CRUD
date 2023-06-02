import toml
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

config = toml.load('settings.toml')

db_host: str = config['database']['DB_HOST']
db_name: str = config['database']['DB_NAME']
db_user: str = config['database']['DB_USER']
db_password: str = config['database']['DB_PASSWORD']


# Create the engine
engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}/{db_name}') # noqa
# Define the base class for models
Base: declarative_base = declarative_base()
