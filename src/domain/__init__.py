class Expense:
    def __init__(self, _day: int, _amount: int, _type: str):
        self.__day = _day
        self.__amount = _amount
        self.__type = _type

    @property
    def day(self):
        return self.__day

    @property
    def amount(self):
        return self.__amount

    @property
    def type(self):
        return self.__type

    def __str__(self):
        return "Day: " + str(self.__day) + " | " + "Amount: " + str(self.__amount) + " | " + "Type: " + str(self.__type)

    __repr__ = __str__

    pass
