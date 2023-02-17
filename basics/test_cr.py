while True:
    num1 = int (input('Введите число 1: '))
    num2 = int (input('Введите число 2: '))

    operacia = int (input('Какую операцию вы хотите выполнить? \n 1 Сложение \n 2 Вычитание \n 3 Деление \n 4 Умножение \n'))

    if operacia == 1:
        result = num1 + num2
        p = 'сложения'
        print (f'Результат {p} = {result}')
    if operacia == 2:
        result = num1 - num2
        l = 'вычитания'
        print (f'Результат {l} = {result}')
    if operacia == 3:
        try:
            result = float(num1 / num2)
            m = 'деления'
            print (f'Результат {m} = {result}')
        except ZeroDivisionError:
            print('Нельзя делить на 0!')
    if operacia == 4:
        result = num1 * num2
        n = 'умножения'
        print (f'Результат {n} = {result}')