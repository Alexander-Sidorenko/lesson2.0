month = int(input("Введите номер месяца "))
if month == 1 or month == 12 or month == 2:
    print('Зима')
elif month >= 3 and month <= 5:
    print('Весна')
elif month >= 6 and month <= 8:
    print('Лето')
elif month >= 9 and month <= 11:
    print('Осень')
else:
    print('Нет такого месяца! Введите от 1 до 12')
