def anaMenu():
  print("\033[1;32;40m")
  print("╔" + "═" * 20 + "╗")
  print("║ \033[1;31;40m Ana Menü \033[1;32;40m   ║")
  print("║                    ║")
  print("║                    ║")
  print("║ 1-Hesap Makinesi   ║")
  print("║ 2-Adam Asmaca Oyunu║")
  print("║ 3-...              ║")
  print("║ 4-...              ║")
  print("║                    ║")
  print("║                    ║")
  print("║ Seçiminiz nedir?   ║")
  print("╚" + "═" * 20 + "╝")
  secim = input()
  anaMenu()

  print("Seçiminiz:", secim)
  if secim == "1" :

def hesapMakinesi():
  hesapMakinesi()
  print("\033[1;32;40m")
  print("╔" + "═" * 20 + "╗")
  print("║ \033[1;31;40m Hesap Makinesi \033[1;32;40m   ║")
  print("║                    ║")
  print("║                    ║")
  print("║ 1-TOPLAMA          ║")
  print("║ 2-ÇIKARMA          ║")
  print("║ 3-ÇARPMA           ║")
  print("║ 4-BÖLME            ║")
  print("║ 5-ÜS ALMA          ║")
  print("║ 6-Kare Alan Hesabı ║")
  print("║ 7-Karenin Çevresi  ║")
  print("║                    ║")
  print("║                    ║")
  print("║ Seçiminiz nedir?   ║")
  print("╚" + "═" * 20 + "╝")
  secim = input()

  print("Seçiminiz:", secim)
  if secim == "1":
    print("Toplamayı seçtiniz")
    sayi1 = int(input("1.sayıyı giriniz:"))
    sayi2 = int(input("2.sayıyı giriniz:"))
    print("Toplam :", sayi1 + sayi2)
  if secim == "2":
    print("Çıkarmayı seçtiniz")
    a = int(input("1.sayıyı giriniz:"))
    b = int(input("2.sayıyı giriniz:"))
    print("İki sayının farkı:", a - b)
  if secim == "3":
    print("Çarpmayı seçtiniz")
    x = input("x sayısını giriniz:")
    y = input("y sayısını giriniz:")
    print("x ve y'nin çarpımı:", int(x) * int(y))
  if secim == "4":
    print("Bölmeyi seçtiniz")
    k = int(input("k sayısını giriniz:"))
    m = int(input("l sayısını giriniz:"))
    print("İki sayının birbirine bölümü:", k / m)
  if secim == "5":
    print("Üs Almayı seçtiniz")
    sayi3 = int(input("1. sayıyı giriniz:"))
    sayi4 = int(input("2. sayıyı giriniz:"))
    print("Girdiğiniz sayının kuvveti:", sayi3**sayi4)
  if secim == "6":
    print("Kare Alan Hesabını seçtiniz")
    kenar1 = int(input("1.kenar uzunluğu:"))
    kenar2 = int(input("2.kemar uzunluğu:"))
    print("Karenin Alanı:", kenar1 * kenar2)
  if secim == "7":
    print("Karenin Çevresini seçtiniz")
    akenari = int(input("Karenin bir kenarını giriniz:"))
    print("Karenin çevresi:", akenari * 4)

  # ╔ 201
  # ║ 186
  # ═ 205
  # ╚ 200
  # ╗ 187
  # ╝ 188
  

