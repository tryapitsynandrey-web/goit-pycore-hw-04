"""Домашнє завдання 3: Візуалізація структури директорії з кольоровим виведенням.

Скрипт приймає шлях до директорії як аргумент командного рядка та виводить
структуру цієї директорії (піддиректорії та файли) у вигляді дерева.

Вимоги:
- шлях до директорії передається як аргумент при запуску;
- рекурсивний обхід директорій;
- використання colorama для кольорового виведення;
- перевірка помилок (шлях не існує / не є директорією);
- обробка PermissionError на iterdir() та під час входу в підпапки.
"""

from __future__ import annotations

import sys
from pathlib import Path

from colorama import Fore, Style, init


def _safe_iterdir(directory: Path) -> list[Path]:
    """Безпечно повертає список елементів директорії.

    Аргументи:
        directory: Директорія, вміст якої потрібно прочитати.

    Повертає:
        Список шляхів (Path). Якщо доступ заборонено — порожній список.

    Примітки:
        - PermissionError перехоплюється, щоб скрипт не падав на реальних системах.
    """

    try:
        return list(directory.iterdir())
    except PermissionError:
        return []


def _print_tree(root: Path, prefix: str = "") -> None:
    """Рекурсивно друкує дерево директорій.

    Аргументи:
        root: Директорія для обходу.
        prefix: Відступ для коректного малювання дерева.

    Примітки:
        - Директорії друкуються окремим кольором, файли — іншим.
        - Якщо доступ до папки заборонено, виводиться позначка і рекурсія не продовжується.
        - За замовчуванням не заходимо в symlink-директорії, щоб уникнути циклів та "вилазок" за межі структури.
    """

    items = _safe_iterdir(root)
    if not items and root.exists():
        # Якщо директорія існує, але список порожній, можливі два сценарії:
        # 1) вона реально порожня; 2) немає доступу (PermissionError) і ми повернули [].
        # Визначити це без додаткових спроб складно, але можна спробувати відкрити ще раз.
        try:
            next(root.iterdir())
        except PermissionError:
            print(prefix + "└── " + Fore.RED + "[Немає доступу]" + Style.RESET_ALL)
            return
        except StopIteration:
            return

    # Сортуємо: спочатку папки, потім файли; назви — у нижньому регістрі для стабільності.
    items.sort(key=lambda path: (path.is_file(), path.name.lower()))

    for index, item in enumerate(items):
        is_last = index == len(items) - 1
        connector = "└── " if is_last else "├── "

        if item.is_dir():
            # Якщо це symlink-директорія — не заходимо всередину, щоб уникнути циклів.
            if item.is_symlink():
                print(prefix + connector + Fore.CYAN + item.name + Style.RESET_ALL + Fore.YELLOW + " [symlink]" + Style.RESET_ALL)
                continue

            print(prefix + connector + Fore.CYAN + item.name + Style.RESET_ALL)

            next_prefix = prefix + ("    " if is_last else "│   ")
            # Обхід підпапки: можливий PermissionError вже всередині _safe_iterdir().
            _print_tree(item, next_prefix)
        else:
            print(prefix + connector + Fore.GREEN + item.name + Style.RESET_ALL)


def main() -> None:
    """Точка входу для запуску скрипта з командного рядка."""

    init(autoreset=True)

    if len(sys.argv) != 2:
        print("Помилка: потрібно передати шлях до директорії.")
        print("Приклад: python ht3_colorama.py /шлях/до/директорії")
        return

    root = Path(sys.argv[1]).expanduser()

    if not root.exists():
        print(f"Помилка: шлях не існує -> {root}")
        return

    if not root.is_dir():
        print(f"Помилка: шлях не веде до директорії -> {root}")
        return

    print(Fore.CYAN + f"{root.name}/" + Style.RESET_ALL)
    _print_tree(root)


if __name__ == "__main__":
    main()