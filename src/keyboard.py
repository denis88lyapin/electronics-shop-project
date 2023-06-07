from src.item import Item


class LanguageMixin:
    """
    Mixin для хранения и изменения раскладки клавиатуры (EN, RU).
    По умолчанию - EN.
    """
    def __init__(self, name: str, price: float, quantity: int) -> None:

        super().__init__(name, price, quantity)
        self._language = "EN"

    def change_lang(self) -> object:
        """
        Функция изменения раскладки клавиатуры.
        """
        if self._language == "EN":
            self._language = "RU"
        else:
            self._language = "EN"
        return self

    @property
    def language(self) -> str:
        """
        Защита от возможности установить другую раскладку.
        """
        return self._language

    @language.setter
    def language(self, new_language: str) -> Exception:
        raise AttributeError("property 'language' of 'KeyBoard' object has no setter")


class KeyBoard(LanguageMixin, Item):
    """
    Класс для товара “клавиатура”
    """

    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__(name, price, quantity)

    @property
    def name(self):
        """
        Переопределение геттера для атрибута _name
        """
        return self._name

    @name.setter
    def name(self, new_name) -> None:
        """
        Переопределение сеттера для атрибута _name. Проверяет количество символов.
        Допустимо не более 30-ти.
        """
        if len(new_name) <= 30:
            self._name = new_name
        else:
            raise ValueError("Длина наименования товара превышает 30 символов")
