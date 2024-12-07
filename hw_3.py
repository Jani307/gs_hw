# Умовні конструкції:
# 1
PASSWORD = 'password123'

user_password = 'aa'  # input('Ведіть пароль: ')
if user_password == PASSWORD:
    print("Ви увійшли в систему")
else:
    print("Неправильний пароль")

# 2
week = {1: 'Понеділок',
        2: 'Вівторок',
        3: 'Середа',
        4: 'Четвер',
        5: "П'ятниця",
        6: 'Субота',
        7: 'Неділя'}
day_number = None
while not day_number:
    try:
        day_number = 5  # int(input('Вкажіть день тижня (ціле число): '))
    except ValueError:
        pass
if day := week.get(day_number):
    print(day)
else:
    print('Ви ввели неправильний номер')

# Цикли
# 1
number = 1.5  # float(input('Введіть число: '))
[print(f'{number} * {x} = {number*x}') for x in range(1, 11)]

# 2
print(sum(list(range(23, 5, -2))))

# 3
from functools import reduce
number = 4  # int(input("Введіть число: "))
print(reduce(lambda x, y: x * y, range(1, number+1), 1), '\n')

# 4
[print(x) for x in range(2, 51, 2)]

# 5
number = 58
for divider in range(2, number):
    if not (number % divider):
        print(f'Число {number} не є простим.')
        break
else:
    print(f'Число {number} - просте.')

