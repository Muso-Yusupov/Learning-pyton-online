#1-vazifa
#Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son kiritsa "Rahmat!", agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.
son = int(input("Juft son kiriting\n"))
if not son%2:##nimaga buni ishlatganimni tushunmadim.
    print("Rahmat!")
else:
    print("Bu son juft son emas")
#2-vazifa
#Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:
#Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
#Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
#Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm
yosh = int(input("Yoshingizni kiriting:\n"))
if yosh<=4 or yosh>=60:
    print("Sizga kirish bepul")
elif yosh<18:
    print("Sizga kirish 10000so'm")
else:
    print("Sizga kirish 20000so'm")



# 3-vazifa
#Foydalanuvchidan ikita son kiritishni so'rang, sonlarni solishtiring va ularning teng yoki katta/kichikligi haqida xabarni chiqaring
sonlar =[]
sonlar in range(1)
sonlar.append(int(input("Son kiriting\n")))
sonlar.append(int(input("Son kiriting\n")))
if sonlar[0]>sonlar[1]:
        print(f"{sonlar[0]} {sonlar[1]} dan katta ekan")
elif sonlar[0]<sonlar[1]:
        print(f"{sonlar[0]} {sonlar[1]} dan kichik ekan")
else:
    print(f"{sonlar[0]} va {sonlar[1]}sonlari teng ekan")

##4-vazifa
#mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang. Savatdagi elementlarni, mahsulotlar ro'yxati bilan solishtiring va qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor" aks holda, "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.
mahsulotlar = ["Osh", "kartoshka","piyoz", "olma", "banan", "pineapple", "bread", "tea", "potato", "cucumber", "tomato"]
savat = []
for n in range(5):
    savat.append(input(f"{n+1}inchi mahsulotingizni kiriting\n"))
for tovar in savat:
    if tovar in mahsulotlar:
        print(f"Bizda {tovar}lar bor")
    else:
        print(f"Bizda{tovar} lar yo'q")
#5-vazifa
#Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta mahsulot kiritishni so'rang. Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yang, bor_mahsulotlar degan ro'yxatga, do'konda yo'q mahsulotlarni esa mavjud_emas degan ro'yxatga qo'shing.  Agar mavjud_emas ro'yxati bo'sh bo'lsa, "Siz so'ragan barcha mahsulotlar do'konimizda bor" degan xabarni, aks holda esa "Quyidagi mahsulotlar do'konimizda yo'q: ....." degan xabarni chiqaring.
mahsulotlar = ["Osh", "kartoshka","piyoz", "olma", "banan", "pineapple", "bread", "tea", "potato", "cucumber", "tomato"]
savat = []
bor_mahsulotlar = []
mavjud_emas = []
for n in range(5):
    savat.append(input(f"{n+1}inchi mahsulotingizni kiriting\n"))
for tovar in savat:
        if tovar not in mahsulotlar:
            mavjud_emas.append(tovar)
        else:
            bor_mahsulotlar.append(tovar)

if tovar in mavjud_emas:
     print(f"{mavjud_emas} bizda yo'q!")

for tovar in bor_mahsulotlar:
     print(tovar)
else:
     print(f"{bor_mahsulotlar} Siz so'ragan ma'lumotlar bizda bor.")
     



#6-vazifa
# foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing. Foydalanuvchidan yangi login tanlashni so'rang va foydalanuvchi kiritgan loginni foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring. Agar ro'yxatda bunday login mavjud bo'lsa, "Login band, yangi login tanlang!" aks holda "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring.

users = ["Mrx", "DarkNet", "Muso", "Ibrohim", "Ismoil"]
new_login =input("Yangi login kiriting\n")
if new_login.title() not in users:
    print(f"{new_login.title()} Bro xush kelibsiz")
else:
    print(f"{new_login.title()} logini band, boshqa login tanlang")
#7-vazifa
#Foydalanuvchidan biror butun son kiritishni so'rang. Foydalanuvchi kiritgan sonni 2 da 10 gacha bo'lgan sonlardan qay biriga qoldiqsiz bo'linishini konsolga chiqaring. 
butun_son = int(input("Butun son kiriting:\n"))
for sonlar in range(2,11):
    if not butun_son%sonlar:
        print(f"{butun_son}i {sonlar}iga qoldiqsiz bo'linadi")
    else:
        print(f"{butun_son}i {sonlar}iga qoldiqsiz bo'linmaydi")