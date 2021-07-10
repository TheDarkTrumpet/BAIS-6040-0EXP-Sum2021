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

    def new(self, person):
        self.session.add(person)
        self.session.commit()
