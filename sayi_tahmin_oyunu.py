import random

bilg_secimi=random.randint(0,1000)
# print("Bilgisayarin sectiği sayi:", bilg_secimi,"\n")

while True:
    kullanici_tahmini=int(input("Bilgisayarin rasgele seçtiği sayi nedir (0-1000)? "))
    if kullanici_tahmini<1000 and kullanici_tahmini>0:
        if kullanici_tahmini==bilg_secimi:
            print("Doğru sonuc" )
            break
        if kullanici_tahmini>bilg_secimi:
            print("daha kücük")
        elif kullanici_tahmini<bilg_secimi:
            print("daha büyük")
    else:
        print("yanlis tuslama yaptiniz yeniden deneyiniz..")


