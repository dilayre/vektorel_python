#print("--------ÖRNEK 1---------")
#rr = 8
#for abc in range(rr):
#   print(abc,".sayı")
#print("------------------------------------------------")
#print("--------ÖRNEK 2---------")
#arabalar= ["Audi","Mercedes","Seat","Honda","Opel"]
#for tasit in arabalar:
 #   print(tasit)
#print("------------------------------------------------")
#print("--------ÖRNEK 3---------")
#bas = 90
#son = 50
#art = -5
#for abc in range(bas,son,art):
 #   print(abc,".sayi")

#print("------------------------------------------------")
#print("--------ÖRNEK 4(Kullanıcıya seçtirerek saydırma)---------")

def saydir():
    sayi1 = int(input("Kaçtan başlayayım:"))
    sayi2 = int(input("Kaça kadar sayayım:"))
    artis = int(input("kaçar kaçar sayayım:"))
    for abc in range(sayi1,sayi2,artis):
        print(abc)

