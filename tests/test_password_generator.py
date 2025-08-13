import string

import pytest

from src.password_generator import generate_password


class TestPasswordGenerator:
    def test_default_values(self):
        """Проверка значения по умолчанию."""
        assert len(generate_password()) == 15

    @pytest.mark.parametrize("length", [4, 15, 36, 42])
    def test_valid_lengths(self, length):
        """Проверка корректных и граничных значений длины."""
        assert len(generate_password(length)) == length

    @pytest.mark.parametrize(
        "invalid_input, expected_exception, match",
        [
            ("str", TypeError, "Введите целое число"),
            (3.14, TypeError, "Введите целое число"),
            (-4, ValueError, "Введите число от 4 до 42"),
            (3, ValueError, "Введите число от 4 до 42"),
            (43, ValueError, "Введите число от 4 до 42"),
        ],
    )
    def test_invalid_inputs(self, invalid_input, expected_exception, match):
        """Проверка, что некорректные вводы вызывают ожидаемые исключения."""
        with pytest.raises(expected_exception, match=match):
            generate_password(invalid_input)

    @pytest.mark.parametrize("length", [4, 8, 15, 42])
    def test_guaranteed_char_types_inclusion(self, length):
        """Гарантирует, что в пароле есть хотя бы по одному символу каждого типа."""

        # Наборы символов
        lower = set(string.ascii_lowercase)
        upper = set(string.ascii_uppercase)
        digits = set(string.digits)
        symbols = set("!@#$%^&*()-_=+[]{}|;:,.<>?/")

        password = generate_password(length)
        pwd_set = set(password)

        assert pwd_set & lower, "Нет строчной буквы"
        assert pwd_set & upper, "Нет заглавной буквы"
        assert pwd_set & digits, "Нет цифры"
        assert pwd_set & symbols, "Нет спецсимвола"
