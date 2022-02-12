import math

R = float(input("Введите значение внешнего радиуса окружности: "))
r = float(input("Введите значение внутреннего радиуса окружности: "))
SR = math.pi * (R**2)
Sr = math.pi * (r**2)
S = SR - Sr
S = float('{:.3f}'.format(S))
print('Площадь кольца = ', S)