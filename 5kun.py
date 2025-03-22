, #birinchi vazifa
ismlar = ['Eldiyor', 'Abdulloh', 'Micheal', 'Diyor'] #ismlar degan ro'yxat yaratdik va 4ta ism kirg'izdik 
salomlashish = ["Qalesan ", "Nima gap ", "Salom ", "Qande "] #'salomlashish' degan ro'yxat yaratdik va 4ta salom so'zlarini kirg'izdik
yaxshimi = "ishlaring yaxshimi?" #yaxshimi degan o'zgaruvchiga "ishlaring yaxshimi?" so'zini tayinladik
a = f"{salomlashish[0]}{ismlar[2]} {yaxshimi}"#a degan o'zgaruvchiga f-string yordamida salomlashish ro'yxatidagi birinchi elementni va ismlar ro'yxatidagi uchinchi elementni qo'shdim
b = f"{salomlashish[1]}{ismlar[1]} {yaxshimi}"
c = f"{salomlashish[3]}{ismlar[0]} {yaxshimi}"
d = f"{salomlashish[2]}{ismlar[3]} {yaxshimi}"
cs = f'{a}\n{b}\n{c}\n{d}'#cs degan o'zgaruvchiga f-string yordamida a,b,c,d o'zgaruvchilarini qo'shdim
print(cs)#cs o'zgaruvchisini chiqardik terminalga

#ikkinchi vazifa
sonlar = [ 2, 4, -42112, 1293.1232]
print(sonlar)
sonlar[0] = sonlar[0]+sonlar[2]
sonlar[1] = sonlar[1]//2
sonlar[2] = sonlar[2]-sonlar[2]
del sonlar[3]   
print(sonlar)

#uchinchi vazifa
t_shaxslar = ['Amir Temur', 'Abdulla Qodiriy', 'Alisher Navoiy']
z_shaxslar = ['Tim Cook', 'Elon Musk', 'Teacher Azam', 'Sobir']
tilak = f"\nMen tarixiy shaxslardan " + t_shaxslar.pop(1) + " bilan suhbatlashishni xohlar edim. \nHozir hurmat qilgan shaxslardan esa " + z_shaxslar.pop(0) + " xohlar edim."
print(tilak)

#to'rtinchi vazifa
friends = []
friends.append('Eldi')
friends.append('Diyor')
friends.append("Abdulloh")
friends.append("Micheal")
friends.append("Hayday")
friends.insert(1,"Omonyor")
print(friends)
friends.remove('Eldi')
del friends[2]
print(f"\nMehmonga faqat {friends}lar kelishar ekan")
kelganmehmonlar = friends.pop(2)
print(f"\n{kelganmehmonlar} ketmadi qoldi uyda yotib ,bekorchi bola")








###birinchi vazifa 
# Quyidagi mashqlarni bajaring:

# ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting

# Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring: 


# sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik). 

# Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring. Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring. 

# t_shaxslarva z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz eng ko'p hurmat qilgan tarixiy shaxslarning, ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting. 

# Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib (.pop()), quyidagi ko'rinishda chiqaring:


# friends nomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting. 

# Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlang. 

# Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.

# Yangi mehmonlardeb nomlangan bo'sh ro'yxat yarating. .pop() va .append() metodlari yordamida mehmonga kelgan do'stlaringizning ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.

ismlar = ['Abdulla', "Abdulloh", "Tursunboy", "Abdurashid"]
salomlashishlar = ["Qalesan", "Qalesan", "Nima gap", "Tinchmi"]
a = f"{salomlashishlar[0]} {ismlar[3]} charchamayapsanmi?" 
b = f"\n{salomlashishlar[1]} {ismlar[3]} charchamayapsanmi?"
c = f"\n{salomlashishlar[2]} {ismlar[2]} charchamayapsanmi?"
d = f"\n{salomlashishlar[3]} {ismlar[1]} charchamayapsanmi?"
print(a,b,c,d)

sonlar = [1, -2, 0.45, 123412321312313]
a = f"{sonlar[0]+213123} birinchi son va 213123 yig'indisi"
b = f"\n{sonlar[1]}ning kvadrati {sonlar[1]**2}ga teng"
c = f"\n{sonlar[3]/sonlar[2]}"
print(a,b,c)
del sonlar[2]
sonlar.remove(1)
sonlar.append(2132)
print(sonlar)


friends =[]
friends.append('Tursun')
friends.insert(0,"Xasan")
friends.append("Abdumurod")
friends.append("Jamshidxon")
print(friends)
friends.remove('Xasan')
del friends[2]
print(f"Kela oladiganlar {friends}")
friends.insert(1,"Hasanboy")
friends.append("Olimjon")
print(f"Bekorchi do'stlarimiz{friends}")

yangi_mehmonlar = []
yangi_mehmonlar.append('Muhammad')
yangi_mehmonlar.append('Suxrob')
yangi_mehmonlar.append('Ismoil')
kelganlar = yangi_mehmonlar.pop(0)
print (f"Biznikiga {kelganlar} keldi faqatgina")
print(f"Kelmaganlar esa{yangi_mehmonlar} bo'ldi")