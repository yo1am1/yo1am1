#шахматы

print("Сначала проверим туру...")
rock_x1 = int(input("Введите номер столбика (начальное положение):"))
rock_y1 = int(input("Введите номер строки (начальное положение):"))
rock_x2 = int(input("Введите номер столбика (конечное положение):"))
rock_y2 = int(input("Введите номер строки (конечное положение):"))

if (rock_x1 == rock_x2 and rock_y1 != rock_y2) or (rock_x1 != rock_x2 and rock_y1 == rock_y2):
    print("YES")
else:
    print("NO")

print("После - слона...")
bishop_x1 = int(input("Введите номер столбика (начальное положение):"))
bishop_y1 = int(input("Введите номер строки (начальное положение):"))
bishop_x2 = int(input("Введите номер столбика (конечное положение):"))
bishop_y2 = int(input("Введите номер строки (конечное положение):"))

if abs(bishop_x1 - bishop_x2) == abs(bishop_y1 - bishop_y2):
    print("YES")
else:
    print("NO")

print("Конь...")
horse_x1 = int(input("Введите номер столбика (начальное положение):"))
horse_y1 = int(input("Введите номер строки (начальное положение):"))
horse_x2 = int(input("Введите номер столбика (конечное положение):"))
horse_y2 = int(input("Введите номер строки (конечное положение):"))

if abs(horse_x1 - horse_x2) == 1 and abs(horse_y1 - horse_y2) == 2 or abs(horse_x1 - horse_x2) == 2 and abs(horse_y1 - horse_y1) == 1:
    print('YES')
elif horse_x1 == horse_x2 and horse_y1 == horse_y2:
    print("YES")
else:
    print('NO')
"""
print("Пешка...")
pawn_x1 = int(input("Введите номер столбика (начальное положение):"))
pawn_y1 = int(input("Введите номер строки (начальное положение):"))
pawn_x2 = int(input("Введите номер столбика (конечное положение):"))
pawn_y2 = int(input("Введите номер строки (конечное положение):"))

if pawn_x1 == pawn_x2 and (pawn_y1 != pawn_y2 or pawn_y1 == pawn_y2):
    if pawn_y1 == 2 and (pawn_y2 - pawn_y1) == {0, 1, 2}:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
"""

print("И наконец... Ферзь!")
queen_x1 = int(input("Введите номер столбика (начальное положение):"))
queen_y1 = int(input("Введите номер строки (начальное положение):"))
queen_x2 = int(input("Введите номер столбика (конечное положение):"))
queen_y2 = int(input("Введите номер строки (конечное положение):"))

if ((queen_x1 == queen_x2 and queen_y1 != queen_y2) or (queen_x1 != queen_x2 and queen_y1 == queen_y2)) or (abs(queen_x1 - queen_x2) == abs(queen_y1 - queen_y2)):
    print("YES")
else:
    print("NO")