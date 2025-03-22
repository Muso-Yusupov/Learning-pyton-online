a = int(input("Istalgan son kiriting\n"))
b = a**2
c = a**3
b2c3 = f"{a} ning kvadrati {b}ga, kubi {c}ga teng"
print(b2c3)
yil = int(input("Tug'ilgan yilingizni kiriting bro\n"))
yosh = 2025- yil
print(f"Siz {yosh} yoshda ekansiz tog'asi")
son = int(input("istalgan sonni kiritvorasmi okaxonim\n"))
son2 = int(input("Bro ikkinchi sonniyam kiritvorin malol kelmasa\n"))
ayirma = son - son2
qoshish = son + son2
kopaytma = son * son2
bolish = son / son2
barchayechim = f"Sonlar ayirmasi  {ayirma}ga, yig'indisi {qoshish}ga, ko'paytmasi {kopaytma}ga, bo'lingani esa {bolish}ga teng ekan okamligi"
print(barchayechim)