print('Задача 8. НОД')

#Напишите функцию, вычисляющую наибольший общий делитель двух чисел
x = int(input('x: '))
y = int(input('y: '))

def nod(x, y):
	while x != 0 and y != 0:
		if x > y:
			x = x % y
		else:
			y = y % x
	print(x + y)

nod(x, y)