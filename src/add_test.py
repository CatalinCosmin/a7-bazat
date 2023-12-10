import unittest
from src.services import Services
from src.repository import Repository
from src.domain import Expense


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.__repo = Repository()
        self.__services = Services(self.__repo)

    def test_add_repo(self):
        ex = Expense(1, 1, "test")
        result = [ex]

        self.__repo.add_expense(ex)

        self.assertListEqual(self.__repo.get_all(), result)

    def test_add_services(self):
        ex = Expense(1, 1, "test")
        result = [ex]

        self.__services.add_expense(ex.day, ex.amount, ex.type)

        self.assertEqual(self.__services.list_all(), result)


if __name__ == '__main__':
    unittest.main()
