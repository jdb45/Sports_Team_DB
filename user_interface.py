
def open_menu():
    # a menu for the user interface
    print('''
        1. Star Selling!
        2. View all sales
        3. Delete ALL data
        4. View top selling item
        5. View worst selling items
        6. Top grossing game
        q. Quit
    ''')

    choice = input('Enter your selection: ')

    return choice


def get_date():
    # a function to ask the user to enter the date of the game
    user_date = input("Please enter the date of the game: ")

    return user_date


def get_location():
    # a function to ask the user the location of the game
    user_location = input('Please enter the location of the game:')

    return user_location


def get_opponent():
    # a function to ask the user the opponent of the game
    user_opponent = input("Please enter the opponent:")

    return  user_opponent

def selling_menu():
    # user interface for the selling menu
    print('''
        1. Sell jersey
        2. Sell poster
        3. Sell hat
        q. Quit
        e. Exit without saving
    ''')

    choice = input('Enter your selection: ')

    return choice
