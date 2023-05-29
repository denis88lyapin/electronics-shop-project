from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int = 1) -> None:
        """
        Создание экземпляра класса Phone (наследуется от Item).
        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        :param quantity: Количество поддерживаемых сим-карт.
        """
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    @property
    def number_of_sim(self):
        """
        Геттер number_of_sim
        """
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, new_number_of_sim):
        """
        Сеттер number_of_sim
        """
        if new_number_of_sim > 0 and isinstance(new_number_of_sim, int):
            self._number_of_sim = new_number_of_sim
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
