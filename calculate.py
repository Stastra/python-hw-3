"""" Покращити програму calculate (файл calculate_raw.py) яка була створена на лекції 
функцією виконання арифметичної операції в одній строчці. А також розширена новими 
арифметичними операціями.
Можна використовувати вихідний код вашої програми виконання відповідного ДЗ, 
але попередньо повинні бути виправлені помилки.
Програма має задовольняти наступні потреби:

Створити файл calculate.py
Программа повина зчитувати аргументи командної строки (за допомогою модуля sys) 
і виконувати арифметичні операції.
Необхідна підтримка 5 базових арифметичних операцій: +, -, *, /, % (додавання, віднімання,
 множення, ділення, остача від ділення). Додано нову операцію - %.
Результат виконання арифметичної операції потрібно виводити у консоль.
Программа повинна адекватно оброблювати помилки.
Программа повинна запускатись наступним чином: python calculate.py 2 + 2 або 
python calculate.py 2+2
Приклади:
python calculate.py 2 + 2 -> 4
python calculate.py 2 - 200 -> -198
python calculate.py 2 * 8 -> 16
python calculate.py 200 / 2 -> 100
python calculate.py 3+3 -> 6
python calculate.py 100-20 -> 80
python calculate.py 4*4 -> 16
python calculate.py 25/2 -> 12.5
Заборонено використовувати eval для обчислення результату.
Повинна бути створена і використана функція обчислення def calc(left_operand, right_operand, operation) 
яка повертає результат арифметичного обчислення. """

import sys

print(sys.argv)

if len(sys.argv) != 4:
    print('Arg len should be 4')
    sys.exit()


left_operand = sys.argv[1]
right_operand = sys.argv[3]

operation = sys.argv[2]

allowed_operations = ['+', '-', '/', '*', '%']

if operation not in allowed_operations:
    print('Operation is not allowed')
    sys.exit()
try:
    left_operand = int(left_operand)
    right_operand = int(right_operand)
except ValueError:
    print('Left and Right operands must be int')
    sys.exit()

if operation == '/' and right_operand == 0:
    print('Division by zero is not allowed')
    sys.exit()


match operation:
    case '+':
        print(left_operand + right_operand)
    case '-':
        print(left_operand - right_operand)
    case '*':
        print(left_operand * right_operand)
    case '/':
        print(left_operand / right_operand)
    case '%':
        print(left_operand % right_operand)


    





