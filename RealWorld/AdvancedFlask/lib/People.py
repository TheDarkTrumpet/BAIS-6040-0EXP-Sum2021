from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Person(Base):
    __tablename__ = 'People'

    id = Column(Integer, primary_key=True)
    fname = Column(String)
    lname = Column(String)
    address = Column(String)
    phone = Column(String)

    def __repr__(self):
        return f"{self.lname}, {self.fname}: {self.address} - {self.phone}"
