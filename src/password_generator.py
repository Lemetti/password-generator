import random
import string


def generate_password(length: int = 15) -> str:
    """
    Генерирует случайный пароль указанной длины.

    Пароль содержит буквы верхнего и нижнего регистра, цифры и спецсимволы.
    Гарантируется наличие хотя бы одного символа каждого типа.

    Args:
        length (int): Длина пароля от 4 до 42. По умолчанию 15.

    Returns:
        str: Сгенерированный пароль.

    Raises:
        ValueError: Если длина меньше 4 или больше 42.
    """

    # Валидация входных данных
    if not 4 <= length <= 42:
        raise ValueError("Введите число от 4 до 42")

    # Наборы символов
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%^&*()-_=+[]{}|;:,.<>?/"

    # Гарантированное наличие всех типов символов
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols),
    ]

    # Добавление остальных символов
    all_chars = lower + upper + digits + symbols
    password.extend(random.choices(all_chars, k=length - 4))

    # Перемешивание символов
    random.shuffle(password)

    return "".join(password)
