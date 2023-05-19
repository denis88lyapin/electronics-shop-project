import pytest

from src.item import Item


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


def test_name_len_exclclusion(item):
    with pytest.raises(ValueError) as e:
        item.name = "СуперСмартфон"
    assert str(e.value) == "Длина наименования товара превышает 10 символов"


def test_instantiate_from_csv(item):
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    assert isinstance(Item.all[0], Item)


def test_string_to_number():
    assert Item.string_to_number("123 ") == 123


def test_string_to_number_exclclusion():
    with pytest.raises(ValueError) as e:
        Item.string_to_number("1n3 ")
    assert str(e.value) == "Ошибка: Невозможно преобразовать строку в число."
