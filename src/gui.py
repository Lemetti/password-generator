import customtkinter as ctk
import pyperclip

from password_generator import generate_password


class PasswordGeneratorApp(ctk.CTk):  # pragma: no cover
    def __init__(self):
        """
        Инициализация приложения генератора паролей.

        Создает окно приложения, настраивает тему и интерфейс.
        """
        super().__init__()
        self.title("Portable Password Generator")
        self.geometry("400x300")

        # Настройка темы
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Инициализация элементов интерфейса
        self.frame = None
        self.label_title = None
        self.label_length = None
        self.entry_length = None
        self.button_generate = None
        self.label_result = None
        self.button_copy = None

        self.setup_ui()
        self.setup_defaults()  # Настройки по умолчанию

    def setup_ui(self) -> None:
        """
        Создание элементов графического интерфейса.

        Инициализирует все виджеты: фреймы, метки, поля ввода, кнопки.
        """
        self.frame = ctk.CTkFrame(self)
        self.frame.pack(pady=20, padx=40, fill="both", expand=True)

        self.label_title = ctk.CTkLabel(
            self.frame, text="Наколдуем паролей?", font=("Roboto", 20)
        )
        self.label_title.pack(pady=10)

        self.label_length = ctk.CTkLabel(self.frame, text="Длина пароля:")
        self.label_length.pack()

        self.entry_length = ctk.CTkEntry(self.frame, width=100)
        self.entry_length.pack(pady=5)

        self.button_generate = ctk.CTkButton(
            self.frame, text="Сгенерировать пароль", command=self.on_generate
        )
        self.button_generate.pack(pady=10)

        self.label_result = ctk.CTkLabel(
            self.frame, text="", font=("Roboto", 16), wraplength=300
        )
        self.label_result.pack(pady=10)

        self.button_copy = ctk.CTkButton(
            self.frame, text="Копировать", command=self.on_copy, state="disabled"
        )
        self.button_copy.pack(pady=5)

    def setup_defaults(self) -> None:
        """
        Настройка значений по умолчанию для интерфейса.

        Устанавливает начальное значение длины пароля,
        фокус на поле ввода и обработку клавиши Enter.
        """
        self.entry_length.insert(0, "15")
        self.entry_length.focus()
        self.entry_length.bind("<Return>", lambda event: self.on_generate())

    def on_generate(self) -> None:
        """
        Обработчик кнопки генерации пароля.

        Получает длину из поля ввода, генерирует пароль
        и отображает его в интерфейсе.
        """
        try:
            length = int(self.entry_length.get())
        except ValueError:
            self.label_result.configure(text="Введите целое число")
            return

        try:
            password = generate_password(length)
            self.label_result.configure(text=password)
            self.button_copy.configure(state="normal")
        except ValueError as e:
            self.label_result.configure(text=str(e))

        except Exception as e:
            self.label_result.configure(text=f"Ошибка: {str(e)}")

    COPIED_MESSAGE = "Пароль скопирован! <3"

    def on_copy(self) -> None:
        """
        Обработчик кнопки копирования пароля.

        Копирует сгенерированный пароль в буфер обмена
        и отображает подтверждение.
        """
        if self.button_copy.cget("state") == "normal":
            password = self.label_result.cget("text")
            pyperclip.copy(password)
            self.label_result.configure(text=self.COPIED_MESSAGE)
