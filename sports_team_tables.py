from sqlalchemy import Column, Integer, String, REAL, ForeignKey, ForeignKeyConstraint

from base import Base


class Games(Base):

   # creating a table
    __tablename__ = 'games'

    # creating the columns
    id = Column(Integer, primary_key=True)
    date = Column(String)
    opponent_team = Column(String)
    location = Column(String)

    def __init__(self, date, opponent_team, location):
        self.date = date
        self.opponent_team = opponent_team
        self.location = location

    def __repr__(self):
        return 'games: id = {} date = {} opponent_team = {} location = {}'.format(self.id, self.date, self.opponent_team, self.location)


class Sales(Base):


   # creating a table
    __tablename__ = 'sales'

    # creating the columns
    id = Column(Integer, primary_key=True)
    total_sales = Column(REAL)
    jersey_sales = Column(REAL)
    hat_sales = Column(REAL)
    poster_sales = Column(REAL)
    date_sales = Column(String)
    ForeignKeyConstraint(['date_sales'], ['Games.date'])


    def __init__(self, total_sales, jersey_sales, hat_sales, poster_sales, date_sales):
        self.total_sales = total_sales
        self.jersey_sales = jersey_sales
        self.hat_sales = hat_sales
        self.poster_sales = poster_sales
        self.date_sales = date_sales



    def __repr__(self):
        return 'sales: id = {} total_sales = {} jersey_sales = {} hat_sales = {} poster_sales = {} date = {}'\
            .format(self.id, self.total_sales, self.jersey_sales, self.hat_sales, self.poster_sales, self.date_sales)


class Merchandise(Base):


   # creating a table
    __tablename__ = 'merchandise'

    # creating the columns
    id = Column(Integer, primary_key=True)
    jerseys = Column(Integer)
    hats = Column(Integer)
    posters = Column(Integer)
    date_merchandise = Column(String)
    # I probably don't need this.
    ForeignKeyConstraint(['date_sales'], ['Games.date'])


    def __init__(self, jerseys, hats, posters, date_merchandise):
     self.jerseys = jerseys
     self.hats = hats
     self.posters = posters
     self.date_merchandise = date_merchandise


    def __repr__(self):
        return 'merchandise: id = {} jerseys = {} hats = {} posters = {} date = {}'\
            .format(self.id, self.jerseys, self.hats, self.posters, self.date_merchandise)