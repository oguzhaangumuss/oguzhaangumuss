# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#atm makinası oluşturma
bakiye =1000
print("***** ATM MAKİNASINA HOŞ GELDİNİZ *****\n1) Bakiye sorgulama\n2) Para Yatırma\n3) Para çekme \n***************************")
islem = int(input("Seçmek istediğiniz işlemi seçiniz : "))

while True:
    islem = int(input("Seçmek istediğiniz işlemi seçiniz : "))
    if islem==1:
        print("Bakiyeniz : {}".format(bakiye))
    elif islem==2:
        x = int(input("yatırmak istediginiz miktarı giriniz : "))
        bakiye = bakiye + x
        print("yeni bakiyeniz {}".format(bakiye))
    elif islem==3:
        y = int(input("çekmek istediğiniz miktarı giriniz : "))
        if y >= bakiye:
            print("bu kadar bakiyeniz yok!")
            continue
        print("Yeni bakiyeniz {}".format(bakiye-y))
    else: print ("geçersiz işlem ...")

