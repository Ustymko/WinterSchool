import datetime
from typing import List, Union
from xmlrpc.client import _datetime


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

    def __init__(self, name = "oseledets", weight = 100, price_in_uah_per_kilo = 11.2, 
                catch_date = datetime("21/01/2022"), origin = "Norway", body_only = True) -> None:
        self.name = name
        self.weight = weight
        self.price_in_uah_per_kilo = price_in_uah_per_kilo
        self.catch_date = catch_date
        self.origin = origin
        self.body_only = body_only
        


class FishShop:
    fishes = {}
    expiration_date = datetime("21/01/2022")
    def add_fish(self, fish_name: str, price_in_uah_per_kilo: float) -> None:
        self.fishes[fish_name] = price_in_uah_per_kilo

    #def get_fish_names_sorted_by_price(self) -> List[Union[str, float]]:
    #    pass

    def sell_fish(self, fish_name: str, weight: float) -> float:
        if fish_name in self.fishes:
            return self.fishes[fish_name] * weight

    def cast_out_old_fish(self, fish_name: str, date: datetime) -> str:
        if date >= self.expiration_date:
            return fish_name
        


class Seller:
    pass


class Buyer:
    pass


#oleh = Student("oleh", "petrovych")
#oleh.print_name()
#taras = Student()
#taras.print_name()
#vasyl = Dean()
