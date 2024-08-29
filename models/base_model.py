import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BaseModel:
    """A base class for all models with common attributes."""
    
    id = Column(String(60), primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __init__(self, *args, **kwargs):
        """Initialize the BaseModel instance."""
        if kwargs:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
    
    def save(self):
        """Save the instance to the storage."""
        from models import storage
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert model instance to dictionary."""
        dict_representation = {}
        for column in self.__table__.columns:
            dict_representation[column.name] = getattr(self, column.name)
        dict_representation['id'] = self.id
        dict_representation['created_at'] = self.created_at.isoformat() if self.created_at else None
        dict_representation['updated_at'] = self.updated_at.isoformat() if self.updated_at else None
        dict_representation['__class__'] = self.__class__.__name__
        return dict_representation

    def __str__(self):
        """Return a string representation of the model."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
