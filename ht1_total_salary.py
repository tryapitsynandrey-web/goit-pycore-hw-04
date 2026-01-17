"""Домашнє завдання 1: Обчислення загальної та середньої заробітної плати.

Модуль зчитує текстовий файл, у якому кожен непорожній рядок має формат:
    <ім'я_працівника>,<зарплата>

На основі цих даних функція повертає загальну суму зарплат
та їх середнє арифметичне значення.
"""

from __future__ import annotations

from pathlib import Path
from typing import Tuple


def total_salary(path: str | Path) -> Tuple[int, float]:
    """Обчислює загальну та середню заробітну плату з текстового файлу.

    Аргументи:
        path: Шлях до текстового файлу. Кожен непорожній рядок файлу
            повинен мати формат "ім'я,зарплата".

    Повертає:
        Кортеж (total, average), де:
            - total — загальна сума всіх коректних зарплат (int)
            - average — середня заробітна плата (float)
            
    Примітки:
        - Рядки з некоректним форматом ігноруються, програма не завершується з помилкою.
        - Функція навмисно зроблена стійкою до реальних проблем із даними.
    """

    file_path = Path(path)
    total_salary_amount: int = 0
    valid_rows_count: int = 0

    try:
        with file_path.open("r", encoding="utf-8") as file:
            for raw_line in file:
                line = raw_line.strip()
                if not line:
                    continue

                # Для підвищення надійності розділяємо рядок лише за першою комою
                parts = line.split(",", 1)
                if len(parts) != 2:
                    # Некоректний рядок: відсутня кома-роздільник
                    continue

                _, salary_str = parts[0].strip(), parts[1].strip()
                if not salary_str:
                    # Некоректний рядок: значення зарплати порожнє
                    continue

                try:
                    salary_value = int(salary_str)
                except ValueError:
                    # Некоректний рядок: зарплата не може бути перетворена у число
                    continue

                total_salary_amount += salary_value
                valid_rows_count += 1

    except FileNotFoundError:
        print("Файл не знайдено")
        return 0, 0.0

    if valid_rows_count == 0:
        return 0, 0.0

    average_salary = total_salary_amount / valid_rows_count
    return total_salary_amount, float(average_salary)


def main() -> None:
    """Точка входу для демонстраційного запуску модуля з консолі."""

    base_dir = Path(__file__).parent
    salary_path = base_dir / "salary_file.txt"

    total, average = total_salary(salary_path)

    print("Звіт по заробітній платі")
    print("------------------------")
    print(f"Загальна сума: {total}")
    print(f"Середня заробітна плата: {average}")


if __name__ == "__main__":
    main()