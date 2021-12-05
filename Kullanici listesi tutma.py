kullanici_adi_listesi = []
sifre_listesi = []
kullanici_sayisi = 0
while True:
   kullanici_sayisi +=1
   kullanici_adi = input("Bir kullanici adi giriniz : ")
   sifre = input("Bir sifre giriniz : ")
   kullanici_adi_listesi.append(kullanici_adi)
   sifre_listesi.append(sifre)
   print("{}. kullanicisiniz tebrikler".format(kullanici_sayisi))
   print("Kullanici adiniz ve sifreniz listeye eklenmiştir k.a {} pw {}".format(kullanici_adi_listesi,sifre_listesi) )
   print("kullanici adiniz {} sifreniz {}".format(kullanici_adi_listesi[-1],sifre_listesi[-1]))
   break