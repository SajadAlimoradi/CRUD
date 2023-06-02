from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from logs.log_conf import LogCrud
from database import Base, engine
from sqlalchemy.sql import func

logging = LogCrud.log_establish()


class Student(Base):
    """Model class representing a student in the database."""
    __tablename__ = 'student'
    id: int = Column(Integer, primary_key=True)
    first_name: str = Column(String(50), nullable=False)
    last_name: str = Column(String(50), nullable=False)
    student_number: str = Column(String(50), unique=True, nullable=False)
    gender: str = Column(String(10), nullable=False)
    date_of_birth: Date = Column(Date, nullable=False)
    educational_level: str = Column(String(50), nullable=False)
    registration_date: Date = Column(Date, nullable=False, default=func.now())
    graduation_date: Date = Column(Date)
    address: str = Column(String(100), nullable=False)
    phone_number: str = Column(String(20), nullable=False)


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
