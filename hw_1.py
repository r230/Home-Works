import math

#Условие
a = 1
b = 2
c = 3
print('Найти результат выражения для произвольных значений:')

print('e = a + b * (c / 2)')
e = a + b * (c / 2)
print('e =', e,'\n')

print('e2 = (a2 + b2) % 2')
e2 = (a**2 + b**2) % 2
print('e2 =', e2,'\n')

print('e3 = (a + b) / 12 * c % 4 + b')
e3 = (a + b) / 12 * c % 4 + b
print('e3 =', e3,'\n')

print('e4 = (a - b * c) / (a + b) % c')
e4 = (a - b * c) / (a + b) % c
print('e4 =', e4,'\n')

print('e5 = |a - b| / (a + b)3 - cos( c )')
e5 = math.fabs(a - b)/(a + b)**3 - math.cos(c)
print('e5 =', e5,'\n')

print('e6 = (ln( 1 + c) / -b)4 + | a |')
e6 = (math.log(1 + c) / -b)**4 + math.fabs(a)
print('e6 =', e6,'\n')
