# 1-vazifa
#Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing


ismlar = ['Ibrohim', 'Ismoil', 'Diyor', 'Eldiyor', 'Abdulloh']
for ism in ismlar:
    print("Salom qande!", ism)
    print("Ha do'stlar", ism)
print("Kod 10 marta takrorlandi")



# 2-vazifa
#10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqaring.


toq_sonlar = list(range(1,100,2))
for square in toq_sonlar:
    print(f"{square}ning kubi {square**3} ga teng")



# 3-vazifa
#Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, va kinolar degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.



kinolar = []
print("Filmlar odatda tomosha qilasizmi")
for n in range(5):
    kinolar.append(input(f"{n+1}inchi eng sevimli kinolaringizni kirg'izing bg'atan: "))
movies = (f"Shular sizning sevimli kinolaringiz ekan {kinolar}")
print(movies)