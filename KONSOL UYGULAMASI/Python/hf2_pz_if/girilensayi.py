def bul():
    sayi = int(input("Lütfen bir sayı giriniz:"))

    if sayi < 100:
        print("girdiğiniz sayı 100'den küçük")
        bul()
    else:
        print ("Girdiğiniz sayı 100'den büyük")
