def fact(sayi):
    if sayi == 0:
        return 1
    else:
        return sayi * fact(sayi - 1)
    
if __name__ == '__main__':
    sayi=int(input("Faktoriyelini almak istediğiniz sayiyi girin: "))
    print(fact(sayi))