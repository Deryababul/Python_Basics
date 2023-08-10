"""Seçtiğimiz sayıya akdar olan asal sayıları dosya içine yazar"""


sayi=int(input("Kaça kadar sayilari istiyorsunuz? "))
asal=[]
for i in range(2,sayi):
    for j in range(2,i,i):
        if i%j==0:
            break  
        else:
            asal.append(i) 
dosya=open('asalSayi.txt', 'w')
dosya.write(f'0 - {sayi} arasinda olan asal sayilar: ')
dosya.write(str(asal))   
