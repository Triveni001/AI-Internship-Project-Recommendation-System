from sqlalchemy import Column, Integer, String

from .database import Base


class Student(Base):

    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    email = Column(
        String,
        unique=True,
        nullable=False,
        index=True
    )

    password = Column(String, nullable=False)

    branch = Column(String, nullable=False)

    college = Column(String, nullable=True)

    degree = Column(String, nullable=True)

    graduation_year = Column(String, nullable=True)

    technical_skills = Column(String, nullable=True)

    selected_skills = Column(String, nullable=True)

    interests = Column(String, nullable=True)

    projects = Column(String, nullable=True)

    certifications = Column(String, nullable=True)


class Internship(Base):

    __tablename__ = "internships"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False)

    company = Column(String, nullable=False)

    description = Column(String, nullable=True)

    skills = Column(String, nullable=True)

    duration = Column(String, nullable=True)

    location = Column(String, nullable=True)


class Application(Base):

    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)

    student_id = Column(Integer, nullable=False)

    internship_id = Column(Integer, nullable=False)

    status = Column(
        String,
        default="Applied"
    )


class Project(Base):

    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False)

    description = Column(String, nullable=True)

    skills = Column(String, nullable=True)

    category = Column(String, nullable=True)


class SavedProject(Base):

    __tablename__ = "saved_projects"

    id = Column(Integer, primary_key=True, index=True)

    student_id = Column(Integer, nullable=False)

    project_id = Column(Integer, nullable=False)