import pytest

from src.item import Item
from src.instantiate_CSV_error import InstantiateCSVError


def test_repr(item):
    assert repr(item) == "Item('Товар', 10.0, 5)"


def test_str(item):
    assert str(item) == 'Товар'


def test_calculate_total_price(item):
    # Проверка, что возвращает правильную общую стоимость товара
    expected_total_price = item.price * item.quantity
    total_price = item.calculate_total_price()
    assert total_price == expected_total_price


def test_apply_discount(item):
    # Проверка, что метод применяет скидку к цене товара
    expected_discounted_price = item.price * Item.pay_rate
    item.apply_discount()
    assert item.price == expected_discounted_price


def test_all_items_list(item):
    # Проверка, что экземпляр класса Item добавлен в список всех товаров
    assert len(Item.all) == 1
    assert Item.all[0] == item


def test_name(item):
    assert item.name == 'Товар'
    item.name = "Смартфон"
    assert item.name == 'Смартфон'


def test_name_len_exclusion():
    with pytest.raises(ValueError) as e:
        item = Item("СуперСмартфон", 7000000, 1)
        assert str(e.value) == "Длина наименования товара превышает 10 символов"


def test_instantiate_from_csv(item):
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    assert isinstance(Item.all[0], Item)


def test_instantiate_from_csv_invalid_file(capfd):
    Item.instantiate_from_csv("test.csv")
    captured = capfd.readouterr()
    assert f"Отсутствует файл test.csv" in captured.out


def test_instantiate_from_csv_invalid_data_error(capfd):
    Item.instantiate_from_csv("test2.csv")
    captured = capfd.readouterr()
    assert f"Файл test2.csv поврежден" in captured.out


def test_string_to_number():
    assert Item.string_to_number("123 ") == 123


def test_string_to_number_exclusion():
    with pytest.raises(ValueError) as e:
        Item.string_to_number("1n3 ")
        assert str(e.value) == "Ошибка: Невозможно преобразовать строку в число."


def test_add(item, phone):
    assert item + phone == 10


def test_add_exclusion(item):
    with pytest.raises(ValueError) as e:
        item + 10
        assert str(e.value) == 'Складывать можно только объекты Item и дочерние от них.'
