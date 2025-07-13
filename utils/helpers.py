from datetime import datetime


def print_menu():
    print("\n=== Личный финансовый менеджер ===")
    print("1. Добавить транзакцию")
    print("2. Показать статистику")
    print("3. Установить лимит")
    print("0. Выход")


def input_date(prompt="Введите дату (ГГГГ-ММ-ДД): ") -> str:
    """
    Запрашивает у пользователя дату в формате ГГГГ-ММ-ДД с валидацией.
    Возвращает строку с датой или None при отмене.
    """
    while True:
        date_str = input(prompt).strip()

        if not date_str:
            return None

        try:
            date_obj = datetime.strptime(date_str, "%Y-%m-%d")
            return date_obj.strftime("%Y-%m-%d")
        except ValueError:
            print("Ошибка: Некорректный формат даты. Используйте ГГГГ-ММ-ДД (например: 2023-10-15)")