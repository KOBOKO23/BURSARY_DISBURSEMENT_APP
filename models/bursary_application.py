# bursary_application.py

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel

class BursaryApplication(BaseModel):
    student_id = Column(String, ForeignKey('user.id'))
    institution_id = Column(String, ForeignKey('institution.id'))
    status = Column(String, default="pending")
    student = relationship("User", back_populates="applications")
    institution = relationship("Institution", back_populates="applications")

    def review(self):
        # Logic to review the application
        pass
    
    def approve(self):
        # Logic to approve the application
        pass
