from sqlalchemy import Column, String, Float
from models.base_model import BaseModel, Base

class User(BaseModel, Base):
    __tablename__ = "users"

    id = Column(String(60), primary_key=True)
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
