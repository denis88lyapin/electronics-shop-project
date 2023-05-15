import pytest
from src.item import Item

@pytest.fixture
def item():
    Item.all = []
    item = Item(name="Тестовый товар", price=10.0, quantity=5)
    return item
