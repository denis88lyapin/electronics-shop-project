import pytest
from src.phone import Phone


def test_repr(phone):
    assert repr(phone) == "Phone('iPhone 14', 120000, 5, 1)"


def test_number_of_sim(phone):
    assert phone.number_of_sim == 1


def test_number_of_sim_exclusion_1():
    with pytest.raises(ValueError) as e:
        phone = Phone('iPhone 14', 120000, 5, 0)
        assert str(e.value) == "Количество физических SIM-карт должно быть целым числом больше нуля."


def test_number_of_sim_exclusion_2():
    with pytest.raises(ValueError) as e:
        phone = Phone('iPhone 14', 120000, 5, 2.5)
        assert str(e.value) == "Количество физических SIM-карт должно быть целым числом больше нуля."
