import logging
logging.basicConfig(
    filename='filelog.log',
    filemode = 'a',
    level = logging.INFO,
    encoding='utf-8',
    format = '%(name)s | %(asctime)s | %(levelname)s | %(message)s'
)


Chisla = {}
def Plus (a:int,b:int)->dict:
    S=a+b
    Chisla['Plus']=S
    logging.info('Процесс сложения')
    return Chisla
def Minus (a:int,b:int)->dict:
    S=a-b
    Chisla['Minus']=S
    logging.info('Процесс вычитания')
    return Chisla
def Umnoj (a:int,b:int)->dict:
    S=a*b
    Chisla['Umnoj']=S
    logging.info('Процесс умножения')
    return Chisla
def Del (a:int,b:int)->dict:
    try:
        S=a/b
        logging.info('Процесс деления')
    except ZeroDivisionError:
        print('На ноль делить нельзя')
        logging.error('Пользователь делит на 0 😂😂😂')
        S=None
    finally:
        Chisla['Del']=S
    return Chisla

try:
    logging.info('Берём данные у пользователя')
    a = int(input('Введите int: '))
    b = int(input('Введите int: '))
    do = int(input('Что хотите сделать  '
                   '1-умножить  '
                   '2-сложить  '
                   '3-вычесть  '
                   '4-разделить: '))

    if do == 1:
        print(Umnoj(a, b))
    elif do == 2:
        print(Plus(a, b))
    elif do == 3:
        print(Minus(a, b))
    elif do == 4:
        print(Del(a, b))
    else:
        print('Вы ввели тчо-то не то')
        logging.error('Пользователь не ввёл число от 1 до 4рех')

except ValueError:
    print('Вы ввели не int')
    logging.error('Пользователь ввёл не int')







