import sys
from pathlib import Path
from colorama import Fore, Style, init


def print_tree(root: Path, prefix: str = "") -> None:

    items = list(root.iterdir())
    items.sort(key=lambda p: (p.is_file(), p.name.lower()))

    for index, item in enumerate(items):
        is_last = index == len(items) - 1
        connector = "└── " if is_last else "├── "

        if item.is_dir():

            print(prefix + connector + Fore.CYAN + item.name + Style.RESET_ALL)

            next_prefix = prefix + ("    " if is_last else "│   ")
            print_tree(item, next_prefix)
        else:

            print(prefix + connector + Fore.GREEN + item.name + Style.RESET_ALL)


def main() -> None:
    init(autoreset=True)

    if len(sys.argv) != 2:
        print("Помилка: потрібно передати шлях до директорії.")
        print("Приклад: python hw03.py /шлях/до/папки")
        return

    path_str = sys.argv[1]
    root = Path(path_str)

    if not root.exists():
        print(f"Помилка: шлях не існує -> {root}")
        return

    if not root.is_dir():
        print(f"Помилка: шлях не веде до директорії -> {root}")
        return

    print(Fore.CYAN + root.name + Style.RESET_ALL)
    print_tree(root)


if __name__ == "__main__":
    main()