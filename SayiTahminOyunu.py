import random # random kütüphanesi, rasgele sayı üretimi ile ilgili hazır fonksiyonları içerir.

MIN_SAYI=1
MAX_SAYI=100

sayi=random.randint(MIN_SAYI,MAX_SAYI) # randint(min,max) fonksiyonu, min ile max arasında rasgele bir tamsayı döndürür.

tahmin=int(input("Lütfen tahmini bir sayı giriniz:"))
tahmin_say=1

while (sayi!=tahmin):
    if tahmin<sayi:
        print("YUKARI!")
    else:
        print("AŞAĞI!")

    tahmin=int(input("Lütfen tahmini bir sayı giriniz:"))
    tahmin_say+=1

print("TEBRİKLER! Doğru tahmin ettiniz.")
print(f"{tahmin_say} tahminde bilgisayarın tuttuğu sayıyı buldunuz.")