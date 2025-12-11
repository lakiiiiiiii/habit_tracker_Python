import json

def load_data():# Открытие и чтение файла, если файл отсутствует тогда, создает новый
    try:
        with open('habits.json', 'r', encoding='utf-8') as f:
            data = json.load(f)

    except FileNotFoundError:
        data = {}
    return data

def save_data(data): # Открытие файла на запись
    with open('habits.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def add_habits(data):
    text_name = input('Введите название привычки:')

    if not text_name or text_name in data:
        print('Некорректное название или привычка уже существует')
        return

    text_description = input('Введите описание(по желанию): ')

    text_periodicity = input('Введите периодичность(по желанию): ')

    text_time = input('Введите затраченное время(по желанию в минутах или часах)')

    data[text_name] = {
        "описание": text_description,
        "периодичность": text_periodicity,
        "время": text_time,
        "история": []
    }
    save_data(data)
