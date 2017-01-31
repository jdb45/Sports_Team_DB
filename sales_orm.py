from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base import Base
import user_interface
from sales_objects import Sales_Object
from sports_team_tables import Games, Sales, Merchandise


engine = create_engine('sqlite:///sports_sales.db', echo=False)

# Creating a table for all the things that use Base
Base.metadata.create_all(engine)

# Making a Session class
Session = sessionmaker(bind=engine)


def handle_choice_main(choice):
    # Main menu handler

    if choice == '1':
        selling_screen()

    elif choice == '2':
        view_all_sales()

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

    elif choice == '3':
        sell_hat()

    elif choice == 'q':
        save_sales()
        main()

    else:
        print('Please enter a valid selection')


def selling_screen():

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


def save_sales():
    global sales_list
    GAME_DATE = user_interface.get_date()
    LOCATION_GAME = user_interface.get_location()
    OPPONENT_GAME = user_interface.get_opponent()
    SALE_TOTAL = (sales_list[0] + sales_list[2] + sales_list[4])
    JERSEYS_SOLD_TOTAL = sales_list[0]
    JERSEYS_SOLD_COUNT = sales_list[1]
    HATS_SOLD_TOTAL = sales_list[2]
    HATS_SOLD_COUNT = sales_list[3]
    POSTERS_SOLD_TOTAL = sales_list[4]
    POSTERS_SOLD_COUNT = sales_list[5]

    record1 = Games(date=GAME_DATE, opponent_team=OPPONENT_GAME, location=LOCATION_GAME)
    record2 = Sales(total_sales=SALE_TOTAL, jersey_sales=JERSEYS_SOLD_TOTAL, hat_sales=HATS_SOLD_TOTAL, poster_sales=POSTERS_SOLD_TOTAL, date_sales=GAME_DATE)
    record3 = Merchandise(jerseys=JERSEYS_SOLD_COUNT, hats=HATS_SOLD_COUNT, posters=POSTERS_SOLD_COUNT, date_merchandise=GAME_DATE)

    save_session = Session()

    save_session.add_all([record1, record2, record3])

    save_session.commit()  # All data saved. Now nothing is new, or dirty

    save_session.close()


def view_all_sales():
    # viewing all the records
    search_session = Session()

    for sale in search_session.query(Sales):
        print(sale)

def main():

    quit = 'q'
    choice = None

    while choice != quit:
        choice = user_interface.open_menu()
        handle_choice_main(choice)


if __name__ == '__main__':
    main()