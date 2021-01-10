import numpy

arr = numpy.array([1,3,5,6,9])

print("1 ile 3arasını seç", arr[1:3])

print("reverse : " , arr[::-1])

# 2 boyutlu dizi yaratalım

arr2 = numpy.array([ [1,3,9], [4,6,7] ])

# 9 u basalım
print("gelen değer:" , arr2[0,2]) #  0. elemanda yer alıyor,  2. satırında

## 1. elemanın ilk 2 değerini görelim
print("1. elemanın ilk 2 değeri şunlar:" , arr2[1][:2])
print("---------------")

#tüm satırların 1. değerlerini alalım
print("tüm satırların 1. değerleri : " , arr2[:,1])

print("---------------")

# 1. elemanın 1 ile 4 e kadar olan değerleri gelir
print("gelen değerler : " , arr2[1,1:4])

# en son gelen satırı ve bunun tüm sütunlarını alalım
print("son satır ve tüm sütunlar : " , arr2[-1, :])
