###Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing. Lug'atdagi har bir kalit va qiymatni for tsikli yordamida, alifbo ketma-ketligida chiroyli qilib konsolga chiqaring. 
python_lugati = {'input':'ma\'lumot oluvchi function','print':'funtion displaying codes','if/else/elif':'shart functions','lower()':'kichik harf qiluvchi method','upper()':'barcha harflarni katta qiluvchi method','title()':'bosh harfni katta qiluvchi method','for':'for cyclei','title':'ma\'lumot turini aniqlovchi function','del':'ma\'lumot o\'chiruvchi method','append()':'ro\'yxatga ma\'lumot qo\'shadi'}
for k in sorted(python_lugati):
    print(k)


###Davlatlar va ularning poytaxtlari lug'atini tuzing. Avval lug'atdagi davlatlarni, keyin poytaxtlarni alohida-alohida, alifbo ketma-ketligida konsolga chiqaring. 
davlatlar = {'O\'zbekiston':'Toshkent','USA':'Washington','China':'Beijing','Japan':'Tokyo','Germany':'Berlin','Canada':'Otawwa'}
for k in sorted(davlatlar):
    print(f"Davlat nomi {k}")
print("\n")
for v in davlatlar.values():
    print(f"Poytaxt nomlari {v}")
print("\n")
###Foydalanuvchidan istalgan davlatni kiritishni so'rang va shu davlatning poytaxtini konsolga chiqaring. Agar foydalanuvchi lug'atda yo'q davlatni kiritsa, "Bizda bunday ma'lumot yo'q" degan xabarni chiqaring.
country = input("Davlat kirg'izing:\n")
capital = davlatlar.get(country)
if capital == None:
    print(f"Kechirasiz {country.title()} bizning lug'atda mavjud emas.")
else:
    print(f"{country.title()}ning poytaxti {capital.title()}.")

print("\n")
##Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting). Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rang. Foydalanuvchi kiritgan taomlarni menu bilan solishtiring, agar taom menuda bo'lsa narhini ko'rsating, aks holda "bizda bunday taom yo'q" degan xabarni chiqaring.
menu = {'Osh':35000,
        'Sho\'rva':28000,
        'Steak':220000,
        'Coke 1.5l':15000,
        'Mastava':27000,
        'Somsa':12000,
        'Suv':7000,
        'Chuchvara':32000,
        'Go\'sht':120000.}

meal = input("Taom tanlang:\n").title()
narh = menu.get(meal)

if narh==None:
    print(f"Bizda {meal} taom yo'q. Balki boshqalarani tanlab ko'rarsiz")

else:
    print(f"{meal}ning narxi {narh}so'm ekan.")
    a = float(input("Nechi xissa xohlaysiz?:\n"))
    print(f"Jami {meal} uchun {narh*a}so'm")


