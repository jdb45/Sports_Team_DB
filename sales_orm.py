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


def handle_choice_main(choice):
    # menu handler

    if choice == '1':
        selling_screen()

    elif choice == 'q':
        quit()

    else:
        print('Please enter a valid selection')

def handle_choice_selling(choice):
    # menu handler for selling screen

    if choice == '1':
        print()

    elif choice == 'q':
        main()

    else:
        print('Please enter a valid selection')

def selling_screen():

    game_date = user_interface.get_date()
    location_game = user_interface.get_location()
    opponent_game = user_interface.get_opponent()

    quit = 'q'
    choice = None

    while choice != quit:
        choice = user_interface.selling_menu()
        handle_choice_selling(choice)


def main():

    quit = 'q'
    choice = None

    while choice != quit:
        choice = user_interface.open_menu()
        handle_choice_main(choice)


if __name__ == '__main__':
    main()