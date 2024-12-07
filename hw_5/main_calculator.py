import calculator

user_a = float(input('Enter first number: '))
user_b = float(input('Enter second number: '))
user_operation = input('Enter operation (+ - * /): ')

match user_operation:
    case '+':
        print(calculator.add(user_a, user_b))
    case '-':
        print(calculator.subtract(user_a, user_b))
    case '*':
        print(calculator.multiply(user_a, user_b))
    case '/':
        print(calculator.divide(user_a, user_b))
