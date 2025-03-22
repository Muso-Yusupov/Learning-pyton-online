# 1-vazifa
# O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
countries = ["O'zbekiston", "USA", "UK", "Australia", "China", "Japan", "Turkey"]
countries_asl_holat = countries[:]
print(countries)
print("\nBu ro'yhat uzunligi ",len(countries))
# 2-vazifa
# sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
countries.sort()
print("\nO'zgargan ro'yxat", sorted(countries))# sorted funksiyasidan keyin listni qavs ichida yozish kerak "sorted(blablabla)" shunday qilib
# 3-vazifa
# sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring
print("\nTeskari holdagi ro'yhat", sorted(countries, reverse=True))
# 3-vazifa
# Asl ro'yxatni qaytadan konsolga chiqaring
print("\nAsl ro'yhat",countries_asl_holat)#It's working wrongly 
#4-vazifa
sonlar = list(range(120,1201))
print(sonlar)
# 5-vazifa
# Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
print("\nSonlar yig'indisi", sum(sonlar))
# 6-vazifa
# Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring
min_sonlar = min(sonlar)
max_sonlar = max(sonlar)
print("\nEng katta qiymat va eng kichik qiymat ayirmasi", max_sonlar-min_sonlar)
# 7-vazifa
# Ro'yxatdagi elementlar sonini hisoblang
print("\nElementlar soni", len(sonlar))
# 8-vazifa
# Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring
bosh_qiymat = sonlar[:21]
orta_qiymat = sonlar[1180:1200]
print("\nBoshidan 20ta qiymat", bosh_qiymat,"\nOxiridan 20ta qiymant", orta_qiymat)
# 9-vazifa
# taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
taomlar = []
taomlar.append("Osh")
taomlar.append("Kasha")
taomlar.append("Mastava")
taomlar.append("Somsa")
taomlar.append("Qozonkabob")
# 10-vazifa
# nonushta degan yangi ro'yxatga taomlardan nusxa oling
nonushta1 = taomlar[:]
# 11-vazifa\
# Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing
nonushta = taomlar[0:1]
nonushta.append("Qaymoq")
nonushta.append("Tuxum")
# 12-vazifa
# Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring
print("\nTaomlar:", taomlar,"\nNonushta:", nonushta)
# 13-vazifa
# Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring.
nonushta = list(nonushta)
nonushta[0] = "qaymoq va non"
nonushta = tuple(nonushta)