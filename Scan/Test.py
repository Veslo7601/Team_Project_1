from pathlib import Path

def find_folder(folder_name, search_path="."):
    # Перетворюємо шлях в об'єкт Path
    search_path = Path(search_path)

    # Шукаємо вказану папку у вказаному шляху (або поточному, якщо шлях не вказано)
    for path in search_path.iterdir():
        if path.is_dir() and path.name == folder_name:
            # Якщо папка знайдена, повертаємо повний шлях до неї
            return path

    # Якщо папка не знайдена, повертаємо None
    return None

# Приклад використання
folder_name = "Test"
folder_path = find_folder(folder_name, "C:/Users/VESLO/HomeWork2/Team_Project_1/")
if folder_path:
    print(f"Шлях до папки '{folder_name}': {folder_path}")
else:
    print(f"Папку '{folder_name}' не знайдено.")