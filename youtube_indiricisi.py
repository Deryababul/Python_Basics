from pytube import YouTube

kaydedilecek_konum='C:/Users/babul/Downloads'
link="https://www.youtube.com/watch?v=MwpMEbgC7DA"

try: 
    yt = YouTube(link) 
except: 
    print("Connection Error")

ys=yt.streams.get_highest_resolution()

ys.download(kaydedilecek_konum)
print("indirilme tamamlandi")