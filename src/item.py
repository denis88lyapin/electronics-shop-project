import csv
import math
import os


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
        self._name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    # def __repr__(self):
    #     return f"{self.__class__.__name__},\n" \
    #            f"name = {self.name},\n" \
    #            f"price = {self.price},\n" \
    #            f"quantity = {self.quantity}"

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
    def name(self, new_name) -> None:
        """
        Сеттер для атрибута _name. Проверяет количество символов.
        Доустимо не более 10-ти.
        """
        if len(new_name) <= 10:
            self._name = new_name
        else:
            raise ValueError("Длина наименования товара превышает 10 символов")

    @classmethod
    def instantiate_from_csv(cls) -> None:
        """
        класс-метод, инициализирующий экземпляры класса `Item`
        данными из файла _src/items.csv_
        """
        current_dir = os.path.dirname(os.path.abspath(__file__))
        csv_file = os.path.join(current_dir, 'items.csv')
        Item.all = []
        with open(csv_file, encoding="cp1251") as csvfile:
            item_reader = csv.DictReader(csvfile)
            for i in item_reader:
                cls(name=i["name"], price=float(i["price"]), quantity=int(i["quantity"]))

    @staticmethod
    def string_to_number(string) -> int:
        try:
            num = int(math.floor(float(string)))
            return num
        except ValueError:
            raise ValueError("Ошибка: Невозможно преобразовать строку в число.")
