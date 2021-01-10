import numpy

arr= numpy.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]) # 1*15 lük vektör

print(arr.shape)

#reshape yapmaya gerek olmadan da matris oluşturabiliriz
na = numpy.array([[1,2,3],[4,5,6],[7,8,9]])
print("yeni shape:", na)  # 3 e 3 lük bir matris oluşturdum

#####################
print("-------------")
#####################

# 3 e 5 lik bir matris yaratalım - 3 satırlı 5 sütunlu matris oluşur
a = arr.reshape(3,5)
print("işte 3e 5 lik matris: ", a)

#####################
print("-------------")
#####################

# Vektörün kaç boyutlu olduğnu öğrenelim - Dimension
print("Dimension: ", a.ndim)

#####################
print("-------------")
#####################

# matristeki değerlerin data type larını göster
print("Data type names: ", a.dtype.name)

#####################
print("-------------")
#####################

# size - matristeki toplam değer sayısı
print("size: ", a.size)

#####################
print("-------------")
#####################

## ZEROS - SIFIRLARDAN OLUŞAN MATRİSLER YARATMA - append ı düşündüğümüzde ciddi derecede yorucu olur. Zeros ile yer açarız ve sonra update ederiz.
cr = numpy.zeros((3,4))
print("sıfırlardan oluşanlar:", cr)

# Ayırdığımız yerlerden güncelleme yapalım
cr[0,0] = 5 # 0 a 0 elemanını 5 olarak atadık
print("son güncelleme -> (0,0): ", cr[0,0])
print("hepsini görelim: " , cr) # 0. satırın 0. column u 5 olduğunu görebiliriz.

#####################
print("-------------")
#####################

# Zeros ile aynı mantıkta Ones var 1 li matrisler yaratıyor. 
orx = numpy.ones((1,5))
print("1 likler:", orx)

#####################
print("-------------")
#####################

## 0 ya da 1 yapmak yerine boş yapmak istersek empty var
emp = numpy.empty((1,5))
print("boşluklar:", emp)

## Belirli aralıklardaki sayıları yazdırmak istersek

arg = numpy.arange(1,25,5) # 1 den 25 e kadar 5 şer 5 şer yaz, ilk değere +5 sonrasına +5 diye devam eder.
print("yaz bakam:", arg)

# 0 ile 10 arasında bana 20 tane sayı yazdır
numbers =  numpy.linspace(0,10,20)
print("0 ile 10 arasında 20 sayı: " , numbers)