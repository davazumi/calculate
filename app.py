def function(calc):
    """ Функция, принимающая строку от пользователя и возвращающая строку """
    result = None #результат еще не определен
    list_letter = ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть',
                   'семь', 'восемь', 'девять', 'десять', 'одиннадцать',
                   'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать',
                   'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
    list_ten = ['двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят',
                'семьдесят', 'восемьдесят', 'девяносто']
    list_hundred = ['сто', 'двести', 'триста', 'четыреста', 'пятьсот',
                    'шестьсот', 'семьсот', 'восемьсот', 'девятьсот']
    list_num = [] 

    for ten in list_ten:
        for num in [''] + list_letter[1:10]:
            if num != '': # позволяет корректо обрабатовать случай когда к десятку добавляется 0
                list_letter.append(ten + ' ' + num)
            else:
                list_letter.append(ten + num) #комбинация десятков с еденицами 

    for hundred in list_hundred:
        for ten in [''] + list_letter[1:100]: #комбинация тысяч с сотнями
            if ten != '':
                list_letter.append(hundred + ' ' + ten) #если ten пустая строка то добавляем комбинацию сотни и десятки
            else:
                list_letter.append(hundred + ten)
    for num in range(0, 10000): #заполнение списка чисел
        list_num.append(num)

    if '  ' in calc or calc[0] == ' ' or calc[-1] == ' ': #проверка на ошибку ввода 
        print('Ошибка ввода')
        return True
    calc = calc.replace('минус', '-')
    calc = calc.replace('плюс', '+')
    calc = calc.replace('умножить на', '*')
    calc = calc.replace('скобка открывается', '(')
    calc = calc.replace('скобка закрывается', ')')
    for indx, num in enumerate(reversed(list_letter[0:100])):  #для перебора элементов списка list_letter, начиная с конца до 100-го элемента
        calc = calc.replace(num, str(list_num[100 - indx - 1]))    #замена чисел если в calc находится "относящееся к числу", например, "пятьдесят", то оно будет заменено на "50" 
    try:
        result = eval(calc) # елси есть ошибка 
    except SyntaxError:
        print('Ошибка ввода')
    except NameError:
        print('Ошибка ввода')
    
    if result != None: # Проверка результата
        calc = calc.replace(' ', '') #Удаление пробелов
        if ('**' in calc or '++' in calc or calc[0] == '+' or '++' in calc or #Проверка корректности ввода
            '---' in calc or '-+' in calc or '+--' in calc or '*--' in calc or
            calc.find('--') == 0):
            print('Ошибка ввода')
            return True
        else:
            try:
                print(list_letter[list_num.index(result)]) #Попытка найти индекс результата
            except ValueError:#Обработка исключений Если result не найден в list_num, это приведет к выбросу исключения ValueError.
                print('Ошибка ввода')

function(input('Введите выражение: ')) 
input('Введите Enter для выхода')
