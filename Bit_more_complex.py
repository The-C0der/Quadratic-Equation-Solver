import math

print('This is a quadratic equation sovler. Here x refers to the variable in the equation. ')

a = int(input('Coefficient of x\u00b2 (a):'))
b = int(input('Coefficient of x (b):'))
c = int(input('Constant Term (c):'))

discriminant = (b**2) - (4*a*c)

if discriminant > 0:
    print('There are 2 roots present.')
    first_root = (-b + math.sqrt(discriminant))/(2*a)
    second_root = (-b - math.sqrt(discriminant))/(2*a)
    print('The first root is :', first_root)
    print('The second root is :', second_root)
elif discriminant == 0:
    print('only one root is present.')
    root = (-b + math.sqrt(discriminant))/(2*a)
    print('The first root is :', root)
elif discriminant < 0:
    print('No roots present for this equation')




