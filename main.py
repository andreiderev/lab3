# Практична робота: Робота зі словником
# Тімлід: Деревцов Андрій
# Учасник команди: Басанець Олександр

people = {
    "Коваленко Олександр": {"height": 182, "gender": "ч"},
    "Шевченко Марія": {"height": 165, "gender": "ж"},
    "Бондаренко Дмитро": {"height": 178, "gender": "ч"},
    "Ткаченко Анна": {"height": 170, "gender": "ж"},
    "Мельник Максим": {"height": 185, "gender": "ч"},
    "Кравченко Олена": {"height": 162, "gender": "ж"},
    "Олійник Артем": {"height": 175, "gender": "ч"},
    "Поліщук Софія": {"height": 168, "gender": "ж"},
    "Савченко Ігор": {"height": 190, "gender": "ч"},
    "Лисенко Катерина": {"height": 164, "gender": "ж"}
}


def print_all(data):
    """Виведення всіх записів словника."""
    if not data:
        print("Словник порожній.")
        return
    print("\nСписок усіх осіб:")
    for name, info in data.items():
        print(f"  {name} — зріст: {info['height']} см, стать: {info['gender']}")


def add_record(data):
    """Додавання нового запису до словника."""
    name = input("Введіть прізвище та ім'я: ").strip()
    if not name:
        print("Помилка: ім'я не може бути порожнім.")
        return
    if name in data:
        print("Така особа вже є у словнику.")
        return

    try:
        height = int(input("Введіть зріст (у см): "))
        if height <= 0 or height > 250:
            raise ValueError("Некоректне значення зросту.")
    except ValueError as e:
        print(f"Помилка введення зросту: {e}")
        return

    gender = input("Введіть стать (ч/ж): ").strip().lower()
    if gender not in ("ч", "ж"):
        print("Помилка: потрібно ввести 'ч' або 'ж'.")
        return

    data[name] = {"height": height, "gender": gender}
    print(f"Запис '{name}' успішно додано.")


def delete_record(data):
    """Видалення запису зі словника за ключем."""
    name = input("Введіть прізвище та ім'я для видалення: ").strip()
    try:
        del data[name]
        print(f"Запис '{name}' видалено.")
    except KeyError:
        print(f"Помилка: запису '{name}' не знайдено у словнику.")


def print_sorted(data):
    """Перегляд вмісту словника за відсортованими ключами."""
    if not data:
        print("Словник порожній.")
        return
    print("\nСписок осіб (відсортовано за алфавітом):")
    for name in sorted(data.keys()):
        info = data[name]
        print(f"  {name} — зріст: {info['height']} см, стать: {info['gender']}")


def average_men_height(data):
    """Обчислення середнього зросту чоловіків."""
    men_heights = [info["height"] for info in data.values() if info["gender"] == "ч"]
    try:
        avg = sum(men_heights) / len(men_heights)
        print(f"\nКількість чоловіків: {len(men_heights)}")
        print(f"Середній зріст чоловіків: {avg:.2f} см")
    except ZeroDivisionError:
        print("\nУ словнику немає записів про чоловіків.")


def find_min_max_height(data):
    """Пошук найвищої та найнижчої особи у словнику (реалізував Басанець Олександр)."""
    if not data:
        print("\nСловник порожній, пошук неможливий.")
        return

    tallest = max(data.items(), key=lambda item: item[1]["height"])
    shortest = min(data.items(), key=lambda item: item[1]["height"])

    print(f"\nНайвища особа: {tallest[0]} ({tallest[1]['height']} см, стать: {tallest[1]['gender']})")
    print(f"Найнижча особа: {shortest[0]} ({shortest[1]['height']} см, стать: {shortest[1]['gender']})")


def main():
    while True:
        print("\n МЕНЮ ")
        print("1. Вивести всі записи")
        print("2. Додати запис")
        print("3. Видалити запис")
        print("4. Вивести записи за відсортованими ключами")
        print("5. Визначити середній зріст чоловіків")
        print("6. Знайти найвищу та найнижчу особу")
        print("0. Вихід")

        choice = input("Оберіть дію: ").strip()

        if choice == "1":
            print_all(people)
        elif choice == "2":
            add_record(people)
        elif choice == "3":
            delete_record(people)
        elif choice == "4":
            print_sorted(people)
        elif choice == "5":
            average_men_height(people)
        elif choice == "6":
            find_min_max_height(people)
        elif choice == "0":
            print("Роботу завершено.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()