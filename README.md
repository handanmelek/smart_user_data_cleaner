# smart_user_data_cleaner
1.GİRİŞ
*Kirli olarak girilen verilerin toplu ve düzenli hale getirilmesi bu projenin amacıdır.

*Kirli verinin okunması ve işlenmesi zor olduğu için temizleme işleminden geçirilmesi gerekmektedir.

*Veriler sayısal olarak gelebildiği gibi string halde de gelebilmekte iki tür veri de kirli olarak bulunabilmektedir,data veri işleme sürecinde alınmadan önce temizleme işlemine tabi tutulmalıdır.

2.KULLANILAN PYTHON KONULARI 
*Değişkenler:Bir veriyi geçici olarak saklamak için kullanılan elemanlardır.

*String Veri Tipi:metin şeklinde olan veri tipidir.

*String Slicing: String verilerin bazı işlemlere tabi tutulma sürecinde maruz kaldıkları parçalanma işlemidir.

*String Methodları:Stringler üzerinde işlemler yapan fonksiyonlardır.

  Strip:boşlukları temizler.
  Lower:tüm harfleri küçültür.
  title:İlk harfi büyütür.
  split:bir stringi bölümlere ayırır.
  find:stringin içindeki belli bir karakteri bulur.

*Dönüşümler:Diğer adı type castingdir veri tipleri arasında dönüşüm sağlanır.

3.VERİ TEMİZLEME SÜRECİ

*Ham Verideki Problemler:Büyük küçük karakter hataları  yapılmış, gereksiz boşluklar bırakılmıştı.Sayılarda değerler string halde kalmıştı.

*İsim olarak belirtilen kısımda isimler düzenlendi; büyük, küçük harf sorunları giderildi;boşluklar temizlendi.Yaş ve boy olarak belirtilen kısımlarda type casting uygulandı,veriler sayısal işleme tabi tutulabilecek konuma getirildi.

*Yanlış girilen veriler okunma ve işlenme zorluğu yaşatıyordu ayrıca sayısal veriler string değerde olduğu için sayısal işleme tabi tutulamıyordu.

4.SONUÇ VE DEĞERLENDİRME

*Projenin Çözdüğü Problemler: Dağınık girilen string verilerin temizlenip düzenli hale getirilmesi, sayısal verilerin sayısal işleme tabi tutulabilecek hale gelmesi.

*Gerçek Hayatta Kullanım Alanları:Form verisi temizleme,Csv öncesi ön işleme ,kullanıcı kayıt normalizasyonu işlemlerinde birebir kullanılabilir.

*Kazanılan Python Becerileri:String verileri düzenleme, String Slicing, type casting işlemi yapabilme.


