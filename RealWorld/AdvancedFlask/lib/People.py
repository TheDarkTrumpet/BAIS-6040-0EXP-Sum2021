from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
import json

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

    def as_dict(self):
        return {
            "FirstName": self.fname,
            "LastName": self.lname,
            "Address": self.address,
            "Phone": self.phone
        }

    @classmethod
    def from_json(self, json_str):
        personJson = json.loads(json_str)
        return Person(
            fname=personJson.get("FirstName"),
            lname=personJson.get("LastName"),
            address=personJson.get("Address"),
            phone=personJson.get("Phone")
        )
