def get_cats_info(path: str) -> list:
    cats = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                cat_id, name, age = line.split(",")

                cat_info = {
                    "id": cat_id,
                    "name": name,
                    "age": age
                }

                cats.append(cat_info)

        return cats

    except FileNotFoundError:
        print("Файл не знайдено")
        return []

    except ValueError:
        print("Помилка у форматі даних файлу")
        return []

if __name__ == "__main__":
    cats_info = get_cats_info("cats_file.txt")

    print("Список котів")
    print("------------")

    for cat in cats_info:
        print(f"ID:   {cat['id']}")
        print(f"Ім'я: {cat['name']}")
        print(f"Вік:  {cat['age']}")
        print()