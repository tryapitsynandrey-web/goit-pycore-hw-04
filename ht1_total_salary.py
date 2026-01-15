from pathlib import Path

def total_salary(path: str) -> tuple[int, float]:
    total = 0
    count = 0

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                _, salary = line.split(",")
                total += int(salary)
                count += 1

        if count == 0:
            return 0, 0

        return total, total / count

    except FileNotFoundError:
        print("Файл не знайдено")
        return 0, 0


if __name__ == "__main__":
    base_dir = Path(__file__).parent
    salary_path = base_dir / "salary_file.txt"

    total, average = total_salary(salary_path)

    print("Звіт по заробітній платі")
    print("------------------------")
    print(f"Загальна сума: {total}")
    print(f"Середня заробітна плата: {average}")