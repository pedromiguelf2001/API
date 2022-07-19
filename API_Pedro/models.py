from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Course(Base):
    __tablename__ = "course"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    university = Column(Integer, ForeignKey("university.id"))

    students = relationship("Student", back_populates="courses")

class Student(Base):
    __tablename__ = "student"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String,index=True)
    average = Column(Integer,index = True)
    university = Column(Integer, ForeignKey("university.id"))
    course = Column(Integer, ForeignKey("course.id"))

    courses = relationship("Course", back_populates="students")
    universitys = relationship("University", back_populates="students")


class University(Base):
    __tablename__ = "university"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    students = relationship("Student", back_populates="universitys")
    
