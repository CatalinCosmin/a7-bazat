import copy
import pickle

from src.domain import Expense


class RepoError(Exception):
    def __str__(self):
        return "Error on repository"


class Repository:
    def __init__(self):
        self._data = []
        self._history = []

    def add_to_history(self):
        self._history.append(copy.deepcopy(self._data))

    def pop_history(self):
        if len(self._history) == 0:
            raise RepoError()
        self._data = copy.deepcopy(self._history[-1])
        self._history.pop()

    def add_expense(self, value: Expense):
        self.add_to_history()

        self._data.append(value)

    def get_all(self):
        return self._data

    def filter_above_value(self, value: int):
        self.add_to_history()

        ok = 0
        while ok == 0:
            ok = 1
            for x in self._data:
                if x.amount <= value:
                    self._data.remove(x)
                    ok = 0

    pass


class TextFileRepository(Repository):
    def __init__(self, file_name: str):
        super().__init__()

        self.__file_name = file_name

        self.load()

    def load(self):
        file = open(self.__file_name, "r")
        self._data = file.readlines()

    def save(self):
        values = []

        for expense in self._data:
            values.append(str(expense) + '\n')

        file = open(self.__file_name, "w")
        file.writelines(values)

    def filter_above_value(self, value: int):
        super().filter_above_value(value)

        self.save()

    def add_expense(self, value: Expense):
        super().add_expense(value)

        self.save()

    pass


class BinaryRepository(Repository):
    def __init__(self, file_name: str):
        super().__init__()

        self.__file_name = file_name

        self.load()

    def load(self):
        file = open(self.__file_name, "rb")
        self._data = pickle.load(file)

        file.close()

    def save(self):
        file = open(self.__file_name, "wb")
        pickle.dump(self._data, file)

        file.close()

    def filter_above_value(self, value: int):
        super().filter_above_value(value)

        self.save()

    def add_expense(self, value: Expense):
        super().add_expense(value)

        self.save()

    pass
