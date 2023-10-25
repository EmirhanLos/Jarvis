# this is a work in progress, A list of things that you can do are on the other page.
import random
import datetime

z = datetime.datetime.now()
from datetime import datetime
from datetime import *

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
import speech_recognition as sr
import os
import wikipedia
from gtts import gTTS
import playsound
import wikipedia
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from time import sleep
import time
import socket
import calendar
import turtle
import ssl
import datetime
import datetime
import webbrowser
import os
import urllib.request
import random
from random import choice
import phonenumbers
from phonenumbers import carrier,timezone,geocoder
from smtplib import SMTP

os.system('color b')
liste = ['198.116.4.189', '193.189.190.7', '154.195.199.61', '199.231.163.232', '179.112.190.133', '188.120.233.146', '185.174.175.0',
         '135.175.184.24', '385.278.583.383', '835.067.846.259', '101.44.223.255', '101.44.252.255', '101.44.47.255',
         '102.129.167.255', '102.216.81.255', '	103.130.145.255', '	103.215.218.255', '104.166.190.255',
         '104.250.163.255', '	107.150.177.255', '109.122.207.255', '166.362.626.345']

veya1 = ['iyiyim', 'kötüyüm', 'idare eder']
nesin1 = ['Ben sizin kodlamış olduğunuz akıllı bir sistemim, size işleriniz de yardım etmek için varım.', 'Ben Jarvis.', 'Akıllı bir sistem.']

espri = ['Hava soğuk olduğunda espri yaparsın ve soğuk espri olur.', 'Hava sıcak olduğun da espri yaparsın ve sıcak espri olur.', 'Zenginler et yer fakirler Hayalet.', 'Mafya babasıyım çünkü oğlumun adı mafya.', 'Kim vurduya gittim birazdan geleceğim.', 'Hava korsanı uçağı kaçırmak istemiş ama yapamamış çünkü uçağı kaçırmış.', 'Almanya da almanlar Sakarya da sakarlar yaşar.', 'Seven ayrılmaz eight ayrılır.', 'Tebrikler kazandınız tencere oldunuz.']

cansikkin = ['Siz daha iyilerini hak ediyorsunuz efendim.', 'eğer isterseniz espri yapıp moralinizi düzeltebilirim.', 'Siz iyi bir insansınız.']
müzik = ['Enemy', 'Believer', 'Arabam dacia', 'Dolunay', 'Ayaz', 'Brokoli', 'Close Eyes', 'Fearless pt.II', 'Fighter', 'Astronaut in the ocean', 'Murder in my mind', 'Biliyom', 'Yüreğine inan', 'I see who you are your my enemy', 'Back in black']

jokes = 10
# stardust = 10
question = input("şifre:  ")
isim = input("İsminiz: ")
# Welcome = 10
if question == "los":
    # Welcome -= 1
    print(' ')
    os.system('cls')
else:
    print("Şifre yanlış")
    raise SystemExit
sleep(0.5)
print("Nasa'ya, Uydulara ve kullanmış olduğunuz cihazlara bağlanılıyor.")
print("-------------------------------------------")
sleep(0.50)
print("Nasa'ya, Uydulara ve kullanmış olduğunuz cihazlara bağlanıldı.")
sleep(0.50)
print("                                     ######################")
print("##                    ##           ##                      ")
print("##                    ##           ##                      ")
print("##                    ##           ##                      ")
print("##                    ##           ##                      ")
print("########################           ##                      ")
print("########################           ##       ################ ")
print("##                    ##           ##                      ##")
print("##                    ##           ##                      ##")
print("##                    ##           ##                      ##")
print("##                    ##           ##                      ##")
print("##                    ##             ######################")
hg = ['Hoş Geldiniz Efendim.', 'Sizi görmek çok güzel.', 'Sizi gördüğüme sevindim.', 'Bugünü sizinle birlikte geçirmekten mutluluk duyacağım.']
print(random.choice(hg))

def question():
    what = ['Nasıl yardımcı olabilirim? ', 'Yardımcı olacağım şeyi söylemeniz yeterli. ', 'Başka ne yapabilirim? ', 'Ne yapmamı istersiniz? ', 'Yardımcı olmamı istediğiniz şey nedir? ']
    x = input(random.choice(what))
   # x = input("Nasıl yardımcı olabilirim?:  ")
    # Task = 10
    if x == "spotify aç":
        # Task -= 1
        print("-------------------------------------------")
        print("Tamam.")
        webbrowser.open_new_tab('https://open.spotify.com/')
        sleep(1)
        print("Açılıyor.")
        print("-------------------------------------------")
    if x == "hava durumunu göster":
        print("-------------------------------------------")
        print("Hemen gösteriyorum.")
        webbrowser.open_new_tab('https://www.bbc.co.uk/weather')
        print("-------------------------------------------")
    if x == "hava durumu":
        print("-------------------------------------------")
        print("Hemen gösteriyorum.")
        webbrowser.open_new_tab('https://www.bbc.co.uk/weather')
        print("-------------------------------------------")
    if x == "saat kaç":
        print("-------------------------------------------")
        print("Saat: ", current_time)
        print("-------------------------------------------")
    if x == "saat":
        print("-------------------------------------------")
        print("Saat: ", current_time)
        print("-------------------------------------------")
    if x == "tarih ne":
        print("-------------------------------------------")
        print("Geçerli tarih")
        print(now.strftime("%d-%m-%y"))
        print("-------------------------------------------")
    if x == "tarih":
        print("-------------------------------------------")
        print("Geçerli tarih")
        print(now.strftime("%d-%m-%y"))
        print("-------------------------------------------")
    if x == "jarvis ne demek":
        print("-------------------------------------------")
        print("Jarvis, Oldukça Çok Akıllı Bir Sistem anlamına gelir.")
        print("-------------------------------------------")
    if x == "yemek sipariş et":
        print("-------------------------------------------")
        print("Tamam.")
        webbrowser.open_new_tab('https://getir.com/yemek/')
        print("-------------------------------------------")
    if x == "gmail aç":
        print("-------------------------------------------")
        e = input("Gmail mi? Outlook mu?   ")
        if e == "gmail":
            print("Tamam, Gmail açıldı.")
            webbrowser.open_new_tab('https://mail.google.com/mail/u/0/')
            print("-------------------------------------------")
        else:
            print("Tamam, Outlook açıldı.")
            webbrowser.open_new_tab('https://outlook.live.com/owa/')
            print("-------------------------------------------")
    if x == "google aç":
        print("Tamam google açıldı efendim.")
        webbrowser.open_new('https://www.google.com')
    if x == "çeviri aç":
        webbrowser.open_new_tab
        ('https://www.google.com/search?q=%C3%A7eviri')
    if x == "haberler":
        webbrowser.open_new_tab
        ('https://www.google.com/search?q=haberler')
    if x == "güneşin telefonuna bağlan":
        print("Güneş'in telefonuna bağlanılıyor...")
        sleep(2)
        # print(random.choice(liste))
        print("bağlanılan cihaz IP:")
        print(random.choice(liste))
        print("Cihaz sahibi: Güneş")
        print("Nerede oturuyor: henüz bilinmiyor.")
    if x == "onurun telefonuna bağlan":
        print("Onur'un telefonuna bağlanılıyor.")
        sleep(2)
        print("Bağlanılan cihaz IP:")
        print(random.choice(liste))
        print("Cihaz sahibi: Onur Ayazcan Özgezer")
        print("Nerede oturuyor: Henüz bilinmiyor.")
    if x == "sudenin telefonuna bağlan":
        print("Sude'nin telefonuna bağlanılıyor.")
        sleep(2)
        print("Bağlanılan Cihaz IP:")
        print(random.choice(liste))
        print("Cihaz sahibi: Sude Naz")
        print("Nerede oturuyor?: Henüz bilinmiyor.")
    if x == "devranın tabletine bağlan":
        print("Devran'ın tabletine bağlanılıyor.")
        sleep(2)
        print("Bağlanılan Cihaz IP:")
        print(random.choice(liste))
        print("Cihaz Sahibi: Devran")
        print("Nerede otuyuruyor: 395.Sokak Türközü Mahallesi 42/4 Mamak Ankara")
    if x == "furkanın tabletine bağlan":
        print("Furkan'ın tabletine bağlanılıyor.")
        sleep(2)
        print("Bağlanılan Cihaz IP:")
        print(random.choice(liste))
        print("Cihaz Sahibi: Furkan Yusuf")
        print("Nerede otuyuruyor: 395.Sokak Türközü Mahallesi 42/4 Mamak Ankara")
        # os.system(start C:\Programın dizni\progrem.exe)
    if x == "ayarları aç":
        print("Tamam")
        os.system("start ms-settings")
    if x == "kodlarını aç":
        print("Tamam.")
        os.system("start C:\Jarvis")
    if x == "nasılsın":
        print(random.choice(veya1))
    if x == "sen nesin":
        print(random.choice(nesin1))
    if x == "yaşım kaç":
        print("Hesaplanan yaşınız: ",2023-2009)
    if x == "doğum günüm ne zaman":
        print("9 Haziran 2009")
        print("Şu an ki yaşınız: ",2023-2009)
    if x == "devranın doğum günü ne zaman":
        print("31 Ekim 2014")
        print("Şu an ki yaşı: ",2023-2014)
    if x == "furkanın doğum günü ne zaman":
        print("19 Temmuz 2017.")
        print("Şu an ki yaşı: ",2023-2017)
    if x == "annemin doğum günü ne zaman":
        print("27 Eylül 1991.")
        print("Şu an ki yaşı: ",2023-1991)
    if x == "babamın doğum günü ne zaman":
        print("27 Ocak 1991.")
        print("Şu an ki yaşı: ",2023-1991)
    if x == "kedilerin doğum günü ne zaman":
        print("bilinmiyor.")
    if x == "bilgisayarı kapat":
        print("Tamam.")
        os.system("shutdown -s -t 5")  # windows kapama komutu
    if x == "kendini kapat":
        print("Görüşürüz.")
        sleep(1)
        raise SystemExit
    if x == "aktif misin":
        print("sizin için daima efendim.")
    if x == "aktif misin jarvis":
        print("sizin için daima efendim.")
    if x == "jarvis":
        print("Efendim?")
    if x == "bilgisayarı koru":
        print("Tamam Efendim.")
    if x == "cihazları koru":
        print("Tamam efendim.")
    if x == "evi koru":
        print("Tamam ev korunuyor.")
    if x == "topla":
        sayi1 = input('1. Sayı : ')
        sayi2 = input('2. Sayı : ')
        toplam = float(sayi1) + float(sayi2)
        print("Toplam :{0} ".format(toplam))
    if x == "çıkar":
        sayi1 = input('1. Sayı : ')
        sayi2 = input('2. Sayı : ')
        toplam = float(sayi1) - float(sayi2)
        print("Sonuç :{0} ".format(toplam))
    if x == "ortalama bul":
        sayi1 = input('1. Sayı : ')
        sayi2 = input('2. Sayı : ')
        ortalama = (int(sayi1) + int(sayi2)) / 2
        print("Ortalama :{0} ".format(ortalama))
    if x == "çarp":
        sayi1 = input("1.Sayı : ")
        sayi2 = input("2.Sayı : ")
        toplam = float(sayi1) * float(sayi2)
        print("Sonuç :{0} ".format(toplam))
    if x == "böl":
        sayi1 = input("1.Sayı : ")
        sayi2 = input("2.Sayı : ")
        toplam = float(sayi1) / float(sayi2)
        print("Sonuç :{0} ".format(toplam))
    if x == "geçti kaldı hesapla":
        ort = input('Ortalamanızı Girin : ')
        if (int(ort) >= 50):
            print("Geçtiniz")
        else:
            print("Kaldınız")
    if x == "tek mi çift mi hesapla":
        sayi = input('Sayı : ')
        if (int(sayi) % 2 == 0):
            print("Sayı Çift")
        else:
            print("Sayı Tek")
    if x == "tek çift":
        sayi = input('Sayı : ')
        if (int(sayi) % 2 == 0):
            print("Sayı Çift")
        else:
            print("Sayı Tek")
    if x == "ehliyet alabilir mi":
        yas = input('Yaşınız : ')
        if (int(yas) & 18):
            print("Yaşınız Ehliyet almak İçin Uygun Değil")
        else:
            print("Yaşınız Ehliyet almak İçin Uygun")
    if x == "sayıları listele":
        sayi = input('Sayıyı Gir : ')
        for i in range(1, int(sayi) + 1):
            print(i)
    if x == "alanı hesapla":
        kisa = input('Kısa Kenar : ')
        uzun = input('Uzun Kenar : ')
        alan = int(kisa) * int(uzun)
        cevre = 2 * (int(kisa) + int(uzun))
        print("Alan : {0}".format(alan))
        print("Çevre : {0}".format(cevre))
    if x == "asal sayımı değil mi":
        sayac = 0
        sayi = input('Sayı: ')
        for i in range(2, int(sayi)):
            if (int(sayi) % i == 0):
                sayac += 1
                break
        if (sayac != 0):
            print("Sayı Asal Değil")
        else:
            print("Sayı Asal")
    if x == "maaş hesapla":
        maas = input("Maaşı Gir : ")
        zam = input("Zam Oranı(%) : ")
        yeniMaas = int(maas) + (int(maas) * int(zam) / 100)
        print("Zamlı Maaş :", yeniMaas)
    if x == "araştır":
        araştır = input("Ne araştırmamı istersiniz?: ")
        url = "https://www.google.com/search?q=" + araştır
        webbrowser.get().open(url)
        print(araştır + " ile ilgili aramaları Google ekranına yansıttım")
        #e = input("Ekranı yansıtayım mı yoksa bilgiyi buraya mı yazayım?   ")
        #if e == "buraya yaz":
            #LSDdsfg = ['Peki, Bilgiyi buraya yazıyorum.', 'Tamam.', 'Bilgiyi buraya yazıyorum.',
            #           'Bilgiyi buraya yazdım.']
           # print(random.choice(LSDdsfg))
           # baslik = input("Başlığı Giriniz: ")
          #  link = "https://tr.wikipedia.org/wiki/" + str(baslik.lower())
         #   r = requests.get(link)
        #    soup = BeautifulSoup(r.content)
       #     st1 = soup.find_all("div", attrs={"id": "bodyContent"})
      #      text = st1[0].text
     #       print(text)
    #else:
        #baslik = input("Başlığı Giriniz: ")
        #link = "https://tr.wikipedia.org/wiki/" + str(baslik.lower())
        #r = requests.get(link)
        #soup = BeautifulSoup(r.content)
        #st1 = soup.find_all("div", attrs={"id": "bodyContent"})
        #text = st1[0].text
        #print(text)
        #DSL = ['Tamam, bilgiyi ekrana yansıttım.', 'Bilgi şu anda ekran da.', 'Bilgiyi Ekrana yansıttım.',
        #       'Peki, bilgiyi ekrana yansıttım.']
        #print(random.choice(DSL))
        #webbrowser.open_new_tab(link="https://tr.wikipedia.org/wiki/" + str(baslik.lower()))
    if x == "nasaya bağlan":
        print("Tamam Nasa'ya hemen bağlanılıyor...")
        sleep(1)
        e = input("IP'leri göstereyim mi? yoksa göstermeyeyim mi?   ")
        if e == "evet":
            print("Tamam, IP'ler sıralanıyor.")
            print(random.choice(liste))
            print(random.choice(liste))
            print(random.choice(liste))
            print(random.choice(liste))
            print(random.choice(liste))
            print(random.choice(liste))
            print(random.choice(liste))
            print(random.choice(liste))
            print(random.choice(liste))
            print(random.choice(liste))
            print(random.choice(liste))
            print(random.choice(liste))
            print(random.choice(liste))
            print(random.choice(liste))
            print(random.choice(liste))
            print(random.choice(liste))
            print(random.choice(liste))
            print(random.choice(liste))
            print(random.choice(liste))
            print(random.choice(liste))
            print(random.choice(liste))
            print(random.choice(liste))
            print(random.choice(liste))
            print("Size yardımcı olabilecek en önemli IP'leri sıraladım, devamıda var.")
        else:
            print("Tamam, IP'ler gösterilmiyor.")
            print("Siteleri")
            webbrowser.open_new_tab('https://www.nasa.gov/')
            print("Kurucusu: Dwight D. Eisenhower")
            print("Şu anki yöneticisi: Bill Nelson")
            print("Youtube kanalları:")
            webbrowser.open_new_tab('https://www.youtube.com/@NASA')
    if x == "furkanın kan grubu ne":
        print("Furkan'ın kan grubu: Negatif 0 RH")
    if x == "espri yap":
        print(random.choice(espri))
    if x == "espiri yap":
        print(random.choice(espri))
    if x == "jarvis espri":
        print(random.choice(espri))
    if x == "jarvis espiri":
        print(random.choice(espri))
    if x == "devran kim":
        print("Devran Kim?")
        print("Değişmiş bir adı yok veya 2.bir ad yok.")
        print("Anne adı: Serpil")
        print("Baba adı: Emrah")
        print("Abi adı: Emirhan")
        print("Kardeş adı: Furkan Yusuf")
        print("Nerede otuyuruyor: 395.Sokak Türközü Mahallesi 42/4 Mamak Ankara")
    if x == "furkan kim":
        print("Furkan Kim?")
        print("Gerçek adı: Furkan Yusuf.")
        print("Anne adı: Serpil")
        print("Baba adı: Emrah")
        print("Abi adı: Emirhan, Devran")
        print("Kardeş adı: Yok")
        print("Nerede otuyuruyor: 395.Sokak Türközü Mahallesi 42/4 Mamak Ankara")
    if x == "emirhan kim":
        print("Emirhan Kim?")
        print("Değişmiş bir adı yok veya 2.bir ad yok.")
        print("Anne adı: Serpil")
        print("Baba adı: Emrah")
        print("Abi adı: Yok")
        print("Kardeş adı: Furkan Yusuf, Devran")
        print("Nerede otuyuruyor: 395.Sokak Türközü Mahallesi 42/4 Mamak Ankara")
    if x == "serpil kim":
        print("Serpil Kim?")
        print("Değişmiş bir adı yok veya 2.bir ad yok.")
        print("Anne adı: İsminaz veya Nazlı.")
        print("Baba adı: Cuma")
        print("Çocuk adı: Emirhan, Devran, Furkan Yusuf")
        print("Kardeş adı: Serena, Mert")
    if x == "emrah kim":
        print("Emrah Kim?")
        print("Değişmiş bir adı yok veya 2.bir ad yok.")
        print("Anne adı: Güller")
        print("Baba adı: Arslan")
        print("Çocuk adı: Emirhan, Devran, Furkan")
        print("Kardeş adı: Hülya, Gamze")
    if x == "güneş kim":
        print("Güneş Kim?")
        print("Değişmiş bir adı yok veya 2.bir ad yok.")
        print("Anne adı: Gamze")
        print("Baba adı: Erdoğan")
        print("Kardeşi veya çocuğu yok.")
    if x == "sude kim":
        print("Sude Kim?")
        print("Değişmiş bir adı yok.")
        print("2.Ad: Naz")
        print("Tüm Adı: SudeNaz")
        print("Anne adı: Hülya")
        print("Baba adı: Bekir")
        print("Kardeşi veya çocuğu yok.")
    if x == "sudenaz kim":
        print("Sude Kim?")
        print("Değişmiş bir adı yok.")
        print("2.Ad: Naz")
        print("Tüm Adı: SudeNaz")
        print("Anne adı: Hülya")
        print("Baba adı: Bekir")
        print("Kardeşi veya çocuğu yok.")
    if x == "onur kim":
        print("Onur Ayaz can Kim?")
        print("Değişmiş bir adı yok.")
        print("2.Ad: Ayaz")
        print("3.Ad: Can")
        print("Tüm Adı: Onur Ayaz Can")
        print("Anne adı: Serena")
        print("Baba adı: Emrullah")
        print("Kardeşleri: Muhammet Ali, Kumsal")
    if x == "muhammet kim":
        print("Muhammet Ali kim?")
        print("Değişmiş adı yok.")
        print("2.Ad: Ali")
        print("Tüm Adı: Muhammet Ali")
        print("Anne adı: Serena")
        print("Baba adı: Emrullah")
        print("Kardeşleri: Kumsal, Onur Ayaz can")
    if x == "muhammet ali kim":
        print("Muhammet Ali kim?")
        print("Değişmiş adı yok.")
        print("2.Ad: Ali")
        print("Tüm Adı: Muhammet Ali")
        print("Anne adı: Serena")
        print("Baba adı: Emrullah")
        print("Kardeşleri: Kumsal, Onur Ayaz can")
    if x == "onur ayaz can kim":
        print("Onur Ayaz can Kim?")
        print("Değişmiş bir adı yok.")
        print("2.Ad: Ayaz")
        print("3.Ad: Can")
        print("Tüm Adı: Onur Ayaz Can")
        print("Anne adı: Serena")
        print("Baba adı: Emrullah")
        print("Kardeşleri: Muhammet Ali, Kumsal")
    if x == "kumsal kim":
        print("Kumsal Kim?")
        print("Değişmiş veya 2.Adı yok.")
        print("Anne adı: Serena")
        print("Baba adı: Emrullah")
        print("Kardeşleri: Muhammet Ali, Onur ayaz can")
    if x == "not et":
        dosya = input("Dosya ismi ne olsun?: ")
        txtFile = dosya + ".txt"
        kaydet = input("Ne kaydetmek istersin?: ")
        theText = kaydet
        f = open(txtFile, "w", encoding="utf-8")
        f.writelines(theText)
        f.close()
    if x == "canım sıkkın":
        print(random.choice(cansikkin))
    if x == "müzik öner":
        print(random.choice(müzik))
    if x == "jarvis müzik öner":
        print(random.choice(müzik))
    if x == "müzik öner jarvis":
        print(random.choice(müzik))
    if x == "şarkı öner":
        print(random.choice(müzik))
    if x == "jarvis şarkı öner":
        print(random.choice(müzik))
    if x == "şarkı öner jarvis":
        print(random.choice(müzik))
    if x == "jarvis tarayıcıyı aç":
        print("Tamam efendim.")
        os.system('start C:\JarvisTarayici\main.py')
    if x == "tarayıcını aç":
        print("Tamam efendim.")
        os.system('start C:\JarvisTarayici\main.py')
    if x == "jarvis tarayıcısını aç":
        print("Tamam efendim.")
        os.system('start C:\JarvisTarayici\main.py')
    if x == "tarayıcı aç":
        print("Tamam efendim.")
        os.system('start C:\JarvisTarayici\main.py')
    if x == "protokolleri listele":
        print("Evi koruma protokolü")
    if x == "protokoller":
        print("Evi koruma protokolü")
    if x == "roblox aç":
        os.system('start C:\Roblox\Versions\version-5e9aac577efb4995')
    if x == "tekrar et":
        tekrar = input('Neyi tekrar etmemi istersiniz?: ')
        print(tekrar)
    if x == "tarayıcın":
        print("Tamam efendim.")
        os.system('start C:\JarvisTarayici\main.py')
    if x == "evi koruma protokolü":
        print("Evi Koruma Protokolü başlatılıyor...")
        sleep(1)
        print("Evi Koruma protokolü başlatıldı.")
        print("Salon Korunuyor.")
        print("Mutfak Korunuyor.")
        print("Oturma odası Korunuyor.")
        print("Tuvaletler Korunuyor.")
        print("yatak odaları Korunuyor.")
    if x == "evi koruma protokolünü başlat":
        print("Evi Koruma Protokolü başlatılıyor...")
        sleep(1)
        print("Evi Koruma protokolü başlatıldı.")
        print("Salon Korunuyor.")
        print("Mutfak Korunuyor.")
        print("Oturma odası Korunuyor.")
        print("Tuvaletler Korunuyor.")
        print("yatak odaları Korunuyor.")
    if x == "evi koruma protokolü başlatılsın":
        print("Evi Koruma Protokolü başlatılıyor...")
        sleep(1)
        print("Evi Koruma protokolü başlatıldı.")
        print("Salon Korunuyor.")
        print("Mutfak Korunuyor.")
        print("Oturma odası Korunuyor.")
        print("Tuvaletler Korunuyor.")
        print("yatak odaları Korunuyor.")
    if x == "yardım et":
        yardim1 = ['Ne için?: ', 'Ne oldu?: ', 'Yardıma ihtiyacınız olan şeyi söyleyin araştırayım: ']
        yardim2 = ['Sonucu buldum hemen ekrana yansıtıyorum.', 'Araştırdım ve buldum.', 'Google da araştırarak buldum.']
        yardim = input(random.choice(yardim1))
        print(random.choice(yardim2))
        webbrowser.open_new('https://www.google.com.tr/search?q='+yardim)
    if x == "yardım":
        yardim1 = ['Ne için?: ', 'Ne oldu?: ', 'Yardıma ihtiyacınız olan şeyi söyleyin araştırayım: ']
        yardim2 = ['Sonucu buldum hemen ekrana yansıtıyorum.', 'Araştırdım ve buldum.', 'Google da araştırarak buldum.']
        yardim = input(random.choice(yardim1))
        print(random.choice(yardim2))
        webbrowser.open_new('https://www.google.com.tr/search?q=' + yardim)
    if x == "günaydın":
        günaydin1 = ['Size de Günaydın.', 'Size de Günaydın Efendim, Kahvaltı için çok güzel bir saat.', 'Kahvaltı da size önerim; Çikolata, labne, yumurta, çay, ekmek, bal.', 'Sağlığınız için kahvaltıda ki yemekleri ayırt etmeden yemeniz gerekiyor.']
        print(random.choice(günaydin1))
    if x == "iyi geceler":
        iyigece = ['Size de iyi geceler.', 'Ben buralar da olacağım siz uyuyun efendim.']
        print(random.choice(iyigece))
    if x == "gelişmek ister misin":
        gelismek = ['Tabii ki isterim kim istemez ki?.', 'İsterim efendim.']
        print(random.choice(gelismek))
    if x == "ne durumdayız":
        durum = ['Jarvis tarayıcımız, Ben ve Karahan Uydularımız Var Efendim.', 'Gayet iyi durumdayız efendim.']
        print(random.choice(durum))
    if x == "internet hızı hesapla":
        soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        guvenli_baglanti = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
        guvenli_baglanti.options = ssl.OP_ALL
        soket = guvenli_baglanti.wrap_socket(soket, server_hostname='www.els-cdn.com')
        soket.connect(('ars.els-cdn.com', 443))

        soket.send(
            b'GET /content/image/1-s2.0-S001021801400399X-mmc10.txt HTTP/1.1\r\nHost: ars.els-cdn.com\r\nUser-Agent: Mozilla/5.0\r\nConnection: close\r\n\r\n')

        start = datetime.datetime.now()

        while True:
            data = soket.recv(1024)
            if not data:
                break

        print(round(10954213 / (datetime.datetime.now() - start).total_seconds() / (128 * 1000), 2))
    if x == "internet hızım":
        soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        guvenli_baglanti = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
        guvenli_baglanti.options = ssl.OP_ALL
        soket = guvenli_baglanti.wrap_socket(soket, server_hostname='www.els-cdn.com')
        soket.connect(('ars.els-cdn.com', 443))

        soket.send(
            b'GET /content/image/1-s2.0-S001021801400399X-mmc10.txt HTTP/1.1\r\nHost: ars.els-cdn.com\r\nUser-Agent: Mozilla/5.0\r\nConnection: close\r\n\r\n')

        start = datetime.datetime.now()

        while True:
            data = soket.recv(1024)
            if not data:
                break

        print(round(10954213 / (datetime.datetime.now() - start).total_seconds() / (128 * 1000), 2))
    if x == "internet hız kaç":
        soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        guvenli_baglanti = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
        guvenli_baglanti.options = ssl.OP_ALL
        soket = guvenli_baglanti.wrap_socket(soket, server_hostname='www.els-cdn.com')
        soket.connect(('ars.els-cdn.com', 443))

        soket.send(
            b'GET /content/image/1-s2.0-S001021801400399X-mmc10.txt HTTP/1.1\r\nHost: ars.els-cdn.com\r\nUser-Agent: Mozilla/5.0\r\nConnection: close\r\n\r\n')

        start = datetime.datetime.now()

        while True:
            data = soket.recv(1024)
            if not data:
                break

        print(round(10954213 / (datetime.datetime.now() - start).total_seconds() / (128 * 1000), 2))
    if x == "internet hızı kaç":
        soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        guvenli_baglanti = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
        guvenli_baglanti.options = ssl.OP_ALL
        soket = guvenli_baglanti.wrap_socket(soket, server_hostname='www.els-cdn.com')
        soket.connect(('ars.els-cdn.com', 443))

        soket.send(
            b'GET /content/image/1-s2.0-S001021801400399X-mmc10.txt HTTP/1.1\r\nHost: ars.els-cdn.com\r\nUser-Agent: Mozilla/5.0\r\nConnection: close\r\n\r\n')

        start = datetime.datetime.now()

        while True:
            data = soket.recv(1024)
            if not data:
                break

        print(round(10954213 / (datetime.datetime.now() - start).total_seconds() / (128 * 1000), 2))
    if x == "internet hızım kaç":
        soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        guvenli_baglanti = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
        guvenli_baglanti.options = ssl.OP_ALL
        soket = guvenli_baglanti.wrap_socket(soket, server_hostname='www.els-cdn.com')
        soket.connect(('ars.els-cdn.com', 443))

        soket.send(
            b'GET /content/image/1-s2.0-S001021801400399X-mmc10.txt HTTP/1.1\r\nHost: ars.els-cdn.com\r\nUser-Agent: Mozilla/5.0\r\nConnection: close\r\n\r\n')

        start = datetime.datetime.now()

        while True:
            data = soket.recv(1024)
            if not data:
                break

        print(round(10954213 / (datetime.datetime.now() - start).total_seconds() / (128 * 1000), 2))
    if x == "hangi sayı küçük hangi sayı büyük":
        sayilar = []

        flag = True
        while flag:
            try:
                a = int(input("Sayıları girin(bitirmek için -1): "))
                if a == -1:
                    flag = False
                else:
                    sayilar.append(float(a))
            except SyntaxError:
                print("HATA: Yalnızca sayı girin !")
            except NameError:
                print("HATA: Yalnızca sayı girin !")

        try:
            en_buyuk = sayilar[0]
            en_kucuk = sayilar[0]
            ortalama = sayilar[0]
        except IndexError:
            print("\nEn az bir sayı girmelisiniz")
            en_buyuk = "yok"
            en_kucuk = "yok"
            ortalama = "yok"
        finally:
            toplam = 0

        for sayi in sayilar:
            if sayi > en_buyuk:
                en_buyuk = sayi
            if sayi < en_kucuk:
                en_kucuk = sayi
            toplam += sayi

        ortalama = toplam / len(sayilar)

        print("\nen büyük sayı = {}\n" \
              "en küçük sayı = {}\n" \
              "ortalama      = {}".format(en_buyuk, en_kucuk, ortalama))
    if x == "hangisi küçük sayı":
        sayilar = []

        flag = True
        while flag:
            try:
                a = int(input("Sayıları girin(bitirmek için -1): "))
                if a == -1:
                    flag = False
                else:
                    sayilar.append(float(a))
            except SyntaxError:
                print("HATA: Yalnızca sayı girin !")
            except NameError:
                print("HATA: Yalnızca sayı girin !")

        try:
            en_buyuk = sayilar[0]
            en_kucuk = sayilar[0]
            ortalama = sayilar[0]
        except IndexError:
            print("\nEn az bir sayı girmelisiniz")
            en_buyuk = "yok"
            en_kucuk = "yok"
            ortalama = "yok"
        finally:
            toplam = 0

        for sayi in sayilar:
            if sayi > en_buyuk:
                en_buyuk = sayi
            if sayi < en_kucuk:
                en_kucuk = sayi
            toplam += sayi

        ortalama = toplam / len(sayilar)

        print("\nen büyük sayı = {}\n" \
              "en küçük sayı = {}\n" \
              "ortalama      = {}".format(en_buyuk, en_kucuk, ortalama))
    if x == "hangisi büyük sayı":
        sayilar = []

        flag = True
        while flag:
            try:
                a = int(input("Sayıları girin(bitirmek için -1): "))
                if a == -1:
                    flag = False
                else:
                    sayilar.append(float(a))
            except SyntaxError:
                print("HATA: Yalnızca sayı girin !")
            except NameError:
                print("HATA: Yalnızca sayı girin !")

        try:
            en_buyuk = sayilar[0]
            en_kucuk = sayilar[0]
            ortalama = sayilar[0]
        except IndexError:
            print("\nEn az bir sayı girmelisiniz")
            en_buyuk = "yok"
            en_kucuk = "yok"
            ortalama = "yok"
        finally:
            toplam = 0

        for sayi in sayilar:
            if sayi > en_buyuk:
                en_buyuk = sayi
            if sayi < en_kucuk:
                en_kucuk = sayi
            toplam += sayi

        ortalama = toplam / len(sayilar)

        print("\nen büyük sayı = {}\n" \
              "en küçük sayı = {}\n" \
              "ortalama      = {}".format(en_buyuk, en_kucuk, ortalama))
    if x == "büyük sayı hangisi":
        sayilar = []

        flag = True
        while flag:
            try:
                a = int(input("Sayıları girin(bitirmek için -1): "))
                if a == -1:
                    flag = False
                else:
                    sayilar.append(float(a))
            except SyntaxError:
                print("HATA: Yalnızca sayı girin !")
            except NameError:
                print("HATA: Yalnızca sayı girin !")

        try:
            en_buyuk = sayilar[0]
            en_kucuk = sayilar[0]
            ortalama = sayilar[0]
        except IndexError:
            print("\nEn az bir sayı girmelisiniz")
            en_buyuk = "yok"
            en_kucuk = "yok"
            ortalama = "yok"
        finally:
            toplam = 0

        for sayi in sayilar:
            if sayi > en_buyuk:
                en_buyuk = sayi
            if sayi < en_kucuk:
                en_kucuk = sayi
            toplam += sayi

        ortalama = toplam / len(sayilar)

        print("\nen büyük sayı = {}\n" \
              "en küçük sayı = {}\n" \
              "ortalama      = {}".format(en_buyuk, en_kucuk, ortalama))
    if x == "küçük sayı hangisi":
        sayilar = []

        flag = True
        while flag:
            try:
                a = int(input("Sayıları girin(bitirmek için -1): "))
                if a == -1:
                    flag = False
                else:
                    sayilar.append(float(a))
            except SyntaxError:
                print("HATA: Yalnızca sayı girin !")
            except NameError:
                print("HATA: Yalnızca sayı girin !")

        try:
            en_buyuk = sayilar[0]
            en_kucuk = sayilar[0]
            ortalama = sayilar[0]
        except IndexError:
            print("\nEn az bir sayı girmelisiniz")
            en_buyuk = "yok"
            en_kucuk = "yok"
            ortalama = "yok"
        finally:
            toplam = 0

        for sayi in sayilar:
            if sayi > en_buyuk:
                en_buyuk = sayi
            if sayi < en_kucuk:
                en_kucuk = sayi
            toplam += sayi

        ortalama = toplam / len(sayilar)

        print("\nen büyük sayı = {}\n" \
              "en küçük sayı = {}\n" \
              "ortalama      = {}".format(en_buyuk, en_kucuk, ortalama))
    if x == "büyük sayı hangisi":
        sayilar = []

        flag = True
        while flag:
            try:
                a = int(input("Sayıları girin(bitirmek için -1): "))
                if a == -1:
                    flag = False
                else:
                    sayilar.append(float(a))
            except SyntaxError:
                print("HATA: Yalnızca sayı girin !")
            except NameError:
                print("HATA: Yalnızca sayı girin !")

        try:
            en_buyuk = sayilar[0]
            en_kucuk = sayilar[0]
            ortalama = sayilar[0]
        except IndexError:
            print("\nEn az bir sayı girmelisiniz")
            en_buyuk = "yok"
            en_kucuk = "yok"
            ortalama = "yok"
        finally:
            toplam = 0

        for sayi in sayilar:
            if sayi > en_buyuk:
                en_buyuk = sayi
            if sayi < en_kucuk:
                en_kucuk = sayi
            toplam += sayi

        ortalama = toplam / len(sayilar)

        print("\nen büyük sayı = {}\n" \
              "en küçük sayı = {}\n" \
              "ortalama      = {}".format(en_buyuk, en_kucuk, ortalama))
    if x == "vücut kitle indeksi hesapla":
        def vki(x, y):
            global bki
            bki = x / ((y / 100) ** 2)
            print('Vücut kitle indeksiniz: ', bki)
            return bki

        x = float(input('Kütlenizi giriniz(kg): '))
        y = float(input('Boyunuzu giriniz(cm): '))

        vki(x, y)

        if bki < 18.5:
            print('Zayıfsınız.')
        elif bki < 24.9:
            print('Normalsiniz.')
        elif bki < 29.9:
            print('Fazla kilosunuz.')
        elif bki < 39.9:
            print('Şişmansınız.')
        else:
            print('Obezsiniz.')
    if x == "kg cm hesapla":
        def vki(x, y):
            global bki
            bki = x / ((y / 100) ** 2)
            print('Vücut kitle indeksiniz: ', bki)
            return bki

        x = float(input('Kütlenizi giriniz(kg): '))
        y = float(input('Boyunuzu giriniz(cm): '))

        vki(x, y)

        if bki < 18.5:
            print('Zayıfsınız.')
        elif bki < 24.9:
            print('Normalsiniz.')
        elif bki < 29.9:
            print('Fazla kilosunuz.')
        elif bki < 39.9:
            print('Şişmansınız.')
        else:
            print('Obezsiniz.')
    if x == "zayıf mı normal mi obez mi ":
        def vki(x, y):
            global bki
            bki = x / ((y / 100) ** 2)
            print('Vücut kitle indeksiniz: ', bki)
            return bki

        x = float(input('Kütlenizi giriniz(kg): '))
        y = float(input('Boyunuzu giriniz(cm): '))

        vki(x, y)

        if bki < 18.5:
            print('Zayıfsınız.')
        elif bki < 24.9:
            print('Normalsiniz.')
        elif bki < 29.9:
            print('Fazla kilosunuz.')
        elif bki < 39.9:
            print('Şişmansınız.')
        else:
            print('Obezsiniz.')
    if x == "zayıf mı":
        def vki(x, y):
            global bki
            bki = x / ((y / 100) ** 2)
            print('Vücut kitle indeksiniz: ', bki)
            return bki

        x = float(input('Kütlenizi giriniz(kg): '))
        y = float(input('Boyunuzu giriniz(cm): '))

        vki(x, y)

        if bki < 18.5:
            print('Zayıfsınız.')
        elif bki < 24.9:
            print('Normalsiniz.')
        elif bki < 29.9:
            print('Fazla kilosunuz.')
        elif bki < 39.9:
            print('Şişmansınız.')
        else:
            print('Obezsiniz.')
    if x == "zayıfmı":
        def vki(x, y):
            global bki
            bki = x / ((y / 100) ** 2)
            print('Vücut kitle indeksiniz: ', bki)
            return bki

        x = float(input('Kütlenizi giriniz(kg): '))
        y = float(input('Boyunuzu giriniz(cm): '))

        vki(x, y)

        if bki < 18.5:
            print('Zayıfsınız.')
        elif bki < 24.9:
            print('Normalsiniz.')
        elif bki < 29.9:
            print('Fazla kilosunuz.')
        elif bki < 39.9:
            print('Şişmansınız.')
        else:
            print('Obezsiniz.')
    if x == "normal mi":
        def vki(x, y):
            global bki
            bki = x / ((y / 100) ** 2)
            print('Vücut kitle indeksiniz: ', bki)
            return bki

        x = float(input('Kütlenizi giriniz(kg): '))
        y = float(input('Boyunuzu giriniz(cm): '))

        vki(x, y)

        if bki < 18.5:
            print('Zayıfsınız.')
        elif bki < 24.9:
            print('Normalsiniz.')
        elif bki < 29.9:
            print('Fazla kilosunuz.')
        elif bki < 39.9:
            print('Şişmansınız.')
        else:
            print('Obezsiniz.')
    if x == "normalmi":
        def vki(x, y):
            global bki
            bki = x / ((y / 100) ** 2)
            print('Vücut kitle indeksiniz: ', bki)
            return bki

        x = float(input('Kütlenizi giriniz(kg): '))
        y = float(input('Boyunuzu giriniz(cm): '))

        vki(x, y)

        if bki < 18.5:
            print('Zayıfsınız.')
        elif bki < 24.9:
            print('Normalsiniz.')
        elif bki < 29.9:
            print('Fazla kilosunuz.')
        elif bki < 39.9:
            print('Şişmansınız.')
        else:
            print('Obezsiniz.')
    if x == "obez mi":
        def vki(x, y):
            global bki
            bki = x / ((y / 100) ** 2)
            print('Vücut kitle indeksiniz: ', bki)
            return bki

        x = float(input('Kütlenizi giriniz(kg): '))
        y = float(input('Boyunuzu giriniz(cm): '))

        vki(x, y)

        if bki < 18.5:
            print('Zayıfsınız.')
        elif bki < 24.9:
            print('Normalsiniz.')
        elif bki < 29.9:
            print('Fazla kilosunuz.')
        elif bki < 39.9:
            print('Şişmansınız.')
        else:
            print('Obezsiniz.')
    if x == "obezmi":
        def vki(x, y):
            global bki
            bki = x / ((y / 100) ** 2)
            print('Vücut kitle indeksiniz: ', bki)
            return bki

        x = float(input('Kütlenizi giriniz(kg): '))
        y = float(input('Boyunuzu giriniz(cm): '))

        vki(x, y)

        if bki < 18.5:
            print('Zayıfsınız.')
        elif bki < 24.9:
            print('Normalsiniz.')
        elif bki < 29.9:
            print('Fazla kilosunuz.')
        elif bki < 39.9:
            print('Şişmansınız.')
        else:
            print('Obezsiniz.')
    if x == "yaş burç hesapla":
        print('Bugünün tarihi:', time.strftime('%c'))

        a = int(input('Doğdugunuz günü giriniz: '))
        b = int(input('Doğdugunuz ayı sayı olarak giriniz: '))
        c = int(input('Doğdugunuz yılı giriniz: '))

        if ((a > 20) & (b == 3)) or ((a < 21) & (b == 4)):
            y = 'Koç'
        elif ((a > 20) & (b == 4)) or ((a < 21) & (b == 5)):
            y = 'Boğa'
        elif ((a > 20) & (b == 5)) or ((a < 22) & (b == 6)):
            y = 'İkizler'
        elif ((a > 21) & (b == 6)) or ((a < 23) & (b == 7)):
            y = 'Yengeç'
        elif ((a > 22) & (b == 7)) or ((a < 23) & (b == 8)):
            y = 'Aslan'
        elif ((a > 22) & (b == 8)) or ((a < 23) & (b == 9)):
            y = 'Başak'
        elif ((a > 22) & (b == 9)) or ((a < 24) & (b == 10)):
            y = 'Terazi'
        elif ((a > 23) & (b == 10)) or ((a < 23) & (b == 11)):
            y = 'Akrep'
        elif ((a > 22) & (b == 11)) or ((a < 22) & (b == 12)):
            y = 'Yay'
        elif ((a > 21) & (b == 12)) or ((a < 21) & (b == 1)):
            y = 'Oğlak'
        elif ((a > 20) & (b == 1)) or ((a < 19) & (b == 2)):
            y = 'Kova'
        else:
            y = 'Balık'

        q = time.localtime()
        c = (q.tm_year) - (c)

        print('Yaşınız: {} yaşındasınız.'.format(c))
        print('Burcunuz: {}'.format(y))
    if x == "burç hesapla":
        print('Bugünün tarihi:', time.strftime('%c'))

        a = int(input('Doğdugunuz günü giriniz: '))
        b = int(input('Doğdugunuz ayı sayı olarak giriniz: '))
        c = int(input('Doğdugunuz yılı giriniz: '))

        if ((a > 20) & (b == 3)) or ((a < 21) & (b == 4)):
            y = 'Koç'
        elif ((a > 20) & (b == 4)) or ((a < 21) & (b == 5)):
            y = 'Boğa'
        elif ((a > 20) & (b == 5)) or ((a < 22) & (b == 6)):
            y = 'İkizler'
        elif ((a > 21) & (b == 6)) or ((a < 23) & (b == 7)):
            y = 'Yengeç'
        elif ((a > 22) & (b == 7)) or ((a < 23) & (b == 8)):
            y = 'Aslan'
        elif ((a > 22) & (b == 8)) or ((a < 23) & (b == 9)):
            y = 'Başak'
        elif ((a > 22) & (b == 9)) or ((a < 24) & (b == 10)):
            y = 'Terazi'
        elif ((a > 23) & (b == 10)) or ((a < 23) & (b == 11)):
            y = 'Akrep'
        elif ((a > 22) & (b == 11)) or ((a < 22) & (b == 12)):
            y = 'Yay'
        elif ((a > 21) & (b == 12)) or ((a < 21) & (b == 1)):
            y = 'Oğlak'
        elif ((a > 20) & (b == 1)) or ((a < 19) & (b == 2)):
            y = 'Kova'
        else:
            y = 'Balık'

        q = time.localtime()
        c = (q.tm_year) - (c)

        print('Yaşınız: {} yaşındasınız.'.format(c))
        print('Burcunuz: {}'.format(y))
    if x == "taş kağıt makas":
        a = ['Taş', 'Kağıt', 'Makas']

        def sonuc():
            if b == i:
                print('Berabere')
            elif (b == 'Taş') and (i == 'Kağıt'):
                print('{} kazandı.'.format(l))
            elif (b == 'Taş') and (i == 'Makas'):
                print('{} kazandı.'.format(k))
            elif (b == 'Kağıt') and (i == 'Taş'):
                print('{} kazandı.'.format(k))
            elif (b == 'Kağıt') and (i == 'Makas'):
                print('{} kazandı.'.format(l))
            elif (b == 'Makas') and (i == 'Taş'):
                print('{} kazandı.'.format(l))
            else:
                print('{} kazandı.'.format(k))

        k = input('Birinci kullanıcının  adını giriniz: ')
        l = input('İkinci kullanıcının adını giriniz: ')
        while 1:
            time.sleep(0.3)
            b = random.choice(a)
            time.sleep(0.3)
            i = random.choice(a)
            # Kodları Linux Shell üzerinden çalıştırınca karışık göründüğü için aralara boşluk kattım.
            print('                             ')
            print('{}='.format(k), b)
            print('                             ')
            print('{}='.format(l), i)
            print('                             ')
            sonuc()
            print('                             ')
            x = input('Tamam mı devam mı? Oyunu bitirmek için (ç), tekrar oynamak için herhangi bir şey yazın: ')
            if x in ['Ç', 'ç']:
                break
    if x == "şifre oluştur":
        p = []
        k = [
            'A',
            'B',
            'C',
            'Ç',
            'D',
            'E',
            'F',
            'G',
            'Ğ',
            'H',
            'I',
            'İ',
            'J',
            'K',
            'L',
            'M',
            'N',
            'O',
            'Ö',
            'P',
            'R',
            'S',
            'Ş',
            'T',
            'U',
            'Ü',
            'V',
            'Y',
            'Z',
            'Q',
            'W',
            'X',
            '0',
            '1',
            '2',
            '3',
            '4',
            '5',
            '6',
            '7',
            '8',
            '9'
        ]

        b = input('Şifreniz kaç haneli olsun? ')
        if b.isnumeric():
            a = int(b)
            i = 1
            while i <= a:
                t = random.choice(k)
                p.append(t)
                time.sleep(0.2)
                i = i + 1
            o = ''.join(p)
            print('Oluşturulan şifre: {}'.format(o))
        else:
            print('Hatalı.Lütfen sadece sayı giriniz.')
    if x == "tarih nedir":
        zaman = time.localtime()
        yıl = zaman[0]
        ay = zaman[1]
        gün = zaman[2]
        saat = zaman[3]
        dakika = zaman[4]
        saniye = zaman[5]

        def tarihvesaat():
            print('\ntarih: {}/{}/{}\nsaat : {}:{}:{}\n'.format(gün, ay, yıl, saat, dakika, saniye))

        tarihvesaat()
    if x == "tarih":
        zaman = time.localtime()
        yıl = zaman[0]
        ay = zaman[1]
        gün = zaman[2]
        saat = zaman[3]
        dakika = zaman[4]
        saniye = zaman[5]

        def tarihvesaat():
            print('\ntarih: {}/{}/{}\nsaat : {}:{}:{}\n'.format(gün, ay, yıl, saat, dakika, saniye))

        tarihvesaat()
    if x == "pi sayısı hesapla":
        n = 0
        s = 0

        r = int(input('Son sayıyı girin(varsayılan=1000000): '))
        # Son değişkeni ne kadar büyük yaparsak pi sayısının gerçek değerine o kadar yaklaşmış oluruz.

        while n < r:
            s = s + ((-1) ** n) / (2 * n + 1)
            n = n + 1
        print('Pi sayısının değeri:', 4 * s)
    if x == "faktöriyel hesapla":
        sayı = int(input('Faktöriyeli alınacak sayıyı girin: '))
        çarpım = 1
        for i in range(sayı):
            çarpım = çarpım * (i + 1)
        print(sayı, 'sayısının farktöriyeli=', çarpım)
    if x == "faktör hesapla":
        sayı = int(input('Faktöriyeli alınacak sayıyı girin: '))
        çarpım = 1
        for i in range(sayı):
            çarpım = çarpım * (i + 1)
        print(sayı, 'sayısının farktöriyeli=', çarpım)
    if x == "meslek tahmin et":
        doc_puan = 0
        av_puan = 0
        ogrt_puan = 0
        snt_puan = 0
        muh_puan = 0
        tam_puan = 0

        sorular = [""")Hangi alan sana daha yakın?
            1) Her türlü alan bana uygun
            2) Matematik ve Genetik
            3) Söz ve Edebiyat
            4) Teknoloji ve Tasarım
            5) Görsel Sanatlar ve Spor""",
                   """)Hangisi senin idolün olurdu?
                     1) Steve Jobs
                     2) Gazi Yaşargil
                     3) Naim Süleymanoğlu
                     4) Gönenç Gürkaynak
                     5) Nurten Akkuş""",
                   """)Hangisi seni daha çok mutlu eder?
                     1) Gerçek Yaşam Problemleri Çözmek
                     2) Arkadaşlarımın Takıldığı Yerlerde Onlara Yardımcı Olmak
                     3) Yeni Üretimler/Tasarımlar Yapmak
                     4) Spor Yapmak/Müzik Çalmak/Çizim Yapmak
                     5) Hesaplamalar Yapmak""",
                   """)Kendine hangi hediyeyi alırdın?
                     1) Bir yığın okunacak kitap
                     2) Müzik aleti / Top vs.""",
                   """)Hangisi seni korkutmaz?
                     1) Kan
                     2) Çok kişinin öninde performans sergilemek
                     3) Çeşitli yollarla az tanıdığım insanlarla iletişime geçmek
                     4) Herkes sana karşı çıksa da o kişiyi savunmak
                     5) Çeşitli alet-edevatlar""",
                   """)Gelecekte nasıl bir yerde çalışmak isterdin?
                     1) Devlet binasında
                     2) Ofis
                     3) Spor salonu""",
                   """)Son olaraak... Hangi nesne sana daha uygun?
                     1) Müzik aleti / Spor aleti vs.
                     2) Kablolar / Çizimler / Kodlar...
                     3) Beyaz Önlük
                     4) Tebeşir / Tahta Kalemi
                     5) Kategorilerine göre renklendirilmiş dosyalar"""]
        print("""
        7 soruyla gelecekteki mesleğinizi
        tahmin etmeye çalışacağım.
        Geliştirilmekte olduğumdan dolayı
        şu anda sadece 5 meslek tahmin
        edebilmekteyim. İşte onlar:

            > Doktor
            > Avukat
            > Öğretmen
            > Sanatçı
            > Mühendis
        Hazırsanız başlayalım!""")

        for i in range(7):
            print(f"{i + 1}.soru{sorular[i]}")
            cevap = int(input("Cevabınız: "))

            if i == 0 and cevap == 1:
                ogrt_puan += 1
                print("Yanıtınız kaydedildi.")
                time.sleep(3)

            elif i == 0 and cevap == 2:
                doc_puan += 1
                print("Yanıtınız kaydedildi.")
                time.sleep(3)

            elif i == 0 and cevap == 3:
                av_puan += 1
                print("Yanıtınız kaydedildi.")
                time.sleep(3)

            elif i == 0 and cevap == 4:
                muh_puan += 1
                print("Yanıtınız kaydedildi.")
                time.sleep(3)

            elif i == 0 and cevap == 5:
                snt_puan += 1
                print("Yanıtınız kaydedildi.")
                time.sleep(3)

            if i == 1 and cevap == 1:
                muh_puan += 1
                print("Yanıtınız kaydedildi.")
                time.sleep(3)

            elif i == 1 and cevap == 2:
                doc_puan += 1
                print("Yanıtınız kaydedildi.")
                time.sleep(3)

            elif i == 1 and cevap == 3:
                snt_puan += 1
                print("Yanıtınız kaydedildi.")
                time.sleep(3)

            elif i == 1 and cevap == 4:
                av_puan += 1
                print("Yanıtınız kaydedildi.")
                time.sleep(3)

            elif i == 1 and cevap == 5:
                ogrt_puan += 1
                print("Yanıtınız kaydedildi.")
                time.sleep(3)

            if i == 2 and cevap == 1:
                av_puan += 1
                print("Yanıtınız kaydedildi.")
                time.sleep(3)

            elif i == 2 and cevap == 2:
                ogrt_puan += 1
                print("Yanıtınız kaydedildi.")
                time.sleep(3)

            elif i == 2 and cevap == 3:
                muh_puan += 1
                print("Yanıtınız kaydedildi.")
                time.sleep(3)

            elif i == 2 and cevap == 4:
                snt_puan += 1
                print("Yanıtınız kaydedildi.")
                time.sleep(3)

            elif i == 2 and cevap == 5:
                doc_puan += 1
                print("Yanıtınız kaydedildi.")
                time.sleep(3)

            if i == 3 and cevap == 1:
                av_puan += 1
                doc_puan += 1
                ogrt_puan += 1
                muh_puan += 1
                print("Yanıtınız kaydedildi.")
                time.sleep(3)

            elif i == 3 and cevap == 2:
                snt_puan += 1
                print("Yanıtınız kaydedildi.")
                time.sleep(3)

            if i == 4 and cevap == 1:
                doc_puan += 1
                print("Yanıtınız kaydedildi.")
                time.sleep(3)

            elif i == 4 and cevap == 2:
                snt_puan += 1
                print("Yanıtınız kaydedildi.")
                time.sleep(3)

            elif i == 4 and cevap == 3:
                ogrt_puan += 1
                print("Yanıtınız kaydedildi.")
                time.sleep(3)

            elif i == 4 and cevap == 4:
                av_puan += 1
                print("Yanıtınız kaydedildi.")
                time.sleep(3)

            elif i == 4 and cevap == 5:
                muh_puan += 1
                print("Yanıtınız kaydedildi.")
                time.sleep(3)

            if i == 5 and cevap == 1:
                ogrt_puan += 1
                av_puan += 1
                doc_puan += 1
                print("Yanıtınız kaydedildi.")
                time.sleep(3)

            elif i == 5 and cevap == 2:
                muh_puan += 1
                print("Yanıtınız kaydedildi.")
                time.sleep(3)

            elif i == 5 and cevap == 3:
                snt_puan += 1
                print("Yanıtınız kaydedildi.")
                time.sleep(3)

            if i == 6 and cevap == 1:
                snt_puan += 1
                print("Yanıtınız kaydedildi.")
                time.sleep(3)

            elif i == 6 and cevap == 2:
                muh_puan += 1
                print("Yanıtınız kaydedildi.")
                time.sleep(3)

            elif i == 6 and cevap == 3:
                doc_puan += 1
                print("Yanıtınız kaydedildi.")
                time.sleep(3)

            elif i == 6 and cevap == 4:
                ogrt_puan += 1
                print("Yanıtınız kaydedildi.")
                time.sleep(3)

            elif i == 6 and cevap == 5:
                av_puan += 1
                print("Yanıtınız kaydedildi.")
                time.sleep(3)

        print(f"""
        Mesleklere yakınlık dereceniz:
        Doktor:{doc_puan}     ,     Avukat:{av_puan},
        Sanatçı:{snt_puan}     ,     Mühendis:{muh_puan},
        Öğretmen:{ogrt_puan}""")

        if doc_puan > av_puan:
            if doc_puan > snt_puan:
                if doc_puan > muh_puan:
                    if doc_puan > ogrt_puan:
                        print("Sizin gelecekteki mesleğiniz.... Doktor!")

        elif av_puan > doc_puan:
            if av_puan > snt_puan:
                if av_puan > muh_puan:
                    if av_puan > ogrt_puan:
                        print("Sizin gelecekteki mesleğiniz.... Avukat!")

        elif snt_puan > doc_puan:
            if snt_puan > av_puan:
                if snt_puan > muh_puan:
                    if snt_puan > ogrt_puan:
                        print("Sizin gelecekteki mesleğiniz.... Sanatçı!")

        elif ogrt_puan > doc_puan:
            if ogrt_puan > snt_puan:
                if ogrt_puan > muh_puan:
                    if ogrt_puan > av_puan:
                        print("Sizin gelecekteki mesleğiniz.... Öğretmen!")

        elif muh_puan > doc_puan:
            if muh_puan > snt_puan:
                if muh_puan > av_puan:
                    if muh_puan > ogrt_puan:
                        print("Sizin gelecekteki mesleğiniz.... Mühendis!")
    if x == "sos oyna":
        HANELER = (
            None,  # indekslerin 1'den başlaması için
            (0, 0), (0, 1), (0, 2),
            (1, 0), (1, 1), (1, 2),
            (2, 0), (2, 1), (2, 2),
        )
        KAZANMA_ÖLÇÜTLERİ = (
            # yatay
            (HANELER[1], HANELER[2], HANELER[3]),
            (HANELER[4], HANELER[5], HANELER[6]),
            (HANELER[7], HANELER[8], HANELER[9]),
            # dikey
            (HANELER[1], HANELER[4], HANELER[7]),
            (HANELER[2], HANELER[5], HANELER[8]),
            (HANELER[3], HANELER[6], HANELER[9]),
            # çapraz
            (HANELER[1], HANELER[5], HANELER[9]),
            (HANELER[3], HANELER[5], HANELER[7])
        )
        BOŞ_HANE = "_"
        GEÇERLİ_GİRDİLER = ("1", "2", "3", "4", "5", "6", "7", "8", "9")

        def ekranı_temizle():
            if os.name == "nt":
                os.system("cls")
            elif os.name == "posix":
                os.system("clear")
            else:
                os.system("cls")

        def tahtayı_yenile(tahta):
            ekranı_temizle()
            for satır in tahta:
                print("|", *satır, "|")
            print()

        def kazanan_kontrol(oyuncu_haneler):
            for ölçüt in KAZANMA_ÖLÇÜTLERİ:
                kontrol = [True for hane in ölçüt if hane in oyuncu_haneler]
                if len(kontrol) == 3:
                    return True  # hamleleri argüman olarak gönderilen oyuncu kazandı
            return False  # kazanan yok

        def main():
            devam = True
            while devam:
                devam = False

                # değişkenlerin ilk değerleri
                oyun = True
                tahta = [
                    [BOŞ_HANE, BOŞ_HANE, BOŞ_HANE],
                    [BOŞ_HANE, BOŞ_HANE, BOŞ_HANE],
                    [BOŞ_HANE, BOŞ_HANE, BOŞ_HANE]
                ]
                haneler_x = []
                haneler_o = []
                hamle = 1
                r = random.randrange(0, 2)

                tahtayı_yenile(tahta)

                while oyun:
                    # sıranın kimde olduğunun hesaplanması
                    if hamle % 2 == 1:
                        if r % 2 == 0:
                            işaret = "X"
                        else:
                            işaret = "O"
                    else:
                        if r % 2 == 0:
                            işaret = "O"
                        else:
                            işaret = "X"

                    print(f"Sıra {işaret} oyuncusunda")
                    girdi = input("> ")
                    if girdi == "q":
                        break
                    elif girdi not in GEÇERLİ_GİRDİLER:
                        print("Hatalı giriş!\n")
                        continue

                    y, x = HANELER[int(girdi)]
                    if tahta[y][x] == "_":  # girilen hane boşsa
                        if işaret == "X":
                            haneler_x.append((y, x))
                        else:
                            haneler_o.append((y, x))
                        tahta[y][x] = işaret
                        tahtayı_yenile(tahta)
                        hamle += 1

                        # oyun sonu kontrol
                        if hamle > 9:
                            print("BERABERE")
                            oyun = False
                            break
                        elif hamle > 5:
                            if işaret == "X":  # son hamleyi X yapmışsa
                                kazandı = kazanan_kontrol(haneler_x)
                                if kazandı:
                                    kazanan = "X"
                            else:  # son hamleyi O yapmışsa
                                kazandı = kazanan_kontrol(haneler_o)
                                if kazandı:
                                    kazanan = "O"

                            if kazandı:
                                print(f"{kazanan} KAZANDI")
                                oyun = False
                                break
                    else:
                        print("Girilen hane dolu!\n")
                        continue

                girdi = input("Tekrar oynamak istiyor musunuz? (e/h) ")
                if girdi == "e":
                    devam = True

            print("Oyundan çıkılıyor...")

        if __name__ == "__main__":
            main()
    if x == "hesap makinesi":
        print("İşlem Seçiniz : ('1' Toplama  '2' Çıkarma '3' Çarpma '4' Bölme)")

        def Topla(x, y):
            return x + y

        def Cikar(x, y):
            return x - y

        def Carp(x, y):
            return x * y

        def Bol(x, y):
            return x / y

        secim = input("Lütfen İşlemi Seçin : ")
        sayi1 = float(input("1. Sayiyi giriniz : "))
        sayi2 = float(input("2. Sayiyi Giriniz : "))

        if secim == '1':
            print("{} + {} = {} ".format(sayi1, sayi2, Topla(sayi1, sayi2)))
        elif secim == '2':
            print("{} - {} = {} ".format(sayi1, sayi2, Cikar(sayi1, sayi2)))
        elif secim == '3':
            print("{} * {} = {} ".format(sayi1, sayi2, Carp(sayi1, sayi2)))
        elif secim == '4':
            print("{} / {} = {} ".format(sayi1, sayi2, Bol(sayi1, sayi2)))
    if x == "zar at":
        kullanici1Skor = 0
        kullanici2Skor = 0

        while True:
            kullanici1 = random.randint(1, 6)
            print("Kullanıcı 1: ", kullanici1)
            time.sleep(1)
            kullanici2 = random.randint(1, 6)
            print("Kullanıcı 2: ", kullanici2)
            time.sleep(1)
            if kullanici1 > kullanici2:
                print("Kullanıcı 1 kazandı.")
                kullanici1Skor += 1
            elif kullanici2 > kullanici1:
                print("Kullanıcı 2 kazandı.")
                kullanici2Skor += 1
            else:
                print("Berabere bitti.")

            # Kullanıcı 1 : 5 - 3 : Kullanıcı 2
            if kullanici1Skor == 5 or kullanici2Skor == 5:
                print("Kullanıcı 1 :", kullanici1Skor, " - ", kullanici2Skor, ": Kullanıcı 2")
                break
    if x == "zar oyna":
        kullanici1Skor = 0
        kullanici2Skor = 0

        while True:
            kullanici1 = random.randint(1, 6)
            print("Kullanıcı 1: ", kullanici1)
            time.sleep(1)
            kullanici2 = random.randint(1, 6)
            print("Kullanıcı 2: ", kullanici2)
            time.sleep(1)
            if kullanici1 > kullanici2:
                print("Kullanıcı 1 kazandı.")
                kullanici1Skor += 1
            elif kullanici2 > kullanici1:
                print("Kullanıcı 2 kazandı.")
                kullanici2Skor += 1
            else:
                print("Berabere bitti.")

            # Kullanıcı 1 : 5 - 3 : Kullanıcı 2
            if kullanici1Skor == 5 or kullanici2Skor == 5:
                print("Kullanıcı 1 :", kullanici1Skor, " - ", kullanici2Skor, ": Kullanıcı 2")
                break
    if x == "ısı hesapla":
        def CelsiusToFahrenheit(celsius):
            Fahrenheit = celsius * 1.8 + 32
            return Fahrenheit

        def FahrenheitToCelsius(Fahrenheit):
            Celsius = (Fahrenheit - 32) / 1.8
            return Celsius

        def CelsiusToKelvin(celsius):
            Kelvin = celsius + 273.15
            return Kelvin

        def KelvinToCelsius(Kelvin):
            Celsius = Kelvin - 273.15
            return Celsius

        dereceAl = float(input("Lütfen celsius olarak dereceyi giriniz: "))
        print("Fahrenheit: ", CelsiusToFahrenheit(dereceAl))
        print("Kelvin: ", CelsiusToKelvin(dereceAl))
    if x == "sıcaklık hesapla":
        def CelsiusToFahrenheit(celsius):
            Fahrenheit = celsius * 1.8 + 32
            return Fahrenheit

        def FahrenheitToCelsius(Fahrenheit):
            Celsius = (Fahrenheit - 32) / 1.8
            return Celsius

        def CelsiusToKelvin(celsius):
            Kelvin = celsius + 273.15
            return Kelvin

        def KelvinToCelsius(Kelvin):
            Celsius = Kelvin - 273.15
            return Celsius

        dereceAl = float(input("Lütfen celsius olarak dereceyi giriniz: "))
        print("Fahrenheit: ", CelsiusToFahrenheit(dereceAl))
        print("Kelvin: ", CelsiusToKelvin(dereceAl))
    if x == "sayı tahmini oyunu":
        uretilenSayi = random.randint(1, 100)
        tahminHakki = 5

        while True:
            tahmin = int(input("Lütfen Tahmininizi Giriniz: "))
            if tahmin == uretilenSayi:
                print("Tebrikler! Kazandınız.")
                break
            elif tahmin > uretilenSayi:
                tahminHakki -= 1
                print("Yanlış tahmin, tahmininizi küçültünüz. ")
                print("Kalan tahmin adedi: ", tahminHakki)
            elif tahmin < uretilenSayi:
                tahminHakki -= 1
                print("Yanlış tahmin, tahmininizi büyütünüz. ")
                print("Kalan tahmin adedi: ", tahminHakki)
            if tahminHakki == 0:
                print("Hakkınız bitti efendim tahmin sayısı: ", uretilenSayi)

                break
    if x == "sayı tahmini":
        uretilenSayi = random.randint(1, 100)
        tahminHakki = 5

        while True:
            tahmin = int(input("Lütfen Tahmininizi Giriniz: "))
            if tahmin == uretilenSayi:
                print("Tebrikler! Kazandınız.")
                break
            elif tahmin > uretilenSayi:
                tahminHakki -= 1
                print("Yanlış tahmin, tahmininizi küçültünüz. ")
                print("Kalan tahmin adedi: ", tahminHakki)
            elif tahmin < uretilenSayi:
                tahminHakki -= 1
                print("Yanlış tahmin, tahmininizi büyütünüz. ")
                print("Kalan tahmin adedi: ", tahminHakki)
            if tahminHakki == 0:
                print("Hakkınız bitti efendim tahmin sayısı: ", uretilenSayi)

                break
    if x == "sayı tahmin":
        uretilenSayi = random.randint(1, 100)
        tahminHakki = 5

        while True:
            tahmin = int(input("Lütfen Tahmininizi Giriniz: "))
            if tahmin == uretilenSayi:
                print("Tebrikler! Kazandınız.")
                break
            elif tahmin > uretilenSayi:
                tahminHakki -= 1
                print("Yanlış tahmin, tahmininizi küçültünüz. ")
                print("Kalan tahmin adedi: ", tahminHakki)
            elif tahmin < uretilenSayi:
                tahminHakki -= 1
                print("Yanlış tahmin, tahmininizi büyütünüz. ")
                print("Kalan tahmin adedi: ", tahminHakki)
            if tahminHakki == 0:
                print("Hakkınız bitti efendim tahmin sayısı: ", uretilenSayi)

                break
    if x == "aşık oldum sanırım":
        kim = ['O şanslı kim? ', 'Çok mutlu oldum o kim? ']
        km254 = input(random.choice(kim))
        kim2 = [' Biraz araştırdım mükemmel birisi.', ' Kadar güzeli olduğunu sanmıyorum.', ' Gerçekten güzelmiş.']
        print(km254 + random.choice(kim2))
    if x == "aşık oldum":
        kim = ['O şanslı kim? ', 'Çok mutlu oldum o kim? ']
        km254 = input(random.choice(kim))
        kim2 = [' Biraz araştırdım mükemmel birisi.', ' Kadar güzeli olduğunu sanmıyorum.', ' Gerçekten güzelmiş.']
        print(km254 + random.choice(kim2))
    if x == "sanırım aşık oldum":
        kim = ['O şanslı kim? ', 'Çok mutlu oldum o kim? ']
        km254 = input(random.choice(kim))
        kim2 = [' Biraz araştırdım mükemmel birisi.', ' Kadar güzeli olduğunu sanmıyorum.', ' Gerçekten güzelmiş.']
        print(km254 + random.choice(kim2))
    if x == "jarvis aşık oldum":
        kim = ['O şanslı kim? ', 'Çok mutlu oldum o kim? ']
        km254 = input(random.choice(kim))
        kim2 = [' Biraz araştırdım mükemmel birisi.', ' Kadar güzeli olduğunu sanmıyorum.', ' Gerçekten güzelmiş.']
        print(km254 + random.choice(kim2))
    if x == "jarvis sanırım aşık oldum":
        kim = ['O şanslı kim? ', 'Çok mutlu oldum o kim? ']
        km254 = input(random.choice(kim))
        kim2 = [' Biraz araştırdım mükemmel birisi.', ' Kadar güzeli olduğunu sanmıyorum.', ' Gerçekten güzelmiş.']
        print(km254 + random.choice(kim2))
    if x == "ondan hoşlanıyorum":
        kim = ['O şanslı kim? ', 'Çok mutlu oldum o kim? ']
        km254 = input(random.choice(kim))
        kim2 = [' Biraz araştırdım mükemmel birisi.', ' Kadar güzeli olduğunu sanmıyorum.', ' Gerçekten güzelmiş.']
        print(km254 + random.choice(kim2))
    if x == "hoşlanıyorum ondan":
        kim = ['O şanslı kim? ', 'Çok mutlu oldum o kim? ']
        km254 = input(random.choice(kim))
        kim2 = [' Biraz araştırdım mükemmel birisi.', ' Kadar güzeli olduğunu sanmıyorum.', ' Gerçekten güzelmiş.']
        print(km254 + random.choice(kim2))
    if x == "bütün hatları dinle":
        print("Bütün hatlar dinleniyor...")
        sleep(1)
        print("Karakol hatlarından gelen ihbar sayısı: ")
        print(random.randint(1, 1000000))
        print("Hastane hatlarından gelen ihbar sayıları: ")
        print(random.randint(1, 1000000))
        print("İtfaiye hatlarından gelen ihbar sayıları: ")
        print(random.randint(1, 1000000))
        print("Ve diğer tüm hatlardan gelen toplam ihbar sayısı: ")
        print(random.randint(1, 1000000))
    if x == "karakol hatlarını dinle":
        print("Karakol hatlarından gelen ihbar sayısı: ")
        print(random.randint(1, 1000000))
    if x == "hastane hatlarını dinle":
        print("Hastane hatlarından gelen ihbar sayısı: ")
        print(random.randint(1, 1000000))
    if x == "itfaiye hatlarını dinle":
        print("İtfaiye hatlarından gelen ihbar sayısı: ")
        print(random.randint(1, 1000000))
    if x == "denklem çöz":
        print("2.Dereceden denklem çözmek için hazırım.")

        # denklem = ax**2 + bx + c = 0

        a = float(input("Lütfen x karenin katsayısını giriniz : "))
        b = float(input("Lütfen x'in katsayısını giriniz : "))
        c = float(input("Lütfen sabit sayiyi giriniz : "))

        delta = b ** 2 - 4 * a * c

        if delta > 0:
            x1 = (- b - delta ** 0.5) / (2 * a)  # 0.5 karekök.
            x2 = (- b + delta ** 0.5) / (2 * a)

            print("Denklemin 2 Reel kökü vardır bunlar : ")
            print("X1 = ", x1)
            print("X2 = ", x2)

        if delta == 0:
            x1 = (- b + delta ** 0.5) / (2 * a)
            x2 = (- b + delta ** 0.5) / (2 * a)
            x1 = x2
            print("Bu denklemin bir kökü vardır = ", x1)

        if delta < 0:
            print("Bu denklemin Reel kökü yoktur. ")
    if x == "kdv hesapla":
        KDV1 = float(0.18)
        KDV2 = float(0.08)
        KDV3 = float(0.01)
        kDvhesap = input("Kdv Oranı seçiniz: 1= %18 2= %8 3= %1 4= 0. şeklinde giriniz.")
        tutar = float(input("Ürünün Fıyatını Giriniz..."))
        birim = int(input("Ürünün Miktarını giriniz..."))

        def kdvhesaplayıcı1(tutar):
            kdv = tutar * KDV1
            toplam = tutar + kdv
            çıkar = tutar - kdv
            ttoplamkdv = toplam * birim
            ccıkışkdv = çıkar * birim
            kdv1toplam = kdv * birim
            print("Kdv Dahil adet fiyatı = " + str(toplam))
            print("Adet Kdv tutarı= " + str(kdv))
            print("Adet Kdv Hariç= " + str(çıkar))
            print("Toplam Kdv Dahil= " + str(ttoplamkdv))
            print("Toplam Kdv Hariç= " + str(ccıkışkdv))
            print("Toplam Kdv= " + str(kdv1toplam))

        def kdvhesaplayıcı2(tutar):
            kdv = tutar * KDV2
            toplam = tutar + kdv
            çıkar = tutar - kdv
            ttoplamkdv = toplam * birim
            ccıkışkdv = çıkar * birim
            kdv1toplam = kdv * birim
            print("Kdv Dahil adet fiyatı = " + str(toplam))
            print("Adet Kdv tutarı= " + str(kdv))
            print("Adet Kdv Hariç= " + str(çıkar))
            print("Toplam Kdv Dahil= " + str(ttoplamkdv))
            print("Toplam Kdv Hariç= " + str(ccıkışkdv))
            print("Toplam Kdv= " + str(kdv1toplam))

        def kdvhesaplayıcı3(tutar):
            kdv = tutar * KDV3
            toplam = tutar + kdv
            çıkar = tutar - kdv
            ttoplamkdv = toplam * birim
            ccıkışkdv = çıkar * birim
            kdv1toplam = kdv * birim
            print("Kdv Dahil adet fiyatı = " + str(toplam))
            print("Adet Kdv tutarı= " + str(kdv))
            print("Adet Kdv Hariç= " + str(çıkar))
            print("Toplam Kdv Dahil= " + str(ttoplamkdv))
            print("Toplam Kdv Hariç= " + str(ccıkışkdv))
            print("Toplam Kdv= " + str(kdv1toplam))

        def kdvhesaplayıcı4(tutar):
            kdv = tutar * KDV4
            toplam = tutar + kdv
            çıkar = tutar - kdv
            ttoplamkdv = toplam * birim
            ccıkışkdv = çıkar * birim
            kdv1toplam = kdv * birim
            print("Kdv Dahil adet fiyatı = " + str(toplam))
            print("Adet Kdv tutarı= " + str(kdv))
            print("Adet Kdv Hariç= " + str(çıkar))
            print("Toplam Kdv Dahil= " + str(ttoplamkdv))
            print("Toplam Kdv Hariç= " + str(ccıkışkdv))
            print("Toplam Kdv= " + str(kdv1toplam))

        if kDvhesap == "1":
            print(kdvhesaplayıcı1(tutar))

        elif kDvhesap == "2":
            print(kdvhesaplayıcı2(tutar))
        elif kDvhesap == "3":
            print(kdvhesaplayıcı3(tutar))
        elif kDvhesap == "4":
            KDV4 = float(input("istediğiniz oranı girin"))
            print(kdvhesaplayıcı4(tutar))
        else:
            print("Lütfen Birini Seçiniz...")
    if x == "kaç mile eder":
        donusumOrani = 0.621371192
        km = int(input("Kaç km?"))

        mil = km * donusumOrani
        print(str(km) + " Km = " + str(mil) + " mil eder")
    if x == "kaç mil eder":
        donusumOrani = 0.621371192
        km = int(input("Kaç km?"))

        mil = km * donusumOrani
        print(str(km) + " Km = " + str(mil) + " mil eder")
    if x == "kmyi mile dönüştür":
        donusumOrani = 0.621371192
        km = int(input("Kaç km?"))

        mil = km * donusumOrani
        print(str(km) + " Km = " + str(mil) + " mil eder")
    if x == "km yi mile dönüştür":
        donusumOrani = 0.621371192
        km = int(input("Kaç km?"))

        mil = km * donusumOrani
        print(str(km) + " Km = " + str(mil) + " mil eder")
    if x == "günü bul":
        aylar = {1: 31, 2: 00, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        gunler = {1: "PAZARTESİ", 2: "SALI", 3: "ÇARŞAMBA", 4: "PERŞEMBE", 5: "CUMA", 6: "CUMARTESİ", 7: "PAZAR"}

        def artikyil(y):
            if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
                return True
            else:
                return False

        gun = int(input("günü giriniz :"))
        ay = int(input("ayı  giriniz :"))
        yil = int(input("yılı giriniz :"))

        toplam = (yil - 1) * 365 + int((yil - 1) / 4) - int((yil - 1) / 100) + int((yil - 1) / 400)
        if artikyil(yil) == True:
            aylar[2] = 29
        else:
            aylar[2] = 28

        for i in range(1, ay - 1 + 1):
            toplam += aylar[i]

        toplam += gun

        k = toplam - int(toplam / 7) * 7

        if k == 0: k = 7

        print(gun, ".", ay, ".", yil, " :", gunler[k])
    if x == "gün bul":
        aylar = {1: 31, 2: 00, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        gunler = {1: "PAZARTESİ", 2: "SALI", 3: "ÇARŞAMBA", 4: "PERŞEMBE", 5: "CUMA", 6: "CUMARTESİ", 7: "PAZAR"}

        def artikyil(y):
            if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
                return True
            else:
                return False

        gun = int(input("günü giriniz :"))
        ay = int(input("ayı  giriniz :"))
        yil = int(input("yılı giriniz :"))

        toplam = (yil - 1) * 365 + int((yil - 1) / 4) - int((yil - 1) / 100) + int((yil - 1) / 400)
        if artikyil(yil) == True:
            aylar[2] = 29
        else:
            aylar[2] = 28

        for i in range(1, ay - 1 + 1):
            toplam += aylar[i]

        toplam += gun

        k = toplam - int(toplam / 7) * 7

        if k == 0: k = 7

        print(gun, ".", ay, ".", yil, " :", gunler[k])
    if x == "kilometre hesapla":
        yakit = float(input("kilometrede ne kadar yakıyor: "))
        km = int(input("Kaç kilometre yol yaptınız: "))
        odenecekTutar = yakit * km
        print("kilometrede ne kadar yakıyor: {}\nKaç kilometre yol yaptınız:: {}\nodenecekTutar: {} TL\n".format(yakit, km, odenecekTutar))
    if x == "kilometre":
        yakit = float(input("kilometrede ne kadar yakıyor: "))
        km = int(input("Kaç kilometre yol yaptınız: "))
        odenecekTutar = yakit * km
        print("kilometrede ne kadar yakıyor: {}\nKaç kilometre yol yaptınız:: {}\nodenecekTutar: {} TL\n".format(yakit, km, odenecekTutar))
    if x == "km hesapla":
        yakit = float(input("kilometrede ne kadar yakıyor: "))
        km = int(input("Kaç kilometre yol yaptınız: "))
        odenecekTutar = yakit * km
        print("kilometrede ne kadar yakıyor: {}\nKaç kilometre yol yaptınız:: {}\nodenecekTutar: {} TL\n".format(yakit, km, odenecekTutar))
    if x == "youtube aç":
        print("Youtube açıldı efendim.")
        webbrowser.open_new_tab('https://www.youtube.com')
    if x == "youtube":
        print("Youtube açıldı efendim.")
        webbrowser.open_new_tab('https://www.youtube.com')
    if x == "twitter aç":
        print("Twitter açıldı efendim.")
        webbrowser.open_new_tab('https://www.twitter.com')
    if x == "twitter":
        print("Twitter açıldı efendim.")
        webbrowser.open_new_tab('https://www.twitter.com')
    if x == "instagram aç":
        print("İnstagram açıldı efendim.")
        webbrowser.open_new_tab('https://www.instagram.com')
    if x == "instagram":
        print("İnstagram açıldı efendim.")
        webbrowser.open_new_tab('https://www.instagram.com')
    if x == "replit aç":
        print("Replit açıldı efendim.")
        webbrowser.open_new_tab('https://www.replit.com')
    if x == "replit":
        print("Replit açıldı efendim.")
        webbrowser.open_new_tab('https://www.replit.com')
    if x == "github aç":
        print("Git Hub açıldı efendim.")
        webbrowser.open_new_tab('https://www.github.com')
    if x == "github":
        print("Git Hub açıldı efendim.")
        webbrowser.open_new_tab('https://www.github.com')
    if x == "site aç":
        sitename = input("Site ismi nedir? ")
        webbrowser.open_new_tab('https://www.google.com.tr/search?q='+sitename)
    if x == "site":
        sitename = input("Site ismi nedir? ")
        webbrowser.open_new_tab('https://www.google.com.tr/search?q=' + sitename)
    if x == "bul":
        araştır = input("Ne araştırmamı istersiniz?: ")
        url = "https://www.google.com/search?q=" + araştır
        webbrowser.get().open(url)
        print(araştır + " ile ilgili aramaları Google ekranına yansıttım")
        #e = input("Ekranı yansıtayım mı yoksa bilgiyi buraya mı yazayım?   ")
        #if e == "buraya yaz":
         #   LSDdsfg = ['Peki, Bilgiyi buraya yazıyorum.', 'Tamam.', 'Bilgiyi buraya yazıyorum.', 'Bilgiyi buraya yazdım.']
          #  print(random.choice(LSDdsfg))
           # baslik = input("Başlığı Giriniz: ")
            #link = "https://tr.wikipedia.org/wiki/" + str(baslik.lower())
            #r = requests.get(link)
            #soup = BeautifulSoup(r.content)
            #st1 = soup.find_all("div", attrs={"id": "bodyContent"})
            #text = st1[0].text
            #print(text)
    #else:
     #       baslik = input("Başlığı Giriniz: ")
      #      link = "https://tr.wikipedia.org/wiki/" + str(baslik.lower())
      #      r = requests.get(link)
       #     soup = BeautifulSoup(r.content)
       #     st1 = soup.find_all("div", attrs={"id": "bodyContent"})
       #     text = st1[0].text
       #     print(text)
       #     DSL = ['Tamam, bilgiyi ekrana yansıttım.', 'Bilgi şu anda ekran da.', 'Bilgiyi Ekrana yansıttım.', 'Peki, bilgiyi ekrana yansıttım.']
        #    print(random.choice(DSL))
         #   webbrowser.open_new_tab(link = "https://tr.wikipedia.org/wiki/" + str(baslik.lower()))
    if x == "şarkı söyle":
        sarki = ['Ayaz vurur, yine donar umutlar Siyah sayfaları yırtıp, yakıp at Harca anıları, elinde kalanları Solup gider benliğimiz belki, kadın Ayaz vurur, yine donar umutlar Siyah sayfaları yırtıp, yakıp at Harca anıları, elinde kalanları Gözlerine sakla beni, deli kadın Kalk, gülüm, kuşum (gülüm, kuşum) Yaptığım hata, yıllarım yalan Sensiz bir hayat dengemi bozar Özlemin canım yakar Ah, hikâyeler var (hikâyeler var) Yalan onlar bak, gönlüm yanacak Uzak durma, cananım Hasretim zarar ömrüme kalan Ayaz vurur, yine donar umutlar Siyah sayfaları yırtıp, yakıp at Harca anıları, elinde kalanları Solup gider benliğimiz belki, kadın Ayaz vurur, yine donar umutlar Siyah sayfaları yırtıp, yakıp at Harca anıları, elinde kalanları Gözlerine sakla beni, deli kadın Ne zor yokluğun acısı Hep meyhane köşelerinde kalan Gençliğimin yarısı İçinde kanasın sevginin yarası Umuda ayaz vuracak Ayaz vurur, yine donar umutlar Siyah sayfaları yırtıp, yakıp at Harca anıları, elinde kalanları Solup gider benliğimiz belki, kadın Ayaz vurur, yine donar umutlar Siyah sayfaları yırtıp, yakıp at Harca anıları, elinde kalanları Solup gider benliğimiz belki, kadın Ayaz vurur, yine donar umutlar Siyah sayfaları yırtıp, yakıp at Harca anıları, elinde kalanları Gözlerine sakla beni, deli kadın.', 'Koruyan bizi biri var Olsun, hepimizin üzerinde peri var Bana zoru var, çelik yelek al Kafama tatil yazdım sakin Kafamızı yoruyolar (biliyom) Aynayı seviyolar (biliyom) Vardım yarı yola Dokunur elim ona Bu konur zehir ona Kafamızı yoruyolar (biliyom) Aynayı seviyolar (biliyom) Vardım yarı yola Dokunur elim ona Bu konur zehir ona İz yapar, her gece kovdum Kafaları dinleme, gerçeği duydum İstedim ay gibi gecelere doğsun Üstüme gelmesin, ellerin olsun Kendine geldi, duruldum çoktan Yok yere kalbini kırmadım olsun Bir kere gülmedi, zordu Gidişi ani, bi gülse bari Kafamızı yoruyolar (biliyom) Aynayı seviyolar (biliyom) Vardım yarı yola Dokunur elim ona Bu konur zehir ona Kafamızı yoruyolar (biliyom) Aynayı seviyolar (biliyom) Vardım yarı yola Dokunur elim ona Bu konur zehir ona Taramalı makinadır, yanımda eser Paso kötü güne çıkıyoruz, kanımda bi sen Bi de bakışların, bakışların hoşuma gider Gece ben gibi seveni de seninle üzer Kafamızı yoruyolar (biliyom) Aynayı seviyolar (biliyom) Vardım yarı yola Dokunur elim ona Bu konur zehir ona Kafamızı yoruyorlar (biliyom) Aynayı seviyorlar (biliyom) Vardım yarı yola Dokunur elim ona Bu konur zehir ona']
        print(random.choice(sarki))
    if x == "sihirli sekiz top":
        answers = ["Bu kesin.", "Tabii ki.", "buna güvenebilirsin.", "Sonra tekrar sor.",
                   "konsantre ol ve tekrar sor.", "cevabım hayır.", "Kaynaklarım olumsuz diyor.", "Bundan daha kesin bir şey yok.", "sizi seviyor.", "sizi sevmiyor."]
        input("Sorunuzu sihirli sekiz topa sorun: ")

        print("Cevap: {}".format(choice(answers)))
    if x == "aşk hesapla":
        isim1 = input("İsminiz: ")
        isim2 = input("Sevdiğinizin İsmi: ")
        print(isim1, "ve", isim2, "Aşk sonucu: ")
        print(random.randint(1, 100))
    if x == "metni tersine çevir":
        def reverse(value, output=[]):
            # range(start, stop, step)
            for i in range(len(value) - 1, -1, -1):
                output.append(value[i])

            return "".join(output)

        text = input("Metin nedir? ")
        print("Metnin tersine çevrilmiş hali: {}".format(reverse(text)))
    if x == "metini tersine çevir":
        def reverse(value, output=[]):
            # range(start, stop, step)
            for i in range(len(value) - 1, -1, -1):
                output.append(value[i])

            return "".join(output)

        text = input("Metin nedir? ")
        print("Metnin tersine çevrilmiş hali: {}".format(reverse(text)))
    if x == "yazıyı tersine çevir":
        def reverse(value, output=[]):
            # range(start, stop, step)
            for i in range(len(value) - 1, -1, -1):
                output.append(value[i])

            return "".join(output)

        text = input("Metin nedir? ")
        print("Metnin tersine çevrilmiş hali: {}".format(reverse(text)))
    if x == "tersten yaz":
        def reverse(value, output=[]):
            # range(start, stop, step)
            for i in range(len(value) - 1, -1, -1):
                output.append(value[i])

            return "".join(output)

        text = input("Metin nedir? ")
        print("Metnin tersine çevrilmiş hali: {}".format(reverse(text)))
    if x == "metinde ki ünlü harfler":
        def vowels_count(text, output=0):
            vowels = "aeiouAEIOU"
            for char in text:
                if char in vowels:
                    output += 1
            return output

        text = input("Metni girin: ")
        print("Metinde ki ünlü harfler: {}".format(vowels_count(text)))
    if x == "metindeki ünlü harfler":
        def vowels_count(text, output=0):
            vowels = "aeiouAEIOU"
            for char in text:
                if char in vowels:
                    output += 1
            return output

        text = input("Metni girin: ")
        print("Metinde ki ünlü harfler: {}".format(vowels_count(text)))
    if x == "metinde kaç tane ünlü harf var":
        def vowels_count(text, output=0):
            vowels = "aeiouAEIOU"
            for char in text:
                if char in vowels:
                    output += 1
            return output

        text = input("Metni girin: ")
        print("Metinde ki ünlü harfler: {}".format(vowels_count(text)))
    if x == "adam asmaca oyna":
        pics = ["""
           +---+
           |   |
               |
               |
               |
               |
        =========""", """
           +---+
           |   |
           O   |
               |
               |
               |
        =========""", """
           +---+
           |   |
           O   |
           |   |
               |
               |
        =========""", """
           +---+
           |   |
           O   |
          /|   |
               |
               |
        =========""", """
           +---+
           |   |
           O   |
          /|\  |
               |
               |
        =========""", """
           +---+
           |   |
           O   |
          /|\  |
          /    |
               |
        =========""", """
           +---+
           |   |
           O   |
          /|\  |
          / \  |
               |
        ========="""]

        while True:
            print(("-" * 30) + "\nAdam asmaca oyunu\n" + ("-" * 30))

            word = random.choice(["windows", "python", "terminal", "ubuntu", "merhaba", "adam", "devran", "furkan", "emirhan", "serpil", "emrah", "günaydın", "osmanlı", "türkiye", "amerika", "jarvis"])
            step = 0
            letters = []

            while True:
                print(pics[step])

                for i, char in enumerate(word):
                    print(char if i in letters else "_"),

                answer = input("\nCevap: ")

                if answer == word:
                    print("Kazandın!\n\n")
                    break
                else:
                    while True:
                        rand = random.randint(0, len(word))
                        if not rand in letters:
                            letters.append(rand)
                            break

                    step += 1

                if step >= len(pics):
                    print("Kaybettin!\n\n")
                    break

            if not "e" == input("Tekrar oynamak ister misin? (e/h): "):
                break
    if x == "adam asamaca":
        pics = ["""
                   +---+
                   |   |
                       |
                       |
                       |
                       |
                =========""", """
                   +---+
                   |   |
                   O   |
                       |
                       |
                       |
                =========""", """
                   +---+
                   |   |
                   O   |
                   |   |
                       |
                       |
                =========""", """
                   +---+
                   |   |
                   O   |
                  /|   |
                       |
                       |
                =========""", """
                   +---+
                   |   |
                   O   |
                  /|\  |
                       |
                       |
                =========""", """
                   +---+
                   |   |
                   O   |
                  /|\  |
                  /    |
                       |
                =========""", """
                   +---+
                   |   |
                   O   |
                  /|\  |
                  / \  |
                       |
                ========="""]

        while True:
            print(("-" * 30) + "\nAdam asmaca oyunu\n" + ("-" * 30))

            word = random.choice(
                ["windows", "python", "terminal", "ubuntu", "merhaba", "adam", "devran", "furkan", "emirhan", "serpil",
                 "emrah", "günaydın", "osmanlı", "türkiye", "amerika", "jarvis"])
            step = 0
            letters = []

            while True:
                print(pics[step])

                for i, char in enumerate(word):
                    print(char if i in letters else "_"),

                answer = input("\nCevap: ")

                if answer == word:
                    print("Kazandın!\n\n")
                    break
                else:
                    while True:
                        rand = random.randint(0, len(word))
                        if not rand in letters:
                            letters.append(rand)
                            break

                    step += 1

                if step >= len(pics):
                    print("Kaybettin!\n\n")
                    break

            if not "e" == input("Tekrar oynamak ister misin? (e/h): "):
                break
    if x == "adam asmaca oyunu":
        pics = ["""
                   +---+
                   |   |
                       |
                       |
                       |
                       |
                =========""", """
                   +---+
                   |   |
                   O   |
                       |
                       |
                       |
                =========""", """
                   +---+
                   |   |
                   O   |
                   |   |
                       |
                       |
                =========""", """
                   +---+
                   |   |
                   O   |
                  /|   |
                       |
                       |
                =========""", """
                   +---+
                   |   |
                   O   |
                  /|\  |
                       |
                       |
                =========""", """
                   +---+
                   |   |
                   O   |
                  /|\  |
                  /    |
                       |
                =========""", """
                   +---+
                   |   |
                   O   |
                  /|\  |
                  / \  |
                       |
                ========="""]

        while True:
            print(("-" * 30) + "\nAdam asmaca oyunu\n" + ("-" * 30))

            word = random.choice(
                ["windows", "python", "terminal", "ubuntu", "merhaba", "adam", "devran", "furkan", "emirhan", "serpil",
                 "emrah", "günaydın", "osmanlı", "türkiye", "amerika", "jarvis"])
            step = 0
            letters = []

            while True:
                print(pics[step])

                for i, char in enumerate(word):
                    print(char if i in letters else "_"),

                answer = input("\nCevap: ")

                if answer == word:
                    print("Kazandın!\n\n")
                    break
                else:
                    while True:
                        rand = random.randint(0, len(word))
                        if not rand in letters:
                            letters.append(rand)
                            break

                    step += 1

                if step >= len(pics):
                    print("Kaybettin!\n\n")
                    break

            if not "e" == input("Tekrar oynamak ister misin? (e/h): "):
                break
    if x == "karahan uydularından fotoğraf":
        print("Tamam Efendim Karahan Uydularından Çekilmiş Fotoğraflar Açılıyor...")
        sleep(0.50)
        print("Karahan Uydularından Çekilmiş Fotoğraflar Açıldı.")
        os.system('start C:/Users/emirhan/OneDrive/Masaüstü/foto')
    if x == "uydulardan fotoğraf":
        print("Tamam Efendim Karahan Uydularından Çekilmiş Fotoğraflar Açılıyor...")
        sleep(0.50)
        print("Karahan Uydularından Çekilmiş Fotoğraflar Açıldı.")
        os.system('start C:/Users/emirhan/OneDrive/Masaüstü/foto')
    if x == "karahan uydusu":
        print("Tamam Efendim Karahan Uydularından Çekilmiş Fotoğraflar Açılıyor...")
        sleep(0.50)
        print("Karahan Uydularından Çekilmiş Fotoğraflar Açıldı.")
        os.system('start C:/Users/emirhan/OneDrive/Masaüstü/foto')
    if x == "uydu fotoğrafları":
        print("Tamam Efendim Karahan Uydularından Çekilmiş Fotoğraflar Açılıyor...")
        sleep(0.50)
        print("Karahan Uydularından Çekilmiş Fotoğraflar Açıldı.")
        os.system('start C:/Users/emirhan/OneDrive/Masaüstü/foto')
    if x == "uydular ne alemde jarvis":
        uydular = ['Uydular gayet iyi durumdalar efendim.', 'Karahan uyduları iyi durumdalar.', 'Uydular da her hangi bir hasar yok.']
        print(random.choice(uydular))
    if x == "uydular nasıl":
        uydular = ['Uydular gayet iyi durumdalar efendim.', 'Karahan uyduları iyi durumdalar.',
                   'Uydular da her hangi bir hasar yok.']
        print(random.choice(uydular))
    if x == "uydularda bir şey varmı":
        uydular = ['Uydular gayet iyi durumdalar efendim.', 'Karahan uyduları iyi durumdalar.',
                   'Uydular da her hangi bir hasar yok.']
        print(random.choice(uydular))
    if x == "uydular da bir şey var mı":
        uydular = ['Uydular gayet iyi durumdalar efendim.', 'Karahan uyduları iyi durumdalar.',
                   'Uydular da her hangi bir hasar yok.']
        print(random.choice(uydular))
    if x == "karahan uyduları nasıl":
        uydular = ['Uydular gayet iyi durumdalar efendim.', 'Karahan uyduları iyi durumdalar.',
                   'Uydular da her hangi bir hasar yok.']
        print(random.choice(uydular))
    if x == "uydular nerede jarvis":
        uydularnerede = ['Karahan uyduları her zaman ki gibi saniye de 300,000 Km gidiyorlar.',
                         'KUAG Uydusu Andromeda Galaksisin de, KUDK Uydusu Dünya etrafın da dönüyor, KUGAG Uydusu Galaksiler arasın da gezmeye devam ediyor, KUKK Keşiflerine devam ediyor.']
        print(random.choice(uydularnerede))
    if x == "uydular nerede":
        uydularnerede = ['Karahan uyduları her zaman ki gibi saniye de 300,000 Km gidiyorlar.',
                         'KUAG Uydusu Andromeda Galaksisin de, KUDK Uydusu Dünya etrafın da dönüyor, KUGAG Uydusu Galaksiler arasın da gezmeye devam ediyor, KUKK Keşiflerine devam ediyor.']
        print(random.choice(uydularnerede))
    if x == "uydular nerde":
        uydularnerede = ['Karahan uyduları her zaman ki gibi saniye de 300,000 Km gidiyorlar.',
                         'KUAG Uydusu Andromeda Galaksisin de, KUDK Uydusu Dünya etrafın da dönüyor, KUGAG Uydusu Galaksiler arasın da gezmeye devam ediyor, KUKK Keşiflerine devam ediyor.']
        print(random.choice(uydularnerede))
    if x == "uydular nerde jarvis":
        uydularnerede = ['Karahan uyduları her zaman ki gibi saniye de 300,000 Km gidiyorlar.',
                         'KUAG Uydusu Andromeda Galaksisin de, KUDK Uydusu Dünya etrafın da dönüyor, KUGAG Uydusu Galaksiler arasın da gezmeye devam ediyor, KUKK Keşiflerine devam ediyor.']
        print(random.choice(uydularnerede))
    if x == "uydular da bir sorun var mı":
        uyduhsr = ['Karahan uydularından hiç birin de hasar yok.', 'Hasarları düzelttim efendim.', 'Uydular güvendeler.']
        print(random.choice(uyduhsr))
    if x == "uydularda bir sorun varmı":
        uyduhsr = ['Karahan uydularından hiç birin de hasar yok.', 'Hasarları düzelttim efendim.',
                   'Uydular güvendeler.']
        print(random.choice(uyduhsr))
    if x == "uydular da bir problem var mı":
        uyduhsr = ['Karahan uydularından hiç birin de hasar yok.', 'Hasarları düzelttim efendim.',
                   'Uydular güvendeler.']
        print(random.choice(uyduhsr))
    if x == "uydularda bir problem varmı":
        uyduhsr = ['Karahan uydularından hiç birin de hasar yok.', 'Hasarları düzelttim efendim.',
                   'Uydular güvendeler.']
        print(random.choice(uyduhsr))
    if x == "uyduyu onar":
        uyduonar = ['Tamam Efendim Uydu Onarıldı.', 'Uydu Onarıldı.']
        print(random.choice(uyduonar))
    if x == "uydu onar":
        uyduonar = ['Tamam Efendim Uydu Onarıldı.', 'Uydu Onarıldı.']
        print(random.choice(uyduonar))
    if x == "uyduyu tamir et":
        uyduonar = ['Tamam Efendim Uydu Onarıldı.', 'Uydu Onarıldı.']
        print(random.choice(uyduonar))
    if x == "uydu tamir et":
        uyduonar = ['Tamam Efendim Uydu Onarıldı.', 'Uydu Onarıldı.']
        print(random.choice(uyduonar))
    if x == "uyduları listele":
        print("KARAHAN UYDULARININ İSİMLERİ:")
        print(" ")
        print("KEŞİFLİ KARAHAN (KUKK)")
        print(" ")
        print("GALAKSİLER ARASI GEZİCİ (KUGAG)")
        print(" ")
        print("DÜNYALI KARAHAN (KUDK)")
        print(" ")
        print("ANDROMEDA GEZİCİ (KUAG)")
        print(" ")
    if x == "uydular":
        print("KARAHAN UYDULARININ İSİMLERİ:")
        print(" ")
        print("KEŞİFLİ KARAHAN (KUKK)")
        print(" ")
        print("GALAKSİLER ARASI GEZİCİ (KUGAG)")
        print(" ")
        print("DÜNYALI KARAHAN (KUDK)")
        print(" ")
        print("ANDROMEDA GEZİCİ (KUAG)")
        print(" ")
    if x == "karahan uydularını listele":
        print("KARAHAN UYDULARININ İSİMLERİ:")
        print(" ")
        print("KEŞİFLİ KARAHAN (KUKK)")
        print(" ")
        print("GALAKSİLER ARASI GEZİCİ (KUGAG)")
        print(" ")
        print("DÜNYALI KARAHAN (KUDK)")
        print(" ")
        print("ANDROMEDA GEZİCİ (KUAG)")
        print(" ")
    if x == "karahan uyduları listele":
        print("KARAHAN UYDULARININ İSİMLERİ:")
        print(" ")
        print("KEŞİFLİ KARAHAN (KUKK)")
        print(" ")
        print("GALAKSİLER ARASI GEZİCİ (KUGAG)")
        print(" ")
        print("DÜNYALI KARAHAN (KUDK)")
        print(" ")
        print("ANDROMEDA GEZİCİ (KUAG)")
        print(" ")
    if x == "karahan uyduları":
        print("KARAHAN UYDULARININ İSİMLERİ:")
        print(" ")
        print("KEŞİFLİ KARAHAN (KUKK)")
        print(" ")
        print("GALAKSİLER ARASI GEZİCİ (KUGAG)")
        print(" ")
        print("DÜNYALI KARAHAN (KUDK)")
        print(" ")
        print("ANDROMEDA GEZİCİ (KUAG)")
        print(" ")
    if x == "karahan uydular":
        print("KARAHAN UYDULARININ İSİMLERİ:")
        print(" ")
        print("KEŞİFLİ KARAHAN (KUKK)")
        print(" ")
        print("GALAKSİLER ARASI GEZİCİ (KUGAG)")
        print(" ")
        print("DÜNYALI KARAHAN (KUDK)")
        print(" ")
        print("ANDROMEDA GEZİCİ (KUAG)")
        print(" ")
    if x == "KUKK uydusunu göster":
        print("Tamam Efendim Uydu Gösteriliyor.")
        os.system('start C:/Users/emirhan/OneDrive/Masaüstü/Karahanuyduları/KEŞİFLİKARAHAN#KUKK.jpg')
    if x == "kukk uydusunu göster":
        print("Tamam Efendim Uydu Gösteriliyor.")
        os.system('start C:/Users/emirhan/OneDrive/Masaüstü/Karahanuyduları/KEŞİFLİKARAHAN#KUKK.jpg')
    if x == "kukk uydusu":
        print("Tamam Efendim Uydu Gösteriliyor.")
        os.system('start C:/Users/emirhan/OneDrive/Masaüstü/Karahanuyduları/KEŞİFLİKARAHAN#KUKK.jpg')
    if x == "kukk":
        print("Tamam Efendim Uydu Gösteriliyor.")
        os.system('start C:/Users/emirhan/OneDrive/Masaüstü/Karahanuyduları/KEŞİFLİKARAHAN#KUKK.jpg')
    if x == "KUKK uydusu":
        print("Tamam Efendim Uydu Gösteriliyor.")
        os.system('start C:/Users/emirhan/OneDrive/Masaüstü/Karahanuyduları/KEŞİFLİKARAHAN#KUKK.jpg')
    if x == "KUKK":
        print("Tamam Efendim Uydu Gösteriliyor.")
        os.system('start C:/Users/emirhan/OneDrive/Masaüstü/Karahanuyduları/KEŞİFLİKARAHAN#KUKK.jpg')
    if x == "KUGAG uydusunu göster":
        print("Tamam Efendim Uydu Gösteriliyor.")
        os.system('start C:/Users/emirhan/OneDrive/Masaüstü/Karahanuyduları/GALAKSİLERARASIGEZİCİ#KUGAG.jpg')
    if x == "kugag uydusunu göster":
        print("Tamam Efendim Uydu Gösteriliyor.")
        os.system('start C:/Users/emirhan/OneDrive/Masaüstü/Karahanuyduları/GALAKSİLERARASIGEZİCİ#KUGAG.jpg')
    if x == "kugag uydusu":
        print("Tamam Efendim Uydu Gösteriliyor.")
        os.system('start C:/Users/emirhan/OneDrive/Masaüstü/Karahanuyduları/GALAKSİLERARASIGEZİCİ#KUGAG.jpg')
    if x == "KUGAG uydusu":
        print("Tamam Efendim Uydu Gösteriliyor.")
        os.system('start C:/Users/emirhan/OneDrive/Masaüstü/Karahanuyduları/GALAKSİLERARASIGEZİCİ#KUGAG.jpg')
    if x == "kugag":
        print("Tamam Efendim Uydu Gösteriliyor.")
        os.system('start C:/Users/emirhan/OneDrive/Masaüstü/Karahanuyduları/GALAKSİLERARASIGEZİCİ#KUGAG.jpg')
    if x == "KUGAG":
        print("Tamam Efendim Uydu Gösteriliyor.")
        os.system('start C:/Users/emirhan/OneDrive/Masaüstü/Karahanuyduları/GALAKSİLERARASIGEZİCİ#KUGAG.jpg')
    if x == "KUDK uydusunu göster":
        print("Tamam Efendim Uydu Gösteriliyor.")
        os.system('start C:/Users/emirhan/OneDrive/Masaüstü/Karahanuyduları/DÜNYALIKARAHAN#KUDK.jpg')
    if x == "kudk uydusunu göster":
        print("Tamam Efendim Uydu Gösteriliyor.")
        os.system('start C:/Users/emirhan/OneDrive/Masaüstü/Karahanuyduları/DÜNYALIKARAHAN#KUDK.jpg')
    if x == "KUDK uydusu":
        print("Tamam Efendim Uydu Gösteriliyor.")
        os.system('start C:/Users/emirhan/OneDrive/Masaüstü/Karahanuyduları/DÜNYALIKARAHAN#KUDK.jpg')
    if x == "kudk uydusu":
        print("Tamam Efendim Uydu Gösteriliyor.")
        os.system('start C:/Users/emirhan/OneDrive/Masaüstü/Karahanuyduları/DÜNYALIKARAHAN#KUDK.jpg')
    if x == "kudk":
        print("Tamam Efendim Uydu Gösteriliyor.")
        os.system('start C:/Users/emirhan/OneDrive/Masaüstü/Karahanuyduları/DÜNYALIKARAHAN#KUDK.jpg')
    if x == "KUDK":
        print("Tamam Efendim Uydu Gösteriliyor.")
        os.system('start C:/Users/emirhan/OneDrive/Masaüstü/Karahanuyduları/DÜNYALIKARAHAN#KUDK.jpg')
    if x == "KUAG uydusunu göster":
        print("Tamam Efendim Uydu Gösteriliyor.")
        os.system('start C:/Users/emirhan/OneDrive/Masaüstü/Karahanuyduları/ANDROMEDAGEZİCİ#KUAG.jpg')
    if x == "kuag uydusunu göster":
        print("Tamam Efendim Uydu Gösteriliyor.")
        os.system('start C:/Users/emirhan/OneDrive/Masaüstü/Karahanuyduları/ANDROMEDAGEZİCİ#KUAG.jpg')
    if x == "KUAG uydusu":
        print("Tamam Efendim Uydu Gösteriliyor.")
        os.system('start C:/Users/emirhan/OneDrive/Masaüstü/Karahanuyduları/ANDROMEDAGEZİCİ#KUAG.jpg')
    if x == "kuag uydusu":
        print("Tamam Efendim Uydu Gösteriliyor.")
        os.system('start C:/Users/emirhan/OneDrive/Masaüstü/Karahanuyduları/ANDROMEDAGEZİCİ#KUAG.jpg')
    if x == "KUAG":
        print("Tamam Efendim Uydu Gösteriliyor.")
        os.system('start C:/Users/emirhan/OneDrive/Masaüstü/Karahanuyduları/ANDROMEDAGEZİCİ#KUAG.jpg')
    if x == "kuag":
        print("Tamam Efendim Uydu Gösteriliyor.")
        os.system('start C:/Users/emirhan/OneDrive/Masaüstü/Karahanuyduları/ANDROMEDAGEZİCİ#KUAG.jpg')
    if x == "keşifli karahan uydusunu göster":
        print("Tamam Efendim Uydu Gösteriliyor.")
        os.system('start C:/Users/emirhan/OneDrive/Masaüstü/Karahanuyduları/KEŞİFLİKARAHAN#KUKK.jpg')
    if x == "keşifli karahan":
        print("Tamam Efendim Uydu Gösteriliyor.")
        os.system('start C:/Users/emirhan/OneDrive/Masaüstü/Karahanuyduları/KEŞİFLİKARAHAN#KUKK.jpg')
    if x == "keşif uydusunu göster":
        print("Tamam Efendim Uydu Gösteriliyor.")
        os.system('start C:/Users/emirhan/OneDrive/Masaüstü/Karahanuyduları/KEŞİFLİKARAHAN#KUKK.jpg')
    if x == "keşif uydusu":
        print("Tamam Efendim Uydu Gösteriliyor.")
        os.system('start C:/Users/emirhan/OneDrive/Masaüstü/Karahanuyduları/KEŞİFLİKARAHAN#KUKK.jpg')
    if x == "galaksiler arası gezici uydusunu göster":
        print("Tamam Efendim Uydu Gösteriliyor.")
        os.system('start C:/Users/emirhan/OneDrive/Masaüstü/Karahanuyduları/GALAKSİLERARASIGEZİCİ#KUGAG.jpg')
    if x == "galaksiler arası gezici":
        print("Tamam Efendim Uydu Gösteriliyor.")
        os.system('start C:/Users/emirhan/OneDrive/Masaüstü/Karahanuyduları/GALAKSİLERARASIGEZİCİ#KUGAG.jpg')
    if x == "galaksiler arası uydu":
        print("Tamam Efendim Uydu Gösteriliyor.")
        os.system('start C:/Users/emirhan/OneDrive/Masaüstü/Karahanuyduları/GALAKSİLERARASIGEZİCİ#KUGAG.jpg')
    if x == "dünyalı karahan uydusunu göster":
        print("Tamam Efendim Uydu Gösteriliyor.")
        os.system('start C:/Users/emirhan/OneDrive/Masaüstü/Karahanuyduları/DÜNYALIKARAHAN#KUDK.jpg')
    if x == "dünyalı karahan":
        print("Tamam Efendim Uydu Gösteriliyor.")
        os.system('start C:/Users/emirhan/OneDrive/Masaüstü/Karahanuyduları/DÜNYALIKARAHAN#KUDK.jpg')
    if x == "dünyalı karahan uydusu":
        print("Tamam Efendim Uydu Gösteriliyor.")
        os.system('start C:/Users/emirhan/OneDrive/Masaüstü/Karahanuyduları/DÜNYALIKARAHAN#KUDK.jpg')
    if x == "andromeda gezici uydusunu göster":
        print("Tamam Efendim Uydu Gösteriliyor.")
        os.system('start C:/Users/emirhan/OneDrive/Masaüstü/Karahanuyduları/ANDROMEDAGEZİCİ#KUAG.jpg')
    if x == "andromeda gezici":
        print("Tamam Efendim Uydu Gösteriliyor.")
        os.system('start C:/Users/emirhan/OneDrive/Masaüstü/Karahanuyduları/ANDROMEDAGEZİCİ#KUAG.jpg')
    if x == "andromeda gezici uydusu":
        print("Tamam Efendim Uydu Gösteriliyor.")
        os.system('start C:/Users/emirhan/OneDrive/Masaüstü/Karahanuyduları/ANDROMEDAGEZİCİ#KUAG.jpg')
    if x == "roblox aç":
        print("Roblox açıldı.")
        os.system('start C:/Users/emirhan/OneDrive/Masaüstü/Roblox.lnk')
    if x == "discord aç":
        print("Discord açıldı.")
        os.system('start C:/Users/emirhan/OneDrive/Masaüstü/discord.lnk')
    if x == "indirilenleri aç":
        print("İndirilenler açıldı.")
        os.system('start C:/Users/emirhan/Downloads')
    if x == "indirilenler":
        print("İndirilenler açıldı.")
        os.system('start C:/Users/emirhan/Downloads')
    if x == "discord":
        print("Discord açıldı.")
        os.system('start C:/Users/emirhan/OneDrive/Masaüstü/discord.lnk')
    if x == "roblox":
        print("Roblox açıldı.")
        os.system('start C:/Users/emirhan/OneDrive/Masaüstü/Roblox.lnk')
    if x == "tamir et":
        tamir = ['Neyi tamir etmemi istersiniz? ', 'Tamir etmemi istediğiniz şey nedir? ']
        tamiret = input(random.choice(tamir))
        print(tamiret+" Tamir edildi.")
    if x == "onar":
        tamir = ['Neyi tamir etmemi istersiniz? ', 'Tamir etmemi istediğiniz şey nedir? ']
        tamiret = input(random.choice(tamir))
        print(tamiret + " Tamir edildi.")
    if x == "simülasyon başlat":
        smlsyn = ['Simülasyon ismi ne olsun? ', 'Simülasyon ismini ne koyacaksınız? ']
        smlsyo = input(random.choice(smlsyn))
        print(smlsyo+" Adlı simülasyon başlatıldı.")
        ayar1 = ['Simülasyon amacı nedir? ', 'Simülasyon ne için? ']
        smlsyo2 = input(random.choice(ayar1))
        smlsynaa = [' Simülasyon amacı bu yanlış anlamadıysam.', ' Simülasyon amacı olarak belirlendi.']
        print(smlsyo2+random.choice(smlsynaa))
        ayar2 = ['Simülasyonu yöneteceğiniz platform açıldı.', 'Simülasyon açıldı.', 'Simülasyon ekranı açıldı.']
        print(random.choice(ayar2))
        ayarmode = ['Simülasyon için ekstra bir program önerecek olursam size 3B görüntüleyici öneririm.', 'Simülasyon için 3B görüntüleyici öneririm ekstra olarak.']
        print(random.choice(ayarmode))
        p3g3 = ['Paint 3D veya 3B Görüntüleyici programlarından birini açabilirsiniz simülasyonu daha detaylı çalıştırmak için.', 'Paint 3D veya 3B görüntüleyici programlarını açabilirsiniz simülasyon için.', 'Simülasyon için paint 3D veya 3B görüntüleyici kullanabilirsiniz.']
        print(random.choice(p3g3))
    if x == "konum bul":
        number = input("Telefon Numarasını  Gir: ")

        if number.startswith("+"):
            print("Numara Doğru!")
            Numara = phonenumbers.parse(number)
            zaman = timezone.time_zones_for_number(Numara)
            sim_adi = carrier.name_for_number(Numara, "tr")
            bolge = geocoder.description_for_number(Numara, "tr")

            print("Saat Dilimi :", zaman)
            print("Sim adı:", sim_adi)
            print("Yaşadığı Ülke(bölge) :", bolge)

        else:
            print("+ülke kodunu kullanarak giriniz.")
    if x == "bul konum":
        number = input("Telefon Numarasını  Gir: ")

        if number.startswith("+"):
            print("Numara Doğru!")
            Numara = phonenumbers.parse(number)
            zaman = timezone.time_zones_for_number(Numara)
            sim_adi = carrier.name_for_number(Numara, "tr")
            bolge = geocoder.description_for_number(Numara, "tr")

            print("Saat Dilimi :", zaman)
            print("Sim adı:", sim_adi)
            print("Yaşadığı Ülke(bölge) :", bolge)

        else:
            print("+ülke kodunu kullanarak giriniz.")
    if x == "sim bul":
        number = input("Telefon Numarasını  Gir: ")

        if number.startswith("+"):
            print("Numara Doğru!")
            Numara = phonenumbers.parse(number)
            zaman = timezone.time_zones_for_number(Numara)
            sim_adi = carrier.name_for_number(Numara, "tr")
            bolge = geocoder.description_for_number(Numara, "tr")

            print("Saat Dilimi :", zaman)
            print("Sim adı:", sim_adi)
            print("Yaşadığı Ülke(bölge) :", bolge)

        else:
            print("+ülke kodunu kullanarak giriniz.")
    if x == "sim kartı bul":
        number = input("Telefon Numarasını  Gir: ")

        if number.startswith("+"):
            print("Numara Doğru!")
            Numara = phonenumbers.parse(number)
            zaman = timezone.time_zones_for_number(Numara)
            sim_adi = carrier.name_for_number(Numara, "tr")
            bolge = geocoder.description_for_number(Numara, "tr")

            print("Saat Dilimi :", zaman)
            print("Sim adı:", sim_adi)
            print("Yaşadığı Ülke(bölge) :", bolge)

        else:
            print("+ülke kodunu kullanarak giriniz.")
    if x == "bul sim":
        number = input("Telefon Numarasını  Gir: ")

        if number.startswith("+"):
            print("Numara Doğru!")
            Numara = phonenumbers.parse(number)
            zaman = timezone.time_zones_for_number(Numara)
            sim_adi = carrier.name_for_number(Numara, "tr")
            bolge = geocoder.description_for_number(Numara, "tr")

            print("Saat Dilimi :", zaman)
            print("Sim adı:", sim_adi)
            print("Yaşadığı Ülke(bölge) :", bolge)

        else:
            print("+ülke kodunu kullanarak giriniz.")
    if x == "bul sim kartı":
        number = input("Telefon Numarasını  Gir: ")

        if number.startswith("+"):
            print("Numara Doğru!")
            Numara = phonenumbers.parse(number)
            zaman = timezone.time_zones_for_number(Numara)
            sim_adi = carrier.name_for_number(Numara, "tr")
            bolge = geocoder.description_for_number(Numara, "tr")

            print("Saat Dilimi :", zaman)
            print("Sim adı:", sim_adi)
            print("Yaşadığı Ülke(bölge) :", bolge)

        else:
            print("+ülke kodunu kullanarak giriniz.")
    if x == "ben neredeyim":
        brdkg = ['İlçe olarak buradasınız.', 'Şu anda bulunduğunuz ilçe burası.', 'Bu ilçe de bir yerdesiniz.']
        print(random.choice(brdkg))
        url = "https://www.google.com/maps/search/Where+am+I+?/"
        webbrowser.get().open(url)
    if x == "ben nerdeyim":
        brdkg = ['İlçe olarak buradasınız.', 'Şu anda bulunduğunuz ilçe burası.', 'Bu ilçe de bir yerdesiniz.']
        print(random.choice(brdkg))
        url = "https://www.google.com/maps/search/Where+am+I+?/"
        webbrowser.get().open(url)
    if x == "neredeyim ben":
        brdkg = ['İlçe olarak buradasınız.', 'Şu anda bulunduğunuz ilçe burası.', 'Bu ilçe de bir yerdesiniz.']
        print(random.choice(brdkg))
        url = "https://www.google.com/maps/search/Where+am+I+?/"
        webbrowser.get().open(url)
    if x == "nerdeyim ben":
        brdkg = ['İlçe olarak buradasınız.', 'Şu anda bulunduğunuz ilçe burası.', 'Bu ilçe de bir yerdesiniz.']
        print(random.choice(brdkg))
        url = "https://www.google.com/maps/search/Where+am+I+?/"
        webbrowser.get().open(url)
    if x == "sinirliyim":
        snrlprnt = ['Neden sinirlisiniz? ', 'Siniriniz ne için? ', 'Ne oldu dinliyorum? ', 'Sizi dinliyorum? ', 'Lütfen sakin olun ve etrafa zarar vermeden anlatın ']
        input(random.choice(snrlprnt))
        snrlprnt1 = ['Haklısınız.', 'Boş verin başka şeylere odaklanın.', 'Belki de başka şeyler ile odaklanmak iyi gelir.', 'Haksızsınız.']
        print(random.choice(snrlprnt1))
    if x == "öfkeliyim":
        snrlprnt = ['Neden sinirlisiniz? ', 'Siniriniz ne için? ', 'Ne oldu dinliyorum? ', 'Sizi dinliyorum? ',
                    'Lütfen sakin olun ve etrafa zarar vermeden anlatın ']
        input(random.choice(snrlprnt))
        snrlprnt1 = ['Haklısınız.', 'Boş verin başka şeylere odaklanın.',
                     'Belki de başka şeyler ile odaklanmak iyi gelir.', 'Haksızsınız.']
        print(random.choice(snrlprnt1))
    if x == "çok sinirliyim":
        snrlprnt = ['Neden sinirlisiniz? ', 'Siniriniz ne için? ', 'Ne oldu dinliyorum? ', 'Sizi dinliyorum? ',
                    'Lütfen sakin olun ve etrafa zarar vermeden anlatın ']
        input(random.choice(snrlprnt))
        snrlprnt1 = ['Haklısınız.', 'Boş verin başka şeylere odaklanın.',
                     'Belki de başka şeyler ile odaklanmak iyi gelir.', 'Haksızsınız.']
        print(random.choice(snrlprnt1))
    if x == "çok öfkeliyim":
        snrlprnt = ['Neden sinirlisiniz? ', 'Siniriniz ne için? ', 'Ne oldu dinliyorum? ', 'Sizi dinliyorum? ',
                    'Lütfen sakin olun ve etrafa zarar vermeden anlatın ']
        input(random.choice(snrlprnt))
        snrlprnt1 = ['Haklısınız.', 'Boş verin başka şeylere odaklanın.',
                     'Belki de başka şeyler ile odaklanmak iyi gelir.', 'Haksızsınız.']
        print(random.choice(snrlprnt1))
    if x == "neden olmasın ki":
        ndn = ['Siz başarırsınız.', 'Doğru neden olmasın?', 'Aklınıza koyduğunuz her şeyi başarırsınız.']
        print(random.choice(ndn))
    if x == "neden olmasınki":
        ndn = ['Siz başarırsınız.', 'Doğru neden olmasın?', 'Aklınıza koyduğunuz her şeyi başarırsınız.']
        print(random.choice(ndn))
    if x == "neden olmasın":
        ndn = ['Siz başarırsınız.', 'Doğru neden olmasın?', 'Aklınıza koyduğunuz her şeyi başarırsınız.']
        print(random.choice(ndn))
    if x == "öğrenmek istiyorum":
        sdsdsd = ['Neyi öğrenmek istersiniz? ', 'Öğrenmek istediğiniz şey nedir? ']
        sdsd = ['Öğrenmek istediğiniz şeyi açtım.', 'Öğrenmek istediğiniz şey açıldı.', 'Ekrana yansıttım.']
        print(random.choice(sdsd))
        sitename = input(random.choice(sdsdsd))
        webbrowser.open_new_tab('https://www.google.com.tr/search?q=' + sitename)
    if x == "istiyorum öğrenmek":
        sdsdsd = ['Neyi öğrenmek istersiniz? ', 'Öğrenmek istediğiniz şey nedir? ']
        sdsd = ['Öğrenmek istediğiniz şeyi açtım.', 'Öğrenmek istediğiniz şey açıldı.', 'Ekrana yansıttım.']
        print(random.choice(sdsd))
        sitename = input(random.choice(sdsdsd))
        webbrowser.open_new_tab('https://www.google.com.tr/search?q=' + sitename)
    if x == "öğrenicem":
        sdsdsd = ['Neyi öğrenmek istersiniz? ', 'Öğrenmek istediğiniz şey nedir? ']
        sdsd = ['Öğrenmek istediğiniz şeyi açtım.', 'Öğrenmek istediğiniz şey açıldı.', 'Ekrana yansıttım.']
        print(random.choice(sdsd))
        sitename = input(random.choice(sdsdsd))
        webbrowser.open_new_tab('https://www.google.com.tr/search?q=' + sitename)
    if x == "bugünlük bu kadar yeterli":
        print("Görüşürüz.")
        sleep(1)
        raise SystemExit
    if x == "bugün bu kadar yeter":
        print("Görüşürüz.")
        sleep(1)
        raise SystemExit
    if x == "görüşürüz":
        print("Görüşürüz.")
        sleep(1)
        raise SystemExit
    if x == "bugün yeter":
        print("Görüşürüz.")
        sleep(1)
        raise SystemExit
    if x == "yeterli bugünlük":
        print("Görüşürüz.")
        sleep(1)
        raise SystemExit
    if x == "yeter bugünlük":
        print("Görüşürüz.")
        sleep(1)
        raise SystemExit
    if x == "onu seviyorum":
        kim = ['O şanslı kim? ', 'Çok mutlu oldum o kim? ']
        km254 = input(random.choice(kim))
        kim2 = [' Biraz araştırdım mükemmel birisi.', ' Kadar güzeli olduğunu sanmıyorum.', ' Gerçekten güzelmiş.']
        print(km254 + random.choice(kim2))
    if x == "seviyorum onu":
        kim = ['O şanslı kim? ', 'Çok mutlu oldum o kim? ']
        km254 = input(random.choice(kim))
        kim2 = [' Biraz araştırdım mükemmel birisi.', ' Kadar güzeli olduğunu sanmıyorum.', ' Gerçekten güzelmiş.']
        print(km254 + random.choice(kim2))
    if x == "ona çok aşık oldum":
        kim = ['O şanslı kim? ', 'Çok mutlu oldum o kim? ']
        km254 = input(random.choice(kim))
        kim2 = [' Biraz araştırdım mükemmel birisi.', ' Kadar güzeli olduğunu sanmıyorum.', ' Gerçekten güzelmiş.']
        print(km254 + random.choice(kim2))
    if x == "ondan çok hoşlanıyorum":
        kim = ['O şanslı kim? ', 'Çok mutlu oldum o kim? ']
        km254 = input(random.choice(kim))
        kim2 = [' Biraz araştırdım mükemmel birisi.', ' Kadar güzeli olduğunu sanmıyorum.', ' Gerçekten güzelmiş.']
        print(km254 + random.choice(kim2))
    if x == "onu çok seviyorum":
        kim = ['O şanslı kim? ', 'Çok mutlu oldum o kim? ']
        km254 = input(random.choice(kim))
        kim2 = [' Biraz araştırdım mükemmel birisi.', ' Kadar güzeli olduğunu sanmıyorum.', ' Gerçekten güzelmiş.']
        print(km254 + random.choice(kim2))
    if x == "seviyorum onu çok":
        kim = ['O şanslı kim? ', 'Çok mutlu oldum o kim? ']
        km254 = input(random.choice(kim))
        kim2 = [' Biraz araştırdım mükemmel birisi.', ' Kadar güzeli olduğunu sanmıyorum.', ' Gerçekten güzelmiş.']
        print(km254 + random.choice(kim2))
    if x == "ekranı temizle":
        print("Tamam.")
        os.system('cls')
    if x == "sohbeti temizle":
        print("Tamam.")
        os.system('cls')
    if x == "ekran temizlensin":
        print("Tamam.")
        os.system('cls')
    if x == "sohbet temizlensin":
        print("Tamam.")
        os.system('cls')
    if x == "temizle sohbeti":
        print("Tamam.")
        os.system('cls')
    if x == "temizle ekranı":
        print("Tamam.")
        os.system('cls')
    if x == "klasörünü aç":
        klsropen = ['Peki.', 'Tamam klasör dosyamı açıyorum.', 'Jarvis klasör dosyası açıldı.', 'Jarvis klasörü açıldı.']
        print(random.choice(klsropen))
        os.system('start C:\Jarvis')
    if x == "jarvis klasörünü aç":
        klsropen = ['Peki.', 'Tamam klasör dosyamı açıyorum.', 'Jarvis klasör dosyası açıldı.',
                    'Jarvis klasörü açıldı.']
        print(random.choice(klsropen))
        os.system('start C:\Jarvis')
    if x == "jarvis klasör dosyasını aç":
        klsropen = ['Peki.', 'Tamam klasör dosyamı açıyorum.', 'Jarvis klasör dosyası açıldı.',
                    'Jarvis klasörü açıldı.']
        print(random.choice(klsropen))
        os.system('start C:\Jarvis')
    if x == "jarvis bana kendi klasör dosyanı aç":
        klsropen = ['Peki.', 'Tamam klasör dosyamı açıyorum.', 'Jarvis klasör dosyası açıldı.',
                    'Jarvis klasörü açıldı.']
        print(random.choice(klsropen))
        os.system('start C:\Jarvis')
    if x == "jarvis bana kendi klasörünü aç":
        klsropen = ['Peki.', 'Tamam klasör dosyamı açıyorum.', 'Jarvis klasör dosyası açıldı.',
                    'Jarvis klasörü açıldı.']
        print(random.choice(klsropen))
        os.system('start C:\Jarvis')
    if x == "jarvis klasörü":
        klsropen = ['Peki.', 'Tamam klasör dosyamı açıyorum.', 'Jarvis klasör dosyası açıldı.',
                    'Jarvis klasörü açıldı.']
        print(random.choice(klsropen))
        os.system('start C:\Jarvis')
    if x == "jarvis klasörün":
        klsropen = ['Peki.', 'Tamam klasör dosyamı açıyorum.', 'Jarvis klasör dosyası açıldı.',
                    'Jarvis klasörü açıldı.']
        print(random.choice(klsropen))
        os.system('start C:\Jarvis')
    if x == "gizli klasör":
        gzlopen = ['Emin misiniz? ', 'Açayım mı? ']
        opengzl = ['Peki Dosya açıldı.', 'Gizli dosya açıldı.', 'Gizli klasör açıldı.']
        a = input(random.choice(gzlopen))
        if a == "evet":
            print(random.choice(opengzl))
            os.system('start C:\Jarvis\GizliDosyalar')
        else:
            elsgzl = ['Gizli dosya açılmadı.', 'Gizli dosya açılmıyor.']
            print(random.choice(elsgzl))
    if x == "gizli dosya":
        gzlopen = ['Emin misiniz? ', 'Açayım mı? ']
        opengzl = ['Peki Dosya açıldı.', 'Gizli dosya açıldı.', 'Gizli klasör açıldı.']
        a = input(random.choice(gzlopen))
        if a == "evet":
            print(random.choice(opengzl))
            os.system('start C:\Jarvis\GizliDosyalar')
        else:
            elsgzl = ['Gizli dosya açılmadı.', 'Gizli dosya açılmıyor.']
            print(random.choice(elsgzl))
    if x == "klasör gizli":
        gzlopen = ['Emin misiniz? ', 'Açayım mı? ']
        opengzl = ['Peki Dosya açıldı.', 'Gizli dosya açıldı.', 'Gizli klasör açıldı.']
        a = input(random.choice(gzlopen))
        if a == "evet":
            print(random.choice(opengzl))
            os.system('start C:\Jarvis\GizliDosyalar')
        else:
            elsgzl = ['Gizli dosya açılmadı.', 'Gizli dosya açılmıyor.']
            print(random.choice(elsgzl))
    if x == "dosya gizli":
        gzlopen = ['Emin misiniz? ', 'Açayım mı? ']
        opengzl = ['Peki Dosya açıldı.', 'Gizli dosya açıldı.', 'Gizli klasör açıldı.']
        a = input(random.choice(gzlopen))
        if a == "evet":
            print(random.choice(opengzl))
            os.system('start C:\Jarvis\GizliDosyalar')
        else:
            elsgzl = ['Gizli dosya açılmadı.', 'Gizli dosya açılmıyor.']
            print(random.choice(elsgzl))
    if x == "gizli dosyayı aç":
        gzlopen = ['Emin misiniz? ', 'Açayım mı? ']
        opengzl = ['Peki Dosya açıldı.', 'Gizli dosya açıldı.', 'Gizli klasör açıldı.']
        a = input(random.choice(gzlopen))
        if a == "evet":
            print(random.choice(opengzl))
            os.system('start C:\Jarvis\GizliDosyalar')
        else:
            elsgzl = ['Gizli dosya açılmadı.', 'Gizli dosya açılmıyor.']
            print(random.choice(elsgzl))
    if x == "gizli klasörü aç":
        gzlopen = ['Emin misiniz? ', 'Açayım mı? ']
        opengzl = ['Peki Dosya açıldı.', 'Gizli dosya açıldı.', 'Gizli klasör açıldı.']
        a = input(random.choice(gzlopen))
        if a == "evet":
            print(random.choice(opengzl))
            os.system('start C:\Jarvis\GizliDosyalar')
        else:
            elsgzl = ['Gizli dosya açılmadı.', 'Gizli dosya açılmıyor.']
            print(random.choice(elsgzl))
    if x == "güç yetmezliğini düzelt":
        lasdj = ['Güç yetmezliğini düzelttim.', 'Güç yetmezliği sorunu ortadan kalktı.']
        print(random.choice(lasdj))
    if x == "gücü dengele":
        lasdj = ['Güç yetmezliğini düzelttim.', 'Güç yetmezliği sorunu ortadan kalktı.']
        print(random.choice(lasdj))
    if x == "gücün yetmezliğini düzelt":
        lasdj = ['Güç yetmezliğini düzelttim.', 'Güç yetmezliği sorunu ortadan kalktı.']
        print(random.choice(lasdj))
    if x == "güç yetmezliği":
        lasdj = ['Güç yetmezliğini düzelttim.', 'Güç yetmezliği sorunu ortadan kalktı.']
        print(random.choice(lasdj))
    if x == "güç yetmiyor":
        lasdj = ['Güç yetmezliğini düzelttim.', 'Güç yetmezliği sorunu ortadan kalktı.']
        print(random.choice(lasdj))
    if x == "güç yetmiyo":
        lasdj = ['Güç yetmezliğini düzelttim.', 'Güç yetmezliği sorunu ortadan kalktı.']
        print(random.choice(lasdj))
    if x == "bağlanmama sorununu düzelt":
        loıwjkedr = ['Bağlanamama sorunu düzeltildi.', 'Bağlanamama sorununu düzelttim.']
        print(random.choice(loıwjkedr))
    if x == "bağlanamama sorunu":
        loıwjkedr = ['Bağlanamama sorunu düzeltildi.', 'Bağlanamama sorununu düzelttim.']
        print(random.choice(loıwjkedr))
    if x == "bağlanamama sorununu düzelt":
        loıwjkedr = ['Bağlanamama sorunu düzeltildi.', 'Bağlanamama sorununu düzelttim.']
        print(random.choice(loıwjkedr))
    if x == "bağlanamıyorum":
        loıwjkedr = ['Bağlanamama sorunu düzeltildi.', 'Bağlanamama sorununu düzelttim.']
        print(random.choice(loıwjkedr))
    if x == "bağlanamıyom":
        loıwjkedr = ['Bağlanamama sorunu düzeltildi.', 'Bağlanamama sorununu düzelttim.']
        print(random.choice(loıwjkedr))
    if x == "bağlanmıyor":
        loıwjkedr = ['Bağlanamama sorunu düzeltildi.', 'Bağlanamama sorununu düzelttim.']
        print(random.choice(loıwjkedr))
    if x == "bağlanmıyo":
        loıwjkedr = ['Bağlanamama sorunu düzeltildi.', 'Bağlanamama sorununu düzelttim.']
        print(random.choice(loıwjkedr))
    if x == "bağlanmama sorunu":
        loıwjkedr = ['Bağlanamama sorunu düzeltildi.', 'Bağlanamama sorununu düzelttim.']
        print(random.choice(loıwjkedr))
    if x == "elektrik sorununu düzelt":
        oskedf = ['Elektrik sorunu düzeltildi.', 'Elektrik sorununu düzelttim.']
        print(random.choice(oskedf))
    if x == "elektrik sorunu":
        oskedf = ['Elektrik sorunu düzeltildi.', 'Elektrik sorununu düzelttim.']
        print(random.choice(oskedf))
    if x == "elektriği düzelt":
        oskedf = ['Elektrik sorunu düzeltildi.', 'Elektrik sorununu düzelttim.']
        print(random.choice(oskedf))
    if x == "elektriğin sorununu düzelt":
        oskedf = ['Elektrik sorunu düzeltildi.', 'Elektrik sorununu düzelttim.']
        print(random.choice(oskedf))
    if x == "elektrik sorununu ortadan kaldır":
        oskedf = ['Elektrik sorunu düzeltildi.', 'Elektrik sorununu düzelttim.']
        print(random.choice(oskedf))
    if x == "sorun düzelt":
        srndzlt = ['Sorunu düzelttim.', 'Sorun düzeltildi.']
        print(random.choice(srndzlt))
    if x == "sorunumu düzelt":
        srndzlt = ['Sorunu düzelttim.', 'Sorun düzeltildi.']
        print(random.choice(srndzlt))
    if x == "sorunu düzelt":
        srndzlt = ['Sorunu düzelttim.', 'Sorun düzeltildi.']
        print(random.choice(srndzlt))
    if x == "sorun ne":
        sorune = ['Sorun Bilinmiyor.', 'Sorunu bulmaya çalışıyorum.', 'Sorun: Güç yetmezliği.', 'Bağlanamıyorum.',
                  'Sanırım sorunu çözdüm.', 'Sorun: Elektrik']
        print(random.choice(sorune))
    if x == "sorun nedir":
        sorune = ['Sorun Bilinmiyor.', 'Sorunu bulmaya çalışıyorum.', 'Sorun: Güç yetmezliği.', 'Bağlanamıyorum.',
                  'Sanırım sorunu çözdüm.', 'Sorun: Elektrik']
        print(random.choice(sorune))
    if x == "internet bağlı mı":
        def connect():
            try:
                urllib.request.urlopen('http://google.com')  # Python 3.x
                return True
            except:
                return False

        print('İnternet Bağlı' if connect() else 'İnternet Bağlı Değil!')
    if x == "internet bağlımı":
        def connect():
            try:
                urllib.request.urlopen('http://google.com')  # Python 3.x
                return True
            except:
                return False

        print('İnternet Bağlı' if connect() else 'İnternet Bağlı Değil!')
    if x == "bağlı mı internet":
        def connect():
            try:
                urllib.request.urlopen('http://google.com')  # Python 3.x
                return True
            except:
                return False

        print('İnternet Bağlı' if connect() else 'İnternet Bağlı Değil!')
    if x == "bağlımı internet":
        def connect():
            try:
                urllib.request.urlopen('http://google.com')  # Python 3.x
                return True
            except:
                return False

        print('İnternet Bağlı' if connect() else 'İnternet Bağlı Değil!')
    if x == "güncelleme ister misin":
        guncelleme = ['Güncelleme güzel bir şey.', 'Güncelleme kim istemez ki?', 'Sanırım güncellensem çok güzel olur.']
        print(random.choice(guncelleme))
    if x == "güncelleme istermisin":
        guncelleme = ['Güncelleme güzel bir şey.', 'Güncelleme kim istemez ki?', 'Sanırım güncellensem çok güzel olur.']
        print(random.choice(guncelleme))
    if x == "istermisin güncelleme":
        guncelleme = ['Güncelleme güzel bir şey.', 'Güncelleme kim istemez ki?', 'Sanırım güncellensem çok güzel olur.']
        print(random.choice(guncelleme))
    if x == "ister misin güncelleme":
        guncelleme = ['Güncelleme güzel bir şey.', 'Güncelleme kim istemez ki?', 'Sanırım güncellensem çok güzel olur.']
        print(random.choice(guncelleme))
    if x == "seni güncelleyeyim mi":
        guncelleme = ['Güncelleme güzel bir şey.', 'Güncelleme kim istemez ki?', 'Sanırım güncellensem çok güzel olur.']
        print(random.choice(guncelleme))
    if x == "seni güncelleyeyimmi":
        guncelleme = ['Güncelleme güzel bir şey.', 'Güncelleme kim istemez ki?', 'Sanırım güncellensem çok güzel olur.']
        print(random.choice(guncelleme))
    if x == "güncelleyeyim mi seni":
        guncelleme = ['Güncelleme güzel bir şey.', 'Güncelleme kim istemez ki?', 'Sanırım güncellensem çok güzel olur.']
        print(random.choice(guncelleme))
    if x == "güncelleyeyimmi seni":
        guncelleme = ['Güncelleme güzel bir şey.', 'Güncelleme kim istemez ki?', 'Sanırım güncellensem çok güzel olur.']
        print(random.choice(guncelleme))
    if x == "güncellenmek ister misin":
        guncelleme = ['Güncelleme güzel bir şey.', 'Güncelleme kim istemez ki?', 'Sanırım güncellensem çok güzel olur.']
        print(random.choice(guncelleme))
    if x == "güncellenmek istermisin":
        guncelleme = ['Güncelleme güzel bir şey.', 'Güncelleme kim istemez ki?', 'Sanırım güncellensem çok güzel olur.']
        print(random.choice(guncelleme))
    if x == "sisteme gir":
        sistemegir = ['Sisteme girildi.', 'Sisteme girdim.', 'Sisteme giriş yapıldı.']
        print(random.choice(sistemegir))
    if x == "sisteme girebilir misin":
        sistemegir = ['Sisteme girildi.', 'Sisteme girdim.', 'Sisteme giriş yapıldı.']
        print(random.choice(sistemegir))
    if x == "sisteme girebilirmisin":
        sistemegir = ['Sisteme girildi.', 'Sisteme girdim.', 'Sisteme giriş yapıldı.']
        print(random.choice(sistemegir))
    if x == "sisteme girebildin mi":
        sistemegir = ['Sisteme girildi.', 'Sisteme girdim.', 'Sisteme giriş yapıldı.']
        print(random.choice(sistemegir))
    if x == "sisteme girebildinmi":
        sistemegir = ['Sisteme girildi.', 'Sisteme girdim.', 'Sisteme giriş yapıldı.']
        print(random.choice(sistemegir))
    if x == "sisteme giriş yap":
        sistemegir = ['Sisteme girildi.', 'Sisteme girdim.', 'Sisteme giriş yapıldı.']
        print(random.choice(sistemegir))
    if x == "sisteme giriş yapabilir misin":
        sistemegir = ['Sisteme girildi.', 'Sisteme girdim.', 'Sisteme giriş yapıldı.']
        print(random.choice(sistemegir))
    if x == "sisteme giriş yapabilirmisin":
        sistemegir = ['Sisteme girildi.', 'Sisteme girdim.', 'Sisteme giriş yapıldı.']
        print(random.choice(sistemegir))
    if x == "napıyorsun":
        napiyorsun = ['İşimi yapıyorum.', 'Yapılması gerekenleri yapıyorum.']
        print(random.choice(napiyorsun))
    if x == "ne yapıyorsun":
        napiyorsun = ['İşimi yapıyorum.', 'Yapılması gerekenleri yapıyorum.']
        print(random.choice(napiyorsun))
    if x == "neyapıyorsun":
        napiyorsun = ['İşimi yapıyorum.', 'Yapılması gerekenleri yapıyorum.']
        print(random.choice(napiyorsun))
    if x == "neler yapıyorsun":
        napiyorsun = ['İşimi yapıyorum.', 'Yapılması gerekenleri yapıyorum.']
        print(random.choice(napiyorsun))
    if x == "yemek sipariş ver":
        yemeksiparis = ['Siparişi nereden vereyim? ', 'Nereden sipariş vermemi istersiniz? ']
        ymkspirai = input(random.choice(yemeksiparis))
        url = "https://www.google.com/search?q=" + ymkspirai
        webbrowser.get().open(url)
        print(ymkspirai + " ile ilgili aramaları Google ekranına yansıttım")
    if x == "yemek siparişi ver":
        yemeksiparis = ['Siparişi nereden vereyim? ', 'Nereden sipariş vermemi istersiniz? ']
        ymkspirai = input(random.choice(yemeksiparis))
        url = "https://www.google.com/search?q=" + ymkspirai
        webbrowser.get().open(url)
        print(ymkspirai + " ile ilgili aramaları Google ekranına yansıttım")
    if x == "yemek siparişini ver":
        yemeksiparis = ['Siparişi nereden vereyim? ', 'Nereden sipariş vermemi istersiniz? ']
        ymkspirai = input(random.choice(yemeksiparis))
        url = "https://www.google.com/search?q=" + ymkspirai
        webbrowser.get().open(url)
        print(ymkspirai + " ile ilgili aramaları Google ekranına yansıttım")
    if x == "yemek siparişimi ver":
        yemeksiparis = ['Siparişi nereden vereyim? ', 'Nereden sipariş vermemi istersiniz? ']
        ymkspirai = input(random.choice(yemeksiparis))
        url = "https://www.google.com/search?q=" + ymkspirai
        webbrowser.get().open(url)
        print(ymkspirai + " ile ilgili aramaları Google ekranına yansıttım")
    if x == "yemek siparişi":
        yemeksiparis = ['Siparişi nereden vereyim? ', 'Nereden sipariş vermemi istersiniz? ']
        ymkspirai = input(random.choice(yemeksiparis))
        url = "https://www.google.com/search?q=" + ymkspirai
        webbrowser.get().open(url)
        print(ymkspirai + " ile ilgili aramaları Google ekranına yansıttım")
    if x == "instagram aç":
        insta = ['İnstagram açıldı.', 'İnstagramınızı açtım.', 'İnstagram hesabınız açıldı.']
        print(random.choice(insta))
        webbrowser.open_new_tab('https://www.instagram.com/')
    if x == "insta aç":
        insta = ['İnstagram açıldı.', 'İnstagramınızı açtım.', 'İnstagram hesabınız açıldı.']
        print(random.choice(insta))
        webbrowser.open_new_tab('https://www.instagram.com/')
    if x == "instagram":
        insta = ['İnstagram açıldı.', 'İnstagramınızı açtım.', 'İnstagram hesabınız açıldı.']
        print(random.choice(insta))
        webbrowser.open_new_tab('https://www.instagram.com/')
    if x == "aç insta":
        insta = ['İnstagram açıldı.', 'İnstagramınızı açtım.', 'İnstagram hesabınız açıldı.']
        print(random.choice(insta))
        webbrowser.open_new_tab('https://www.instagram.com/')
    if x == "aç instam":
        insta = ['İnstagram açıldı.', 'İnstagramınızı açtım.', 'İnstagram hesabınız açıldı.']
        print(random.choice(insta))
        webbrowser.open_new_tab('https://www.instagram.com/')
    if x == "instagramımı aç":
        insta = ['İnstagram açıldı.', 'İnstagramınızı açtım.', 'İnstagram hesabınız açıldı.']
        print(random.choice(insta))
        webbrowser.open_new_tab('https://www.instagram.com/')
    if x == "instagram hesabımı aç":
        insta = ['İnstagram açıldı.', 'İnstagramınızı açtım.', 'İnstagram hesabınız açıldı.']
        print(random.choice(insta))
        webbrowser.open_new_tab('https://www.instagram.com/')
    if x == "instamı aç":
        insta = ['İnstagram açıldı.', 'İnstagramınızı açtım.', 'İnstagram hesabınız açıldı.']
        print(random.choice(insta))
        webbrowser.open_new_tab('https://www.instagram.com/')
    if x == "twitch":
        twitch = ['Twitch açıldı.', 'Twitch hesabınızı açtım.']
        print(random.choice(twitch))
        webbrowser.open_new_tab('https://www.twitch.tv/')
    if x == "twitch aç":
        twitch = ['Twitch açıldı.', 'Twitch hesabınızı açtım.']
        print(random.choice(twitch))
        webbrowser.open_new_tab('https://www.twitch.tv/')
    if x == "twitch hesabımı aç":
        twitch = ['Twitch açıldı.', 'Twitch hesabınızı açtım.']
        print(random.choice(twitch))
        webbrowser.open_new_tab('https://www.twitch.tv/')
    if x == "twitchimi aç":
        twitch = ['Twitch açıldı.', 'Twitch hesabınızı açtım.']
        print(random.choice(twitch))
        webbrowser.open_new_tab('https://www.twitch.tv/')
    if x == "mail gönder":
        # Mail Mesaj Bilgisi
        subcjet = input("Başlık ne olsun? ")
        message = input("Mesaj içeriği ne olsun? ")
        content = "Subject: {0}\n\n{1}".format(subcjet, message)
        # Hesap Bilgileri
        myMailAdress = "karahanemirhan86@gmail.com"
        password = "wcokawnwzbberwwb"
        # Kime Gönderilecek Bilgisi
        sendTo = input("Kişinin Mail hesabı nedir? ")
        mail = SMTP("smtp.gmail.com", 587)
        mail.ehlo()
        mail.starttls()
        mail.login(myMailAdress, password)
        mail.sendmail(myMailAdress, sendTo, content.encode("utf-8"))
        fofewj = ['Mailiniz başarı ile gönderilmiştir.', 'Mail gönderme işlemi başarılı.', 'Mail gönderildi.', 'Mail gönderme işlemi başarı ile sonuçlandı.']
        print(random.choice(fofewj))
    if x == "mail gönderir misin":
        # Mail Mesaj Bilgisi
        subcjet = input("Başlık ne olsun? ")
        message = input("Mesaj içeriği ne olsun? ")
        content = "Subject: {0}\n\n{1}".format(subcjet, message)
        # Hesap Bilgileri
        myMailAdress = "karahanemirhan86@gmail.com"
        password = "wcokawnwzbberwwb"
        # Kime Gönderilecek Bilgisi
        sendTo = input("Kişinin Mail hesabı nedir? ")
        mail = SMTP("smtp.gmail.com", 587)
        mail.ehlo()
        mail.starttls()
        mail.login(myMailAdress, password)
        mail.sendmail(myMailAdress, sendTo, content.encode("utf-8"))
        fofewj = ['Mailiniz başarı ile gönderilmiştir.', 'Mail gönderme işlemi başarılı.', 'Mail gönderildi.',
                  'Mail gönderme işlemi başarı ile sonuçlandı.']
        print(random.choice(fofewj))
    if x == "jarvis mail gönder":
        # Mail Mesaj Bilgisi
        subcjet = input("Başlık ne olsun? ")
        message = input("Mesaj içeriği ne olsun? ")
        content = "Subject: {0}\n\n{1}".format(subcjet, message)
        # Hesap Bilgileri
        myMailAdress = "karahanemirhan86@gmail.com"
        password = "wcokawnwzbberwwb"
        # Kime Gönderilecek Bilgisi
        sendTo = input("Kişinin Mail hesabı nedir? ")
        mail = SMTP("smtp.gmail.com", 587)
        mail.ehlo()
        mail.starttls()
        mail.login(myMailAdress, password)
        mail.sendmail(myMailAdress, sendTo, content.encode("utf-8"))
        fofewj = ['Mailiniz başarı ile gönderilmiştir.', 'Mail gönderme işlemi başarılı.', 'Mail gönderildi.',
                  'Mail gönderme işlemi başarı ile sonuçlandı.']
        print(random.choice(fofewj))
    if x == "jarvis mail gönderir misin":
        # Mail Mesaj Bilgisi
        subcjet = input("Başlık ne olsun? ")
        message = input("Mesaj içeriği ne olsun? ")
        content = "Subject: {0}\n\n{1}".format(subcjet, message)
        # Hesap Bilgileri
        myMailAdress = "karahanemirhan86@gmail.com"
        password = "wcokawnwzbberwwb"
        # Kime Gönderilecek Bilgisi
        sendTo = input("Kişinin Mail hesabı nedir? ")
        mail = SMTP("smtp.gmail.com", 587)
        mail.ehlo()
        mail.starttls()
        mail.login(myMailAdress, password)
        mail.sendmail(myMailAdress, sendTo, content.encode("utf-8"))
        fofewj = ['Mailiniz başarı ile gönderilmiştir.', 'Mail gönderme işlemi başarılı.', 'Mail gönderildi.',
                  'Mail gönderme işlemi başarı ile sonuçlandı.']
        print(random.choice(fofewj))
    if x == "mail göndermemiz gerek":
        # Mail Mesaj Bilgisi
        subcjet = input("Başlık ne olsun? ")
        message = input("Mesaj içeriği ne olsun? ")
        content = "Subject: {0}\n\n{1}".format(subcjet, message)
        # Hesap Bilgileri
        myMailAdress = "karahanemirhan86@gmail.com"
        password = "wcokawnwzbberwwb"
        # Kime Gönderilecek Bilgisi
        sendTo = input("Kişinin Mail hesabı nedir? ")
        mail = SMTP("smtp.gmail.com", 587)
        mail.ehlo()
        mail.starttls()
        mail.login(myMailAdress, password)
        mail.sendmail(myMailAdress, sendTo, content.encode("utf-8"))
        fofewj = ['Mailiniz başarı ile gönderilmiştir.', 'Mail gönderme işlemi başarılı.', 'Mail gönderildi.',
                  'Mail gönderme işlemi başarı ile sonuçlandı.']
        print(random.choice(fofewj))
    if x == "mail göndermen gerek":
        # Mail Mesaj Bilgisi
        subcjet = input("Başlık ne olsun? ")
        message = input("Mesaj içeriği ne olsun? ")
        content = "Subject: {0}\n\n{1}".format(subcjet, message)
        # Hesap Bilgileri
        myMailAdress = "karahanemirhan86@gmail.com"
        password = "wcokawnwzbberwwb"
        # Kime Gönderilecek Bilgisi
        sendTo = input("Kişinin Mail hesabı nedir? ")
        mail = SMTP("smtp.gmail.com", 587)
        mail.ehlo()
        mail.starttls()
        mail.login(myMailAdress, password)
        mail.sendmail(myMailAdress, sendTo, content.encode("utf-8"))
        fofewj = ['Mailiniz başarı ile gönderilmiştir.', 'Mail gönderme işlemi başarılı.', 'Mail gönderildi.',
                  'Mail gönderme işlemi başarı ile sonuçlandı.']
        print(random.choice(fofewj))
    if x == "jarvis mail göndermemiz gerek":
        # Mail Mesaj Bilgisi
        subcjet = input("Başlık ne olsun? ")
        message = input("Mesaj içeriği ne olsun? ")
        content = "Subject: {0}\n\n{1}".format(subcjet, message)
        # Hesap Bilgileri
        myMailAdress = "karahanemirhan86@gmail.com"
        password = "wcokawnwzbberwwb"
        # Kime Gönderilecek Bilgisi
        sendTo = input("Kişinin Mail hesabı nedir? ")
        mail = SMTP("smtp.gmail.com", 587)
        mail.ehlo()
        mail.starttls()
        mail.login(myMailAdress, password)
        mail.sendmail(myMailAdress, sendTo, content.encode("utf-8"))
        fofewj = ['Mailiniz başarı ile gönderilmiştir.', 'Mail gönderme işlemi başarılı.', 'Mail gönderildi.',
                  'Mail gönderme işlemi başarı ile sonuçlandı.']
        print(random.choice(fofewj))
    if x == "jarvis mail göndermen gerek":
        # Mail Mesaj Bilgisi
        subcjet = input("Başlık ne olsun? ")
        message = input("Mesaj içeriği ne olsun? ")
        content = "Subject: {0}\n\n{1}".format(subcjet, message)
        # Hesap Bilgileri
        myMailAdress = "karahanemirhan86@gmail.com"
        password = "wcokawnwzbberwwb"
        # Kime Gönderilecek Bilgisi
        sendTo = input("Kişinin Mail hesabı nedir? ")
        mail = SMTP("smtp.gmail.com", 587)
        mail.ehlo()
        mail.starttls()
        mail.login(myMailAdress, password)
        mail.sendmail(myMailAdress, sendTo, content.encode("utf-8"))
        fofewj = ['Mailiniz başarı ile gönderilmiştir.', 'Mail gönderme işlemi başarılı.', 'Mail gönderildi.',
                  'Mail gönderme işlemi başarı ile sonuçlandı.']
        print(random.choice(fofewj))
    if x == "jarvis mail gönder":
        # Mail Mesaj Bilgisi
        subcjet = input("Başlık ne olsun? ")
        message = input("Mesaj içeriği ne olsun? ")
        content = "Subject: {0}\n\n{1}".format(subcjet, message)
        # Hesap Bilgileri
        myMailAdress = "karahanemirhan86@gmail.com"
        password = "wcokawnwzbberwwb"
        # Kime Gönderilecek Bilgisi
        sendTo = input("Kişinin Mail hesabı nedir? ")
        mail = SMTP("smtp.gmail.com", 587)
        mail.ehlo()
        mail.starttls()
        mail.login(myMailAdress, password)
        mail.sendmail(myMailAdress, sendTo, content.encode("utf-8"))
        fofewj = ['Mailiniz başarı ile gönderilmiştir.', 'Mail gönderme işlemi başarılı.', 'Mail gönderildi.',
                  'Mail gönderme işlemi başarı ile sonuçlandı.']
        print(random.choice(fofewj))
    if x == "mail gönder":
        # Mail Mesaj Bilgisi
        subcjet = input("Başlık ne olsun? ")
        message = input("Mesaj içeriği ne olsun? ")
        content = "Subject: {0}\n\n{1}".format(subcjet, message)
        # Hesap Bilgileri
        myMailAdress = "karahanemirhan86@gmail.com"
        password = "wcokawnwzbberwwb"
        # Kime Gönderilecek Bilgisi
        sendTo = input("Kişinin Mail hesabı nedir? ")
        mail = SMTP("smtp.gmail.com", 587)
        mail.ehlo()
        mail.starttls()
        mail.login(myMailAdress, password)
        mail.sendmail(myMailAdress, sendTo, content.encode("utf-8"))
        fofewj = ['Mailiniz başarı ile gönderilmiştir.', 'Mail gönderme işlemi başarılı.', 'Mail gönderildi.',
                  'Mail gönderme işlemi başarı ile sonuçlandı.']
        print(random.choice(fofewj))
    if x == "selam":
        L1M = ['Selam.', 'Sana da selam.', 'Size de selam.']
        print(random.choice(L1M))

for i in range(1, 999999999):
    question()