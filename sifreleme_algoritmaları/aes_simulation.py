from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def encrypt(key, plaintext):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    iv = cipher.iv
    return iv + ciphertext

def decrypt(key, ciphertext):
    iv = ciphertext[:AES.block_size]
    ciphertext = ciphertext[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return plaintext

# Ana program
key = get_random_bytes(16)  # 128 bitlik rastgele bir anahtar oluşturuluyor
plaintext = input("Şifrelenecek mesajı girin: ").encode()

encrypted_message = encrypt(key, plaintext)
decrypted_message = decrypt(key, encrypted_message)

print("Şifreli mesaj:", encrypted_message)
print("Şifre çözülmüş mesaj:", decrypted_message.decode())
