from random import *

# Задание 1
print("Задание 1")

n = int(input("Введите трехзначное число: "))

a = n // 100
b = (n - (a*100)) // 10
c = n - (a*100) - (b*10)

print(
	f"Сумма цифр числа {n}: {a+b+c}\n"
	f"Произведение цифр числа {n}: {a*b*c}"
)


# Задание 2
print("\n\nЗадание 2")

# 5 - 101 в двоичной системе
# 6 - 110 в двоичной системе

_and = 5 & 6
_or = 5 | 6
_xor = 5 ^ 6
a = 5 >> 2
b = 5 << 2

print(
	f"5 & 6 = {_and}\n"
	f"5 | 6 = {_or}\n"
	f"5 ^ 6 = {_xor}\n"
	f"5 >> 2 = {a}\n"
	f"5 << 2 = {b}"
)

print(
	"5 и 6 равняется 4, потому что, если умножить цифры 101 "
	"(5 в двоичной системе) на цифры 110 (6 в двоичной системе)"
	"в том порядке как они стоят, то есть 1*1, 0*1, 1*0, то в результате "
	"получится 100 (4 в двоичной системе). То же самое и с операцией ИЛИ, "
	"но тут 1+1=1, то есть True + True все равно True. "
	"Операция XOR предполагает, что значение может быть True только,"
	"если один из символов будет 1, а другой 0\n"
)

print(
	"При сдвиге на два знака вправо числа 5 получилось 1,"
	"потому что 5 в двоичной системе равна 101, а для наглядности 00101, "
	"При сдвиге на два знака вправо остается всего лишь одна цифра, "
	"то есть 00001, что в десятиричной системе равно 1."
	"А при сдвиге влево на два знака 00101 прибавляет к концу два нуля "
	"и преобразуется в итоге в 10100, что в десятиричной системе равно 20."
)


# Задание 3
print("\n\nЗадание 3")

x1 = int(input("Введите число x1: "))
y1 = int(input("Введите число y1: "))

x2 = int(input("Введите число x2: "))
y2 = int(input("Введите число y2: "))

k = int((y1 - y2) / (x1 - x2))
b = int(y2 - k*x2)

if b > 0:
	print(f"Ваше уравнение прямой y={k}x+{b}")
else:
	print(f"Ваше уравнение прямой y={k}x{b}")


# Задание 4
print("\n\nЗадание 4")
en_alphabet = [
	'a', 'b', 'c', 'd', 'e', 'f', 'g',
	'h', 'i', 'j', 'k', 'l', 'm', 'n',
	'o', 'p', 'q', 'r', 's', 't', 'u',
	'v', 'w', 'x', 'y', 'z'
]

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
print(f"Ваше случайное целое число: {randint(a, b)}")

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
print(f"Ваше случайное вещественное число: {uniform(a, b)}")

a = str(input(
	"Введите первую букву (английский алфавит, в нижнем регистре): "
))
b = str(input(
	"Введите первую букву (английский алфавит, в нижнем регистре): "
))
print(
	f"Ваш случайный символ " +
	en_alphabet[randint(en_alphabet.index(a), en_alphabet.index(b))]
)


# Задание 5
print("\n\nЗадание 5")

a = str(input(
	"Введите первую букву (русский алфавит, в нижнем регистре): "
))
b = str(input(
	"Введите вторую букву (русский алфавит, в нижнем регистре): "
))
ru_alphabet = [
	"а", "б", "в" ,"г", "д", "е", "ё", "ж", 
	"з", "и", "й", "к", "л", "м", "н", "о", 
	"п", "р", "с", "т", "у", "ф", "х", "ц", 
	"ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"
]

num_a = ru_alphabet.index(a) + 1
num_b = ru_alphabet.index(b) + 1
n = num_a - num_b - 1 if num_a > num_b else num_b - num_a - 1

print(f"Расположение буквы {a} на {num_a} месте.\n"
	  f"Расположение буквы {b} на {num_b} месте.\n"
	  f"Между ними {n} букв.\n")

# Задание 6
print("\n\nЗадание 6")

a = int(input(
	"Введите номер буквы с 1 до 33: "
))
print(f"{a}-я буква - {ru_alphabet[a - 1]}")

# Задание 7
print("\n\nЗадание 7")

a = int(input("Введите длину 1-ого отрезка: "))
b = int(input("Введите длину 2-ого отрезка: "))
c = int(input("Введите длину 3-го отрезка: "))

if a + b > c and a + c > b and b + c > a:
	print("Треугольник существует!")
	if a != b and a != c and b != c:
		print("Треугольник является разносторонним!")
	elif a == b and a == c and c == b:
		print("Треугольник является равносторонним!")
	else:
		print("Треугольник является равнобедренным!")

else:
	print("Треугольник не существует!")

# Задание 8
print("\n\nЗадание 8")

year = int(input("Введите год: "))
print(
	f"Год {year} является високосным." if year%4 == 0
	else f"Год {year} не является високосным."
)

# Задание 9
print("\n\nЗадание 9")

a = int(input("Введите 1-е число: "))
b = int(input("Введите 2-е число: "))
c = int(input("Введите 3-е число: "))

if a > b and a < c or a < b and a > c:
	print(f"Число {a} является средним относительно {b} и {c}.")
elif b > a and b < c or b < a and b > c:
	print(f"Число {b} является средним относительно {a} и {c}.")
else:
	print(f"Число {c} является средним относительно {a} и {b}.")


# Дополнительные задания
print("\n\nДополнительные задания")


# Задание 1

print("\n\nЗадание 1")
print("Подождите, вот-вот загрузится...")

f = open("passwords.txt","r")

if f.mode == 'r':
	content = f.read()
	full_array = content.split()
	password_array = []
	for el in full_array:
		password_array.append(el.split(";")[1])

password_library = {}

for pswd in password_array:
	if pswd[0] not in password_library:
		password_library[pswd[0]] = []
		password_library[pswd[0]].append(pswd)
	else:
		password_library[pswd[0]].append(pswd)

top = []

for ltr in password_library:
	for pswd in password_library[ltr]:
		n=1
		for word in password_library[ltr]:
			if pswd == word:
				n = n + 1
		if n > 1:
			if {'word': pswd, 'quantity': n} not in top:
				object_ = {}
				object_['word'] = pswd
				object_['quantity'] = n
				if top == [] or object_['quantity'] < top[0]['quantity']:
					top.append(object_)
				else:
					top.insert(0, object_)


n = 1
print("Топ 10 самых популярных паролей:")
while n <= 10:
	print(
		f"{n}. {top[n-1]['word']}, "
		f"его использовали {top[n-1]['quantity']} раз"
	)
	n = n + 1


# Задание 2
print("\n\nЗадание 2")

a = randint(1, 100)

n = 9

b = int(input(
	f"Загадано число от 1 до 100.\n"
	f"Осталось попыток {n} из 10\nУгадайте число: "
))

while n >= 1:
	if b != a:
		n = n - 1
		if a > b:
			b = int(input("\nНеверно. Загаданное число больше.\n"
				f"Осталось попыток {n} из 10\nУгадайте число: "	
			))
		else:
			b = int(input("\nНеверно. Загаданное число меньше.\n"
				f"Осталось попыток {n} из 10\nУгадайте число: "	
			))
	else:
		print("Вы угадали!")
		break
if n == 0:
	print("Попытки закончились...")
