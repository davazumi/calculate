def text_calculator(expression):
"""Функция для вычисления арифметических выражений, вводимых на русском языке."""
words_to_numbers = {
'ноль': 0, 'один': 1, 'два': 2, 'три': 3, 'четыре': 4, 'пять': 5,
'шесть': 6, 'семь': 7, 'восемь': 8, 'девять': 9, 'десять': 10,
'одиннадцать': 11, 'двенадцать': 12, 'тринадцать': 13,
'четырнадцать': 14, 'пятнадцать': 15, 'шестнадцать': 16,
'семнадцать': 17, 'восемнадцать': 18, 'девятнадцать': 19,
'двадцать': 20, 'тридцать': 30, 'сорок': 40, 'пятьдесят': 50,
'шестьдесят': 60, 'семьдесят': 70, 'восемьдесят': 80,
'девяносто': 90, 'сто': 100, 'двести': 200, 'триста': 300,
'четыреста': 400, 'пятьсот': 500, 'шестьсот': 600, 'семьсот': 700,
'восемьсот': 800, 'девятьсот': 900, 'тысяча': 1000,
}

# Словарь для комбинирования чисел
composite_numbers = []

# Генерация комбинированных чисел от 1 до 9999
for i in range(10000):
num_word = []
if i >= 1000:
num_word.append(words_to_numbers['тысяча'])
i -= 1000
if i >= 100:
hundreds = (i // 100) * 100
num_word.append(next(word for word, num in words_to_numbers.items() if num == hundreds))
i %= 100
if i >= 20:
tens = (i // 10) * 10
num_word.append(next(word for word, num in words_to_numbers.items() if num == tens))
i %= 10
if i > 0:
num_word.append(next(word for word, num in words_to_numbers.items() if num == i))

composite_numbers.append(' '.join(num_word) if num_word else words_to_numbers['ноль'])

# Замены для математики
expression = expression.replace('минус', '-')
expression = expression.replace('плюс', '+')
expression = expression.replace('умножить на', '*')
expression = expression.replace('скобка открывается', '(')
expression = expression.replace('скобка закрывается', ')')

# Обработка текста в числа
for word, num in words_to_numbers.items():
if word in expression:
expression = expression.replace(word, str(num))

try:
# Выполнить вычисление
result = eval(expression)
except (SyntaxError, NameError):
print('Произошла ошибка при обработке выражения!')
return

# Проверка результата
if abs(result) > 9999:
print('Ошибка: результат превышает допустимый предел!')
else:
print('Результат:', composite_numbers[result])

# Приветственное сообщение
print('''Добро пожаловать в текстовый калькулятор!
Вы можете выполнять операции с целыми числами, включая отрицательные,
скобки и неограниченное количество операций. Убедитесь, что результат
не превышает 9999 по модулю.''')

# Ввод выражения пользователем
text_input = input('Введите арифметическое выражение: ')
text_calculator(text_input)
input('Нажмите Enter для выхода')
