"""girilen yaziyi ters cevirerek yazar"""

yazi_girme=input("Lütfen ters cevirmek istediğiniz yaziyi girin: ")
dizi=[yazi_girme]
yazinin_tersi=[]
length=len(yazi_girme)
print(length)
for i in range(1,length+1):
    yazinin_tersi.append(yazi_girme[length-i])

print(yazinin_tersi)
