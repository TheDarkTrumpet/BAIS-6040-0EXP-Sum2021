import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from .People import Person


class db:
    def __init__(self, sa_engine):
        maker = sessionmaker(bind=sa_engine)
        self.session = maker()

    def get_people(self):
        users = self.session.query(Person).all()
        return users

    def new(self, fname, lname, address, phone):
        new_user = Person(fname=fname, lname=lname, address=address, phone=phone)
        self.session.add(new_user)
        self.session.commit()
