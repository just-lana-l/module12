print('Задача 9. Недоделка')

# Вы пришли на работу в контору по разработке игр,
# целевая аудитория которых - дети и их родители.
# 
# У прошлого программиста было задание
# сделать две игры в одном приложении, чтобы пользователь мог выбирать одну из них.
# 
# Однако программист, на место которого вы пришл
# и, перед увольнением не успел сделать эту задачу и оставил только небольшой шаблон проекта.
# 
# Используя этот шаблон,
# реализуйте игры «Камень, ножницы, бумага» и «Угадай число».
# 
# Правила игры «Камень, ножницы, бумага»:
# программа запрашивает у пользователя строку
# и выводит победил он или проиграл.
# 
# Камень бьёт ножницы, ножницы режут бумагу, бумага кроет камень.
# 
# Правила игры “Угадай число”:
# программа запрашивает у пользователя число до тех пор, пока он его не отгадает.

import random

def rock_paper_scissors():
  #Здесь будет игра "Камень, ножницы, бумага"
	variations = ["камень", "бумага", "ножницы"]
	print("Камень бьёт ножницы, ножницы режут бумагу, бумага кроет камень.")

	player = input("Выберите: камень, ножницы, бумага? ")
	computer = random.choice(variations)

	print(f"Твой выбор: {player}. Выбор компьютера: {computer}.")

	if player == computer:
		print("Ничья")
	elif player =="камень" and computer == "ножницы":
		print("ты победил!")
	elif player == "бумага" and computer == "камень":
		print ("Ты победил!")
	elif player == "ножницы" and computer == "бумага":
		print ("Ты победил!")
	else:
		print('Выиграл компьютер')
	mainMenu()


def guess_the_number():
	count = 0
	min_num = 0
	max_num = 100

	while True:
		n = (min_num + max_num) // 2
		print('Это число больше, меньше или равно: ', n)
		answer = int(input('больше - 1, меньше - 2, равно - 3: ' ))
		count += 1
		print('Попытка: ', count)
		if answer == 1: # больше
			# Если число больше загаданного это диапазаон от 50 до 100. 
			min_num = n - 1
		elif answer == 2: # меньше
			# если меньше 50, то 50 это новый максимум
			max_num = n + 1
		else: # иначе число угадано и выход
			print('Верно! Число попыток:', count)
			break

def mainMenu():
	var = int(input('Во что играем? 1 - Камень, ножницы, бумага. 2 - Угадай число. '))
	#Здесь главное меню игры
	if var == 1:
		rock_paper_scissors()
	elif var == 2:
		guess_the_number()

mainMenu()