from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base import Base
import user_interface
from sales_objects import Sales_Object
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
        sell_jersey()

    elif choice == '2':
        sell_poster()

    elif choice == 'q':
        main()

    else:
        print('Please enter a valid selection')

def selling_screen():

    game_date = user_interface.get_date()
    location_game = user_interface.get_location()
    opponent_game = user_interface.get_opponent()

    save_session = Session()

    quit = 'q'
    choice = None

    global sales_list
    sales_list = [0,0,0,0,0,0]

    while choice != quit:
        choice = user_interface.selling_menu()
        handle_choice_selling(choice)


def sell_jersey():
    global sales_list
    Sales_Object.total = 50
    Sales_Object.count = 1
    sales_list[0] += Sales_Object.total
    sales_list[1] += Sales_Object.count


def sell_poster():
    global sales_list
    Sales_Object.total = 5
    Sales_Object.count = 1
    sales_list[2] += Sales_Object.total
    sales_list[3] += Sales_Object.count


def sell_hat():
    global sales_list
    Sales_Object.total = 20
    Sales_Object.count = 1
    sales_list[4] += Sales_Object.total
    sales_list[5] += Sales_Object.count


def main():

    quit = 'q'
    choice = None

    while choice != quit:
        choice = user_interface.open_menu()
        handle_choice_main(choice)


if __name__ == '__main__':
    main()