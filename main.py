import datetime
from typing import List, Union


# method
# attributes
class Student:
    group = "IP-11"

    def __init__(self, first_name: str = "", last_name: str = "") -> None:
        self.first_name = first_name  # public
        self.last_name = last_name  # public
        self.__name = "hidden"  # private
        self._another = "another"  # protected

    def print_name(self):
        self.full_name = "Mr/Mrs. " + self.first_name + " " + self.last_name
        print(self.full_name)

    @staticmethod
    def pass_exam() -> None:
        print(Student.group)


class Dean:
    pass


class Fish:

    def __init__(self) -> None:
        self.name = "oseledets"
        self.price_in_uah_per_kilo = 11.2
        self.catch_date = datetime("21/01/2022")
        self.origin = "Norway"
        self.body_only = True
        self.weight = 100


class FishShop:

    def add_fish(self, fish_name: str, total_weight: float) -> None:
        pass

    def get_fish_names_sorted_by_price(self) -> List[Union[str, float]]:
        pass

    def sell_fish(self, fish_name: str, weight: float) -> float:
        pass

    def cast_out_old_fish(self) -> List[Union[str, float]]:
        pass


class Seller:
    pass


class Buyer:
    pass


oleh = Student("oleh", "petrovych")
oleh.print_name()
taras = Student()
taras.print_name()
vasyl = Dean()
