raw_data ="  AhMeT  yILMAZ ;  23 ;  1.78 ;  ahmetYILMAZ@GMAIL.Com   "

ayrilmisForm=raw_data.strip().split()

isimSoyisim=ayrilmisForm[:2]

#İsim
isim=isimSoyisim[0].strip().title()
Soyisim=isimSoyisim[1].strip().title()
isimSoyisim=isim+" "+Soyisim
isimSoyisim

#Yaş
yas=int(ayrilmisForm[3])
on_yil_sonra=float(yas+10)
on_yil_sonra

#Boy
boy=float(ayrilmisForm[5])
cmCinsinden=boy*100
cmCinsinden

#Email
mail=ayrilmisForm[7]
düzenlenmis=mail.lower().rstrip()
index=düzenlenmis.find("@")
ilkbolum=düzenlenmis[:index]
sonuc=ilkbolum[:3]
sonuc

#ÇIKTI
print(f"Kullanıcı: {isimSoyisim}\nYaş(on yıl sonra): {on_yil_sonra}\nBoy(cm): {cmCinsinden}\nEmail Kullanıcı kodu: {sonuc}")