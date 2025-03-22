#otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga shu inson haqida kamida 3 ta m'alumot kiriting (ismi, tu'gilgan yili, shahri, manzili va hokazo). Lug'atdagi ma'lumotni matn shaklida konsolga chiqaring :Otamning ismi Mavlutdin, 1954-yilda, Samarqand viloyatida tug'ilgan

dadam = {'ism':"Ahmadjon", 't_yil':1971,'t_joy':'Tojikiston','Malumoti':'oliy'}
print(f"Dadamning ismi {dadam['ism']},\ntug'ilgan joyi {dadam['t_joy']},\ntug'ilgan yili {dadam['t_yil']},\nma'lumoti {dadam['Malumoti']}.")

#Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 5 ta ism-taom jufltigi bo'lsin. Kamida uch kishining sevimli taomini konsolga chiqaring: Alining sevimli taomi osh
sevimli_taomlar = {'dadam':'sho\'rva','oyim':'osh','Bro':'somsa','little_bro':'shashlik','Sister':'g\'ilmindi','ozim':'dimlama'}
print(f"Dadamning sevimli taomi {sevimli_taomlar['dadam']},\nOyimning sevimli taomi {sevimli_taomlar['oyim']},\nMadinaning sevimli taomi {sevimli_taomlar['Sister']},\nBroni sevimli ovqati {sevimli_taomlar['Bro']},\nLittle broning sevimli taomi {sevimli_taomlar['little_bro']},\nO'zimning sevimli taomim {sevimli_taomlar['ozim']}.")

#Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z (atamani) kiriting (masalan integer, float, string, if, else va hokazo) va har birining qisqacha tarjimasini yozing.
python_lugati = {'print':'code chiqarish','input':'malumot sorash','int':'butun son','float':'kasr sonlar','if/else/elif':'shart bajarish'}
print(f"{python_lugati['print']} so'zi chop etmoq degani o'zbek tilida,\n{python_lugati['input']} kirish degani,\n{python_lugati['int']} butun son deganini,\n{python_lugati['float']} o'nli kasrlar degani,\n{python_lugati['if/else/elif']} agar deb tarjima qilinadi")
lugat = python_lugati.get('ma\'lumot o\'chirib tashlash', 'Bunday lug\'at ro\'yxatda mavjud emas')
print(lugat)
#Yuqoridagi vazifani if-else yordamida qiling va natijani ham foydalanuvchiga tushunarli ko'rinishda chiqaring.
lugat1 = input('so\'z kiriting:\n')
tarjima = python_lugati.get(lugat1)
if lugat1 not in python_lugati:
    print(f"'{lugat1}' bunday so'z lug'atda mavjud emas")
else:
    print(f"{lugat1} funksiya/methodining vazifasi {tarjima}.")
#Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini yuqoridagi lug'atdan chiqarib bering. Agar so'z lu'gatda mavjud bo'lmasa, "Bunda so'z mavjud emas" degan xabarni chiqaring.
lugat = {'olma':'apple','chexol':'phonecase','bajarmoq':'do','sayrga chiqmoq':'go for a walk','keng':'wide'}
eng_uz = lugat.get('uxlamoq','Bunday so\'z lug\'atda mavjud emas')
print(eng_uz)
