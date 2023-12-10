from src.repository import Repository
from src.domain import Expense


class Services:
    def __init__(self, repository: Repository):
        self.__repo = repository

    def add_expense(self, day: int, amount: int, type: str):
        self.__repo.add_expense(Expense(day, amount, type))

    def list_all(self):
        return self.__repo.get_all()

    def filter_above_value(self, value: int):
        self.__repo.filter_above_value(value)

    def undo(self):
        self.__repo.pop_history()

    pass
