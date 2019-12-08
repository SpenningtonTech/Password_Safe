from sqlalchemy import create_engine, String, Column, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///vault.db")
session = sessionmaker(bind=engine)()
meta = MetaData()

Base = declarative_base()

Passwords = Table(
    'Passwords', meta,
    Column('website', String, primary_key=False),
    Column('password', String)
)
meta.create_all(engine)


class PassVault(Base):

    __tablename__ = 'Passwords'

    website = Column(String, primary_key=True)
    password = Column(String)

    def __init__(self, website, password):
        self.website = website
        self.password = password
