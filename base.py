from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

# Create engine.
engine = create_engine('sqlite:///sports_sales.db', echo=True)
Base = declarative_base()
