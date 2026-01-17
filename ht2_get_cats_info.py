"""Домашнє завдання 2: Зчитування інформації про котів з текстового файлу.

Кожен непорожній рядок файлу повинен мати формат:
    <id>,<ім'я>,<вік>

Функція повертає список словників з ключами: id, name, age.
"""

from __future__ import annotations

from pathlib import Path
from typing import Dict, List


def get_cats_info(path: str | Path) -> List[Dict[str, str]]:
    """Зчитує інформацію про котів з текстового файлу.

    Аргументи:
        path: Шлях до файлу з записами про котів.

    Повертає:
        Список словників, де кожен словник містить:
            - "id": унікальний ідентифікатор кота (рядок)
            - "name": ім'я кота (рядок)
            - "age": вік кота у вигляді рядка
            
    Примітки:
        - Рядки з некоректним форматом ігноруються, щоб уникнути аварійного завершення програми.
        - Якщо ідентифікатор кота дублюється, у результат потрапляє лише перший запис.
    """

    file_path = Path(path)
    cats: List[Dict[str, str]] = []
    seen_ids: set[str] = set()

    try:
        with file_path.open("r", encoding="utf-8") as file:
            for raw_line in file:
                line = raw_line.strip()
                if not line:
                    continue

                # Обмежуємо split, щоб уникнути помилок через зайві коми
                parts = [part.strip() for part in line.split(",", 2)]
                if len(parts) != 3:
                    # Некоректний рядок: очікується рівно три частини
                    continue

                cat_id, name, age = parts
                if not cat_id or not name or not age:
                    # Некоректний рядок: відсутні обов'язкові значення
                    continue

                if cat_id in seen_ids:
                    # Дубльований запис за ідентифікатором — пропускаємо
                    continue

                cats.append({"id": cat_id, "name": name, "age": age})
                seen_ids.add(cat_id)

    except FileNotFoundError:
        print("Файл не знайдено")
        return []

    return cats


def main() -> None:
    """Точка входу для демонстраційного запуску модуля з консолі."""

    base_dir = Path(__file__).parent
    cats_file_path = base_dir / "cats_file.txt"

    cats_info = get_cats_info(cats_file_path)

    print("Список котів")
    print("------------")

    for cat in cats_info:
        print(f"ID:   {cat['id']}")
        print(f"Ім'я: {cat['name']}")
        print(f"Вік:  {cat['age']}")
        print()


if __name__ == "__main__":
    main()