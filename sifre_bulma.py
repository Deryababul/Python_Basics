import random

char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()"
passwd_len = int(input("Sifre kac karakterden oluşsun? "))
passwd_count=int(input("Kac adet sifre olusturulsun? "))

for i in range(0, passwd_count):
    passwd = ""
    for j in range(0, passwd_len):
        passwd += random.choice(char)
    print(passwd)
    