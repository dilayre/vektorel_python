import hesapMakinesi
import adamasmaca
import hf2_pz_if.nothesabi
import hf2_pz_if.girilensayi
import h003_ct_for.for01

def anaMenu():
  print("\033[1;32;40m")
  print("╔" + "═" * 25 + "╗")
  print("║       Ana Menü          ║")
  print("║                         ║")
  print("║                         ║")
  print("║ 1-Hesap Makinesi        ║")
  print("║ 2-Adam Asmaca Oyunu     ║")
  print("║ 3-Not Hesabı            ║")
  print("║ 4- Girilen Sayı         ║")
  print("║ 5- Saydir                ║")
  print("║ 6- ...                  ║")
  print("║ 7- Çıkış(e)             ║")
  print("║                         ║")
  print("║                         ║")
  print("║ Seçiminiz nedir?        ║")
  print("╚" + "═" * 25 + "╝")
  secim = input()

  print("Seçiminiz:", secim)
  if secim == "1": hesapMakinesi.anaMenu()
  if secim == "2": adamasmaca.oyna()
  if secim == "3": hf2_pz_if.nothesabi.gectikaldi()
  if secim == "4": hf2_pz_if.girilensayi.bul()
  if secim == "5": h003_ct_for.for01.saydir()
  if secim == "7" : 
    print("Programdan çıkılıyor")
    selamlama.iyiAksamlar()
    exit()
