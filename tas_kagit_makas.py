import random

bilg_puan=0
kullanici_puan=0
bilg_secenekleri=["tas","kagit","makas"]

while True:
    kullanici_secimi=input("tas mi kagit mi makas mi? (tas/kagit/makas):\n")
    bilg_secimi=random.choice(bilg_secenekleri)
    

    if kullanici_secimi in bilg_secenekleri:
        print("bilgisayar secimi: " ,bilg_secimi)
        if kullanici_secimi== "tas":
            if bilg_secimi==bilg_secenekleri[0]:
                print("----berabere----")
            elif bilg_secimi==bilg_secenekleri[1]:
                bilg_puan+=1
                print("----bilgisayar kazandi----")
            elif bilg_secimi==bilg_secenekleri[2]:
                kullanici_puan+=1
                print("----kullanici kazandi----")
        elif kullanici_secimi=="kagit":
            if bilg_secimi==bilg_secenekleri[0]:
                kullanici_puan+=1
                print("----kullanici kazandi----")
            elif bilg_secimi==bilg_secenekleri[1]:
                print("----berabere----")
            elif bilg_secimi==bilg_secenekleri[2]:
                bilg_puan+=1
                print("----bilgisayar kazandi----")
        elif kullanici_secimi=="makas":
            if bilg_secimi==bilg_secenekleri[0]:
                bilg_puan+=1
                print("----bilg kazandi----")
            elif bilg_secimi==bilg_secenekleri[1]:
                kullanici_puan+=1
                print("----kullanici kazandi----")
            else:
                print("----berabere----")
        
        print("Bilgisayar puani:", bilg_puan)
        print("kullanici puani", kullanici_puan)
        print(" \n ")
    else:
        print("hatali tuslama yaptiniz")
