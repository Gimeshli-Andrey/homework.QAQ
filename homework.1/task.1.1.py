# task 01 == Виправте синтаксичні помилки
print("Hello", end = " ")
print("world!")

# task 02 == Виправте синтаксичні помилки
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")

# task 03  == Вcтавте пропущену змінну у ф-цію print
for letter in "Hello world!":
    print(letter)

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
apples = 2
banana = apples * 4
print(banana)

# task 05 == виправте назви змінних
storona_1 = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4
print(storona_1,storona_2,storona_3,storona_4)

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
storona_1 = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4
perimeter = storona_1 + storona_2 + storona_3 + storona_4
print(f"Периметр фігури: {perimeter}")


"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""
яблуні: int = 4
груші = яблуні + 5
сливи = яблуні - 2
всього_дерев = яблуні + груші + сливи
print("Всього дерев у саду:", всього_дерев)

# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
температура_до_обіду = 5
температура_після_обіду = температура_до_обіду - 10
температура_надвечір = температура_після_обіду + 4
print("Температура надвечір:", температура_надвечір, "градусів")

# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
хлопчики = 24
дівчатка = хлопчики // 2
хлопчики_прийшли = хлопчики - 1
дівчатка_прийшли = дівчатка - 2
всього_дітей = хлопчики_прийшли + дівчатка_прийшли
print("Сьогодні у театральному гуртку:", всього_дітей, "дітей")

# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
перша_книжка = 8
друга_книжка = перша_книжка + 2
третя_книжка = (перша_книжка + друга_книжка) / 2
всього_вартість = перша_книжка + друга_книжка + третя_книжка
print("Вартість усіх книжок:", всього_вартість, "грн.")