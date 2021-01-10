# NUMPY ADVENCED - BASIC OPERATIONS

import numpy

# TOPLAMA/ÇIKARMA İŞLEMİ - DİZİ KARŞILIKLARINI BİREBİR TOPLAR
value1 = numpy.array([1,3,5])
value2 = numpy.array([2,4,6])

print("TOPLAMA: " , value1+value2)
print("ÇIKARMA: ", value1-value2)

print("---------------")
# SINUS ALMA
print("Sinus alma: ", numpy.sin(value1)) # her bir değerin sinüsünü alır

print("---------------")
# CONDITION LAR İLE KULLANMA
print("{} değeri 2 den küçük mü:,".format(value1), value1 < 2)

print("---------------")
# transpos u alma ve matrisleri çarpma
v1 = numpy.array([1,3,5])
v2 = numpy.array([2,4,6])

d1 = v1.dot(v2.T)
print("transpos : ", d1)

print("---------------")
# expenension değerini alma

print("expenension:" , numpy.exp(v1))

print("---------------")
# random değerler üretme
# 0 ile 1 arasında 5 e 5 lik random değerler üretir ve sonrasında bunları toplayalım

rndx = numpy.random.random((5,5)) 
total = rndx.sum()
maxV = rndx.max()
columnTotal = rndx.sum(axis=0) ## sadece columnları toplayalım
rowTotal = rndx.sum(axis=1) ## sadece satırları toplayalım
print("Randoms: " , rndx, " allTotal : ", total, " max Value: ", maxV, " columnTotal : " , columnTotal, " rowTotal: ", rowTotal )

print("---------------")
## karesi ve karekök alma
nmb = numpy.array([9,25,144])
print("Karekökü: " , numpy.sqrt(nmb))
print("Karesi: " , numpy.square(nmb))

print("-------------")
# iki değeri toplama işini add ile de yapabiliriz
arr1 = numpy.array([1,3,5])
arr2 = numpy.array([4,5,6])
print("topla: ", numpy.add(arr1,arr2) )