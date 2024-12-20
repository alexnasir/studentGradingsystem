from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base

class Grade(Base):
    __tablename__ = 'grades'

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id', ondelete="CASCADE"), nullable=False)
    subject = Column(String, nullable=False)
    score = Column(Float, nullable=False)
    student = relationship("Student", back_populates="grades")

