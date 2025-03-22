# 1-vazifa
# Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing, ro'yxat elementlarining birinchi harfini katta qilib konsolga chqaring. GM uchun ikkala harfni katta qiling.
yangi_cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in yangi_cars:
    if car == 'gm':
        print(car.upper())
    else:
        print(car.title())

#2-vazifa
#Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring. 
    if car != 'gm':
        print(car.title())
    else:
        print(car.upper())

# 3-vazifa
#Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?" xabarini konsolga chiqaring. Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!"  matnini konsolga chiqaring.
login_ism = input('Loginingizni kiriting:\n')
login_ism = login_ism.lower()
if login_ism == 'admin':
    print(f"Xush kelibsiz {login_ism.title()}. Foydalanuvchilar ro'yxatini ko'rasizmi") 
else:
    print(f"Xush kelibsiz {login_ism}!")

#4-vazifa
#Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng bo'lsa, "Sonlar teng" ekan degan yozuvni konsolga chiqaring.
print("Ikkita son kiriting")
sonlar = []
sonlar.append(input("Birinchi sonni kiriting\n"))
sonlar.append(input("Ikkinchi sonni kiriting\n"))
if sonlar[0]==sonlar[1]:
    print(f"Sonlar biriga teng.{sonlar}")
else:
    print(f"Sonlar teng emas {sonlar}")

# 4-vazifa
#Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa konsolga "Manfiy son", agar musbat bo'lsa "Musbat son" degan xabarni chiqaring. Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa konsolga "Manfiy son", agar musbat bo'lsa "Musbat son" degan xabarni chiqaring. 

sonlar = int(input("Istalgan son kiriting:\n"))
if sonlar>=0:
    print(f"Bu {sonlar} musbat son.")
else:
    print(f"Bu {sonlar} soni manfiy son.")

# 5-vazifa
#Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini hisoblab konsolga chiqaring. Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring. 
sonlar = int(input("Istalgan son kiriting:\n"))
if sonlar>=0:
    print(f"{sonlar}ning ildizi {sonlar**(1/2)}ga teng")
else:
    print("Musbat son kiriting.")