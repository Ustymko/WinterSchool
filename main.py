import datetime
from datetime import date
from typing import List, Union
from unicodedata import name
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

    def __init__(self, age_in_months: int) -> None:
        self.age_in_months = age_in_months
        

class FishInfo:
    def __init__(self, name: str, origin:str, catch_date: datetime, due_date: datetime) -> None:
        self.name = name
        self.origin = origin
        self.catch_date = catch_date
        self.due_date = due_date

class FishBox:
    def __init__(self, fish_info: FishInfo, weight: float, package_date: datetime,
                height: float, width: float, length: float, price_in_uah_per_kilo: float,
                is_alive: bool) -> None:
        self.fish_info = fish_info
        self.weight = weight
        self.package_date = package_date
        self.height = height
        self.width = width
        self.length = length
        self.price_in_uah_per_kilo = price_in_uah_per_kilo
        self.is_alive = is_alive

class FishShop:
    frozen_fish_boxes = {}
    fresh_fish = {}
    def add_fish(self, fish_box: FishBox) -> None:
        if fish_box.is_alive == True:
            self.fresh_fish[fish_box.fish_info.name] = fish_box
        else:
            self.frozen_fish_boxes[fish_box.fish_info.name] = fish_box

    #def add_fish(self, fish: Fish) -> None:
    #    pass

    def sell_fish(self, name: str, weight: float, is_fresh: bool) -> Union[str, float]:
        if is_fresh:
            if name in self.fresh_fish:
                if date.today() > self.fresh_fish[name].fish_info.due_date:
                    return [name, weight*self.fresh_fish[name].price_in_uah_per_kilo]
                else:
                    print("Fish is not fresh")
        else:
            if name in self.frozen_fish_boxes:
                if date.today() > self.frozen_fish_boxes[name].fish_info.due_date:
                    return [name, weight*self.frozen_fish_boxes[name].price_in_uah_per_kilo]
                else:
                    print("Fish is not fresh")
            
    def get_fish_names_sorted_by_price(self) -> List[Union[str, bool, float]]:
        all_fishes_sorted_by_price = []
        # appending elements of dicts' to list for more comfortable sorting
        for name in self.fresh_fish:
            all_fishes_sorted_by_price.append([name, self.fresh_fish[name].is_alive, self.fresh_fish[name].price_in_uah_per_kilo])
        for name in self.frozen_fish_boxes:
            all_fishes_sorted_by_price.append([name, self.frozen_fish_boxes[name].is_alive, self.frozen_fish_boxes[name].price_in_uah_per_kilo])

        # insertion sort
        for i in range(1, len(all_fishes_sorted_by_price)):
            key_item = all_fishes_sorted_by_price[i]
            j = i - 1
            while j >= 0 and all_fishes_sorted_by_price[j].fish_info.price_in_uah_per_kilo > key_item.fish_info.price_in_uah_per_kilo:
                all_fishes_sorted_by_price[j + 1] = all_fishes_sorted_by_price[j]
                j -= 1
            all_fishes_sorted_by_price[j + 1] = key_item
        return all_fishes_sorted_by_price
    
    def get_fresh_fish_names_sorted_by_price(self) -> List[Union[str, float]]:
        fresh_fishes_sorted_by_price = []
        for name in self.fresh_fish:
            fresh_fishes_sorted_by_price.append([name, self.fresh_fish[name].price_in_uah_per_kilo])

        # insertion sort
        for i in range(1, len(fresh_fishes_sorted_by_price)):
            key_item = fresh_fishes_sorted_by_price[i]
            j = i - 1
            while j >= 0 and fresh_fishes_sorted_by_price[j].fish_info.price_in_uah_per_kilo > key_item.fish_info.price_in_uah_per_kilo:
                fresh_fishes_sorted_by_price[j + 1] = fresh_fishes_sorted_by_price[j]
                j -= 1
            fresh_fishes_sorted_by_price[j + 1] = key_item
        return fresh_fishes_sorted_by_price

    def get_frozen_fish_names_sorted_by_price(self) -> List [Union[str, float]]:
        frozen_fishes_sorted_by_price = []
        for name in self.fresh_fish:
            frozen_fishes_sorted_by_price.append([name, self.fresh_fish[name].price_in_uah_per_kilo])

        # insertion sort
        for i in range(1, len(frozen_fishes_sorted_by_price)):
            key_item = frozen_fishes_sorted_by_price[i]
            j = i - 1
            while j >= 0 and frozen_fishes_sorted_by_price[j].fish_info.price_in_uah_per_kilo > key_item.fish_info.price_in_uah_per_kilo:
                frozen_fishes_sorted_by_price[j + 1] = frozen_fishes_sorted_by_price[j]
                j -= 1
            frozen_fishes_sorted_by_price[j + 1] = key_item
        return frozen_fishes_sorted_by_price

    #def cast_out_old_fish(self, fish_name: str, date: datetime):
    #    if date >= self.expiration_date:
    #        return fish_name
        


class Seller:
    pass


class Buyer:
    pass
