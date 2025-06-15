# Переменные предназначены для хранения данных.
name='Artem'
my_age=27
group=['Python',47]

# Основные типы данных:
# Тип bool представляет два логических значения: True и False 
isAlive = True
print(isAlive)
isMarried = False
print(isMarried) 
print(isAlive==isMarried)
# Тип int представляет целое число
age = 21
print("Возраст:", age)
# По умолчанию стандартные числа расцениваются как числа в десятичной системе. Но Python также поддерживает числа в двоичной, восьмеричной и шестнадцатеричной системах.
# Для указания, что число представляет двоичную систему, перед числом ставится префикс 0b:
a = 0b11
b = 0b1011
print(a)
print(b)
# Для указания, что число представляет восьмеричную систему, перед числом ставится префикс 0o:
a = 0o7
b = 0o11
print(a)
print(b)
# Для указания, что число представляет шестнадцатеричную систему, перед числом ставится префикс 0x:
a = 0x0A
b = 0xFF
print(a)
print(b) 
# Тип float представляет число с плавающей точкой
height = 1.68
print(height)
x = 3.9e3
print(x)  # 3900.0
# Тип complex представляет комплексные числа в формате вещественная_часть+мнимая_частьj - после мнимой части указывается суффикс j
complexNumber = 1+2j
print(complexNumber)
# Тип str представляет строки.
message = "Hello World!"
print(message)
text = ("Laudate omnes gentes laudate "
        "Magnificat in secula ")
print(text)
'''
Это комментарий
'''
text = '''Laudate omnes gentes laudate
Magnificat in secula
Et anima mea laudate
Magnificat in secula 
'''
print(text)
# Списки
numbers = [1, 2, 3, 4, 5]
print(numbers)
people = ["Tom", "Sam", "Bob"]
print(people)
listInList=[['adw','ewd'],[12,2]]
# Кортежи
tom = ("Tom", 23)
print(tom) 
tom_ = ("Tom", 37, "Google", "software developer")
print(tom_[0])       # Tom
print(tom_[1])   
# Словари
users = {1: "Tom", 2: "Bob", 3: "Bill"}
print(users)
user = {
    "+11111111": "Tom",
    "+33333333": "Bob",
    "+55555555": "Alice"
}
print(users["+11111111"])      
users["+33333333"] = "Bob Smith"
print(users["+33333333"]) 
# Множества
users_ = {"Tom", "Bob", "Alice", "Tom"}
print(users_)
users__ = frozenset({"Tom", "Bob", "Alice"})