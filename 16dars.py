###Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta mashxur shaxlar haqidagi ma'lumotlarni lug'at ko'rinishida saqlang. Lug'atlarni bitta ro'yxatga joylang, va har bir shaxs haqidagi ma'lumotni konsolga chiqaring.


artist0 = {'name':'The Weeknd','t_yil': 1990,'t_joy':'Canada','job':'artist','b_ishlar':'Spotify platformasida eng ko\'p stream qilingan qo\'shiq ijrochisi.'}
artist1 = {'name':'Ed Sheeran','t_yil': 1991,'t_joy':'England','job':'artist','b_ishlar':'Ko\'plab ajoyib musiqalar yaratgan san\'atkor.'}
artist2 = {'name':'Selena Gomez','t_yil':1992,'t_joy':'Texas','job':'artist','b_ishlar':'Ko\'plab mashhur qo\'shiqlar yozgan.'}
artist3 = {'name':'Cillian Murphy','t_yil':1976,'t_joy':'Duoglas','job':'actor','b_ishlar':'Ko\'plab ajoyib kinolarda ijro etgan, Peaky Blinders va Oppenheimer kabi.'}

artists = [artist0,artist1,artist2,artist3]

for artist in artists:
    print(f"Ismi {artist['name']}, tug'ilgan yili {artist['t_yil']}, tug'ilgan joyi {artist['t_joy']}, kasbi/qiladigan ishi {artist['job']},\nqilgan mashhur ishlaridan biri {artist['b_ishlar']}\n")


###Yuqoridagi lug'atlarga har bir shaxsning mashxur asarlari ro'yxatini ham qo'shing. For tsikli yordamida muallifning ismi va uning asarlarini konsolga chiqaring.

asarlari = []
for asarlar in artists:
    asarlari.append(input(f"{asarlar['name']}ning mashhur san'at asarlarini kiriting:\n"))
    
print(f"{artist0['name']}ning mashur san'at asari '{asarlari[0]}'\n")
print(f"{artist1['name']}ning mashur san'at asari '{asarlari[1]}'\n")
print(f"{artist2['name']}ning mashur san'at asari '{asarlari[2]}'\n")
print(f"{artist3['name']}ning mashur san'at asari '{asarlari[3]}'\n")

##Oila a'zolaringiz (do'stlaringiz) dan 3 ta sevimli kino-seriali haqida so'rang. Do'stingiz ismi kalit, uning sevimli kinolarini esa ro'yxat ko'rinishida lug'atga saqlang.  Natijani konsolga chiqaring.

s_kinolar = []
ismlar = []

for n in range(5):

    ism = input("Ismingizni kiriting:|\n")
    kino = input("Sevimli filmingizni kiriting: ")
    ismlar.append(ism)
    s_kinolar.append(kino)

for b in range(5):
    print(f"{ismlar[b].title()}ning sevimli filmi \"{s_kinolar[b]}\"")


##Davlatlar degan lug'at yarating, lug'at ichida bir nechta davlatlar haqida ma'lumotlarni lug'at ko'rinishida saqlang. Har bir davlat haqida ma'lumotni konsolga chiqaring.


davlat0= {'davlat_nomi':'Usa','maydoni' : 98000000,
            'aholisi' : 340000000,
            'economy' : 27000000000000.}

davlat1 = {'davlat_nomi':'China',
            'maydoni': 9600000000,
            'aholisi': 1400000000,
            'economy':17000000000000.}

davlat2 = {'davlat_nomi':'Uzbekistan',
            'maydoni':448000,
            'aholisi': 38000000,
            'economy' : 10000000000.}
    #### 3ta lug'at yaratdik va uni 'davlatlar'degan list/ro'yxat ichiga soldik/joyladik.
davlatlar = [davlat0,davlat1,davlat2]##
    ###davlat ichidagi har bir ma'lumotni for cycli yordamida chaqirdik
for davlat in davlatlar:
        print(f"{davlat['davlat_nomi']}ning maydoni {davlat['maydoni']}, aholisi {davlat['aholisi']} va iqtisodiyoti {davlat['economy']}ni tashkil etmoqda.\n")### bu yerda chaqirgan so'z yoziladi (davlatlar emas davlat)

    ###Yuqoridagi dasturga o'zgartirish kiriting: konsolga barcha davlatlarni emas, foydalanuvchi so'ragan davlat haqida ma'lumot bering. Agar davlat sizning lug'atingizda mavjud bo'lmasa, "Bizda bu davlat haqida ma'lumot yo'q" degan xabarni chiqaring.
users = input("Davlat nomi kirg'izing agar bizda u haqida ma'lumot bo'lsa sizga u haqida ma'lumot taqdim etamiz:\n").title()

found = False
for country in davlatlar:
    if country['davlat_nomi'].title() == users:
        print(f"{country['davlat_nomi']}ning maydoni {country['maydoni']}, "
              f"aholisi {country['aholisi']} va iqtisodiyoti {country['economy']}ni tashkil etmoqda.\n")
        found = True
        break

# Agar davlat topilmagan bo'lsa
if not found:
    print("Bizda bu davlat haqida ma'lumot yo'q.")