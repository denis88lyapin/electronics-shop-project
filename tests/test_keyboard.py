from src.keyboard import KeyBoard
import pytest


def tests_keyboard(keyboard):
    assert keyboard.name == 'Dark Project KD87A'
    assert keyboard.language == "EN"
    keyboard.change_lang()
    assert keyboard.language == "RU"
    keyboard.change_lang().change_lang()
    assert keyboard.language == "RU"


def test_name_setter(keyboard):
    keyboard.name = "Какая-то клава"
    assert keyboard.name == "Какая-то клава"


def test_name_setter_exclusion_1():
    with pytest.raises(ValueError) as e:
        keyword = KeyBoard("Очень длинное название клавиатуры", 10000, 5)
        assert str(e.value) == "Длина наименования товара превышает 30 символов"


def test_set_language(keyboard):
    with pytest.raises(AttributeError) as e:
        keyboard.language = "BU"
        assert str(e.value) == "property 'language' of 'KeyBoard' object has no setter"
