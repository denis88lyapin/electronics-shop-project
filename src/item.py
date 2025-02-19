import csv
import math
import os
from src.instantiate_CSV_error import InstantiateCSVError

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self) -> str:
        return f"{self.name}"

    def __add__(self, other: object) -> int:
        if isinstance(other, Item):
            return self.quantity + other.quantity
        raise ValueError('Складывать можно только объекты Item и дочерние от них.')

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        """
        Геттер для атрибута _name
        """
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        """
        Сеттер для атрибута _name. Проверяет количество символов.
        Доустимо не более 10-ти.
        """
        if len(new_name) <= 10:
            self._name = new_name
        else:
            raise ValueError("Длина наименования товара превышает 10 символов")

    @classmethod
    def instantiate_from_csv(cls, file="items.csv") -> None:
        """
        класс-метод, инициализирующий экземпляры класса `Item`
        данными из файла _src/items.csv_
        """
        current_dir = os.path.dirname(os.path.abspath(__file__))
        csv_file = os.path.join(current_dir, file)
        Item.all = []
        try:
            with open(csv_file, encoding="cp1251") as csvfile:
                item_reader = csv.DictReader(csvfile)
                if all(field in item_reader.fieldnames for field in ["name", "price", "quantity"]):
                    for i in item_reader:
                        cls(name=i["name"], price=float(i["price"]), quantity=int(i["quantity"]))
                else:
                    raise InstantiateCSVError(f"Файл {file} поврежден")
        except InstantiateCSVError as error:
            print(error)
        except FileNotFoundError:
            print(f"Отсутствует файл {file}")

    @staticmethod
    def string_to_number(string) -> int:
        try:
            num = int(math.floor(float(string.strip())))
            return num
        except ValueError:
            raise ValueError("Ошибка: Невозможно преобразовать строку в число.")
