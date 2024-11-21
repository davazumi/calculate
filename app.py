def function(calc):
    """ Функция, принимающая строку от пользователя и возвращающая строку """
    result = None
    list_letter = ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть',
                   'семь', 'восемь', 'девять', 'десять', 'одиннадцать',
                   'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать',
                   'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
    list_ten = ['двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят',
                'семьдесят', 'восемьдесят', 'девяносто']
    list_hundred = ['сто', 'двести', 'триста', 'четыреста', 'пятьсот',
                    'шестьсот', 'семьсот', 'восемьсот', 'девятьсот']
    list_thousand = ['тысяча', 'две тысячи', 'три тысячи', 'четыре тысячи',
                     'пять тысяч', 'шесть тысяч', 'семь тысяч', 'восемь тысяч',
                     'девять тысяч']
    list_num = []

    for ten in list_ten:
        for num in [''] + list_letter[1:10]:
            if num != '':
                list_letter.append(ten + ' ' + num)
            else:
                list_letter.append(ten + num)

    for hundred in list_hundred:
        for ten in [''] + list_letter[1:100]:
            if ten != '':
                list_letter.append(hundred + ' ' + ten)
            else:
                list_letter.append(hundred + ten)

    for thousand in list_thousand:
        for hundred in [''] + list_letter[1:1000]:
            if hundred != '':
                list_letter.append(thousand + ' ' + hundred)
            else:
                list_letter.append(thousand + hundred)

    for num in range(0, 10000):
        list_num.append(num)

    if '  ' in calc or calc[0] == ' ' or calc[-1] == ' ':
        print('Ошибка ввода')
        return True
    calc = calc.replace('минус', '-')
    calc = calc.replace('плюс', '+')
    calc = calc.replace('умножить на', '*')
    calc = calc.replace('скобка открывается', '(')
    calc = calc.replace('скобка закрывается', ')')
    for indx, num in enumerate(reversed(list_letter[0:100])):
        calc = calc.replace(num, str(list_num[100 - indx - 1]))    
    try:
        result = eval(calc)
    except SyntaxError:
        print('Ошибка ввода')
    except NameError:
        print('Ошибка ввода')
    
    if result != None:
        calc = calc.replace(' ', '')
        if ('**' in calc or '++' in calc or calc[0] == '+' or '++' in calc or
            '---' in calc or '-+' in calc or '+--' in calc or '*--' in calc or
            calc.find('--') == 0):
            print('Ошибка ввода')
            return True
        else:
            try:
                print(list_letter[list_num.index(result)])
            except ValueError:
                print('Ошибка ввода')

function(input('Введите выражение: '))
input('Введите Enter для выхода')
