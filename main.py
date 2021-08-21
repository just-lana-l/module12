print('Задача 4. Число наоборот')

# Вводится последовательность чисел,
# которая оканчивается нулём.
#
# Реализуйте функцию,
# которая принимает в качестве аргумента каждое число,
# переворачивает его и выводит на экран.

# Пример:
# Введите число: 1234
# Число наоборот: 4321
# 
# Введите число: 1000
# Число наоборот: 0001
# 
# Введите число: 0
# Программа завершена!
# 
# Дополнительно: добейтесь такого вывода чисел, если в его начале идут нули.
# 
# Введите число: 1230
# Число наоборот: 321
# 
# Кстати, нули, которые мы убрали, называются ведущими.
text = input('Введите текст: ')

letter_request = input('Какую букву ищем: ') 
digit_request = input('Какую цифру ищем: ')

def count_letters(txt, letter, digit):
	count_letter = 0
	count_digit = 0
	for i in text:
		if i == letter:
			count_letter += 1
			
		elif i == digit:
			count_digit +=1

	print(f'Количество букв {letter}: {count_letter}')		
	print(f'Количество цифр {digit}: {count_digit}')


count_letters(text, letter_request, digit_request)
