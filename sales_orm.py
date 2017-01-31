from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base import Base
import user_interface
from sports_team_tables import Games, Sales, Merchandise


engine = create_engine('sqlite:///sports_sales.db', echo=False)

# Creating a table for all the things that use Base
Base.metadata.create_all(engine)

#Making a Session class
Session = sessionmaker(bind=engine)


def handle_choice(choice):
    # menu handler

    if choice == 'q':
        quit()

    else:
        print('Please enter a valid selection')



def main():

    quit = 'q'
    choice = None

    while choice != quit:
        choice = user_interface.open_menu()
        handle_choice(choice)


if __name__ == '__main__':
    main()