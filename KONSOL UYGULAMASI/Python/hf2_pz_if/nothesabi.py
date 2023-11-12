def gectikaldi():
    puan = int(input("notunuzu giriniz:"))

    if puan < 0 or puan >100:
        print("geçersiz")
        print("0 ile 100 arası girebilirsin")
        gectikaldi()
    else:
        if puan > 50:
            print("Geçtin")
            if puan > 90: print("süpersin")
            elif puan > 70: print("Orta")
            elif puan > 60: print("idare eder")
        else:
            print("kaldın!")

#gectikaldi()


                                       
