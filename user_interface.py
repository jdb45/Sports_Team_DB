
def open_menu():

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

    user_date = input("Please enter the date of the game: ")

    return user_date


def get_location():

    user_location = input('Please enter the location of the game:')

    return user_location


def get_opponent():

    user_opponent = input("Please enter the opponent:")

    return  user_opponent

def selling_menu():

    print('''
        1. Sell jersey
        2. Sell poster
        3. Sell hat
        q. Quit
        e. Exit without saving
    ''')

    choice = input('Enter your selection: ')

    return choice
