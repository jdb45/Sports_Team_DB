import os
import sys
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

    elif choice == '3':
        delete_sales()

    elif choice == '4':
        view_top_selling_item()

    elif choice == '5':
        view_lowest_selling_item()

    elif choice == '6':
        view_top_grossing_game()

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

    elif choice == 'e':
        main()

    else:
        print('Please enter a valid selection')


def selling_screen():

    quit = 'q'
    choice = None

    global sales_list
    sales_list = [0,0,0,0,0,0] # setting the sales list values for starting

    while choice != quit:
        choice = user_interface.selling_menu()
        handle_choice_selling(choice)


def sell_jersey():
    global sales_list
    Sales_Object.total = 50 # assigning values for the jersey
    Sales_Object.count = 1
    sales_list[0] += Sales_Object.total # holding the first and second spot for the jersey sales
    sales_list[1] += Sales_Object.count


def sell_poster():
    global sales_list
    Sales_Object.total = 5  # assigning values for the poster
    Sales_Object.count = 1
    sales_list[2] += Sales_Object.total  # holding the third and forth spot for the poster sales
    sales_list[3] += Sales_Object.count


def sell_hat():
    global sales_list
    Sales_Object.total = 20  # assigning values for the hat
    Sales_Object.count = 1
    sales_list[4] += Sales_Object.total  # holding the fifth and sixth spot for the hat sales
    sales_list[5] += Sales_Object.count


def save_sales():
    global sales_list
    GAME_DATE = user_interface.get_date() # saving the sales to the DB assigning readable variable names
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

    save_session.commit()

    save_session.close()


def delete_sales():
    # deleting all the sales from the DB
    try:
        user_input = input('This will delete all the data in the database!!! Are you sure you want to do this? y or n')
        if user_input.lower().startswith("y"):
            Sales.__table__.drop(engine)  # dropping the tables
            Games.__table__.drop(engine)
            Merchandise.__table__.drop(engine)
            python = sys.executable  # restarting the program to re-add the tables
            os.execl(python, python, *sys.argv)
        else:
            main()
    except:
        print('There are no sales recorded yet')


def view_all_sales():
    # viewing all the records
    search_session = Session()
    try:
        for sale in search_session.query(Sales):
         print(sale)
    except:
        print('There are no sales recorded yet')


def view_top_selling_item():
    # viewing the top sold item
    try:
        search_session = Session()
        results = search_session.query(Merchandise).all()
        jersey = 0.0
        hat = 0.0
        poster = 0.0
        row_count = search_session.query(Merchandise).filter(Merchandise.id > 0).count()
        count = 0
        # will go through the whole DB and get the totals for all the items sold
        while True:
            jersey += results[count].jerseys
            hat += results[count].hats
            poster += results[count].posters
            count += 1
            if count == row_count:
                break
        # this will display the highest selling item, by total sold, not price
        if jersey >= hat and jersey >= poster:
            print('Jersey\'s are the highest selling item selling a total of', jersey)

        elif hat >= jersey and hat >= poster:
            print('Hat\'s are best selling item selling a total of', hat)

        elif poster >= jersey and poster >= hat:
            print('Poster\'s are best selling item selling a total of', poster)

    except:
        print('There are no sales recorded yet')


def view_lowest_selling_item():
    # viewing the top sold item
    try:
        search_session = Session()
        results = search_session.query(Merchandise).all()
        jersey = 0.0
        hat = 0.0
        poster = 0.0
        # will count how records are in the DB
        row_count = search_session.query(Merchandise).filter(Merchandise.id > 0).count()
        count = 0
        # will go through the whole DB and get the totals for all the items sold
        while True:
            jersey += results[count].jerseys
            hat += results[count].hats
            poster += results[count].posters
            count += 1
            if count == row_count:
                break
        # this will display the lowest selling item, by total sold, not price
        if jersey <= hat and jersey <= poster:
            print('Jersey\'s are the lowest selling item selling a total of', jersey)

        elif hat <= jersey and hat <= poster:
            print('Hat\'s are lowest selling item selling a total of', hat)

        elif poster <= jersey and poster <= hat:
            print('Poster\'s are lowest selling item selling a total of', poster)
    except:
        print('There are no sales recorded yet')

def view_top_grossing_game():
    # this will display the top grossing game in the DB
    try:
        search_session = Session()
        results = search_session.query(Sales).all()
        highest_sale = []
        row_count = search_session.query(Sales).filter(Sales.id > 0).count()
        count = 0

        while True:
            # adding each total to the list
            highest_sale.append(results[count].total_sales)
            count += 1
            if count == row_count:
                break
        # getting the max value of the list
        highest_sale = max(highest_sale)
        get_date = search_session.query(Sales).filter(Sales.total_sales >= highest_sale).all()
        # getting the date of the highest total game
        get_date = get_date[0].date_sales
        get_opponent = search_session.query(Games).filter(Games.date == get_date).all()
        # getting the opponent of the highest total game
        get_opponent = get_opponent[0].opponent_team
        print('The top grossing game was on,', get_date, 'it was played against The', get_opponent,
              'the total sales were,', "$"+str(highest_sale))
    except:
        print('There are no sales recorded yet')


def main():
    quit = 'q'
    choice = None

    while choice != quit:
        choice = user_interface.open_menu()
        handle_choice_main(choice)


if __name__ == '__main__':
    main()