import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker

class People:
    def __init__(self, sa_engine):
        self.session = sessionmaker(bind=sa_engine)

    def get_people(self):
        pass