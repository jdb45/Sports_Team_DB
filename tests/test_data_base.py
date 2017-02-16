import unittest
from unittest.mock import patch, call
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import sales_orm
import sports_team_tables
from sports_team_tables import Merchandise, Games, Sales
from base import Base


class TestDataBase(unittest.TestCase):

    test_db = 'sqlite:///test_database.db'
    # the setup will run before each test, to create a new database each time
    def setUp(self):
        sales_orm.engine = create_engine(self.test_db, echo=False)
        sales_orm.Session = sessionmaker(bind=sales_orm.engine)
        sales_orm.session = sales_orm.Session()
        self.session = sales_orm.session
        Base.metadata.create_all(sales_orm.engine)

    # tear down to drop the tables and delete the database
    def tearDown(self):
        sports_team_tables.Base.metadata.drop_all(sales_orm.engine)
        sales_orm.session.close()

    def test_viw_all_sales(self):
        self.add_example_sales()
        results = sales_orm.view_all_sales()  # expecting to return all the sales in the database
        self.assertCountEqual(results, self.test_sales)

    def test_top_selling_item(self):
        self.add_example_merchandise()
        results = sales_orm.view_top_selling_item() # expecting to return the top selling item in the database
        self.assertEqual(1, results)

    def test_lowest_selling_item(self):
        self.add_example_merchandise()
        results = sales_orm.view_lowest_selling_item() # expecting to return the lowest selling item in the database
        self.assertEqual(3, results)

    @patch('builtins.print')
    def test_top_grossing_game(self, mock_print):
        self.add_example_games()
        self.add_example_merchandise()
        self.add_example_sales()
        sales_orm.view_top_grossing_game() # expecting to return the top grossing item in the database
        expected_calls = [call('The top grossing game was on,', '12/14/15', 'it was played against The', 'packers', 'the total sales were,', '$200.0')]
        self.assertEqual(expected_calls, mock_print.call_args_list)

    def add_example_sales(self):
        sale1 = Sales(150, 100, 25, 25, '12/13/14') # adding sample data
        sale2 = Sales(200, 125, 50, 25, '12/14/15')
        self.test_sales = [sale1, sale2]
        sales_orm.session.add_all(self.test_sales)
        self.session.commit()

    def add_example_merchandise(self):
        merchandise1 = Merchandise(10, 3, 2, '12/13/14') # adding sample data
        merchandise2 = Merchandise(12, 7, 5, '12/14/15')
        self.test_merchandise = [merchandise1, merchandise2]
        sales_orm.session.add_all(self.test_merchandise)
        self.session.commit()

    def add_example_games(self):
        games1 = Games('12/13/14', 'vikings', 'minneapolis') # adding sample data
        games2 = Games('12/14/15', 'packers', 'green bay')
        self.test_games = [games1, games2]
        sales_orm.session.add_all(self.test_games)
        self.session.commit()


if __name__ == '__main__':
    unittest.main()