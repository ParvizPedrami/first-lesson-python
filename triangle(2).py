import math

q1 = float (input('Введите число 1: '))
q2 = float (input('Введите число 2: '))
q3 = float (input('Введите число 3: '))


if q1 < q2 +q3 and q2 < q1 + q3 and q3 < q1 + q2:
    print("true")

else:
    print("false")

input()
