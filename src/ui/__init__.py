from src.services import Services


class Ui:
    def __init__(self, services: Services):
        self.__services = services

    @staticmethod
    def display_menu():
        print("Select one of the options:")
        print("1. Add an expense")
        print("2. Display all expenses")
        print("3. Filter the list so that it contains only expenses above a certain value read from the console")
        print("4. Undo previous operation")
        print("0. Exit")

    @staticmethod
    def get_input(txt: str = "> "):
        return input(txt)

    def couple_option(self, option: str):
        if option == "1":
            self.add_expense_option()
        elif option == "2":
            self.display_all_option()
        elif option == "3":
            self.filter_above_value()
        elif option == "4":
            self.undo()
        elif option == "0":
            exit()
        else:
            print("Invalid option")

    def start(self):
        while True:
            try:
                self.display_menu()
                self.couple_option(self.get_input("> "))
            except Exception as ex:
                print(ex)

    def display_all_option(self):
        print(self.__services.list_all())

    def add_expense_option(self):
        self.__services.add_expense(int(self.get_input("Day: ")), int(self.get_input("Amount: ")),
                                    self.get_input("Type: "))

    def filter_above_value(self):
        self.__services.filter_above_value(int(self.get_input("Value: ")))

    def undo(self):
        self.__services.undo()

    pass
