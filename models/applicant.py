from sqlalchemy import Column, String, Float
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel

# Create a Base class for declarative mapping
Base = declarative_base()

class Applicant(BaseModel, Base):
    """Represents an applicant for a bursary"""
    __tablename__ = "applicants"

    # Define columns
    id = Column(String(60), primary_key=True, nullable=False)  # Primary key column
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    institution = Column(String(128), nullable=False)
    course = Column(String(128), nullable=False)
    amount_requested = Column(Float, nullable=False)
