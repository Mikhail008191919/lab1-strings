<<<<<<< HEAD
def to_upper(s):
    return s.upper()

def to_lower(s):
    return s.lower()

if __name__ == "__main__":
    text = input("Введите строку: ")
    print("Верхний регистр:", to_upper(text))
    print("Нижний регистр:", to_lower(text))
=======
# Функция для работы со строками: смена регистра
# Вариант 2b: Приведение всех букв к верхнему и нижнему регистру

def convert_case(input_string):
    """
    Функция принимает строку и возвращает её в верхнем и нижнем регистре.
    """
    # .upper() - встроенный метод Python для перевода в ВЕРХНИЙ РЕГИСТР
    upper_case = input_string.upper()
    
    # .lower() - встроенный метод Python для перевода в нижний регистр
    lower_case = input_string.lower()
    
    return upper_case, lower_case

# Основная часть программы для демонстрации работы
if __name__ == "__main__":
    print("Программа демонстрации смены регистра строки")
    
    # Запрос строки у пользователя
    user_input = input("Введите любую строку (например, 'Привет Мир'): ")
    
    # Вызов функции
    upper_result, lower_result = convert_case(user_input)
    
    # Вывод результатов
    print("\n--- Результаты ---")
    print(f"Верхний регистр: {upper_result}")
    print(f"Нижний регистр:  {lower_result}")
>>>>>>> 19162ae96f40e579579d86f31026d21014c3ecf1
