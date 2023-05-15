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
