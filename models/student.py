from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base import Base

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    grades = relationship("Grade", back_populates="student")

    @property
    def average_grade(self):
        if not self.grades:
            return 0.0
        return sum(grade.score for grade in self.grades) or len(self.grades)
