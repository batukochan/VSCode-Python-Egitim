#region örnekler

"""delta örneği"""
"""
a=1
b=4
c=2
delta= (b**2)-(4*a*c)
print("delta değeri : ", delta)
"""
"""
a=int(input("vize notunuzu giriniz : "))
b=int(input("lütfen final notunuzu giriniz : "))
ort=(a+b)/2
print('Geçme notunuz [(vize+final)/2 ]= {}'.format(ort))
"""
#saat bilgisini saniyeye dönüştür
"""
saat=2
saniye=3600
saniyeCinsi=saat*saniye
print("saat")
print(saat,"saat",saniyeCinsi,"saniyedir.")
"""
"""
a=int(input("Lütfen 3 basamaklı bir sayı giriniz : "))
yuzler=int(a/100)
onlar=int((a-yuzler*100)/10)
birler=int((a-yuzler*100)-(onlar*10))
toplam=yuzler+onlar+birler
print(a,"sayısının basamakları toplamı : {} ".format(toplam)) 
"""
"""
sayi = 562
kalan = sayi % 10
birler = kalan // 1
kalan = sayi % 100
onlar = kalan // 10
kalan = sayi % 1000
yuzler = kalan //100
toplamDegeri = birler + onlar + yuzler
print(yuzler, onlar, birler)
print(sayi, " sayısının basamakları toplamı " , toplamDegeri)
"""
# endregion


#region input giriş

'''Örneğimizde kullanıcıdan yaşını isteyelim 
ve yaşı çıktı olarak alalım. '''

yas = int(input("Lütfen yaşınızı giriniz: "))
print(f"Yaşınız → {yas}")

#endregion
