print('//calculator')
import math

f = int(input('Select a function: \nAddition -- 1\nSubtraction -- 2\nMultiply -- 3\nDivision -- 4\nSquaring -- 5\nSquare Root -- 6\nSine -- 7\nCosine -- 8\n '))


if f == 1:
    x1 = int(input('Enter the first number: '))
    x2 = int(input('Enter the second number: '))
    r = x1 + x2
elif f == 2:
    x1 = int(input('Enter the first number: '))
    x2 = int(input('Enter the second number: '))
    r = x1 - x2
elif f == 3:
    X1 = int(input('Enter the first number: '))
    X2 = int(input('Enter the second number: '))
    r = X1 * X2
elif f == 4:
    X1 = int(input('Enter the first number: '))
    X2 = int(input('Enter the second number: '))
    r = float(x1 / x2)
elif f == 5:
    x = int(input('Enter the number: '))
    r = x * x

elif f == 6:
    x = int(input('Enter the number: '))
    sqrt = x ** (0.5)
    r = sqrt

elif f == 7:
    x = int(input('Enter the number: '))
    r = math.sin(x)

elif f == 8:
    x = int(input('Enter the number: '))
    r = math.cos(x)

print('answer:', r)

input("press E to exit")
if input == e:
    exit #stand by for input
