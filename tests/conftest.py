import pytest
from src.item import Item
from src.phone import Phone
from src.keyboard import KeyBoard


@pytest.fixture
def item():
    Item.all = []
    item = Item(name="Товар", price=10.0, quantity=5)
    return item


@pytest.fixture
def phone():
    Phone.all = []
    phone = Phone(name='iPhone 14', price=120000, quantity=5, number_of_sim=1)
    return phone

@pytest.fixture
def keyboard():
    Item.all = []
    keyboard = KeyBoard(name='Dark Project KD87A', price=9600, quantity=5)
    return keyboard

